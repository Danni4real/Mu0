from Gates import *
from Adder import *
MUX_SELLECT_IN_0 = 0
MUX_SELLECT_IN_1 = 1

def bit_mux(in_0, in_1, sel):
    return or_gate(and_gate(in_0, not_gate(sel)),and_gate(in_1, sel))

def mux(in_16bit_0, in_16bit_1, sel):
    out_16bit = 0
    for i in range(16):
        out_16bit += bit_mux(extract_bit(in_16bit_0,i), extract_bit(in_16bit_1,i),sel) << i
    return out_16bit

def x_mux(pc, acc, sel):
    print("x_mux: ",bin(mux(pc, acc, sel)))
    return mux(pc, acc, sel)

def y_mux(ir, mem, sel):
    print("y_mux: ",bin(mux(ir, mem, sel)))
    return mux(ir, mem, sel)

def addr_mux(ir, pc, sel):
    print("addr_mux: ",bin(mux(ir, pc, sel)))
    return mux(ir, pc, sel)


if __name__ == '__main__':
    print("bit mux:")
    print("in_0:0, in_1:1, sel:0")
    print(bit_mux(0,1,MUX_SELLECT_IN_0))
    print("in_0:0, in_1:1, sel:1")
    print(bit_mux(0,1,MUX_SELLECT_IN_1))

    print("x_mux:")
    print("in_0:0b1010101010101010, in_1:0b1000000000000001, sel:0")
    print(bin(x_mux(0b1010101010101010, 0b1000000000000001, MUX_SELLECT_IN_0)))
    print("in_0:0b1010101010101010, in_1:0b1000000000000001, sel:1")
    print(bin(x_mux(0b1010101010101010, 0b1000000000000001, MUX_SELLECT_IN_1)))

    print("y_mux:")
    print("in_0:0b1010101010101010, in_1:0b1000000000000001, sel:0")
    print(bin(y_mux(0b1010101010101010, 0b1000000000000001, MUX_SELLECT_IN_0)))
    print("in_0:0b1010101010101010, in_1:0b1000000000000001, sel:1")
    print(bin(y_mux(0b1010101010101010, 0b1000000000000001, MUX_SELLECT_IN_1)))

    print("addr_mux:")
    print("in_0:0b1010101010101010, in_1:0b1000000000000001, sel:0")
    print(bin(addr_mux(0b1010101010101010, 0b1000000000000001, MUX_SELLECT_IN_0)))
    print("in_0:0b1010101010101010, in_1:0b1000000000000001, sel:1")
    print(bin(addr_mux(0b1010101010101010, 0b1000000000000001, MUX_SELLECT_IN_1)))
