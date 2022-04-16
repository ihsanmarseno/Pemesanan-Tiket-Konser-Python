from prettytable import PrettyTable
import os
import random
import datetime

# Variable Global
nama_tiket = []
harga = []
kode = []

# Function
def garis():
    print("=" * 40)

def garis2():
    print("-" * 40)

def pembuka():
    print("=" * 40)
    print("\t\t\b\b\b\b\bPembelian Tiket BTS")
    print("=" * 40)

def pesanTiket(brp_tiket):
    i = 0
    while i < brp_tiket:
        print("Tiket ke - " ,i+1)
        kode.append(int(input("Masukkan kode : ")))
        if kode[i] == 1:
            harga.append(300000)
            nama_tiket.append("Reguler")
        elif kode[i] == 2:
            harga.append(500000)
            nama_tiket.append("VIP")
        elif kode[i] == 3:
            harga.append(1500000)
            nama_tiket.append("VVIP")
        else:
            print("Kode tidak ditemukan")
            print("Ulang dari pengisian awal")
            exit()
        i += 1
    return brp_tiket

def cetakTotalHarga(brp_tiket):
    y = 0 
    total = 0
    while y < brp_tiket:
        total += harga[y]
        y += 1
    print("Total harga\t\t: " + str(total))
    return total

# End Function

pembuka()
nama = input("Nama\t\t: ")
no_telp = input("No. Telepon\t: ")
print("\n")
garis()
print("\t\tMENU TIKET")
garis()

# Create Table
x = PrettyTable(["Kode", "Nama Tiket", "Harga (IDR)"])
x.add_row([1, "Reguler", 300000])
x.add_row([2, "VIP", 500000])
x.add_row([3, "VVIP", 1500000])
print(x)

brp_tiket = int(input("Berapa tiket? "))

# Call Function for booking some ticket
pesanTiket(brp_tiket)

print("\n")
garis()  
print("\t\tPEMBAYARAN")
garis()

cetakTotalHarga(brp_tiket)


b = PrettyTable(["Kode", "Pembayaran", "Admin (IDR)"])
b.add_row([1, "VA Bank", 5000])
b.add_row([2, "DANA", 0])
print(b)


total3 = 0
while True:
    metode_pembayaran = int(input("Pilih metode pembayaran : "))
    if metode_pembayaran == 1:
      print("Metode Pembayaran\t: VA Bank")
      metode_pembayaran = "VA BANK"
      total3 += 5000
      break
    elif metode_pembayaran == 2:
      print("Metode Pembayaran\t: DANA")
      metode_pembayaran = "DANA"
      total3 += 0
      break
    else:
        continue
print("\n")
garis()
print("\t\t\b\b\b\b\b\bPEMBAYARAN BERHASIL")
garis()

while True:
    print("KETIK 1. Cetak Struk  ||  0.Exit")
    cetak = int(input("Ketik perintah : "))

    if cetak == 1:
        break
    elif cetak == 0:
        exit()
    else:
        continue

garis()
total2 = 0
z = 0 
os.system('cls')
garis()
print("\tSTRUK PEMBELIAN TIKET BTS")
garis()
print("\n")
print("Nama\t\t  : " + nama)
print("No Telepon\t  : " + no_telp)
print("Kode Booking\t  : " + str(random.random()))
print("Tanggal Pembelian : " + str(datetime.date.today()))
print("Metode Pembayaran : " + str(metode_pembayaran))
print("Tanggal Konser    : 2022-12-12")
print("\n")
print("START KONSER JAM 18.00")
print("\n")
print("PENTING!!!")
print("CETAK TIKET MENGGUNAKAN KODE BOOKING")

print("\n")

garis2()
print("Kode\tNama Tiket\tHarga")
garis2()

while z < brp_tiket:
    total2 += int(harga[z])
    print("%i\t%s\t\t%s"% (kode[z], nama_tiket[z], harga[z]))
    z += 1

garis2()
print("\tJumlah\t\t" + str(total2))
print("\tBiaya Admin\t" + str(total3))
total4 = total2 + total3
print("\tTotal Harga\t" + str(total4))
os.system('pause')