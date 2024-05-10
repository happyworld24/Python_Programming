def buy(bag):
    print('[구입]')
    item = input('상품명? ') # 상품 이름을 입력받기 
    if (item == '') : # item이 빈 문자열이면 루프 빠져나가기, enter
        return False
    count = input('수량은? ') # 상품 수량을 입력받기
    bag[item] = count # item : count를 장바구니에 추가  
    print(f'장바구니에 {item} {bag[item]}개가 담겼습니다.\n')

def show(bag):
    # 장바구니의 모든 상품 이름 출력 (딕셔너리 이름 사용) 
    print(f'\n>>> 장바구니 보기: {bag}\n')

def find(bag):
    print('[검색]')
    find = input('장바구니에서 확인하고자 하는 상품은? ')
    if find in bag :
        print(f'{find}은(는) {bag[find]}개 담겨 있습니다.')
    else :
        print(f'장바구니에 {find}은(는) 없습니다.')
        
# ----- 주 프로그램부 ------
shopping_bag = {} # 장바구니
while True :
    if buy(shopping_bag) == False:
        break
show(shopping_bag)
find(shopping_bag)