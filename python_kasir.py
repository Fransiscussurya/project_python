#membuat class Produk dengan menginisiasi nama, qty, dan harga
class Produk:
    def __init__(self, nama, qty, harga):
        self.nama = nama
        self.qty = qty
        self.harga = harga
        
#membuat class Transaksi
class Transaksi:
    #membuat list kosong untuk menampung belanjaan
    list_belanja = []
        
    #membuat fungsi untuk menambahkan belanjaan
    def add_item(self):
        """
        fungsi digunakan untuk menambahkan belanjaan
        nama (string) = nama barang yang dibeli
        qty (integer) = jumlah barang yang dibeli
        harga (integer) = harga barang yang dibeli
        
        output: notifikasi berhasil input list belanja dan display list belanjaan
        """
        while True:
            try:
                nama = str(input(f"masukkan barang yang dibeli: ")).lower()
                while True:
                    try:
                        qty = int(input(f"masukkan jumlah barang: "))
                        break
                    except:
                        print(f"data harus dalam angka, silahkan input ulang")
                while True:
                    try:    
                        harga = int(input(f"masukkan harga barang: "))
                        break
                    except:
                        print(f"data harus dalam angka, silahkan input ulang")
                produk = Produk(nama, qty, harga)
                self.list_belanja.append(produk)
                print(f"Barang {nama} sejumlah {qty} dengan harga {harga} telah ditambahkan ke list belanja")
                
                closing_question = str(input(f"sudah selesai? (y/n) ")).lower()
                if closing_question == "y":
                    break    
                else:
                    print(f"silahkan input lagi")
                    
            except ValueError:
                print("=" * 50)
        self.display_item()      
    
    #membuat fungsi untuk mengubah nama item
    def update_item_name(self):
        """
        fungsi untuk mengubah nama item yang sudah diinput
        output: pesan bahwa nama barang telah berhasil diubah
        """
        while True:
            try:
                old_item = str(input(f"masukkan nama barang yang ingin diubah: ")).lower()
                updated_item = None
                
                for item in self.list_belanja:
                    if item.nama == old_item:
                        new_item = str(input(f"masukkan nama barang yang ingin ditambahkan: ")).lower()
                        item.nama = new_item
                        print(f"barang {old_item} telah diubah menjadi {new_item}")
                        updated_item = item
                        break
                        
                if updated_item == None:
                    print(f"barang {old_item} tidak terdapat pada list belanja")
                    
                closing_question_2 = str(input(f"apakah anda ingin mengubah barang lagi? (y/n) ")).lower()
                if closing_question_2 != "y":
                    break
                else:
                    print(f"silahkan input barang yang akan diubah lagi")  
            except ValueError:
                print("")
        self.display_item() 
        
    #membuat fungsi untuk mengubah jumlah item
    def update_item_qty(self):
        """
        fungsi untuk mengubah jumlah item yang sudah diinput
        output: pesan bahwa barang tertentu telah dirubah jumlahnya
        """
        while True:
            try:
                old_item = str(input(f"masukkan nama barang yang jumlahnya ingin diubah: ")).lower()
                            
                for item in self.list_belanja:
                    if item.nama == old_item:
                        old_qty = item.qty
                        new_qty = int(input(f"masukkan jumlah barang yang ingin ditambahkan: "))
                        item.qty = new_qty
                        print(f"barang {old_item} telah diubah jumlahnya dari {old_qty} menjadi {new_qty}")
                        break

                closing_question_3 = str(input(f"apakah anda ingin mengubah jumlah barang lagi? (y/n) ")).lower()
                if closing_question_3 != "y":
                    break
                else:
                    print(f"silahkan input barang yang jumlahnya akan diubah lagi")
            except ValueError:
                print("")
        self.display_item() 
    
    #membuat fungsi untuk mengubah harga item
    def update_item_harga(self):
        """
        fungsi untuk mengubah harga item yang sudah diinput
        output: pesan bahwa barang tertentu telah dirubah harganya
        """
        while True:
            try:
                old_item = str(input(f"masukkan nama barang yang harganya ingin diubah: ")).lower()
                                
                for item in self.list_belanja:
                    if item.nama == old_item:
                        old_harga = item.harga
                        new_harga = int(input(f"masukkan jumlah harga yang ingin ditambahkan: "))
                        item.harga = new_harga
                        print(f"barang {old_item} telah diubah harganya dari {old_harga} menjadi {new_harga}")
                        break

                closing_question_4 = str(input(f"apakah anda ingin mengubah harga lagi? (y/n) ")).lower()
                if closing_question_4 != "y":
                    break
                else:
                    print(f"silahkan input barang yang harganya akan diubah lagi")
            except ValueError:
                print("")
        self.display_item()    
    
    #membuat fungsi untuk menghapus item dengan jumlah dan harga tertentu yang telah di-input
    def delete_item(self):
        """
        fungsi untuk menghapus item yang sudah diinput
        output: pesan bahwa suatu item  dengan jumlah dan harga tertentu telah berhasil dihapus"
        """
        while True:
            try:
                old_item = str(input(f"masukkan nama barang yang ingin dihapus: ")).lower()
                updated_item = None
                
                for item in self.list_belanja:
                    if item.nama == old_item:
                        self.list_belanja.remove(item)
                        updated_item = item
                        print(f"barang {old_item} telah berhasil dihapus")
                
                if updated_item == None:
                    print(f"barang {old_item} tidak terdapat pada list belanja")
                    
                closing_question_5 = str(input(f"apakah anda ingin menghapus barang lagi? (y/n) ")).lower()
                if closing_question_5 != "y":
                    break
                else:
                    print(f"silahkan input barang yang akan dihapus lagi")  
            except ValueError:
                print("")
        self.display_item() 
    
    #membuat fungsi untuk menghapus seluruh transaksi
    def reset_transaksi(self):
        """
        fungsi untuk me-reset seluruh transaksi yang sudah diinput
        output: pesan bahwa semua transaksi telah berhasil dihapus"
        """
        while True:
            try:
                reset_question = str(input(f"apakah anda yakin ingin menghapus transaksi (y/n) ")).lower()
                if reset_question == "y":
                    self.list_belanja.clear()
                    print(f"semua transaksi telah dihapus!")
                    self.display_item()
                    break
                elif reset_question == "n":
                    self.display_item()
                    break
                else:
                    print(f"pastikan anda menjawab dengan benar, silahkan pilih ulang")
            except ValueError:
                print("")
    
    #membuat fungsi untuk melakukan final check order
    def check_order(self):
        """
        fungsi untuk melakukan final check order
        output: 1) notifikasi kesalahan pesanan jika ada kekosongan atau tipe data non-string pada nama item
                2) notifikasi pesanan sudah benar jika tidak ada kesalahan input
        """
        order_error = False
        for item in self.list_belanja:
            if item.nama == "" or not isinstance(item.nama, str):
                order_error = True
        if order_error:
            print(f"terdapat kesalahan input nama item, silahkan lihat orderan anda")
            self.display_item()
            self.update_item_name()
        else:
            print(f"pesanan anda sudah benar")
            self.display_item()
            
    #membuat fungsi untuk menampilkan total harga, diskon yang didapat, dan jumlah yang harus dibayarkan 
    def total_price(self):
        """
        fungsi untuk menghitung total harga.
        terdapat diskon sebesar:
        a) 5% untuk pesanan di atas Rp 200.000 dan di bawah Rp 300.000
        b) 8% untuk pesanan di atas Rp 300.000 dan di bawah Rp 500.000
        c) 10% untuk pesanan di atas Rp 500.000
        
        output: total harga, diskon yang didapat, dan jumlah yang harus dibayarkan
        """
        
        self.display_item()
        total_price = 0
        for item in self.list_belanja:
            total_price += (item.qty * item.harga)
        print(f"\nTotal belanja anda adalah: Rp {total_price}")
        
        if 200_000 <= total_price < 300_000:
            discounted_price = total_price * 0.95
            print(f"Belanjaan anda lebih dari Rp 200000, anda mendapat diskon sebesar 5%!")
            print(f"Harga yang harus anda bayar adalah sebesar Rp {discounted_price}")
        elif 300_000 <= total_price < 500_000:
            print(f"Belanjaan anda lebih dari Rp 300000, anda mendapat diskon sebesar 8%!")
            discounted_price = (total_price * 0.92)
            print(f"Harga yang harus anda bayar adalah sebesar Rp {discounted_price}")
        elif total_price > 500_000:
            print(f"Belanjaan anda lebih dari Rp 500000, anda mendapat diskon sebesar 10%!")
            discounted_price = (total_price * 0.90)
            print(f"Harga yang harus anda bayar adalah sebesar Rp {discounted_price}")
        
    #membuat fungsi untuk menampilkan list belanja dalam bentuk tabel sederhana
    def display_item(self):
        """
        fungsi untuk menampilkan list belanja yang sudah di-input, di-pdate, ataupun di-delete/di-reset
        output: tabel list belanjaan
        """
        
        print("\nDaftar Belanja")
        print("{:<20} {:<10} {:<10} {:<10}".format("Nama Barang", "Jumlah", "Harga", "Total Harga"))
        print("=" * 70)
        for item in self.list_belanja:
            total_harga = item.qty * item.harga
            print("{:<20} {:<10} {:<10} {:<10}".format(item.nama, item.qty, item.harga, total_harga))    