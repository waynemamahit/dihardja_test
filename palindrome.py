str_input = input('Masukan karakter untuk cek palindrome: ')
if (len(str_input) > 10): 
    print('Karakter yang dimasukan lebih dari 10!')
    exit()
print('Yes' if (''.join(list(reversed(list(str_input)))).lower() == str_input.lower()) else 'No')


