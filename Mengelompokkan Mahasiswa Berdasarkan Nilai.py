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
