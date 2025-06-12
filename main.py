from transaction import transaction
import time

trnsc_123 = transaction()

while True:
    print('Menu :')
    print('1. Menambahkan Item')
    print('2. Mengubah Nama Item')
    print('3. Mengubah Jumlah Item')
    print('4. Mengubah Harga Item')
    print('5. Menghapus Sebuah Item')
    print('6. Menghapus semua Item')
    print('7. Mengecek Order')
    print('8. Selesai Berbelanja')

    choice = int(input('Pilih Menu : '))

    if choice == 1:
        while True:
            try:
                num = int(input('Berapa banyak item yang ingin ditambah : '))
                if num < 1:
                    print('Jumlah tem minimal 1, silakan coba lagi')
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
            except ValueError:
                print('Input jumlah dan harga harus dalam angka')
        print(f'Item yang dibeli adalah : {trnsc_123.items[-num:]}')

        

    elif choice == 2:
        old_nama = input('Masukkan Nama Item Lama : ')
        new_nama = input('Masukkan Nama Item Baru : ')
        trnsc_123.update_item_name(old_nama, new_nama)
    
    elif choice == 3:
        try:
            nama_item = input('Masukkan Nama Item : ')
            new_jumlah = int(input('Masukkan Jumlah Item yang Baru : '))
            trnsc_123.update_item_jumlah(nama_item, new_jumlah)
        except ValueError:
            print('Input Jumlah harus dalam angka')
            break
    
    elif choice == 4:
        try:
            nama_item = input('Masukkan Nama Item : ')
            new_harga = int(input('Masukkan Harga Item yang Baru : '))
            trnsc_123.update_item_harga(nama_item, new_harga) 
        except ValueError:
            print('Input harga harus dalam angka')
            break

    elif choice == 5:
        nama_item = input('Masukkan Nama Item : ')
        trnsc_123.delete_item(nama_item)

    elif choice == 6:
        pilihan = input('Apakah Yakin Ingin Menghapus Semua Item (y/t) : ' )
        if pilihan.lower() == 'y':
            trnsc_123.reset_transaction()
        elif pilihan.lower() == 't':
            print('Kembali ke menu utama')
            break
        else:
            print('Input yang dimasukkan salah, kembali ke menu utama')
            break
    
    elif choice == 7:
        trnsc_123.check_order()
        input('Kembali : ')
        continue
    
    elif choice == 8:
        trnsc_123.total_price()
        break
