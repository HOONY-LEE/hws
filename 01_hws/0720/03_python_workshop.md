1. 세로로 출력하기
자연수 number를 입력받아, 1부터 number까지의 수를 세로로 한 줄씩 출력하시오.

```
number = int(input())

for i in range(number):
    print(i + 1)
```





2. 가로로 출력하기
자연수 number를 입력받아, 1부터 number까지의 수를 가로로 한 칸씩 띄어 출력하시오.

```
number = int(input())
num_list = []
for i in range(number):
    num_list.append(i+1)
for i in range(len(num_list)):
    print(num_list[i], end = ' ')
```




3. 거꾸로 세로로 출력하기
자연수 number를 입력받아, number부터 0까지의 수를 세로로 한 줄씩 출력하시오.


```
number = int(input())

for i in range(number, -1, -15):
    print(i)

```


1. 거꾸로 출력해 보아요 (SWEA #1545)
자연수 number를 입력받아, number부터 0까지의 수를 가로로 한 칸씩 띄어 출력하시오.

```
number = int(input())
num_list = []
for i in range(number, -1, -1):
    num_list.append(i)

for i in range(len(num_list)):
    print(num_list[i], end = ' ')

```



5. N줄 덧셈 (SWEA #2025)
입력으로 자연수 number가 주어질 때, 1부터 주어진 자연수 number까지를 모두 더한
값을 출력하시오. 단, 주어지는 숫자는 10000을 넘지 않는다. 예를 들어, 주어진 숫자가
10일 경우 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55이므로, 출력해야 할 값은 55이다

```
number = int(input())
result = 0
for i in range(number):
    result += i+1

print(result)

```





6. 삼각형 출력하기
자연수 number를 입력받아, 아래와 같이 높이가 number인 직각 삼각형을 출력하시오.

```
입력 예시
7

출력 예시
*
**
***
****
*****
******
*******


number = int(input())

for i in range(number):
    print(' ' * (number-i) + '*' * (i+1))



```


1. 중간값 찾기 (SWEA #2063 변형)
중간값은 통계 집단의 수치를 크기 순으로 배열 했을 때 전체의 중앙에 위치하는 수치를
뜻한다. 리스트 numbers에 입력된 숫자에서 중간값을 출력하라.


```
numbers = list(map(int, input().split()))

numbers.sort()
num_len = len(numbers)
result = 0
if num_len % 2 == 0:
     result = [ numbers[num_len // 2 - 1], numbers[num_len // 2 ] ]
else:
     result = numbers[num_len // 2]    


print(result)

```