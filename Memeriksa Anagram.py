def cek_anagram(teks1, teks2):
    bersih1 = sorted(teks1.replace(" ", "").lower())
    bersih2 = sorted(teks2.replace(" ", "").lower())
    return bersih1 == bersih2
