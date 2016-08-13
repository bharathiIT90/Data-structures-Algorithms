 # /********************************************************************** 
 #  *                                                       *
 #  *                                                                    *
 #  *  Problem: Quicksort                                                *
 #  *                                                                    *
 #  *  Prompt: Given an unsorted array of numbers,                       *
 #  *          return a sorted array using Quicksort sort.               *
 #  *                                                                    *
 #  *  Input:  An unsorted array                                         *
 #  *  Output: A sorted array                                            *
 #  *                                                                    *
 #  *  Example: input = [3,9,1,4,7] , output = [1,3,4,7,9]               *
 #  *                                                                    *
 #  *  What are the time and auxilliary space complexity?                *
 #  *                                                                    *
 #  **********************************************************************/

def quickSort(input):
   quickSortHelper(input,0,len(input)-1)

def quickSortHelper(input,first,last):
   if first<last:

       splitpoint = partition(input,first,last)

       quickSortHelper(input,first,splitpoint-1)
       quickSortHelper(input,splitpoint+1,last)


def partition(input,first,last):
   pivotvalue = input[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and input[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while input[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = input[leftmark]
           input[leftmark] = input[rightmark]
           input[rightmark] = temp

   temp = input[first]
   input[first] = input[rightmark]
   input[rightmark] = temp


   return rightmark

input = [5,96,73,17,1,75,2,20,5]
quickSort(input)
print(input)



