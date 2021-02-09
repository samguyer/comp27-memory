
# -- Memory is a big array of bytes
Size = 32
Memory = [0 for _ in range(Size)]


def clear_memory():
    for i in range(len(Memory)):
        Memory[i] = 0


def as_binary(byte):
    bin = ''
    for bit in range(8):
        if byte & 128 == 0:
            bin = bin + '0'
        else:
            bin = bin + '1'
    return bin


def show_memory():
    for i in range(0, len(Memory), 4):
        line = ''
        for j in range(4):
            b = Memory[i + j]
            line = line + as_binary(b) + ' '
        print('{:3d}  {}'.format(i, line))


def load_byte(address):
    if address >= Size or address < 0:
        print("Seg fault")
        return None
    else:
        return Memory[address]


def store_byte(byte, address):
    if address >= Size or address < 0:
        print("Seg fault")
        return None
    else:
        Memory[address] = byte


def load_uint16(address):
    high = load_byte(address)
    low = load_byte(address+1)
    val = high * 256 + low
    return val


def store_uint16(val, address):
    high = (val // 256) % 256
    low = val % 256
    store_byte(high, address)
    store_byte(low, address+1)


def load_sint16(address):
    uint = load_uint16(address)
    if uint > 32767:
        sint = uint - 65536
    else:
        sint = uint
    return sint


def store_sint16(val, address):
    if val < 0:
        uint = val + 65536
    else:
        uint = val
    store_uint16(uint, address)


val = 0
prev = 0
store_sint16(val, 8)
while prev <= val:
    prev = val
    val = val + 1
    print('prev = {}  val = {}'.format(prev, val))
    store_sint16(val, 8)
    val = load_sint16(8)

print('prev = {}  val = {}'.format(prev, val))
