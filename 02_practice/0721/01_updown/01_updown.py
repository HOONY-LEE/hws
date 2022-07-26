import random

is_playing = True
  # 몇 번만에 정답을 맞혔는지 담는 변수
counts = 0
while is_playing:
    print('================================')
    print('        Up and Down Game        ')
    print('================================')

   
    answer = random.randint(1, 10000  )# 1이상 10000이하의 난수



    answer = 100    #random.randint(1, 10000  )# 1이상 10000이하의 난수


    answer = random.randint(1, 10000  )# 1이상 10000이하의 난수

    

    # 여기부터 코드를 작성하세요.
    
    # 1-1) 
    number_invalid = True       ## 사용자 입력값 유효성 검사
    while number_invalid:
        number = int(input('1이상 10000 이하의 숫자를 입력하세요. :'))        
        if 1 <= number <= 10000 :
            number_invalid = False
            counts += 1
            break
        else:
            print('잘못된 범위의 숫자를 입력하셨습니다. 다시 입력해주세요')
            number_invalid = True
    print(f'사용자 입력값 : {number}')
    print(f'{counts}회차 시도')
    if number < answer :
        print('Up!!!')

    elif number > answer :
        print('Down!!!')

    else:
        print('Correct!!!')
        print(f'{counts}회 만에 정답을 맞히셨습니다')
        restart = input('게임을 재시작 하시려면 y, 종료하시려면 n을 입력하세요. :')
        if restart == 'y':
            counts = 0
            pass
        elif restart == 'n':
            is_playing = False   
print('이용해주셔서 감사합니다. 게임을 종료합니다.')    
<<<<<<< HEAD

=======
            

    

    
>>>>>>> 411747400f167626c41535433688896cd1b410a2
