def selectionSort(input):
    for i in range(0,len(input)-1,1):
        min_index = i
        min_v = input[i]
        for j in range(i+1, len(input)-1):
            if(input[j] < min_v):
                min_v = input[j]
                min_index = j

        input[min_index],input[i] = input[i], input[min_index]

    return input


print selectionSort([5,4,1,3,2,8])
