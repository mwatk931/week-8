def selection_sort(mylist):
    swaps = 0
    n = len(mylist)

    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if mylist[j] < mylist[min_index]:
                min_index = j

        if min_index != i:
            mylist[i], mylist[min_index] = mylist[min_index], mylist[i]
            swaps += 1

    return swaps


if __name__ == "__main__":
    mylist = [19, 1, 20, 47, 47, 91]
    print("Swaps:", selection_sort(mylist))
    print(mylist)