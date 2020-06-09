from Gates import *
from Reg import *
from Mem import *

ir_en    = 0
pc_en    = 0
acc_en   = 0
read_en  = 0
write_en = 0
x_sel    = 0
y_sel    = 0
addr_sel = 0
m        = [0, 0]

def f_to_ir_en(f0, f1, f2, state):
    return not_gate(state)

def f_to_addr_sel(f0, f1, f2, state):
    return state

def f_to_pc_en(f0, f1, f2, state):
    return or_gate(not_gate(state),
                   and_gate(\
                            f2,\
                            and_gate(\
                                     and_not_gate(f0,f1),\
                                     or_gate(\
                                             and_gate(not_gate(f0),not_gate(f1)),\
                                             or_gate(\
                                                     and_gate(f0,reg_acc_positive()),\
                                                     and_gate(f1,reg_acc_non_zero()))))))

def f_to_acc_en(f0, f1, f2, state): 
    return and_gate(state, and_gate(not_gate(f2), or_gate(not_gate(f0),f1)))

def f_to_x_sel(f0, f1, f2, state):
    return and_gate(state, and_gate(not_gate(f2), or_gate(f0,f1)))

def f_to_y_sel(f0, f1, f2, state):
    return f_to_acc_en(f0, f1, f2,state)

def f_to_read_en(f0, f1, f2, state): 
    return or_gate(not_gate(state), f_to_acc_en(f0, f1, f2,state))

def f_to_write_en(f0, f1, f2, state): 
    return and_gate(state, and_gate(not_gate(f2), not_gate(or_gate(not_gate(f0),f1))))

def f_to_m(f0, f1, f2, state):
    m = [-1,-1]
    m[0] = and_gate(state, and_gate(not_gate(f2),f1))
    m[1] = or_gate(not_gate(state), and_gate(not_gate(f2),f0))
    return m

current_state = 1
def state_flip_flop():
    global current_state
    date_and_write =  and_gate(not_gate(current_state), 1)
    idate_and_write = and_gate(not_gate(not_gate(current_state)), 1)
    
    if date_and_write == 1:
        current_state = or_not_gate(or_not_gate(1, current_state), idate_and_write)
    elif idate_and_write == 1:
        current_state = or_not_gate(or_not_gate(0, 0), idate_and_write)

def controler(f0, f1, f2):
    print("==========controler==========")
    global current_state
    global ir_en
    global pc_en
    global acc_en
    global read_en
    global write_en
    global x_sel
    global y_sel
    global addr_sel
    global m
    state_flip_flop()
    ir_en = f_to_ir_en(f0,f1,f2,current_state)
    pc_en = f_to_pc_en(f0,f1,f2,current_state)
    acc_en = f_to_acc_en(f0,f1,f2,current_state)
    read_en = f_to_read_en(f0,f1,f2,current_state)
    write_en = f_to_write_en(f0,f1,f2,current_state)
    x_sel = f_to_x_sel(f0,f1,f2,current_state)
    y_sel = f_to_y_sel(f0,f1,f2,current_state)
    addr_sel = f_to_addr_sel(f0,f1,f2,current_state)
    m = f_to_m(f0,f1,f2,current_state)
    if f0 == 1 and f1 == 1 and f2 == 1:
        print("program exit!")
        dump_mem(32)
        exit(0)
    print("next_s ir_en pc_en acc_en m[1:0] x_sel y_sel a_sel r_en w_en")
    print(not_gate(current_state),"    ", ir_en, "   ",pc_en, "   ",acc_en, "    ",m[1],m[0], "  ",x_sel, "   ",y_sel, "   ",addr_sel, "   ",read_en, "   ",write_en)

def get_ir_en():
    print("ir_en: ", ir_en)
    return ir_en   
def get_pc_en():
    print("pc_en: ", pc_en)
    return pc_en 
def get_acc_en():
    print("acc_en: ", acc_en)
    return acc_en 
def get_read_en():
    print("r_en: ", read_en)
    return read_en 
def get_write_en():
    print("w_en: ", write_en)
    return write_en 
def get_x_sel():
    print("x_sel: ", x_sel)
    return x_sel 
def get_y_sel():
    print("y_sel: ", y_sel)
    return y_sel 
def get_addr_sel():
    print("a_sel: ", addr_sel)
    return addr_sel
def get_m():
    print("m[0]: ", m[0])
    print("m[1]: ", m[1])
    return m

