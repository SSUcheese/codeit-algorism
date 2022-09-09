# binary_search algorism / 이진탐색 알고리즘

def binary_search(element, some_list):
    start_index = 0
    end_index = len(some_list) - 1

    while start_index <= end_index:
        mid = (start_index + end_index) // 2
        if some_list[mid] == element:
            return mid
        elif some_list[mid] > element:
            end_index = mid - 1
        else: start_index = mid + 1
    return None

    # 코드를 작성하세요.


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
