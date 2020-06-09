

DATA_WIDTH = 16




def load_bin(bin_file_path):
    mem_image = [0 for data in range(4096)]
    f = open(bin_file_path, 'r')

    index = 0
    while True:
        line = f.readline()
        if not line:
            break
        line = line.replace("\n", "").strip()
        for i in range(DATA_WIDTH):
            mem_image[index] += int(list(line)[i]) << (DATA_WIDTH - i - 1)
        index += 1

    f.close()
    return mem_image

if __name__ == '__main__':
    load_bin("out.bin")
    