if __name__ == '__main__':
    print("f_to_acc_en:")
    print("state: 0")
    print(f_to_acc_en(0,0,0,0))
    print(f_to_acc_en(0,0,1,0))
    print(f_to_acc_en(0,1,0,0))
    print(f_to_acc_en(0,1,1,0))
    print(f_to_acc_en(1,0,0,0))
    print(f_to_acc_en(1,0,1,0))
    print(f_to_acc_en(1,1,0,0))
    print(f_to_acc_en(1,1,1,0))
    print("f[2:0]: 000")
    print(f_to_acc_en(0,0,0,1))
    print("f[2:0]: 001")
    print(f_to_acc_en(1,0,0,1))
    print("f[2:0]: 010")
    print(f_to_acc_en(0,1,0,1))
    print("f[2:0]: 011")
    print(f_to_acc_en(1,1,0,1))
    print("f[2:0]: 100")
    print(f_to_acc_en(0,0,1,1))
    print("f[2:0]: 101")
    print(f_to_acc_en(1,0,1,1))
    print("f[2:0]: 110")
    print(f_to_acc_en(0,1,1,1))
    print("f[2:0]: 111")
    print(f_to_acc_en(1,1,1,1))
    print("")

    print("f_to_x_sel:")
    print("state: 0")
    print(f_to_x_sel(0,0,0,0))
    print(f_to_x_sel(0,0,1,0))
    print(f_to_x_sel(0,1,0,0))
    print(f_to_x_sel(0,1,1,0))
    print(f_to_x_sel(1,0,0,0))
    print(f_to_x_sel(1,0,1,0))
    print(f_to_x_sel(1,1,0,0))
    print(f_to_x_sel(1,1,1,0))
    print("f[2:0]: 000")
    print(f_to_x_sel(0,0,0,1))
    print("f[2:0]: 001")
    print(f_to_x_sel(1,0,0,1))
    print("f[2:0]: 010")
    print(f_to_x_sel(0,1,0,1))
    print("f[2:0]: 011")
    print(f_to_x_sel(1,1,0,1))
    print("f[2:0]: 100")
    print(f_to_x_sel(0,0,1,1))
    print("f[2:0]: 101")
    print(f_to_x_sel(1,0,1,1))
    print("f[2:0]: 110")
    print(f_to_x_sel(0,1,1,1))
    print("f[2:0]: 111")
    print(f_to_x_sel(1,1,1,1))

    print("f_to_read_en:")
    print("state: 0")
    print(f_to_read_en(0,0,0,0))
    print(f_to_read_en(0,0,1,0))
    print(f_to_read_en(0,1,0,0))
    print(f_to_read_en(0,1,1,0))
    print(f_to_read_en(1,0,0,0))
    print(f_to_read_en(1,0,1,0))
    print(f_to_read_en(1,1,0,0))
    print(f_to_read_en(1,1,1,0))
    print("f[2:0]: 000")
    print(f_to_read_en(0,0,0,1))
    print("f[2:0]: 001")
    print(f_to_read_en(1,0,0,1))
    print("f[2:0]: 010")
    print(f_to_read_en(0,1,0,1))
    print("f[2:0]: 011")
    print(f_to_read_en(1,1,0,1))
    print("f[2:0]: 100")
    print(f_to_read_en(0,0,1,1))
    print("f[2:0]: 101")
    print(f_to_read_en(1,0,1,1))
    print("f[2:0]: 110")
    print(f_to_read_en(0,1,1,1))
    print("f[2:0]: 111")
    print(f_to_read_en(1,1,1,1))

    print("f_to_write_en:")
    print("state: 0")
    print(f_to_write_en(0,0,0,0))
    print(f_to_write_en(0,0,1,0))
    print(f_to_write_en(0,1,0,0))
    print(f_to_write_en(0,1,1,0))
    print(f_to_write_en(1,0,0,0))
    print(f_to_write_en(1,0,1,0))
    print(f_to_write_en(1,1,0,0))
    print(f_to_write_en(1,1,1,0))
    print("f[2:0]: 000")
    print(f_to_write_en(0,0,0,1))
    print("f[2:0]: 001")
    print(f_to_write_en(1,0,0,1))
    print("f[2:0]: 010")
    print(f_to_write_en(0,1,0,1))
    print("f[2:0]: 011")
    print(f_to_write_en(1,1,0,1))
    print("f[2:0]: 100")
    print(f_to_write_en(0,0,1,1))
    print("f[2:0]: 101")
    print(f_to_write_en(1,0,1,1))
    print("f[2:0]: 110")
    print(f_to_write_en(0,1,1,1))
    print("f[2:0]: 111")
    print(f_to_write_en(1,1,1,1))

    reg_acc(0b1000000000000000, HIGH, HIGH)
    print("f_to_pc_en:")
    print("state: 0")
    print(f_to_pc_en(0,0,0,0))
    print(f_to_pc_en(0,0,1,0))
    print(f_to_pc_en(0,1,0,0))
    print(f_to_pc_en(0,1,1,0))
    print(f_to_pc_en(1,0,0,0))
    print(f_to_pc_en(1,0,1,0))
    print(f_to_pc_en(1,1,0,0))
    print(f_to_pc_en(1,1,1,0))
    print("f[2:0]: 000")
    print(f_to_pc_en(0,0,0,1))
    print("f[2:0]: 001")
    print(f_to_pc_en(1,0,0,1))
    print("f[2:0]: 010")
    print(f_to_pc_en(0,1,0,1))
    print("f[2:0]: 011")
    print(f_to_pc_en(1,1,0,1))
    print("f[2:0]: 100")
    print(f_to_pc_en(0,0,1,1))
    print("f[2:0]: 101")
    print(f_to_pc_en(1,0,1,1))
    print("f[2:0]: 110")
    print(f_to_pc_en(0,1,1,1))
    print("f[2:0]: 111")
    print(f_to_pc_en(1,1,1,1))

    print("f_to_y_sel:")
    print("state: 0")
    print(f_to_y_sel(0,0,0,0))
    print(f_to_y_sel(0,0,1,0))
    print(f_to_y_sel(0,1,0,0))
    print(f_to_y_sel(0,1,1,0))
    print(f_to_y_sel(1,0,0,0))
    print(f_to_y_sel(1,0,1,0))
    print(f_to_y_sel(1,1,0,0))
    print(f_to_y_sel(1,1,1,0))
    print("f[2:0]: 000")
    print(f_to_y_sel(0,0,0,1))
    print("f[2:0]: 001")
    print(f_to_y_sel(1,0,0,1))
    print("f[2:0]: 010")
    print(f_to_y_sel(0,1,0,1))
    print("f[2:0]: 011")
    print(f_to_y_sel(1,1,0,1))
    print("f[2:0]: 100")
    print(f_to_y_sel(0,0,1,1))
    print("f[2:0]: 101")
    print(f_to_y_sel(1,0,1,1))
    print("f[2:0]: 110")
    print(f_to_y_sel(0,1,1,1))
    print("f[2:0]: 111")
    print(f_to_y_sel(1,1,1,1))
    print("")

    print("f_to_m:")
    print("state: 0")
    print(f_to_m(0,0,0,0))
    print(f_to_m(0,0,1,0))
    print(f_to_m(0,1,0,0))
    print(f_to_m(0,1,1,0))
    print(f_to_m(1,0,0,0))
    print(f_to_m(1,0,1,0))
    print(f_to_m(1,1,0,0))
    print(f_to_m(1,1,1,0))
    print("f[2:0]: 000")
    print(f_to_m(0,0,0,1))
    print("f[2:0]: 001")
    print(f_to_m(1,0,0,1))
    print("f[2:0]: 010")
    print(f_to_m(0,1,0,1))
    print("f[2:0]: 011")
    print(f_to_m(1,1,0,1))
    print("f[2:0]: 100")
    print(f_to_m(0,0,1,1))
    print("f[2:0]: 101")
    print(f_to_m(1,0,1,1))
    print("f[2:0]: 110")
    print(f_to_m(0,1,1,1))
    print("f[2:0]: 111")
    print(f_to_m(1,1,1,1))
    print("")

    print("state_flip_flop:")
    state_flip_flop()
    state_flip_flop()
    state_flip_flop()
    state_flip_flop()
    state_flip_flop()
    state_flip_flop()

    reg_acc(0b0000000000000001, HIGH, HIGH)
    print("controler:")
    controler(1, 1, 1)
    controler(1, 0, 1)
    print(get_ir_en())
    print(get_pc_en())
    print(get_acc_en())
    print(get_m())
    print(get_x_sel())
    print(get_y_sel())
    print(get_addr_sel())
    print(get_read_en())
    print(get_write_en())

