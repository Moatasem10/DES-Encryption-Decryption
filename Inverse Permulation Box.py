size = int(input())
values = list(map(int,input().strip().split()))[:size]
#print(values)
output= []
if len(values) != len(set(values)):
    print("IMPOSSIBLE")
else:
    i = 1
    j = 0
    #flag = False
    while i <= size :
        while j < size :
            if values[j] == i :
                output.append(j+1)
            j += 1
        i += 1
        j = 0
    print(*output)
