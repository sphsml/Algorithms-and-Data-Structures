import random
import time

def sortTimeUsing(sortf, A):
    timeA = time.time()
    sortf(A)
    timeB = time.time() - timeA
    return timeB
    
def selectionSort(A):
	for i in range(len(A)):
		imin = findMin(i, A)
		swap(i, imin, A)

def findMin(i, A):
	imin = i
	for j in range(i+1, len(A)):
		if A[j] < A[imin]:
			imin = j
	return imin

def swap(i, j, A):
	tmp = A[i]
	A[i] = A[j]
	A[j] = tmp

def insertionSort(A):
	for i in range(1, len(A)):
		insert(A[i], A, i)

def insert(v, A, hi):
	for i in range(hi-1, -1, -1):
		if v>= A[i]:
			A[i+1] = v
			return
		A[i+1] = A[i]
	A[0] = v

A = [30, 25, 67, 99, 8, 16, 28, 63, 12, 20]

selectionResult = sortTimeUsing(selectionSort, A)

def randomIntArray(s,n):
    array = [0]
    if(s != 0):
        array = [0] * s
    t = s
    if(s>n):
        n = s
        s = t
    for i in range(len(array)):
        array[i] = random.randint(s, n)
    return array

def binSearch(arr, v, start, end):
    while start < end:
        mid = start + (end - start) // 2
        if arr[mid] < v:
            start = mid + 1
        else:
            end = mid
    return start

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        insert_position = binSearch(arr, key, 0, j + 1)
        for k in range(i, insert_position, -1):
            arr[k] = arr[k - 1]
        arr[insert_position] = key

    return arr

tests = (randomIntArray(i,100) for i in [0,10,100])
for A in tests:
    B = insertionSort(A)
    print(f"Length: {len(A)} - Sorted array:", B)