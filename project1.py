"""
Math 560
Project 1
Fall 2020

Partner 1:  Xunyu Chu
Partner 2:  Ke Chen
Date:       9/28 2020
"""

"""
SelectionSort
"""
def SelectionSort(listToSort):  # SelectionSort, input is the list and output is still the list. In place sort.
    for i in range(0,len(listToSort)):  # the range of iteration
        index = i                       # As i is unmodified, so we use index to represent i
        for j in range(i,len(listToSort)):  # this will start the iteration in every element to choose the minimum one
            if(listToSort[j] <= listToSort[index]):  # find the minimum
                index = j
        listToSort[i],listToSort[index] = listToSort[index],listToSort[i]; # swap

    return listToSort

"""
InsertionSort
"""


def InsertionSort(listToSort):   # Insertion Sort, input is the list and output is also the list. In place .
    for i in range(1, len(listToSort)): # the element to insert
        for j in range(i, 0, -1):   # iterate in the sorted array
            if (listToSort[j] < listToSort[j - 1]):   #bubble
                listToSort[j], listToSort[j - 1] = listToSort[j - 1], listToSort[j];

    return listToSort
# def InsertionSort(listToSort):
#     lenth = len(listToSort)
#     for i in range(1,lenth):
#         for j in range(0,i):
#             if(listToSort[i-j] <= listToSort[i-j-1]):
#                 listToSort[i-j],listToSort[i-j-1] = listToSort[i-j-1],listToSort[i-j]
#             else:
#                 break
#
#     return listToSort

"""
BubbleSort
"""
def BubbleSort(listToSort):  # Bubble Sort, input is the list and output is also the list. In place .
    length = len(listToSort)  # this variable is for readable
    for i in range(1,length): # The length of sorted array after iteration
        for j in range(0 , length - i ): #The number for comparation
            if(listToSort[j] >= listToSort[j + 1]):
                listToSort[j], listToSort[j+1] = listToSort[j+1] , listToSort[j]

    return listToSort

"""
MergeSort
"""
def MergeSort(listToSort):  # MergeSort, input is the list and output is also the list. Use new space but the output is inplace .
    def help(list,l,m,r): #merge two sorted array
        list1 = list[l:m]
        list2 = list[m:r]
        index = l
        index1 = 0
        index2 = 0
        length1 = len(list1)
        length2 = len(list2)   # Because the index is len - 1, so I just set it as len and use index < length
        while(index1 < length1 and index2 < length2):#compare two element which respectively in list1 and list2
            if(list1[index1] < list2[index2]):
                list[index] = list1[index1]
                index1 += 1
                index += 1
            else:
                list[index] = list2[index2]
                index2 += 1
                index += 1
        if(index1 < length1):#consider the situation when all rest elements in list2 is greater than list1
            for i in list1[index1:]:
                list[index] = i
                index += 1
        if(index2 < length2):#consider the situation when all rest elements in list1 is greater than list2
            for i in list2[index2:]:
                list[index] = i
                index += 1
        #return list
    def help2(list,l,r):#The ring  of the list is [l,r)
        if ((r-l) > 1):
            mid = (r - l) // 2 + l#the middle index, use // to consider (r-l) is odd

            help2(list, l, mid)#spilt the array into two list
            help2(list, mid, r)

            help(list, l, mid, r)#use help function to merge list1 and list2.
        else:
            return
    help2(listToSort,0,len(listToSort))
    #listToSort = help(list1, list2)
    return listToSort

"""
QuickSort

Sort a list with the call QuickSort(listToSort),
or additionally specify i and j.
"""
def QuickSort(listToSort, i=0, j=None):
    # Set default value for j if None.
    if j == None:
        j = len(listToSort)
    if(i >= j - 1 ):  # when to end the recursion
        return
    pindex = (j - i) // 2 + i  # we choose the middle index
    p = listToSort[pindex]  # the corresponding value of middle index
    index = i
    less = []            # assistant array contains the element less than p
    bigger = []          # assistant array contains the element bigger than p
    while(index < j):    # assign the element in input into less array and bigger array
        if(pindex == index):  # skip when encounter the pindex element
            index += 1
            continue
        if(listToSort[index] <= p):
            less.append(listToSort[index])
        elif (listToSort[index] > p):
            bigger.append(listToSort[index])
        index += 1      #move afterward
    len1 = len(less)
    listToSort[i: i + len1] = less   # put the assigned value into the input array
    listToSort[i+len1] = p           # i to i + len1 - 1 is less, i + len1 is the p, i + len1 + 1 to j  is bigger
    listToSort[i+len1 + 1 : j] = bigger
    QuickSort(listToSort,i,i + len1)  #recursion
    QuickSort(listToSort,i + len1 + 1,j)
    return listToSort

"""
Importing the testing code after function defs to ensure same references.
"""
from project1tests import *

"""
Main function.
"""
if __name__ == "__main__":
    print('Testing Selection Sort')
    print()
    testingSuite(SelectionSort)
    print()
    print('Testing Insertion Sort')
    print()
    testingSuite(InsertionSort)
    print()
    print('Testing Bubble Sort')
    print()
    testingSuite(BubbleSort)
    print()
    print('Testing Merge Sort')
    print()
    testingSuite(MergeSort)
    print()
    print('Testing Quick Sort')
    print()
    testingSuite(QuickSort)
    print()
    print('DEFAULT measureTime')
    print()
    measureTime()