def statistik_nilai(nilai):
    minimum = min(nilai)
    maksimum = max(nilai)
    rata_rata = round(sum(nilai) / len(nilai), 2)
    return {"minimum": minimum, "maksimum": maksimum, "rata_rata": rata_rata}
