def insertion_sort(mylist):
    shifts = 0
    n = len(mylist)

    for i in range(1, n):
        insert_index = i
        current_value = mylist.pop(i)
        for j in range(i - 1, -1, -1):
            if mylist[j] > current_value:
                insert_index = j
        shifts += i - insert_index
        mylist.insert(insert_index, current_value)

    return shifts


if __name__ == "__main__":
    mylist = [19, 1, 20, 47, 47, 91]
    print("Shifts:", insertion_sort(mylist))
    print(mylist)