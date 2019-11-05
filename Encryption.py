import math

def hexify(string) :
    myhex = hex(int(string, 2))
    myhex = myhex[2:].upper()
    return myhex

def init_pc (input) :
    output_size = 64
    box_values = [58 ,   50,   42,    34,    26 ,  18,    10,  2,
                60,    52,   44,    36,    28,   20,    12,    4,
                62,    54,   46,    38,    30,   22,    14,    6,
                64,   56,   48,    40,    32,   24,    16,    8,
                57,    49,   41,    33,    25,   17,     9,    1,
                59,    51,   43,    35,    27,   19,    11,    3,
                61,    53,   45,    37,    29,   21,    13,    5,
                63,   55,   47,    39,    31,   23,    15,    7]
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

def p_box1 (input) :
    output_size = 48
    box_values = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7,
                  8, 9, 8, 9, 10, 11, 12, 13, 12,
                  13, 14, 15, 16, 17, 16, 17, 18,
                  19, 20, 21, 20, 21, 22, 23, 24,
                  25, 24, 25, 26, 27, 28, 29, 28,
                  29, 30, 31, 32, 1]
    box_values.insert(0, -1)
    input_size = 32
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
    final = hexify(output)
    while len(final) < 12 :
        final = "0" + final
    return final

def p_box2 (input) :
    output_size = 32
    box_values  = [16 ,7,20,21,29,12,28,17,1,
                   15,23,26,5,18,31,10,2,8,24,
                    14,32, 27,3,9,19,13,30,6,22
                    ,11,4,25]
    box_values.insert(0 , -1)
    input_size = 32
    input_list=[]
    scale = 16
    input = list(bin(int(input, scale))[2:].zfill(input_size))
    input.insert(0 , -1)
    output = []
    for i in range (0 , (output_size+1)) :
        output.append (input[box_values[i]])
    del output[0]
    output = ''.join(output)
    #print(output)
    final = hexify(output)
    while len(final) < 8 :
        final = "0" + final
    return final

def s_box (line_input) :
    table = [
        [
            [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],

            [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],

            [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],

            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],

        ],

        [

            [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],

            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],

            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],

            [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],

        ],

        [

            [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],

            [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],

            [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],

            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],

        ],

        [

            [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],

            [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],

            [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],

            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],

        ],

        [

            [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],

            [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],

            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],

            [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],

        ],

        [

            [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],

            [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],

            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],

            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],

        ],

        [

            [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],

            [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],

            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],

            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],

        ],

        [

            [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],

            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],

            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],

            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],

        ]

    ]
    result = []
    #line_input = input("")

    decimal_list = []
    for num in range(12):
        temp = bin(int(line_input[num], 16)).replace("0b", "")
        while len(temp) < 4:
            temp = "0" + str(temp)
        decimal_list.append(temp)
    decimal_line = "".join(decimal_list)
    s = 0
    x = 0
    while s < 8:
        # print(s)
        plain_num = []
        # print("the value of x is : ",x)
        for i in range(x, x + 6):
            plain_num += decimal_line[i]
        # print(plain_num)
        row = int(plain_num[0] + plain_num[5], 2)
        col = plain_num[1: 5]
        col = "".join(col)
        col = int(col, 2)

        # print("the row is :  " , row)
        # print("the col is : " , col )
        # print("the value is ",table[s][row][col], "\n")
        result.append(table[s][row][col])
        s = s + 1
        x = x + 6
    result_hex = []
    for num in result:
        result_hex.append(hex(num).replace("0x", "").upper())

    result_hex = "".join(result_hex)
    return result_hex

def des_fun (input,key) :
    x = p_box1(input)
    # print("the first box output is :  ",x)
    hex_key = []
    for letter in key:
        hex_key.append(hex(int(letter, 16)).replace("0x", "").upper())
    hex_key = "".join(hex_key)
    xor_result = hex(int(x, 16) ^ int(hex_key, 16))
    while len(xor_result) < 14:
        xor_result = "0" + str(xor_result)
    xor_result = xor_result.replace("0x", "").upper()
    # print("the xor res is: ", xor_result)
    y = s_box(xor_result)
    # print("the s_box res is : " , y)
    result = p_box2(y)
    while len(result) < 8 :
        result = "0" + result
    return result



def inverse1_p (input) :
    output_size = 64
    box_values = [40, 8,   48,    16,    56,   24,    64,   32,
            39,     7,   47,    15,    55,   23,    63,   31,
            38,     6,   46,    14,    54,   22,    62,   30,
            37,     5,   45,    13,    53,   21,    61,   29,
            36,     4  , 44 ,   12 ,   52   ,20   , 60,   28,
            35  ,   3   ,43  ,  11  ,  51 ,  19 ,   59   ,27,
            34  ,   2 ,  42,    10 ,   50 ,  18  ,  58 ,  26,
            33 ,    1  , 41 ,    9   , 49 ,  17 ,   57 ,  25]
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


original_key = input()
plain_text = input()
n = int(input())
if n == 0 :
    print(plain_text)
else:
    for i in range (n) :

        plain_text_after_init = init_pc(plain_text)


        while len(plain_text_after_init) < 16 :
            plain_text_after_init = "0" + plain_text_after_init
        temp = plain_text_after_init
        #print("the plain text is : ",plain_text_after_init)

        for i in range (16) :
            #print("Round : " , i)
            left_plain_text = plain_text_after_init[:8]
            right_plain_text = plain_text_after_init[8:]

            left_output = right_plain_text


            keys = key_generation(original_key)
            #print("the right plain text is : ", right_plain_text)
            #print("the key of this round is : ",keys[i])

            des_out = des_fun(right_plain_text,keys[ -(i + 1)])
            #print("the out of the des fun is : ", des_out)
            right_output = hex(int(des_out,16) ^ int(left_plain_text,16))

            right_output = right_output.replace("0x" ,"").upper()
            while len(right_output) < 8 :
                right_output = "0" + right_output
            #print("the right output is ",right_output)
            output = left_output + right_output
            #print("the round output is : ",output + "\n")
            plain_text_after_init = output

        #print(output)
        swapped_out = rotate(output,8)
        #print(swapped_out)
        final_out = inverse1_p(swapped_out)
        plain_text = final_out
    while len(final_out) < 16 :
        final_out = "0" + final_out
    print(final_out)
