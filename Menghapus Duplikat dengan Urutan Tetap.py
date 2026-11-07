def hapus_duplikat(angka):
    hasil = []
    seen = set()
    for x in angka:
        if x not in seen:
            seen.add(x)
            hasil.append(x)
    return hasil
