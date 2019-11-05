import math

def hexify(string) :
    myhex = hex(int(string, 2))
    myhex = myhex[2:].upper()
    return myhex

def pc1 (input) :
    output_size = 56
    box_values = [ 57, 49, 41, 33, 25, 17, 9, 1,
                   58, 50, 42, 34, 26, 18, 10, 2,
                   59, 51, 43, 35, 27, 19, 11, 3,
                   60, 52, 44, 36, 63, 55, 47, 39,
                   31, 23, 15, 7, 62, 54, 46, 38, 30,
                   22, 14, 6, 61, 53, 45, 37, 29, 21,
                   13, 5, 28, 20, 12, 4 ]
    box_values.insert(0, -1)
    input_size = 64
    input_list = []
    scale = 16
    input = list(bin(int(input, scale))[2:].zfill(input_size))
    input.insert(0, -1)
    output = []
    for i in range(0, (output_size + 1)):
        output.append(input[box_values[i]])
    del output[0]
    output = ''.join(output)
    # print(output)
    return hexify(output)

def pc2 (input) :
    output_size = 48
    box_values = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10,
                  23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2,
                  41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33,
                  48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36,
                  29, 32]
    box_values.insert(0, -1)
    input_size = 56
    input_list = []
    scale = 16
    input = list(bin(int(input, scale))[2:].zfill(input_size))
    input.insert(0, -1)
    output = []
    for i in range(0, (output_size + 1)):
        output.append(input[box_values[i]])
    del output[0]
    output = ''.join(output)
    # print(output)
    return hexify(output)

def hex_to_binary (hex_num) :
    ##### THIS FUNCTION RETURNS STRING ######
    #num_of_bits = 28
    num_of_bits = len(hex_num) * int(math.log2(16))
    return bin(int(hex_num, 16))[2:].zfill(num_of_bits)

def rotate(input, d):
    # slice string in two parts for left and right
    Lfirst =  input[0: d]
    Lsecond = input[d:]
    #Rfirst = input[0: len(input) - d]
    #Rsecond = input[len(input) - d:]

    # now concatenate two parts together
    #print ("Left Rotation : ", (Lsecond + Lfirst))
    return (Lsecond + Lfirst)
    #print ("Right Rotation : ", (Rsecond + Rfirst))
def key_generation(original_key):
    relation = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

    #original_key = input()
    temp = original_key
    result1_key = hex_to_binary(pc1(temp))
    while len(result1_key) < 56 :
        result1_key = "0" + result1_key
    c = result1_key[:28]
    d = result1_key[28:]
    c_rotated = rotate(c , relation[0])
    d_rotated = rotate(d , relation[0])
    new_key = c_rotated + d_rotated

    temp = new_key
    final_key = pc2(hexify(new_key))
    while len(final_key) < 12:
        final_key = "0" + final_key

    keys = []
    keys.append(final_key)

    for i in range ( 1 , 16) :

        c_rotated = rotate(c_rotated, relation[i])
        d_rotated = rotate(d_rotated, relation[i])

        new_key = c_rotated + d_rotated
        new_key_in_hex = pc2(hexify(new_key))
        while len(new_key_in_hex) < 12 :
            new_key_in_hex = "0" + new_key_in_hex
        #print(new_key_in_hex)
        keys.append(new_key_in_hex)
    return keys
original_key = input("")
keys = key_generation(original_key)
for key in keys:
    print(key)
