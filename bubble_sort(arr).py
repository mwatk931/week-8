def bubble_sort(mylist):
    swaps = 0
    n = len(mylist)

    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if mylist[j] > mylist[j + 1]:
                mylist[j], mylist[j + 1] = mylist[j + 1], mylist[j]
                swaps += 1
                swapped = True
        if not swapped:
            break

    return swaps


if __name__ == "__main__":
    mylist = [19, 1, 20, 47, 47, 91]
    print("Swaps:", bubble_sort(mylist))
    print(mylist)
