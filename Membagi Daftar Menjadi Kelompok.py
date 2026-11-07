def bagi_kelompok(data, ukuran):
    hasil = []
    for i in range(0, len(data), ukuran):
        hasil.append(data[i:i + ukuran])
    return hasil
