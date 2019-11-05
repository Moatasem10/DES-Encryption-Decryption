
first_line_input = list(map(int,input().strip().split()))[:2]
inn = int(first_line_input[0])
out = int(first_line_input[1])
#print("The out is : ", type(out) , "the inn is : " , type(inn))
values = list(map(int,input().strip().split()))[:out]
output = []
i = 1
if  inn > len(values) :
    print("IMPOSSIBLE")
elif inn > max(values) :
    print("IMPOSSIBLE")
else:
    while i <= inn :
        for j in range (out) :
            if values[j] == i :
                output.append(j+1)
                break
        i = i + 1
    print(*output)
