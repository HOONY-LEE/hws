1. Built-in 함수와 메서드
sorted()와 .sort()의 차이점을 코드의 실행 결과를 활용하여 설명하시오.

```
my_list = [5, 3, 3, 1, 7, 9]
my_list.sort()
print(my_list)

my_list2 = [5, 3, 3, 1 ,7 ,9]
new_list = sorted(my_list2)
print(my_list2)
print(new_list)

## 실행결과
# [1, 3, 3, 5, 7, 9]
# [5, 3, 3, 1, 7, 9]
# [1, 3, 3, 5, 7, 9]


```

sort()는 원본 my_list 자체를 바꾸는 메서드이고,
sorted()는 원본 my_list는 보존하고, 정렬된 값만 반환하는 함수이다.



2. .extend()와 .append()
.extend()와 .append()의 차이점을 코드의 실행 결과를 활용하여 설명하시오.

```
my_list = [ 1, 2 ,3 ,4 ,5 ]

my_list.append('78')
print(my_list)
my_list.extend('78')
print(my_list)

## 출력

# [1, 2, 3, 4, 5, '78']
# [1, 2, 3, 4, 5, '78', '7', '8']

```

.append() 는 숫자던 문자던 하나의 값만 마지막에 추가한다.
.extend() 는 리스트와 리스트를 합치는 개념으로 여러 값을 넣으면 인덱스 하나당 1개의 값을 할당한다.


3. 복사가 잘 된 건가?
아래의 코드를 실행 하였을 때, 변수 a와 b에 담긴 list의 요소가 같은지 혹은 다른지
여부를 판단하고 그 이유를 작성하시오.

a와 b 모두 같은 list의 요소를 담고있다.
b와 a 모두 해당 리스트의 주소값을 가르키고 있기 때문에, a[2] 의 값을 수정하면
b 역시 같은 메모리 주소를 가지고 있어 두 값이 모두 변한다.



```
a = [1, 2, 3, 4, 5]
b = a
a[2] = 5
print(a)
print(b)

```