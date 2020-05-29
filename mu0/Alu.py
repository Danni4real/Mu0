from Adder import *
from Gates import *

SUM_INDEX   = 0
CARRY_INDEX = 1
SX_index  = 0
SY_index  = 1
SIY_index = 2
CIN_index = 3

alu_output = -1

# ADD:    m0 = 1, m1 = 0
# SUB:    m0 = 1, m1 = 1
# PC+1:   m0 = 0, m1 = 1
# SET Y:  m0 = 0, m1 = 0

def reset_alu():
    global alu_output
    alu_output = 0

def get_alu():
    print("alu output: ",bin(alu_output))
    return alu_output

def alu(bus_x, bus_y, m0, m1):
    print("==========alu==========")
    global alu_output
    alu_output = adder_16bit(\
                             alu_bus_x_selector(bus_x, (alu_func_decoder(m0,m1))[SX_index]), \
                             alu_bus_y_selector(bus_y, (alu_func_decoder(m0,m1))[SY_index], (alu_func_decoder(m0,m1))[SIY_index]),\
                             (alu_func_decoder(m0,m1))[CIN_index])[SUM_INDEX]
    print("alu output: ",bin(alu_output))
    


def alu_func_decoder(m0, m1):
    result = [-1,-1,-1,-1]
    result[SX_index] = or_gate(m0, m1)
    result[SY_index] = not_gate(m1)
    result[SIY_index] = and_gate(m0, m1)
    result[CIN_index] = m1
    return result

def alu_bus_x_selector(bus_x, sx):
    x_out = 0
    for i in range(16):
        x_out += and_gate(extract_bit(bus_x, i), sx) << i
    return x_out

def alu_bus_y_selector(bus_y, sy, siy):
    y_out = 0
    y_out_sy = 0
    y_out_siy = 0
    bus_y_inverse = 0
    for i in range(16):
        bus_y_inverse += not_gate(extract_bit(bus_y, i)) << i

    for i in range(16):
        y_out_sy += and_gate(extract_bit(bus_y, i), sy) << i

    for i in range(16):
        y_out_siy += and_gate(extract_bit(bus_y_inverse, i), siy) << i

    for i in range(16):
        y_out += or_gate(extract_bit(y_out_sy, i), extract_bit(y_out_siy, i)) << i

    return y_out

if __name__ == '__main__':
    print("alu func decoder:")
    print("m0: 0, m1: 0")
    print(alu_func_decoder(0,0))
    print("m0: 0, m1: 1")
    print(alu_func_decoder(0,1))
    print("m0: 1, m1: 0")
    print(alu_func_decoder(1,0))
    print("m0: 1, m1: 1")
    print(alu_func_decoder(1,1))
    print("")

    print("alu bus x selector")
    print("bus_x: 0b1010101010101010, sx: 0")
    print(bin(alu_bus_x_selector(0b1010101010101010, 0)))
    print("bus_x: 0b1010101010101010, sx: 1")
    print(bin(alu_bus_x_selector(0b1010101010101010, 1)))
    print("")

    print("alu bus y selector")
    print("bus_y: 0b1010101010101010, sy: 0, siy: 0")
    print(bin(alu_bus_y_selector(0b1010101010101010, 0, 0)))

    print("alu bus y selector")
    print("bus_y: 0b1010101010101010, sy: 1, siy: 0")
    print(bin(alu_bus_y_selector(0b1010101010101010, 1, 0)))

    print("alu bus y selector")
    print("bus_y: 0b1010101010101010, sy: 0, siy: 1")
    print(bin(alu_bus_y_selector(0b1010101010101010, 0, 1)))

    print("alu:")
    print("bus_x: 0b0101010101010101, bus_y: 0b1010101010101010, m0: 0, m1: 0")
    print(bin(alu(0b0101010101010101, 0b1010101010101010, 0, 0)))

    print("bus_x: 0b0101010101010101, bus_y: 0b1010101010101010, m0: 0, m1: 1")
    print(bin(alu(0b0101010101010101, 0b1010101010101010, 0, 1)))

    print("bus_x: 0b0101010101010101, bus_y: 0b1010101010101011, m0: 1, m1: 0")
    print(bin(alu(0b0101010101010101, 0b1010101010101011, 1, 0)))

    print("bus_x: 0b1000000000000000, bus_y: 0b1, m0: 1, m1: 1")
    print(bin(alu(0b1000000000000000, 0b1, 1, 1)))














   
