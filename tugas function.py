# ==========================================
# 1. Menghitung Statistik Nilai
# ==========================================
def statistik_nilai(nilai):
    minimum = min(nilai)
    maksimum = max(nilai)
    rata_rata = round(sum(nilai) / len(nilai), 2)
    return {"minimum": minimum, "maksimum": maksimum, "rata_rata": rata_rata}


# ==========================================
# 2. Menghapus Duplikat dengan Urutan Tetap
# ==========================================
def hapus_duplikat(angka):
    hasil = []
    seen = set()
    for x in angka:
        if x not in seen:
            seen.add(x)
            hasil.append(x)
    return hasil


# ==========================================
# 3. Mencari Angka Terbesar Kedua
# ==========================================
def terbesar_kedua(angka):
    angka_unik = list(set(angka))
    if len(angka_unik) < 2:
        return None
    angka_unik.sort(reverse=True)
    return angka_unik[1]


# ==========================================
# 4. Menghitung Frekuensi Kata
# ==========================================
def frekuensi_kata(kalimat):
    # Menghapus tanda baca titik dan koma, lalu mengubah ke huruf kecil
    kalimat_bersih = kalimat.replace('.', '').replace(',', '').lower()
    kata_kata = kalimat_bersih.split()
    
    frekuensi = {}
    for kata in kata_kata:
        frekuensi[kata] = frekuensi.get(kata, 0) + 1
    return frekuensi


# ==========================================
# 5. Mengelompokkan Mahasiswa Berdasarkan Nilai
# ==========================================
def kelompokkan_nilai(data):
    hasil = {"A": [], "B": [], "C": [], "D": []}
    for nama, nilai in data.items():
        if nilai >= 85:
            hasil["A"].append(nama)
        elif 70 <= nilai <= 84:
            hasil["B"].append(nama)
        elif 55 <= nilai <= 69:
            hasil["C"].append(nama)
        else:
            hasil["D"].append(nama)
    return hasil


# ==========================================
# 6. Memeriksa Anagram
# ==========================================
def cek_anagram(teks1, teks2):
    bersih1 = sorted(teks1.replace(" ", "").lower())
    bersih2 = sorted(teks2.replace(" ", "").lower())
    return bersih1 == bersih2


# ==========================================
# 7. Membagi Daftar Menjadi Kelompok
# ==========================================
def bagi_kelompok(data, ukuran):
    hasil = []
    for i in range(0, len(data), ukuran):
        hasil.append(data[i:i + ukuran])
    return hasil


# ==========================================
# 8. Mencari Pasangan dengan Jumlah Target
# ==========================================
def pasangan_target(angka, target):
    pasangan_unik = set()
    n = len(angka)
    
    # Memeriksa setiap pasangan berdasarkan posisi (indeks) berbeda
    for i in range(n):
        for j in range(i + 1, n):
            if angka[i] + angka[j] == target:
                # Urutkan angka dari kecil ke besar agar unik di dalam set
                p = tuple(sorted((angka[i], angka[j])))
                pasangan_unik.add(p)
                
    # Urutkan hasil akhir berdasarkan angka pertama lalu angka kedua
    return sorted(list(pasangan_unik))


# ==========================================
# 9. Menjumlahkan Dua Matriks
# ==========================================
def jumlah_matriks(matriks1, matriks2):
    # Memeriksa dimensi baris
    if len(matriks1) != len(matriks2):
        return None
    # Memeriksa dimensi kolom
    if len(matriks1[0]) != len(matriks2[0]):
        return None
        
    hasil = []
    for i in range(len(matriks1)):
        baris = []
        for j in range(len(matriks1[0])):
            baris.append(matriks1[i][j] + matriks2[i][j])
        hasil.append(baris)
    return hasil


# ==========================================
# 10. Mencari Rentetan Angka Meningkat Terpanjang
# ==========================================
def rentetan_meningkat(angka):
    if not angka:
        return []
        
    rentetan_terpanjang = []
    rentetan_saat_ini = [angka[0]]
    
    for i in range(1, len(angka)):
        if angka[i] > angka[i-1]:
            rentetan_saat_ini.append(angka[i])
        else:
            if len(rentetan_saat_ini) > len(rentetan_terpanjang):
                rentetan_terpanjang = rentetan_saat_ini
            rentetan_saat_ini = [angka[i]]
            
    # Pengecekan terakhir setelah loop selesai
    if len(rentetan_saat_ini) > len(rentetan_terpanjang):
        rentetan_terpanjang = rentetan_saat_ini
        
    return rentetan_terpanjang
