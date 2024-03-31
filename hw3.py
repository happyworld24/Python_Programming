def get_fixed_price(saled):
    original = saled / (1- (rate/100))
    return int(original)

global rate
rate = int(input('할인율은? '))

a_saled = int(input('A 상품의 할인된 가격은? '))
b_saled = int(input('B 상품의 할인된 가격은? '))

print('A 상품의 정가는', get_fixed_price(a_saled),'원')
print('B 상품의 정가는', get_fixed_price(b_saled),'원')
