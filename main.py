from fungsi import tambah, kurang, kali, bagi, pangkat  
from pilihan import kalkulator

kalkulator()
'''
    Mencetak pilihan operasi matematika yang ada
'''
  
pilihan = input("Pilih operasi (1/2/3/4/5): ")
'''
    Menerima Input pilihan operasi matematika
'''

angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
'''
    Menerima Input 2 angka yang akan digunakan dalam perhitungan
'''

def input_angka():
  if pilihan == "1":
    hasil = tambah(angka1, angka2)
  elif pilihan == "2":
    hasil = kurang(angka1, angka2)
  elif pilihan == "3":
    hasil = kali(angka1, angka2)
  elif pilihan == "4":
    hasil = bagi(angka1, angka2)
  elif pilihan == "5":
    hasil = pangkat(angka1, angka2)
  else:
    print("Pilihan tidak valid!")
    
    return
  print("Hasil:", hasil)
    
input_angka()
