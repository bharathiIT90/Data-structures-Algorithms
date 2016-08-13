def insertionSort(input):
    for i in range(0,len(input)-1):
        temp = input[i]
        ptr = i
        while(ptr > 0 and temp < input[ptr-1]):
            input[ptr]=input[ptr-1]
            ptr-=1
        input[ptr]=temp

    return input
    
print insertionSort([5,4,1,3,2,8])