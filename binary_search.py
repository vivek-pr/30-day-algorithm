
def binary_search(check_list, start, end, key):

    middle = int((end - start) / 2)
    if middle <= 0:
        return 0
    elif check_list[start+middle] == key:
        return start + middle
    elif check_list[start + middle] < key:
        res = binary_search(check_list, start+middle, end, key)
        return res
    else:
        res = binary_search(check_list, start, end-middle, key)
        return res
check_list = [12, 144, 196, 197, 201, 2000, 10000]
res=binary_search(check_list, 0, 7, 201)
print(res)
