import copy
import random
import time
import matplotlib.pyplot as mp


def mergeSort(list):

    if len(list) > 1:
        mid = len(list) // 2
        left_list = list[:mid]
        right_list = list[mid:]
        mergeSort(left_list)
        mergeSort(right_list)

        i = 0
        j = 0
        k = 0

        while i < len(left_list) and j < len(right_list):
            if left_list[i] <= right_list[j]:
                list[k] = left_list[i]
                i += 1
            else:
                list[k] = right_list[j]
                j += 1
            k += 1

        while i < len(left_list):
            list[k] = left_list[i]
            i += 1
            k += 1

        while j < len(right_list):
            list[k] = right_list[j]
            j += 1
            k += 1
    return list




def insertionSort(list):
    start_time = time.time()
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key
    return list

def form_heap(list,length,i):
    highest = i
    left_node = 2 * i + 1
    right_node = 2 * i + 2

    if left_node < length and list[highest] < list[left_node]:
        highest = left_node
    if right_node < length and list[highest] < list[right_node]:
        highest = right_node

    if highest != i:
        list[i], list[highest] = list[highest], list[i]
        form_heap(list, length, highest)

def heapSort(list):
    length = len(list)
    for i in range(length//2 - 1, -1, -1):
        form_heap(list, length, i)
    for i in range(length-1, 0, -1):
        list[i], list[0] = list[0], list[i]
        form_heap(list, i, 0)
    return list

def bubbleSort(list):
    length = len(list)
    for i in range(length-1):
        for j in range(0, length-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

def selectionSort(list):
    length = len(list)
    for i in range(length):
        smallest_num = i
        for j in range (i+1, length):
            if list[smallest_num] > list[j]:
                smallest_num = j
        list[i], list[smallest_num] = list[smallest_num], list[i]
    return list

def partition(list, start, end):
    i = start - 1
    pivot = list[end]

    for j in range(start, end):
        if list[j] <= pivot:
            i = i+1
            list[i], list[j] = list[j], list[i]
    list[i+1], list[end] = list[end], list[i+1]
    return (i+1)

def quicksort(list, start, end):
    if len(list) == 1:
        return list
    if start < end:
        partIndex = partition(list, start, end)
        quicksort(list, start, partIndex-1)
        quicksort(list, partIndex+1, end)
    return list

def threewaypartition(list, first, last, start, mid):
    pivot = list[last]
    end = last

    # Iterate while mid is not greater than end.
    while (mid[0] <= end):

        # Inter Change position of element at the starting if it's value is less than pivot.
        if (list[mid[0]] < pivot):

            list[mid[0]], list[start[0]] = list[start[0]], list[mid[0]]

            mid[0] = mid[0] + 1
            start[0] = start[0] + 1

        # Inter Change position of element at the end if it's value is greater than pivot.
        elif (list[mid[0]] > pivot):

            list[mid[0]], list[end] = list[end], list[mid[0]]

            end = end - 1

        else:
            mid[0] = mid[0] + 1



def threewayQuicksort(list, first, last):
    #when an array contain only 1 element
    if (first >= last):
        return

    #when an array contain only 2 elements
    if (last == first + 1):

        if (list[first] > list[last]):
            list[first], list[last] = list[last], list[first]

            return

    #when an array contain more than 2 elements
    start = [first]
    mid = [first]

    # Function to partition the array.
    threewaypartition(list, first, last, start, mid)

    # Recursively sort sublist that has elements that are less than the pivot.
    threewayQuicksort(list, first, start[0] - 1)

    # Recursively sort sublist that has elements that are larger than the pivot
    threewayQuicksort(list, mid[0], last)
    return list



def sortingComparison():
    arraylist = []
    MergetimeList = []
    InsertiontimeList = []
    heaptimeList = []
    bubbletimeList = []
    selectiontimeList = []
    quicktimeList = []
    threewayQuickTimeList = []
    n = int(input("Enter the number of lists to sort: "))
    print("Enter the size of elements in each of these lists")
    for i in range(0, n):
        sizeOfLists = int(input())
        arraylist.append(sizeOfLists)
    print("The size of the lists :", arraylist)
    finalSelectedAlgos = []
    print(
        "Select the Algorithm to sort from the options : \n 1.Insertion Sort\n 2.Merge Sort \n 3.HeapSort \n 4.BubbleSort \n 5.Selection Sort\n 6.Quick Sort\n 7.Three Way Quick Sort\n 8.All Algorithms Comparison\n\n Press '9' to view the selected algorithms\n")
    while True:
        try:
            algoChoices = int(input())
            if algoChoices == 9:
                if len(finalSelectedAlgos) > 0:
                    print("The selected algorithms are:", finalSelectedAlgos)
                    break
                else:
                    print("No Algorithms Selected..Please choose at least one algorithm to proceed")
            elif (algoChoices >= 1 and algoChoices <= 8):
                finalSelectedAlgos.append(algoChoices)
            elif algoChoices < 1 or algoChoices > 8:
                raise ValueError  # this will send it to the print message and back to the input option

            continue
        except ValueError:
            print("Invalid integer. The number must be in the range of 1-8.")
    for k in range(0, len(arraylist)):
        sortList = []
        unsortedlist = [random.randint(1, 1000) for i in range(arraylist[k])]
        for i in range (0,max(finalSelectedAlgos)):
            sortList.append(copy.deepcopy(unsortedlist))
            j=0
        if 1 in finalSelectedAlgos or 8 in finalSelectedAlgos:
            # InsertionSort
            print("\nThe list before using sort is :\n", sortList[j])
            start_time = time.time()
            SortedInsert = insertionSort(sortList[j])
            InsertiontimeList.append(time.time() - start_time)
            print("The sorted List after using Insertion Sort is :\n", SortedInsert)
            print("Runtime after using Insertion Sort is :\n", InsertiontimeList)
            j+=1

        if 2 in finalSelectedAlgos or 8 in finalSelectedAlgos:
            # MergeSort
            #unsortedlist = [random.randint(1, 1000) for i in range(arraylist[k])]
            print("\nThe list before using sort is :\n", sortList[j])
            start_time = time.time()
            SortedMerge = mergeSort(sortList[j])
            MergetimeList.append(time.time() - start_time)
            print("The sorted List after using Merge Sort is :\n", SortedMerge)
            print("Runtime after using Merge Sort is :\n", MergetimeList)
            j += 1

        if 3 in finalSelectedAlgos or 8 in finalSelectedAlgos:
            #HeapSort
            #unsortedlist = [random.randint(1, 1000) for i in range(arraylist[k])]
            print("\nThe list before using sort is :\n", sortList[j])
            start_time = time.time()
            SortedHeap = heapSort(sortList[j])
            heaptimeList.append(time.time() - start_time)
            print("The sorted List after using Heap Sort is :\n", SortedHeap)
            print("Runtime after using Heap Sort is :\n", heaptimeList)
            j+=1

        if 4 in finalSelectedAlgos or 8 in finalSelectedAlgos:
            # BubbleSort
            #unsortedlist = [random.randint(1, 1000) for i in range(arraylist[k])]
            print("\nThe list before using sort is :\n", sortList[j])
            start_time = time.time()
            SortedBubble = bubbleSort(sortList[j])
            bubbletimeList.append(time.time() - start_time)
            print("The sorted List after using Bubble Sort is :\n", SortedBubble)
            print("Runtime after using Bubble Sort is :\n", bubbletimeList)
            j += 1

        if 5 in finalSelectedAlgos or 8 in finalSelectedAlgos:
            # SelectionSort
            #unsortedlist = [random.randint(1, 1000) for i in range(arraylist[k])]
            print("\nThe list before using sort is :\n", sortList[j])
            start_time = time.time()
            SortedSelection = selectionSort(sortList[j])
            selectiontimeList.append(time.time() - start_time)
            print("The sorted List after using Selection Sort is :\n", SortedSelection)
            print("Runtime after using Selection Sort is :\n", selectiontimeList)
            j += 1

        if 6 in finalSelectedAlgos or 8 in finalSelectedAlgos:
            # QuickSort
            #unsortedlist = [random.randint(1, 1000) for i in range(arraylist[k])]
            lengthOfList = len(sortList[j])
            print("\nThe list before using sort is :\n", sortList[j])
            start_time = time.time()
            SortedQuick = quicksort(sortList[j], 0, lengthOfList - 1)
            quicktimeList.append(time.time() - start_time)
            print("The sorted List after using Quick Sort is :\n", SortedQuick)
            print("Runtime after using Quick Sort is :\n", quicktimeList)
            j += 1

        if 7 in finalSelectedAlgos or 8 in finalSelectedAlgos:
            # threewayQSort
            #unsortedlist = [random.randint(1, 1000) for i in range(arraylist[k])]
            lengthOfList = len(sortList[j])
            print("\nThe list before using sort is :\n", sortList[j])
            start_time = time.time()
            SortedThreeWayQuick = threewayQuicksort(sortList[j], 0, lengthOfList - 1)
            threewayQuickTimeList.append(time.time() - start_time)
            print("The sorted List after using three way Quick Sort is :\n", SortedThreeWayQuick)
            print("Runtime after using three way Quick Sort is :\n", threewayQuickTimeList)
            j += 1


    # graph
    mp.xlabel('Data Size')
    mp.ylabel('Computation Time')
    if 1 in finalSelectedAlgos or 8 in finalSelectedAlgos:
        tm_plot = mp.plot(arraylist, InsertiontimeList, label="Insertion Sort")
    if 2 in finalSelectedAlgos or 8 in finalSelectedAlgos:
        tm_plot = mp.plot(arraylist, MergetimeList, label="Merge Sort")
    if 3 in finalSelectedAlgos or 8 in finalSelectedAlgos:
        tm_plot = mp.plot(arraylist, heaptimeList, label="Heap Sort")
    if 4 in finalSelectedAlgos or 8 in finalSelectedAlgos:
        tm_plot = mp.plot(arraylist, bubbletimeList, label="Bubble Sort")
    if 5 in finalSelectedAlgos or 8 in finalSelectedAlgos:
        tm_plot = mp.plot(arraylist, selectiontimeList, label="Selection Sort")
    if 6 in finalSelectedAlgos or 8 in finalSelectedAlgos:
        tm_plot = mp.plot(arraylist, quicktimeList, label="Quick Sort")
    if 7 in finalSelectedAlgos or 8 in finalSelectedAlgos:
        tm_plot = mp.plot(arraylist, threewayQuickTimeList, label="ThreeWayQuick Sort")
    mp.grid()
    mp.legend()
    mp.show()

#main method which gets the input from user and executes the algorithms
sortingComparison()



