def bi2hex(x): 
    x_bi = bin(x)
    x_ten = int('0b'+ str(x), 2)
    x_h = hex(x_ten)
    print('hexa number:', end=' ')
    print(x_h)
