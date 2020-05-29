from Gates import *
from Adder import *

WRITE = 1
READ  = 0

HIGH  = 1
LOW   = 0

ACC_index = 0
PC_index = 1
IR_index = 2

UNKNOWN = -1

REG_NUM = 3
REG_BIT_SIZE = 16

reg_volt_outputs = [[0 for col in range(REG_BIT_SIZE)] for row in range(REG_NUM)]

reg_acc_data = 0
reg_ir_data = 0
reg_pc_data = 0

def d_flip_flop(data, write, reg_index, flip_index):
    out = UNKNOWN
    date_and_write =  and_gate(data, write)
    idate_and_write = and_gate(not_gate(data), write)
    
    if date_and_write == HIGH:
        out = or_not_gate(or_not_gate(HIGH, out), idate_and_write)
        reg_volt_outputs[reg_index][flip_index] = out
    elif idate_and_write == HIGH:
        out = or_not_gate(or_not_gate(LOW, LOW), idate_and_write)
        reg_volt_outputs[reg_index][flip_index] = out
    else:
        out = or_not_gate(or_not_gate(reg_volt_outputs[reg_index][flip_index], LOW), LOW)

    return out

def reg_acc(in_16bit, clk, chip_enable):
    out_16bit = 0
    for i in range(REG_BIT_SIZE):
        out_16bit += d_flip_flop(extract_bit(in_16bit, i), and_gate(clk, chip_enable), ACC_index, i) << i

    return out_16bit
  
def reg_acc_positive():
    return not_gate(extract_bit(reg_acc_data, 15))

def reg_acc_non_zero():
    tmp_or = 0
    for i in range(REG_BIT_SIZE):
        tmp_or = or_gate(extract_bit(reg_acc_data, i), tmp_or)
    return tmp_or
    
def reg_pc(in_16bit, clk, chip_enable):
    out_16bit = 0
    for i in range(REG_BIT_SIZE):
        out_16bit += d_flip_flop(extract_bit(in_16bit, i), and_gate(clk, chip_enable), PC_index, i) << i

    return out_16bit

def reg_ir(in_16bit, clk, chip_enable):
    out_16bit = 0
    for i in range(REG_BIT_SIZE):
        out_16bit += d_flip_flop(extract_bit(in_16bit, i), and_gate(clk, chip_enable), IR_index, i) << i

    return out_16bit    

def set_reg_ir(in_16bit, chip_enable):
    print("==========set_reg_ir==========")
    global reg_ir_data
    reg_ir_data = reg_ir(in_16bit, 1, chip_enable)    
    print("Set Reg ir:", bin(reg_ir_data))

def set_reg_pc(in_16bit, chip_enable):
    print("==========set_reg_pc==========")
    global reg_pc_data
    reg_pc_data = reg_pc(in_16bit, 1, chip_enable)
    print("Set Reg pc:", bin(reg_pc_data))

def set_reg_acc(in_16bit, chip_enable):
    print("==========set_reg_acc==========")
    global reg_acc_data
    reg_acc_data = reg_acc(in_16bit, 1, chip_enable)
    print("Set Reg acc:", bin(reg_acc_data))

def get_reg_ir():
    print("Reg ir:", bin(reg_ir_data))
    return reg_ir_data
def get_reg_ir_low_12bit():
    print("Reg ir low 12bit:", bin(reg_ir_data % 4096))
    return reg_ir_data % 4096
def get_reg_ir_high_4bit():
    print("Reg ir high 4bit:", bin(reg_ir_data >> 12))
    return reg_ir_data >> 12
def get_reg_pc():
    print("Reg pc:", bin(reg_pc_data))
    return reg_pc_data
def get_reg_acc():
    print("Reg acc:", bin(reg_acc_data))
    return reg_acc_data

if __name__ == '__main__':
    print("write 1 to flip flop")
    d_flip_flop(HIGH, WRITE, ACC_index, 15) 
    print("read flip flop")  
    print(d_flip_flop(LOW, READ, ACC_index, 15))  
    print("write 0 to flip flop")   
    d_flip_flop(LOW, WRITE, ACC_index, 15) 
    print("read flip flop")    
    print(d_flip_flop(HIGH, READ, ACC_index, 15))

    print("write 0b1010101010101010 to acc")
    print(bin(reg_acc(0b1010101010101010, HIGH, HIGH)))
    print("write 0b1111111111111111 to pc")
    print(bin(reg_pc(0b1111111111111111, HIGH, HIGH)))
    print("write 0b1000000000000000 to ir")
    print(bin(reg_ir(0b1000000000000000, HIGH, HIGH)))



    print("read acc")
    print(bin(reg_acc(0b0, HIGH, LOW)))
    print("read pc")
    print(bin(reg_pc(0b0, HIGH, LOW)))
    print("read ir")
    print(bin(reg_ir(0b0, HIGH, LOW)))

    print("read acc")
    print(bin(reg_acc(0b0, LOW, HIGH)))
    print("read pc")
    print(bin(reg_pc(0b0, LOW, HIGH)))
    print("read ir")
    print(bin(reg_ir(0b0, LOW, HIGH)))

    print("read acc")
    print(bin(reg_acc(0b0, LOW, LOW)))
    print("read pc")
    print(bin(reg_pc(0b0, LOW, LOW)))
    print("read ir")
    print(bin(reg_ir(0b0, LOW, LOW)))

    print("write 0b0 to acc")
    print(bin(reg_acc(0b0, HIGH, HIGH)))
    print("write 0b0 to pc")
    print(bin(reg_pc(0b0, HIGH, HIGH)))
    print("write 0b0 to ir")
    print(bin(reg_ir(0b0, HIGH, HIGH)))

    print("reg_acc_positive")
    reg_acc(0b1, HIGH, HIGH)
    print(reg_acc_positive())
    print("reg_acc_non_zero")
    print(reg_acc_non_zero())

    print("reg_acc_positive")
    reg_acc(0b1000000000000000, HIGH, HIGH)
    print(reg_acc_positive())
    print("reg_acc_non_zero")
    print(reg_acc_non_zero())

    print("reg_acc_positive")
    reg_acc(0, HIGH, HIGH)
    print(reg_acc_positive())
    print("reg_acc_non_zero")
    print(reg_acc_non_zero())

    print("set reg")
    set_reg_ir(1, 1)
    set_reg_pc(2, 1)
    set_reg_acc(3, 1)
    print(get_reg_ir())
    print(get_reg_pc())
    print(get_reg_acc())
    set_reg_ir(4, 0)
    set_reg_pc(5, 0)
    set_reg_acc(6, 0)
    print(get_reg_ir())
    print(get_reg_pc())
    print(get_reg_acc())
    print(reg_acc_positive())
    print(reg_acc_non_zero())
    set_reg_acc(0, 1)
    print(reg_acc_positive())
    print(reg_acc_non_zero())
    set_reg_acc(0b1000000000000000, 1)
    print(reg_acc_positive())
    print(reg_acc_non_zero())









