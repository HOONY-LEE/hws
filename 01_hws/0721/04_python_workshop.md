1. 간단한 N의 약수 (SWEA #1933)
입력으로 1개의 정수 N이 주어진다. 정수 N의 약수를 오름차순으로 출력하는
프로그램을 작성하시오.

```
[제약 사항]
N은 1이상 1,000이하의 정수이다. (1 ≤ N ≤ 1,000)
[입력]
입력으로 정수 N이 주어진다.
[출력]
정수 N의 모든 약수를 오름차순으로 출력한다.
[입력 예시]
10
[출력 예시]
1 2 5 10
```


```

N = int(input())

def factors(n):
    result_lst = []
    for i in range(1, n+1):
        if n % i == 0:
            result_lst.append(i)
    print(result_lst)
    return result_lst

factors(N)

```


2. List의 합 구하기
정수로만 이루어진 list를 전달 받아 해당 list의 모든 요소들의 합을 반환하는
list_sum 함수를 built-in 함수인 sum() 함수를 사용하지 않고 작성하시오.


```
def list_sum(lst):
    result = 0
    for i in lst:
        result += i
    return result

list_sum([1, 2, 3, 4, 5])

```








3. Dictionary로 이루어진 List의 합 구하기
Dictionary로 이루어진 list를 전달 받아 모든 dictionary의 'age' key에 해당하는 value
들의 합을 반환하는 dict_list_sum 함수를 built-in 함수인 sum() 함수를 사용하지 않고
작성하시오.


```
def dict_list_sum(lst):
    result = 0
    for diction in lst:
        result += diction['age']
    return result

dict_list_sum([{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}])


```