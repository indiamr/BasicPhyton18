Teori = input("Nilai Ujian Teori :")
a=float(Teori)
Praktek = input("Nilai Ujian Prakek :")
b=float(Praktek)
if a >= 70 and b >= 70 :
    print("Selamat, Anda lulus!")
elif a >= 70 and b < 70:
    print("Anda harus mengulang ujian praktek")
elif a < 70 and b >= 70:
    print("Anda harus mengulang ujian teori")
else:
    print("Anda harus mengulang ujian teori dan praktek")