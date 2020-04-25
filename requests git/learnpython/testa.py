# -*- coding: UTF-8 -*-

# def quick_sort(L):
#     return q_sort(L, 0, len(L) - 1)


def q_sort(L, left, right):
    if left < right:
        pivot = Partition(L, left, right)

        q_sort(L, left, pivot - 1)
        q_sort(L, pivot + 1, right)
    return L


def Partition(L, left, right):
    pivotkey = L[left]

    while left < right:
        print(L)
        while left < right and L[right] >= pivotkey:
            right -= 1
        print("aaaa")
        print(L[left])
        print(L[right])
        print("bbbb")
        L[left] = L[right]
        print(L)
        print("cccaaaaafddsfdsfdsfds f ds")
        while left < right and L[left] <= pivotkey:
            left += 1
        print("dddd")
        print(L[left])
        print(L[right])
        print("eeeeeeeeeeeeeeee")
        print(L)
        L[right] = L[left]
        print("1eeeeeeeeeeeeeeee")
        print(L)
    L[left] = pivotkey

    return left


if __name__ == '__main__':
    L = [5, 9, 1, 11, 6, 7, 2, 4]
    L1 = q_sort(L, 0, len(L)-1)
    print(L1)
