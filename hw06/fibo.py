def fibo(n):
    fibo = [0 for i in range(100000)]
    fibo[0] = 0
    fibo[1] = 1
    ans = []
    for i in range(1,n+1):
        if i==1:
            ans.append('1')
        else:
            fibo[i] = fibo[i-1] + fibo[i-2]
            ans.append(str(fibo[i]))
    print(' '.join(ans))
    print('F%d = %d' % (n, fibo[i]))
