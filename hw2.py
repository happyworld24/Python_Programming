# 함수 작성
def get_integer(money):
    money = int(money)
    return money

# (반환값 없어도 됨)
def exchange(money):
    change_500 = money // 500
    money %= 500
    change_100 = money // 100
    money %= 100
    change_50 = money // 50
    money %= 50
    change_10 = money // 10
    money %= 10

    print('500원 동전의 개수:',change_500)
    print('100원 동전의 개수:',change_100)
    print('50원 동전의 개수:',change_50)
    print('10원 동전의 개수:',change_10)
    

# 입력 받기
money = input('동전으로 교환하고자 하는 금액은? ')
# 정수로 바꾸기
money = get_integer(money)
# 환전 및 출력
exchange(money)
    