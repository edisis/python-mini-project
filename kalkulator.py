"""
program kalkulator sederhana untuk memahami cara kerja operator aritmatika, 
sekaligus cara mengambil input dari user
menggunakan statement condition
"""

bil1 = float(input('Masukan angka ke-1: '))
operator = input('Operator (+ - * / ** %): ')
bil2 = float(input('Masukan angka ke-2: '))

if operator == '+':
    hasil = bil1 + bil2
    print(f'Hasil {bil1} {operator} {bil2} = {round(hasil,2)}')
elif operator == '-':
    hasil = bil1 - bil2
    print(f'Hasil {bil1} {operator} {bil2} = {round(hasil,2)}')
elif operator == '*':
    hasil = bil1 * bil2
    print(f'Hasil {bil1} {operator} {bil2} = {round(hasil,2)}')
elif operator == '/':
    hasil = bil1 / bil2
    print(f'Hasil {bil1} {operator} {bil2} = {round(hasil,2)}')
elif operator == '**':
    hasil = bil1 ** bil2
    print(f'Hasil {bil1} {operator} {bil2} = {round(hasil,2)}')
elif operator == '%':
    hasil = bil1 % bil2
    print(f'Hasil {bil1} {operator} {bil2} = {round(hasil,2)}')
else:
    print(f'Operator {operator} tidak valid!')
    
    
    
