'''Implement Merge algorithm to sort an integer array in ascending order'''
def merge_sort(alist):
    '''merge sort of list'''
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        merge_sort(lefthalf)
        merge_sort(righthalf)
        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i+1
            else:
                alist[k] = righthalf[j]
                j = j+1
            k = k+1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i+1
            k = k+1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j+1
            k = k+1
    return alist
# Driver code to test above
NUM_IN = int(input())
for _ in range(NUM_IN):
    user_input = input()
    list_ = user_input.split()
    arr = []
    for a in list_:
        arr.append(int(a))
    # arr = [12, 11, 13, 5, 6, 7]
    merge_sort(arr)
    print(arr)
