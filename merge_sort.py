# /********************************************************************** 
 #  *                                                                    *
 #  *  Problem: Mergesort                                                *
 #  *                                                                    *
 #  *  Prompt: Given an unsorted array of numbers,                       *
 #  *          return a sorted array using Mergesort sort.               *
 #  *                                                                    *
 #  *  Input:  An unsorted array                                         *
 #  *  Output: A sorted array                                            *
 #  *                                                                    *
 #  *  Example: input = [3,9,1,4,7] , output = [1,3,4,7,9]               *
 #  *                                                                    *
 #  *  What are the time and auxilliary space complexity?                *
 #  *                                                                    *
 #  **********************************************************************/
 
def mergeSort(lst):
    
    if len(lst)>1:
        mid = len(lst)//2
        lefthalf = lst[:mid]
        righthalf = lst[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                lst[k]=lefthalf[i]
                i=i+1
            else:
                lst[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            lst[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            lst[k]=righthalf[j]
            j=j+1
            k=k+1
    

input = [5,96,73,17,1,75,2,20,5]
mergeSort(input)
print(input)