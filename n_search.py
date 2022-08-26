while (True):
    try:
        n = int(input('Masukan nilai N: '))
        i = 0
        result = 'Tidak ditemukan!'
        while (i != n and i < n):
            for p in range(4):
                j = i
                if p < 2:
                    i += 1
                else:
                    i *= 2
                if i == n:
                    result = j
                    break
        print(result)
        break
    except:
        print('Input invalid try again!')