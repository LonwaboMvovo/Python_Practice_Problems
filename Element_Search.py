# https://www.practicepython.org/exercise/2014/11/11/20-element-search.html
def is_num_in_list(givin_list, num):
    givin_list.sort()
    print(f'Sorted list: {givin_list}')

    first = 0
    last = len(givin_list) - 1

    while first <= last:
        mid = (first + last)//2
        if givin_list[mid] == num :
            return f'Found {num} at position {mid}'
        else:
            if num < givin_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return 'Not found'


print(is_num_in_list([9,7,8,3,4,5,6,1,48,74,69,0,1], 74))