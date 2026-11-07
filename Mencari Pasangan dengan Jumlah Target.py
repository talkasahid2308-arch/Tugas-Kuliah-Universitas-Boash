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
