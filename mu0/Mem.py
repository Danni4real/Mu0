
mem_block = [0 for data in range(4096)]
current_addr = 0

mem_block[0] = 0b0000010000000000    #load data at address 1024
mem_block[1] = 0b0010010000000001    #add  acc and data at address 1025
mem_block[2] = 0b0011010000000010    #sub  acc and data at address 1026
mem_block[3] = 0b0101000000000110    #jge to addr 6
mem_block[4] = 0b0001010000000100    #store acc to address 1028
mem_block[5] = 0b0111000000000000    #stop
mem_block[6] = 0b0011010000000011    #sub  acc and data at address 1027
mem_block[7] = 0b0110000000000010    #jne to addr 2
mem_block[8] = 0b0011010000000011    #sub  acc and data at address 1027
mem_block[9] = 0b0110000000000010    #jne to addr 2
mem_block[1024] = 5
mem_block[1025] = 10
mem_block[1026] = 14
mem_block[1027] = 1
mem_block[1028] = 0

mem_cache = 0

def mem_set_addr(addr_12bit):
    print("==========mem_set_addr==========")
    global current_addr
    current_addr = addr_12bit
    print("set mem addr", bin(current_addr))

def set_mem(data, write_enable):
    print("==========set_mem==========")
    if write_enable == 1:
        mem_block[current_addr] = data
        print("set mem[",current_addr,"]: ", bin(mem_block[current_addr]))

def get_mem(read_enable):
    global mem_cache
    if read_enable == 1:
        mem_cache = mem_block[current_addr]
    print("get mem[",current_addr,"]: ", bin(mem_cache))
    return mem_cache

if __name__ == '__main__':
    print(mem_block[0])
