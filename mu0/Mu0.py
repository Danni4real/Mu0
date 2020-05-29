from Reg import *
from Alu import *
from Mem import *
from Mux import *
from Controler import *

def mu0_init():
    reset_alu()
    set_reg_pc(get_alu(),1)

def mu0_proceed():  
    mu0_update_controler()    
    mu0_update_mem_addr()
    mu0_update_reg_ir()
    mu0_mem_write()
    mu0_alu()
    mu0_update_reg_pc()
    mu0_update_reg_acc()
    
def mu0_update_controler():
    controler(extract_bit(get_reg_ir_high_4bit(),0), extract_bit(get_reg_ir_high_4bit(),1), extract_bit(get_reg_ir_high_4bit(),2)) 

def mu0_update_mem_addr():
    mem_set_addr(addr_mux(get_reg_pc(), get_reg_ir_low_12bit(), get_addr_sel()))

def mu0_mem_write():
    set_mem(x_mux(get_reg_pc(), get_reg_acc(), get_x_sel()), get_write_en())

def mu0_alu():
    alu(x_mux(get_reg_pc(), get_reg_acc(), get_x_sel()),\
        y_mux(get_reg_ir_low_12bit(), get_mem(get_read_en()), get_y_sel()),\
        get_m()[0],get_m()[1])

def mu0_update_reg_ir():
    set_reg_ir(get_mem(get_read_en()), get_ir_en())

def mu0_update_reg_pc():
    set_reg_pc(get_alu(), get_pc_en())

def mu0_update_reg_acc():
    set_reg_acc(get_alu(), get_acc_en())
   

if __name__ == '__main__':
    mu0_init()
    mu0_proceed()
    mu0_proceed()

    mu0_proceed()
    mu0_proceed()

    mu0_proceed()
    mu0_proceed()

    mu0_proceed()
    mu0_proceed()

    mu0_proceed()
    mu0_proceed()

    mu0_proceed()
    mu0_proceed()

    mu0_proceed()
    mu0_proceed()

    mu0_proceed()
    mu0_proceed()

    mu0_proceed()
    mu0_proceed()

    mu0_proceed()
    mu0_proceed()

    mu0_proceed()
    mu0_proceed()

    
    mu0_proceed()
    mu0_proceed()
    
    '''
    print("Utest: mu0_update_controler")
    set_reg_ir(0b0000000000000000, 1)
    mu0_update_controler()
    mu0_update_controler()
    set_reg_ir(0b0001000000000000, 1)
    mu0_update_controler()
    mu0_update_controler()
    set_reg_ir(0b0010000000000000, 1)
    mu0_update_controler()
    mu0_update_controler()
    set_reg_ir(0b0011000000000000, 1)
    mu0_update_controler()
    mu0_update_controler()
    set_reg_ir(0b0100000000000000, 1)
    mu0_update_controler()
    mu0_update_controler()
    set_reg_ir(0b0101000000000000, 1)
    #set_reg_acc(0b0, 1)
    #set_reg_acc(0b1000000000000000, 1)
    set_reg_acc(0b0000000000000001, 1)
    mu0_update_controler()
    mu0_update_controler()
    set_reg_ir(0b0110000000000000, 1)
    mu0_update_controler()
    mu0_update_controler()
    set_reg_ir(0b0111000000000000, 1)
    mu0_update_controler()
    mu0_update_controler()
    print("")
    '''
    '''
    print("Utest: mu0_update_mem_addr")
    mu0_update_controler()
    set_reg_pc(0b0000000000000000, 1)
    set_reg_ir(0b0111000000000001, 1)
    mu0_update_mem_addr()
    '''
    '''
    print("Utest: mu0_update_reg_ir")
    mu0_update_controler()
    mem_set_addr(0b0)
    mu0_update_reg_ir()
    '''
    '''
    print("Utest: mu0_mem_write")
    set_reg_ir(0b0001000000000000, 1)
    set_reg_acc(0b0000000000000111, 1)
    mem_set_addr(0b0000010000000010)
    mu0_update_controler()
    mu0_update_controler()
    mu0_mem_write()
    '''
    '''
    print("Utest: mu0_alu")
    mu0_update_controler()
    mem_set_addr(0b0)
    set_reg_ir(0b0000010000000000, 1)
    set_reg_acc(0b1, 1)
    set_reg_pc(0b0, 1)
    mu0_alu()
    '''
    '''
    # load cmd
    mu0_update_controler()
    set_reg_ir(0b0000010000000000, 1)
    mu0_update_controler()
    set_reg_pc(0b1, 1)
    set_reg_acc(0b0, 1)
    mem_set_addr(0b010000000000)
    mu0_alu()    
    '''
    '''
    # store cmd
    mu0_update_controler()
    set_reg_ir(0b0001010000000010, 1)
    mu0_update_controler()
    set_reg_pc(0b001, 1)
    set_reg_acc(0b111, 1)
    mem_set_addr(0b010000000010)
    mu0_alu() 
    '''
    '''
    # add cmd
    mu0_update_controler()
    set_reg_ir(0b0010010000000001, 1)
    mu0_update_controler()
    set_reg_pc(0b001, 1)
    set_reg_acc(0b011, 1)
    mem_set_addr(0b010000000001)
    mu0_alu() 
    '''
    '''
    # sub cmd
    mu0_update_controler()
    set_reg_ir(0b0011010000000001, 1)
    mu0_update_controler()
    set_reg_pc(0b001, 1)
    set_reg_acc(0b1111, 1)
    mem_set_addr(0b010000000001)
    mu0_alu() 
    '''
    ''''
    # jump cmd
    mu0_update_controler()
    set_reg_ir(0b0100000000000000, 1)
    mu0_update_controler()
    set_reg_pc(0b001, 1)
    set_reg_acc(0b1111, 1)
    mem_set_addr(0b1)
    mu0_alu() 
    '''
    '''
    # jge cmd
    mu0_update_controler()
    set_reg_ir(0b0101000000000000, 1)
    set_reg_acc(0b1000000000000000, 1)
    mu0_update_controler()
    set_reg_pc(0b1, 1)
    mem_set_addr(0b1)
    mu0_alu() 
    '''
    '''
    # jne cmd
    mu0_update_controler()
    set_reg_ir(0b0110000000000000, 1)
    set_reg_acc(0b0000000000000001, 1)
    mu0_update_controler()
    set_reg_pc(0b1, 1)
    mem_set_addr(0b1)
    mu0_alu()
    '''
    '''
    # stp cmd
    mu0_update_controler()
    set_reg_ir(0b0111000000000000, 1)
    set_reg_acc(0b0000000000000001, 1)
    mu0_update_controler()
    set_reg_pc(0b1, 1)
    mem_set_addr(0b1)
    mu0_alu()
    '''




















