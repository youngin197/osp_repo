def set_op(list1, list2):
    list1 = set(list1)
    list2 = set(list2)
    print('union:', end=' ')
    print(list(list1 | list2))
    print('intersection:', end=' ')
    print(list(list1 & list2))
