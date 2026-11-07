def terbesar_kedua(angka):
    angka_unik = list(set(angka))
    if len(angka_unik) < 2:
        return None
    angka_unik.sort(reverse=True)
    return angka_unik[1]
