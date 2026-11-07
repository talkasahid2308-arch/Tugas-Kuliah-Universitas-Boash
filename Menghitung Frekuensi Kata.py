def frekuensi_kata(kalimat):
    # Menghapus tanda baca titik dan koma, lalu mengubah ke huruf kecil
    kalimat_bersih = kalimat.replace('.', '').replace(',', '').lower()
    kata_kata = kalimat_bersih.split()
    
    frekuensi = {}
    for kata in kata_kata:
        frekuensi[kata] = frekuensi.get(kata, 0) + 1
    return frekuensi
