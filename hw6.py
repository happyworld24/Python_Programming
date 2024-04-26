def display_multiplication_table():
    # 2~5단
    for j in range(1,10):
        print()
        for i in range(2,6):
            print(f'{i} x {j} = {i * j:2d}', end='\t')
    # 6~9단
    print()
    for j in range(1,10):
        print()
        for i in range(6,10):
            print(f'{i} x {j} = {i * j:2d}', end='\t')
            
display_multiplication_table()
print()