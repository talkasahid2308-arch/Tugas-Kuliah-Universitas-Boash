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
