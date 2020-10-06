"""
버블정렬하여 리스트 정렬하기
"""
def bubbleSort(arr):
    new_arr = sorted(arr)
    while arr != new_arr:
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr

arr = [4,1,7,35,85,24,31,33]

print(bubbleSort(arr))