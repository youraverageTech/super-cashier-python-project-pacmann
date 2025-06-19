class transaction:
    # Membuat sebuah list kosong untuk menampung items
    def __init__(self):
        self.items = list()

    # fungsi untuk menambahkan item
    def add_item(self,item):
        self.items.append(item)

    # fungsi untuk mengubah nama item
    def update_item_name(self, nama_item, new_nama):

        item_ditemukan = False

        for item in self.items:
            if item[0] == nama_item:
                item[0] = new_nama
                item_ditemukan = True
                print('Nama item telah berhasil diganti')
                break

        if not item_ditemukan:
            print(f'Item "{nama_item}" tidak ada di dalam transaksi')
    
    # fungsi untuk mengubah jumlah item
    def update_item_jumlah(self, nama_item, new_jumlah):
        
        item_ditemukan = False

        for jumlah in self.items:
            if jumlah[0] == nama_item:
                jumlah[1] = new_jumlah
                item_ditemukan = True
                print('Jumlah item telah berhasil diganti')
                break

        if not item_ditemukan:
            print(f'Item "{nama_item}" tidak ada di dalam transaksi')

    # fungsi untuk mengubah harga item
    def update_item_harga(self, nama_item, new_harga):

        item_ditemukan = False

        for harga in self.items:
            if harga[0] == nama_item:
                harga[2] = new_harga
                item_ditemukan = True
                print('harga item telah berhasil diganti')
                break

        if not item_ditemukan:
            print(f'Item "{nama_item}" tidak ada di dalam transaksi')
    
    # fungsi untuk menghapus item
    def delete_item(self, nama_item):

        item_ditemukan = False
        
        for nama in self.items:
            if nama[0] == nama_item:
                self.items.remove(nama)
                item_ditemukan = True
                print(f'Item "{nama_item}" berhasil dihapus')
                self.show_item()
                break
        
        if not item_ditemukan:
            print(f'Item "{nama_item}" tidak ada di dalam transaksi')

    # fungsi untuk me-reset transaksi
    def reset_transaction(self):
        self.items = []
        print("Semua Item berhasil dihapus")

    # fungsi untuk mengkonfirmasi transaksi
    def check_order(self):
        if not self.items:
            print("Tidak ada item di keranjang")
            return
        
        validasi = True

        for item in self.items:
            for value in item:
                if value in (None, '', 0):
                    validasi = False
                    break  # Keluar dari loop dalam
            if not validasi:
                break  # Keluar dari loop luar

        if validasi:
            self.show_item()
            print("")
            print("Pesanan sudah benar dan tidak ada yang salah")
        else:
            print("Terjadi kesalahan input")
            
    # fungsi untuk menunjukkan item
    def show_item(self):
        print("-" * 70)
        print('No\tNama Item\tJumlah Item\tHarga/Item\tTotal Harga')
        print('-' * 70)

        for item in range(len(self.items)):
            total_harga = self.items[item][1] * self.items[item][2]
            print('{}\t{}\t\t{}\t\t{}\t\t{}'.format(item + 1, self.items[item][0],self.items[item][1],self.items[item][2],total_harga))
            print("-" * 70)

    # fungsi untuk menghitung total transaksi
    def total_price(self):

        diskon_5 = 5/100
        diskon_8 = 8/100
        diskon_10 = 10/100
        total = 0

        self.show_item()

        for item in self.items:
            jumlah  = item[1]
            harga = item[2]
            sub_total = jumlah * harga
            total += sub_total
        
        if total >= 500_000:
            diskon = total * diskon_10
        elif total >= 300_000:
            diskon = total * diskon_8
        elif total >= 200_000:
            diskon = total * diskon_5
        else:
            diskon = 0
        total = total - diskon

        print(f'Total Harga : {total + diskon} | Diskon : {diskon} | Total Belanja yang harus dibayarkan : {total}')
    

    



