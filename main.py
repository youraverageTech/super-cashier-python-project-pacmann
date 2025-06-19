from transaction import transaction
import time

trnsc_123 = transaction()

try :
    nama_i = input('Masukkan Nama Item : ')
    jumlah_i = int(input('Masukkan Jumlah Item : '))
    harga_i = int(input('Masukkan Harga Item : '))
    trnsc_123.add_item([nama_i,jumlah_i,harga_i])
    print("")
except ValueError : 
    print('Kesalahan dalam memasukkan Input yang diperlukan')

while True:
    # Membuat Opsi pilihan action
    print('Menu :')
    print('1. Menambahkan Item')
    print('2. Mengubah Nama Item')
    print('3. Mengubah Jumlah Item')
    print('4. Mengubah Harga Item')
    print('5. Menghapus Sebuah Item')
    print('6. Menghapus semua Item')
    print('7. Mengecek Order')
    print('8. Melihat Total Transaksi')
    print('9. Selesai Transaksi')

    choice = int(input('Pilih Menu : '))

    if choice == 1:
        # Opsi untuk Menambahkan item
        while True:
            try:
                num = int(input('Berapa banyak item yang ingin ditambah : '))
                if num < 1:
                    print('Jumlah item minimal 1, silakan coba lagi')
                    continue
                break
            except ValueError:
                print('Input harus dalam angka')

        for count in range(1, num + 1):
            try:
                print(f'Item ke-{count} :')
                nama = input('Masukkan Nama Item : ')
                jumlah = int(input('Masukkan Jumlah Item : '))
                harga = int(input('Masukkan Harga Item : '))
                trnsc_123.add_item([nama, jumlah, harga])
                print("")
                time.sleep(3)
            except ValueError:
                print('Input jumlah dan harga harus dalam angka')
        print(f'Item yang dibeli adalah : {trnsc_123.items[-num:]}')

        

    elif choice == 2:
        # Opsi untuk meng-update nama item
        try:
            old_nama = input('Masukkan Nama Item Lama : ')
            new_nama = input('Masukkan Nama Item Baru : ')
            trnsc_123.update_item_name(old_nama, new_nama)
            print("")
            time.sleep(3)
        except ValueError:
            print('Nama Item tidak ada di dalam transaksi')
    
    elif choice == 3:
        # Opsi untuk meng-update jumlah item
        try:
            nama_item = input('Masukkan Nama Item : ')
            new_jumlah = int(input('Masukkan Jumlah Item yang Baru : '))
            trnsc_123.update_item_jumlah(nama_item, new_jumlah)
            print("")
            time.sleep(3)
        except ValueError:
            print('Input Jumlah harus dalam angka')
            break
    
    elif choice == 4:
        # Opsi untuk meng-update harga item
        try:
            nama_item = input('Masukkan Nama Item : ')
            new_harga = int(input('Masukkan Harga Item yang Baru : '))
            trnsc_123.update_item_harga(nama_item, new_harga) 
            print("")
            time.sleep(3)
        except ValueError:
            print('Input harga harus dalam angka')
            break

    elif choice == 5:
        # Opsi untuk menghapus item
        try:
            nama_item = input('Masukkan Nama Item : ')
            trnsc_123.delete_item(nama_item)
            print("")
            time.sleep(3)
        except ValueError:
            print("Nama Item tidak ada di dalam transaksi")

    elif choice == 6:
        # Opsi untuk menghapus semua item 
        pilihan = input('Apakah Yakin Ingin Menghapus Semua Item (y/t) : ' )
        if pilihan.lower() == 'y':
            trnsc_123.reset_transaction()
            print("")
            time.sleep(3)
        elif pilihan.lower() == 't':
            print('Kembali ke menu utama')
            print("")
            time.sleep(3)
            break
        else:
            print('Input yang dimasukkan salah, kembali ke menu utama')
            print("")
            time.sleep(3)
            break
    
    elif choice == 7:
        # Opsi untuk melihat semua item yang sudah dimasukkan
        trnsc_123.check_order()
        input('Kembali : (enter) ')
        print("")
        time.sleep(3)
        continue
    
    elif choice == 8:
        # Opsi untuk melihat total transaksi
        trnsc_123.total_price()
        print("")
        time.sleep(3)
    
    elif choice == 9:
        # Opsi untuk menyelesaikan transaksi
        trnsc_123.total_price()
        break
