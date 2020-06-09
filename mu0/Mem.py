
mem_block = [0 for data in range(4096)]
current_addr = 0
mem_cache = 0

def load_mem_image(mem_image):
    global mem_block
    mem_block = mem_image

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
 
def dump_mem(num):
    for i in range(num):
        print(str(i).zfill(2),":", bin(mem_block[i]).replace('0b','').zfill(16))

if __name__ == '__main__':
    print(mem_block[0])
