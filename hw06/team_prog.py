import bin2hex as bh
import setop as st
import fibo as fi

menu = 0
while True:
    menu = input('Select menu: 1)b2h 2)set 3)fibo 4)exit ? ')
    menu = int(menu)
    if menu == 1:
        x = int(input('input bin number: '))
        bh.bi2hex(x)
        print('')
    elif menu == 2:
        print('input the 1st list:', end=' ')
        x1 = list(map(int, input().split()))
        print('input the 2nd list:', end=' ')
        x2 = list(map(int, input().split()))
        st.set_op(x1, x2)
        print('')
    elif menu == 3:
        n = input('fibonacci number: ')
        fi.fibo(int(n))
        print('')
    elif menu == 4:
        print('exit the program...')
        break
    else:
        print('wrong menu number..')
