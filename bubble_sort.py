# /********************************************************************** 
#  *                                                     *
#  *                                                                    *
#  *  Problem: Insertion Sort                                           *
#  *                                                                    *
#  *  Prompt: Given an unsorted array of numbers,                       *
#  *          return a sorted array using insertion sort.               *
#  *                                                                    *
#  *  Input:  An unsorted array                                         *
#  *  Output: A sorted array                                            *
#  *                                                                    *
#  *  Example: input = [3,9,1,4,7] , output = [1,3,4,7,9]               *
#  *                                                                    *
#  *  What are the time and auxilliary space complexity?                *
#  *                                                                    *
#  **********************************************************************/

#  /**********************************************************
#   *                                                        *
#   *  Problem: Selection Sort                               *
#   *                                                        *
#   *  Prompt: Given an unsorted array of numbers,           *
#   *          return a sorted array using insertion sort.   *
#   *                                                        *
#   *  Input: An unsorted array                              *
#   *  Output: A sorted array                                *
#   *                                                        *
#   *  Example: input = [8,3,2,10] output = [2,3,8,10]       *
#   *                                                        *
#   *  What are the time and auxilliary space complexity?    *
#   *  What is the best case time complexity?                *
#   *                                                        *
#   **********************************************************/

#  /**********************************************************
#   *                                                        *
#   *  Problem: Bubble Sort                                  *
#   *                                                        *
#   *  Prompt: Given an unsorted array of numbers,           *
#   *          return a sorted array using bubble sort.      *
#   *                                                        *
#   *  Input: An unsorted array                              *
#   *  Output: A sorted array                                *
#   *                                                        *
#   *  Example: input = [8,3,2,10] output = [2,3,8,10]       *
#   *                                                        *
#   *  What are the time and auxilliary space complexity? O(n^2), O(1)    *
#   *                                                        *
#   **********************************************************/


def bubbleSort(input):
    for end in range(len(input)-1, -1, -1):
        swap = False
        for item in range(0,end):
            if (input[item]>input[item+1]):
                input[item],input[item+1] = input[item+1],input[item]
                swap=True
                
        if(swap==False):
            break

    return input
            


print bubbleSort([5,4,1,3,2,8])







    

