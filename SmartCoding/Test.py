import random

random_number = random.randint(1, 100)

#print(random_number)
count = 1
while True:
    try : 
        my_number = int(input("1부터 100 사이의 숫자를 입력하세요 : "))
        
        if my_number > random_number :
            print("Down")
            print()
        elif my_number < random_number :
            print("Up")
            print()
        elif my_number == random_number :
            print(f"축하합니다. {count}회 만에 맞쳤습니다.")
            break
        count = count + 1
    except:
        print("숫자로 입력하세요")
