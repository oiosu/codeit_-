# 이진탐색은 반씩 줄여 나가는 알고리즘 이다. 
# 탐색 범위의 시작관 끝을 나타내는 변수를 각각 보관하면 좋다. 
# 시작할 때의 탐색 버위는 some_list 의 처음부터 끝까지 이므로 인덱스 0부터 인텍스 len(some_list) -1 까지 이다. 

def binary_search(element, some_list):
    start_index = 0
    end_index = len(some_list) - 1

# 반복적으로 하려는 것에 대해 생각해 보기 
# (1) 현재 탐색 범위에서의 중간 값이 element 면, 중간 인덱스를 리턴한다. 
# (2) 그렇지 않으면 탐색 번위를 줄인다. 

# 헷갈린다면, 경우를 나누어 생각해보자. 
# (1) element 가 중간값보다 작으면, 오른쪽 반은 더이상 볼 필요가 없다. 
# (2) element 가 중간값보다 크면, 왼쪽 반은 더 이상 볼 필요가 없다. 

# 범위를 줄이다 보면 start_index 와 end_index 가 엇갈리는 순간이 올 것이다. 그때가 되면 더 이상 탐새할 범위가 없다.

def binary_search(element, some_list):
    start_index = 0
    end_index = len(some_list) - 1
    
    while start_index <= end_index:
        midpoint = (start_index + end_index) // 2
        if some_list[midpoint] == element:
            return midpoint
        elif some_list[midpoint] > element:
            end_index = midpoint - 1
        else:
            start_index = midpoint + 1
    return None

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))