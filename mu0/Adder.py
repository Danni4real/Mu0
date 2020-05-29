from Gates import *

SUM_INDEX   = 0
CARRY_INDEX = 1
HIGH  = 1
LOW   = 0

def half_adder(in_1, in_2):
    result = [-1, -1]
    result[SUM_INDEX]   = xor_gate(in_1, in_2)
    result[CARRY_INDEX] = and_gate(in_1, in_2)
    return result

def full_adder(in_1, in_2, carry):
    result = [-1, -1]
    result[SUM_INDEX]   = (half_adder((half_adder(in_1, in_2))[SUM_INDEX], carry))[SUM_INDEX]
    result[CARRY_INDEX] = or_gate((half_adder((half_adder(in_1, in_2))[SUM_INDEX], carry))[CARRY_INDEX], (half_adder(in_1, in_2))[CARRY_INDEX])
    return result

def extract_bit(in_16bit, index):
    return (in_16bit >> index) % 2

def adder_16bit(in_1, in_2, carry):
    result = [-1, -1]
    _carry = carry
    _sum = 0
    for i in range(16):
        _sum += ((full_adder(extract_bit(in_1,i), extract_bit(in_2,i), _carry))[SUM_INDEX]) << i
        _carry = (full_adder(extract_bit(in_1,i), extract_bit(in_2,i), _carry))[CARRY_INDEX]
    
    result[SUM_INDEX] = _sum
    result[CARRY_INDEX] = _carry
    return result
    
if __name__ == '__main__':
    print("adder_16bit:")
    print("input: 0b1010101010101010, 0b0101010101010101, 0")
    result = adder_16bit(0b1010101010101010, 0b0101010101010101, 0)
    print("output-sum:   ", bin(result[SUM_INDEX]))
    print("output-carry: ", result[CARRY_INDEX])
    print("input: 0b1010101010101011, 0b0101010101010101, 0")
    result = adder_16bit(0b1010101010101011, 0b0101010101010101, 0)
    print("output-sum:   ", bin(result[SUM_INDEX]))
    print("output-carry: ", result[CARRY_INDEX])
    print("input: 0b1010101010101011, 0b0101010101010101, 1")
    result = adder_16bit(0b1010101010101011, 0b0101010101010101, 1)
    print("output-sum:   ", bin(result[SUM_INDEX]))
    print("output-carry: ", result[CARRY_INDEX])
    print("input: 11111, 22222, 0")
    result = adder_16bit(11111, 22222, 0)
    print("output-sum:   ", result[SUM_INDEX])
    print("output-carry: ", result[CARRY_INDEX])
    print("input: 65535, 65535, 1")
    result = adder_16bit(65535, 65535, 1)
    print("output-sum:   ", result[SUM_INDEX])
    print("output-carry: ", result[CARRY_INDEX])

    print("extract_bit:")
    print("input: 0b1010101010101010, 0")
    print("output: ", extract_bit(0b1010101010101010, 0))
    print("input: 0b1010101010101010, 1")
    print("output: ", extract_bit(0b1010101010101010, 1))
    print("input: 0b1010101010101010, 2")
    print("output: ", extract_bit(0b1010101010101010, 2))
    print("input: 0b1010101010101010, 3")
    print("output: ", extract_bit(0b1010101010101010, 3))
    print("input: 0b1010101010101010, 4")
    print("output: ", extract_bit(0b1010101010101010, 4))
    print("input: 0b1010101010101010, 5")
    print("output: ", extract_bit(0b1010101010101010, 5))
    print("input: 0b1010101010101010, 6")
    print("output: ", extract_bit(0b1010101010101010, 6))
    print("input: 0b1010101010101010, 7")
    print("output: ", extract_bit(0b1010101010101010, 7))
    print("input: 0b1010101010101010, 8")
    print("output: ", extract_bit(0b1010101010101010, 8))
    print("input: 0b1010101010101010, 9")
    print("output: ", extract_bit(0b1010101010101010, 9))
    print("input: 0b1010101010101010, 10")
    print("output: ", extract_bit(0b1010101010101010, 10))
    print("input: 0b1010101010101010, 11")
    print("output: ", extract_bit(0b1010101010101010, 11))
    print("input: 0b1010101010101010, 12")
    print("output: ", extract_bit(0b1010101010101010, 12))
    print("input: 0b1010101010101010, 13")
    print("output: ", extract_bit(0b1010101010101010, 13))
    print("input: 0b1010101010101010, 14")
    print("output: ", extract_bit(0b1010101010101010, 14))
    print("input: 0b1010101010101010, 15")
    print("output: ", extract_bit(0b1010101010101010, 15))

    print("half adder:")
    print("input: HIGH, LOW")
    result = half_adder(HIGH, LOW)
    print("output-sum:   ", result[SUM_INDEX])
    print("output-carry: ", result[CARRY_INDEX])

    print("input: HIGH, HIGH")
    result = half_adder(HIGH, HIGH)
    print("output-sum:   ", result[SUM_INDEX])
    print("output-carry: ", result[CARRY_INDEX])

    print("input: LOW, LOW")
    result = half_adder(LOW, LOW)
    print("output-sum:   ", result[SUM_INDEX])
    print("output-carry: ", result[CARRY_INDEX])

    print("input: LOW, HIGH")
    result = half_adder(LOW, HIGH)
    print("output-sum:   ", result[SUM_INDEX])
    print("output-carry: ", result[CARRY_INDEX])
    print("")

    print("full adder:")
    print("input: HIGH, LOW, 0")
    result = full_adder(HIGH, LOW, 0)
    print("output-sum:   ", result[SUM_INDEX])
    print("output-carry: ", result[CARRY_INDEX])    

    print("input: HIGH, LOW, 1")
    result = full_adder(HIGH, LOW, 1)
    print("output-sum:   ", result[SUM_INDEX])
    print("output-carry: ", result[CARRY_INDEX])

    print("input: HIGH, HIGH, 0")
    result = full_adder(HIGH, HIGH, 0)
    print("output-sum:   ", result[SUM_INDEX])
    print("output-carry: ", result[CARRY_INDEX])

    print("input: HIGH, HIGH, 1")
    result = full_adder(HIGH, HIGH, 1)
    print("output-sum:   ", result[SUM_INDEX])
    print("output-carry: ", result[CARRY_INDEX])

    print("input: LOW, HIGH, 0")
    result = full_adder(LOW, HIGH, 0)
    print("output-sum:   ", result[SUM_INDEX])
    print("output-carry: ", result[CARRY_INDEX])

    print("input: LOW, HIGH, 1")
    result = full_adder(LOW, HIGH, 1)
    print("output-sum:   ", result[SUM_INDEX])
    print("output-carry: ", result[CARRY_INDEX])

    print("input: LOW, LOW, 0")
    result = full_adder(LOW, LOW, 0)
    print("output-sum:   ", result[SUM_INDEX])
    print("output-carry: ", result[CARRY_INDEX])

    print("input: LOW, LOW, 1")
    result = full_adder(LOW, LOW, 1)
    print("output-sum:   ", result[SUM_INDEX])
    print("output-carry: ", result[CARRY_INDEX])

