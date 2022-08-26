while(True):
    try:
        n = int(input('Given a number N: '))
        result = ''
        i = 1
        m = n
        while (i <= n):
            j = m
            while (j > 1):
                result += ' '
                j -= 1
            m -= 1 
            s = 1
            while (s <= i):
                result += '*'
                s += 1
            i += 1
            result += '\n'
        print(result)
        break
    except:
        print('Input invalid try again!')