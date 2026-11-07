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
