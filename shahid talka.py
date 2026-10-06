#===1&2. Input Data Pembeli & jumlah Barang===
nama_pembeli = input("nama pembeli")
jumlah_jenis_barang = int(input("jumlah jenis barang: "))

#List Untuk Menyimpan Semua Data Barang Yang Diinput
keranjang = []
total_belanja = 0

print("\n=== Input Barang ===")
#=== 3. perulangan untuk input data barang ===
for i in range(1,jumlah_jenis_barang + 1):
   print(f"\nbarang ke-{i}")
   nama_barang = input("nama    :")
   harga_barang = int(input("harga   : "))
   jumlah_barang = int(input("jumlah   :"))

# === 4. hitung subtotal ===
subtotal = harga_barang * jumlah_barang
total_belanja += subtotal

#menyimpan data ke dalam list keranjang (opsional, untuk keperluan cetak struk)
keranjang.append({
  "nama": nama_barang,
  "harga": harga_barang,
  "jumlah": jumlah_barang
})
# === 5. percabangan untuk menentukan diskon ===
if total_belanja >= 500000:
  persen_diskon = 15
elif total_diskon >= 250000:
  persen_diskon = 10
elif total_diskon >= 100000:
  persen_diskon = 5
else:
  persen_diskon = 0

# === 6. hitung potongan dan total bayar ===
potongan = int(total_belanja * (persen_diskon / 100))
total_bayar = total_belanja - potongan

# === 7. tampilan struk menggunakan f-string ===
print("\n========== STRUK ==========")
print(f"pembeli       : {nama_pembeli}")
print(f"total belanja : Rp{total_belanja:,}")
print(f"diskon        : {persen_diskon}%")
print(f"potongan      : Rp{potongan:,}")
print(f"total bayar   : Rp{total_bayar:,}")
print("===========================")


#BARU


#===1&2. Input Data Pembeli & jumlah Barang===
nama_pembeli = input("nama pembeli: ")
jumlah_jenis_barang = int(input("jumlah jenis barang: "))

#List Untuk Menyimpan Semua Data Barang Yang Diinput
keranjang = []
total_belanja = 0

print("\n=== Input Barang ===")
#=== 3. perulangan untuk input data barang ===
for i in range(1, jumlah_jenis_barang + 1):
    print(f"\nbarang ke-{i}")
    nama_barang = input("nama    : ")
    harga_barang = int(input("harga   : "))
    jumlah_barang = int(input("jumlah  : "))

    # === 4. hitung subtotal (MASUKKAN KE DALAM FOR) ===
    subtotal = harga_barang * jumlah_barang 
    total_belanja += subtotal

    # menyimpan data ke dalam list keranjang
    keranjang.append({
        "nama": nama_barang,
        "harga": harga_barang,
        "jumlah": jumlah_barang
    })

# === 5. percabangan untuk menentukan diskon ===
if total_belanja >= 500000:
    persen_diskon = 15
elif total_belanja >= 250000:
    persen_diskon = 10
elif total_belanja >= 100000:
    persen_diskon = 5
else:
    persen_diskon = 0

# === 6. hitung potongan dan total bayar ===
potongan = int(total_belanja * (persen_diskon / 100))
total_bayar = total_belanja - potongan

# === 7. tampilan struk menggunakan f-string ===
print("\n========== STRUK ==========")
print(f"pembeli       : {nama_pembeli}")

# Menggunakan enumerate agar lebih mudah membaca isi list keranjang mulai dari indeks 0
for idx, barang in enumerate(keranjang, start=1):
    print(f"\nbarang ke-{idx}")
    print(f"nama   : {barang['nama']}")
    print(f"harga  : Rp{barang['harga']}")
    print(f"jumlah : {barang['jumlah']}")

print("\n===========================")
print(f"total belanja : Rp{total_belanja}")
print(f"diskon        : {persen_diskon}%")
print(f"potongan      : Rp{potongan}")
print(f"total bayar   : Rp{total_bayar}")
print("===========================")
