# (1)
def is_palindrome(word):
    return(word == word[::-1])

# ::을 두번 한 이유는 시작점과 끝점을 정해둘 필요 없이 
# 리스트 내 전체 인덱스를 표현하기 위해서 숫자를 안쓰고 나타낸 것입니다. 
# 'new_list['시작점' : '끝점' : '간격'] 여기서 시작점과 끝점을 안 쓴 것'

# (2)
def is_palindrome(word):
    for i in range (len(word)//2):
        j = len(word) - i - 1
        if (word[i] != word[j]):
            return False
    return True
