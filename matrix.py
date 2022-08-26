while (True):
    try:
        d = int(input('Masukan jumlah dimensi matriks: '))
        result = []
        i = 1
        print('Masukan matriks: ')
        while (i <= d):
            arr = input('')
            arr = arr.split(' ')
            arr = [int(arrItem) for arrItem in arr]
            if (len(arr) != d): 
                print('Jumlah angka dalam baris tidak sesuai dengan jumlah dimensi!')
                continue
            result.append(arr)
            i += 1
        pd = 0
        sd = d - 1
        calc_pd = 0
        calc_sd = 0
        while (pd < d):
            # Primary diagonal
            calc_pd += result[pd][pd]
            # Secondary diagonal
            calc_sd += result[pd][sd]
            pd += 1
            sd -= 1   
        print('Difference:', abs(calc_pd - calc_sd))
        break
    except:
        print('Input invalid try again!')
