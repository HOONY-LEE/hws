1. 무엇이 중복일까
문자열을 전달 받아 해당 문자열에서 중복해서 나타난 문자들을 담은 list를 반환하는
duplicated_letters 함수를 작성하시오.

```
def duplicated_letters(string):
    result = []
    duple_set = set()
    for i in string:
        if(string.count(f'{i}') >= 2):
            duple_set.add(i)
    result = list(duple_set)

    return result

duplicated_letters(‘apple’) # => [‘p’]
duplicated_letters(‘banana’) # => [’a’, ‘n’]

```


2. 소대소대
문자열을 전달 받아 해당 문자열을 소문자와 대문자가 번갈아 나타나도록 변환하여
반환하는 low_and_up 함수를 작성하시오.
이때, 전달 받는 문자열은 알파벳으로만 구성된다.

```
def low_and_up(string):
    result = ''
    for i in range(0, len(string)):
        if i % 2 == 0:
            result += (string[i].lower())
        else:
            result += (string[i].upper())
    return result

low_and_up(‘apple’) # => aPpLe
low_and_up(‘banana’) # => bAnAnA

```


3. 솔로 천국 만들기
정수 0부터 9까지로 이루어진 list를 전달 받아, 연속적으로 나타나는 숫자는 하나만 남
기고 제거한 list를 반환하는 lonely 함수를 작성하시오.
이때, 제거된 후 남은 수들이 담긴 list의 요소들은 기존의 순서를 유지해야 한다.

```
def lonely(list):
    result = []
    result.append(list[0])

    for i in range(1, len(list)):
        if list[i] != list[i-1]:
            result.append(list[i])
            
    print(result)
    return result

lonely([1, 1, 3, 3, 0, 1, 1]) # => [1, 3, 0, 1]
lonely([4, 4, 4, 3, 3]) # => [4, 3]

```



