def hexify(string) :
    myhex = hex(int(string, 2))
    myhex = myhex[2:].upper()
    return myhex


output_size = int(input())
box_values  = list(map(int,input().strip().split()))[:output_size]
box_values.insert(0 , -1)
input_size = int(input())
input = input()
input_list=[]
scale = 16
input = list(bin(int(input, scale))[2:].zfill(input_size))
input.insert(0 , -1)
output = []
for i in range (0 , (output_size+1)) :
    output.append (input[box_values[i]])
del output[0]
output = ''.join(output)
print(len(output))
print(output)
print(hexify(output))

