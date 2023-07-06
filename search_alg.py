import random
def sequential_search(item, l:list)->bool:
    """Returns True if the item is in the list else False. Equivalent to 'in' operator"""

    pos = 0
    while pos < len(l):
        if l[pos] == item:
            return True #The implementation given in the book uses an extra variable to stop the search once found. We can also return the moment we find it
        else:
            pos +=1
    return False

def ordered_sequential_search(item, l:list)->bool:
    """Returns True if the item is in the list else False. Equivalent to 'in' operator. 
    l must be ordered, else false negatives will occur"""

    pos = 0
    while pos<len(l):
        if l[pos] == item:
            return True
        elif l[pos] > item:
            return False
        else:
            pos +=1
    #Can also do all this with an super loop


"""
Suppose you are doing a sequential search of the list [15, 18, 2, 19, 18, 0, 8, 14, 19, 14]. How
many comparisons would you need to do in order to find the key 18?
1. 5
2. 10
3. 4
4. 2

2

Suppose you are doing a sequential search of the ordered list [3, 5, 6, 8, 11, 12, 14, 15, 17, 18].
How many comparisons would you need to do in order to find the key 13?
1. 10
2. 5
3. 7
4. 6

7 (there we would stop searching)

"""

#Binary search o biseccion para los amigos

def binary_search(item, l:list, a=0, b=None)->bool:
    """Returns True if the item is in the list else False. Equivalent to 'in' operator. 
    l must be ordered, else false negatives will occur"""

    if b==None:
        b = len(l)
        #For the first call we need a value for b
    if b-a == 0:
        return False

    midpoint =(b+a)//2
    if l[midpoint] == item:
        return True
    elif l[midpoint] > item:
        return binary_search(item, l, a, midpoint)
    else:
        return binary_search(item, l, midpoint+1, b)
    
test_list =  [3, 5, 6, 8, 11, 12, 14, 15, 17, 18] 
print(binary_search(18, test_list))
print(binary_search(6,test_list))
#Implemented following the improvement on the book: using slicing makes this worse than linear
print(test_list[0:5])


"""
Suppose you have the following sorted list [3, 5, 6, 8, 11, 12, 14, 15, 17, 18] and are using the
recursive binary search algorithm. Which group of numbers correctly shows the sequence of
comparisons used to find the key 8.
1. 11, 5, 6, 8
2. 12, 6, 11, 8
3. 3, 5, 6, 8
4. 18, 12, 6, 8

2: 12,6,11,8
Suppose you have the following sorted list [3, 5, 6, 8, 11, 12, 14, 15, 17, 18] and are using the
recursive binary search algorithm. Which group of numbers correctly shows the sequence of
comparisons used to search for the key 16?
1. 11, 14, 17
2. 18, 17, 15
3. 14, 17, 15
4. 12, 17, 15

4:12,17,15
"""

"""
In a hash table of size 13 which index positions would the following two keys map to? 27, 130
1. 1, 10
2. 13, 0
3. 1, 0
4. 2, 3

3: 1,0

Suppose you are given the following set of keys to insert into a hash table that holds exactly 11
values: 113, 117, 97, 100, 114, 108, 116, 105, 99. Which of the following best demonstrates the
contents of the has table after all the keys have been inserted using linear probing?
1. 100, __, __, 113, 114, 105, 116, 117, 97, 108, 99
2. 99, 100, __, 113, 114, __, 116, 117, 105, 97, 108
3. 100, 113, 117, 97, 14, 108, 116, 105, 99, __, __
4. 117, 114, 108, 116, 105, 99, __, __, 97, 100, 113

2.
"""


def sort_test(f):
    print(f([1,2,3,4,5]))
    for i in range(200):
        l = [random.randint(1,2000) for x in range(50)]
        print(l)
        l_sorted = f(l)
        print(l_sorted)
        l.sort()
        print(l)
        print(l == l_sorted)
        if l !=l_sorted: 
            print("mal")
            break
        print(f"#############################\n")
    print(f)

def bubble_sort(l:list)->list:
    """Sort the list in ascending order in place. Also returns the sorted list"""
    """Efficiency: O(n^2). We do n-1 passes (worst case), and do n-1 comparisons on the first pass, n-2 on the second...
        So its basically the sum of the n-1 firsts integers, which is a quadratic function.
    """
    #This is actually short bubble, done ahead of time
    sorted = False
    for pass_n in range(len(l)-1, 0, -1):
        sorted = True
        for i in range(pass_n):
            if l[i] > l[i+1]:
                sorted = False #Slight change in the book's code to stop the algorithm if the list is already sorted
                l[i], l[i+1] = l[i+1], l[i]
        if sorted:
            break
    return l

