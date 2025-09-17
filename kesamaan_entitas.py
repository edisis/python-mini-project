'''
Anda diberikan dua list of integers. 
Tulis sebuah function yang mengembalikan list baru yang berisi elemen-elemen yang ada di kedua list tersebut, 
tanpa duplikat dan dalam keadaan terurut.
Requirements:
1. Return list harus terurut ascending
2. Tidak boleh ada elemen duplikat dalam result
3. Jika tidak ada common elements, return list kosong []
4. Time complexity harus better than O(n²)
'''

def temukan_kesamaan_entitas(list1, list2):
    # method set() untuk menghilangkan duplikat
    # operator & -> intersection (entitas yang ada dikedua set)
    # method sorted() untuk 
    return sorted(set(list1) & set(list2))

print(temukan_kesamaan_entitas([6,3,8,5,2],[0,6,1,5,9]))
print(temukan_kesamaan_entitas([4,9,0],[0,6]))
print(temukan_kesamaan_entitas([8,5,2],[]))