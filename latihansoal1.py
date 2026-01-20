print("=====JAWABAN LK1=====")

nama = "elzhar ararya adam"
umur = 17
tipeumur = type(umur)

print("Nama Siswa: ", nama)
print("Umur Siswa: ", umur)
print ("Tipe Umur:", tipeumur)

print("=====JAWABAN LK2=====")

print ("Mengapa kita harus menggunakan int(...) sebelum fungsi input() pada baris tahun_lahir?")
print ("Jawaban: Agar jawaban user / pengisi form hanya bisa mengisi dengana angka bilangan bulat") 
# Agar jawaban user / pengisi form hanya bisa mengisi dengana angka bilangan bulat 

print("====LK3====")

barang = input("Masukkan nama barang yang dibeli: ")
harga = int(input("Masukkan harga barang: "))
jumlah = int(input("Masukkan jumlah barang yang dibeli: "))
total = harga * jumlah 
tipeharga = type(harga)
tipejumlah = type(jumlah)

print(f"Kamu membeli {barang} sebanyak {jumlah} dengan harga Rp. {total}.")

print("========")
print("Tipe harga:", tipeharga)
print("Tipe jumlah:", tipejumlah)
print("========")

print("====LK4====")

print("Sistem Invoice Penjualan Digital")

namabarang = input("Masukkan nama barang        : ")
hargasatuan = float(input("Masukkan harga satuan      : "))
jumlahbeli = int(input("Masukkan jumlah beli       : "))
diskon = 10  
ppn = 11    

subtotal = hargasatuan * jumlahbeli
potongan_harga = subtotal * (diskon / 100)
total_sebelum_pajak = subtotal - potongan_harga
pajakppn = total_sebelum_pajak * (ppn / 100)
total_akhir = total_sebelum_pajak + pajakppn

print("\n====== STRUK BELANJA TOKO KOMPUTER ======")
print(f"Nama Barang  : {namabarang}")
print(f"Harga Satuan : Rp {hargasatuan}")
print(f"Jumlah Beli  : {jumlahbeli}")
print("----------------------------------------")
print(f"Subtotal            : Rp {subtotal}")
print(f"Diskon ({diskon}%)  : -Rp {potongan_harga}")
print(f"Total Sebelum Pajak : Rp {total_sebelum_pajak}")
print(f"PPN ({ppn}%)        : Rp {pajakppn}")
print("----------------------------------------")
print(f"Total  : Rp {total_akhir}")
print("========================================")