print(bubble_sort([5,2,4,3,5]))

#sort_test(bubble_sort)


"""Self Check
Suppose you have the following list of numbers to sort: [19, 1, 9, 7, 3, 10, 13, 15, 8, 12] which
list represents the partially sorted list after three complete passes of bubble sort?
1. [1, 9, 19, 7, 3, 10, 13, 15, 8, 12]
2. [1, 3, 7, 9, 10, 8, 12, 13, 15, 19]
3. [1, 7, 3, 9, 10, 13, 8, 12, 15, 19]
4. [1, 9, 19, 7, 3, 10, 13, 15, 8, 12]


2: each ith pass of a bubble sort sends the ith biggest item to its position
"""

def selection_sort(l:list)->list:
    """Sort the list in ascending order in place. Also returns the sorted list"""
    """Efficiency: O(n^2). We do n-1 passes (worst case), and do n-1 comparisons on the first pass, n-2 on the second...
        So its basically the sum of the n-1 firsts integers, which is a quadratic function. This differs from bubble sort in that it does not make 
        an assignment for every comparison. This *is* relevant to efficiency but is not seen on O-notation
    """

    sorted = False
    for pass_n in range(len(l)-1,0,-1):
        sorted = True
        pos_max = 0
        for i in range(pass_n+1): #If you've done bubble sort this '+1' might be confusing: think that bubble sort looks to the item ahead
            #This doesn't, so we need i to reach len(l)
            if l[i] > l[pos_max]:
                sorted = False
                pos_max = i
        l[pos_max], l[pass_n] = l[pass_n], l[pos_max]
        if sorted:
            break
    return l

#sort_test(selection_sort)

"""
#Bubble vs selection:
import timeit
t1 = timeit.Timer("bubble_sort([random.randint(1,2000) for x in range(300)])", "from __main__ import bubble_sort,random")
print(f"Bubble sort: {t1.timeit(1000)}ms")
t2 = timeit.Timer("selection_sort([random.randint(1,2000) for x in range(300)])", "from __main__ import selection_sort,random")
print(f"Selectin sort: {t2.timeit(1000)}ms")
#As we can see, while both are quadratic algorithms, the number of assignments really makes a difference
"""

"""Self Check
Suppose you have the following list of numbers to sort: [11, 7, 12, 14, 19, 1, 6, 18, 8, 20] which
list represents the partially sorted list after three complete passes of selection sort?
1. [7, 11, 12, 1, 6, 14, 8, 18, 19, 20]
2. [7, 11, 12, 14, 19, 1, 6, 18, 8, 20]
3. [11, 7, 12, 13, 1, 6, 8, 18, 19, 20]
4. [11, 7, 12, 14, 8, 1, 6, 18, 19, 20]

4: selection sort changes only x*2 items in x passes: the local max and the position it should go in

"""

def insertion_sort(l:list)->list:
    """Sort the list in ascending order in place. Also returns the sorted list"""
    """In terms of efficiency it is again the sum of the first n integers: O(n^2). It does however less operations than bubble sort, which has
    a pretty similar idea. It is faster than bubble sort, but still the number of operations maekes it costlier than selection, even if the operations
    themselves are lighter"""
    for i in range(1, len(l)):
        current_value=l[i]
        pos = i
        while pos >0 and l[pos-1] > current_value:
            l[pos] = l[pos-1]
            pos -=1
        l[pos] = current_value
    return l

#sort_test(insertion_sort)

"""
import timeit
t1 = timeit.Timer("bubble_sort([random.randint(1,2000) for x in range(300)])", "from __main__ import bubble_sort,random")
print(f"Bubble sort: {t1.timeit(1000)}ms")
t2 = timeit.Timer("selection_sort([random.randint(1,2000) for x in range(300)])", "from __main__ import selection_sort,random")
print(f"Selection sort: {t2.timeit(1000)}ms")
t3 = timeit.Timer("insertion_sort([random.randint(1,2000) for x in range(300)])", "from __main__ import insertion_sort,random")
print(f"Insertion sort: {t3.timeit(1000)}ms")"""


"""
Self Check
Suppose you have the following list of numbers to sort: [15, 5, 4, 18, 12, 19, 14, 10, 8, 20] which
list represents the partially sorted list after three complete passes of insertion sort?
1. [4, 5, 12, 15, 14, 10, 8, 18, 19, 20]
2. [15, 5, 4, 10, 12, 8, 14, 18, 19, 20]
3. [4, 5, 15, 18, 12, 19, 14, 10, 8, 20]
4. [15, 5, 4, 18, 12, 19, 14, 8, 10, 20]

3: k passes of an insertion sort sort the first k items
"""
def gap_insertion_sort(l, start, gap): #Auxiliar function for shell sort
    for i in range(start + gap, len(l), gap):
        current_value = l[i]
        position = i
        while position >= gap and l[position - gap] > current_value:
            l[position] = l[position - gap]
            position = position - gap
        l[position] = current_value


