# 리스트의 인텍스에 대해 반복문을 사용하기 위해서는 for문을 사용하는 것이 쉽다. 
# 반복문을 돌다가 element 를 찾으면 현재 위치를 return 해야한다. 
# element가 some_list에 존재하지 않는다는건 None을 return 하면 된다. 

# 정리 : 리스트를 돌면서, 내가 찾고자 하는 원소와 일치하는 원소를 찾으면 인덱스를 리턴해주고, 끝까지 돌았는데
# 결국 찾지 못했다면, None을 리턴해주었다. 

def linear_search(element, some_list):
    for i in range(len(some_list)):
        if some_list[i] == element:
            return i
    return None

# 테스트
print(linear_search(2, [2, 3, 5, 7, 11]))
print(linear_search(0, [2, 3, 5, 7, 11]))
print(linear_search(5, [2, 3, 5, 7, 11]))
print(linear_search(3, [2, 3, 5, 7, 11]))
print(linear_search(11, [2, 3, 5, 7, 11]))