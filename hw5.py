def read_single_digit(digit):
    digits_map = {
        '0': '영',
        '1': '일',
        '2': '이',
        '3': '삼',
        '4': '사',
        '5': '오',
        '6': '육',
        '7': '칠',
        '8': '팔',
        '9': '구'
    }
    return digits_map.get(digit)

def read_number():
    integer = input('세 자리 정수 입력: ')
    digits = [read_single_digit(digit) for digit in integer]
    print(f'{digits[0]} {digits[1]} {digits[2]}')

read_number()
