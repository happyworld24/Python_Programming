def rep_char(c, num):
    print(c * num)

def draw_line_string():
    name = input('Input his/her name: ')
    
    msg1 = f'Hello {name},'
    msg2 = f'Welcome to Seoul'
    
    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
    
    rep_char('-',nstr+2)
    print(f' {msg1} ')
    print(f' {msg2} ')
    rep_char('-',nstr+2)

draw_line_string()