def shell_sort(l:list)->list:
    """Sort the list in ascending order in place. Also returns the sorted list"""
    """Now a very important idea is that sublists are not the first k elements, but elements taken by jumping k spaces. This is what makes it
    so efficient. While this gets into way better times than the rest, it is still not comparable to python's native sort: we should also take overhead
    and language into account. Shell sort is between O(n^2) and O(n*2log(n))
    """
    sublist_count = len(l)//2
    while sublist_count >0:
        for start_position in range(sublist_count):
            gap_insertion_sort(l, start_position, sublist_count)
        sublist_count = sublist_count//2
    return l
shell_sort([54, 26, 93, 17, 77, 31, 44, 55, 20])
"""Self Check
Given the following list of numbers: [5, 16, 20, 12, 3, 8, 9, 17, 19, 7] Which answer illustrates
the contents of the list after all swapping is complete for a gap size of 3?
1. [5, 3, 8, 7, 16, 19, 9, 17, 20, 12]
2. [3, 7, 5, 8, 9, 12, 19, 16, 20, 17]
3. [3, 5, 7, 8, 9, 12, 16, 17, 19, 20]
4. [5, 16, 20, 3, 8, 12, 9, 17, 20, 7]

1
"""

"""import timeit
t1 = timeit.Timer("bubble_sort([random.randint(1,2000) for x in range(300)])", "from __main__ import bubble_sort,random")
print(f"Bubble sort: {t1.timeit(1000)}ms")
t2 = timeit.Timer("selection_sort([random.randint(1,2000) for x in range(300)])", "from __main__ import selection_sort,random")
print(f"Selection sort: {t2.timeit(1000)}ms")
t3 = timeit.Timer("insertion_sort([random.randint(1,2000) for x in range(300)])", "from __main__ import insertion_sort,random")
print(f"Insertion sort: {t3.timeit(1000)}ms")
t4 = timeit.Timer("shell_sort([random.randint(1,2000) for x in range(300)])", "from __main__ import shell_sort,random")
print(f"Shell sort: {t4.timeit(1000)}ms")
t5 = timeit.Timer("sorted([random.randint(1,2000) for x in range(300)])", "from __main__ import shell_sort,random")
print(f"Shell sort: {t5.timeit(1000)}ms")

"""
print([1,2,3,4][0:1])

def merge_sort(l:list, left_index = 0, right_index = None)->list:
    if right_index == None:
        right_index = len(l)
    #Checker for the starting, *not base*, case
    if right_index>left_index+1:
        mid_index = (left_index + right_index)//2
        l = merge_sort(l,left_index, mid_index) + merge_sort(l,mid_index, right_index) #Division and recursive call
        i=left_index % (right_index-left_index)
        j=mid_index% (right_index-left_index)
        k=left_index% (right_index-left_index)
        temp = [None]*(right_index-left_index)
        while i <mid_index % (right_index-left_index)and j <= (right_index+1)% (right_index-left_index):
            if l[i] < l[j]:
                temp[k] = l[i]
                i+=1
            else:
                temp[k] = l[j]
                j+=1
            k+=1
        while i < mid_index% (right_index-left_index):
            temp[k] = l[i]
            i+=1
            k+=1
        while j <= (right_index)% (right_index-left_index):
            temp[k] = l[j]
            j+=1
            k+=1
        return temp
    return l[left_index:right_index]



def merge_sort(l:list, left_index = 0, right_index = None)->list:
    if right_index == None:
        right_index = len(l)
    #Checker for the starting, *not base*, case
    mid_index = (left_index + right_index)//2
    if left_index < right_index:
        merge_sort(l, left_index, mid_index)
        merge_sort(l, mid_index+1, right_index)

    i=left_index
    j=mid_index+1
    k=0
    temp = [None]*(right_index-left_index+1)
    while i <=mid_index and j <= right_index:
        if l[i] < l[j]:
            temp[k] = l[i]
            i+=1
        else:
            temp[k] = l[j]
            j+=1
        k+=1
    if i <= mid_index:
        temp[k:] = l[i:mid_index+1]
    if j <= right_index:
        temp[k:] = l[j:right_index+1]
    k=0
    while left_index <= right_index:
        l[left_index] = temp[k]
        left_index+=1
        k+=1

print(merge_sort([2,1,3,4]))