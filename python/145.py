try:
    list1 = list(map(
        int,
        input("Enter the first list: ").split()
    ))

    list2 = list(map(
        int,
        input("Enter the second list: ").split()
    ))

    common = []

    for number in list1:
        if number in list2 and number not in common:
            common.append(number)

    print("Common elements:", common)

except ValueError:
    print("Please enter integers only.")