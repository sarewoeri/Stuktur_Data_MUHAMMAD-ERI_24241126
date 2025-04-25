print("Nama: Muhammad Eri Nim : 24241126")

inputuser = int(input("masukan angka yang bernilai kurang dari 24 atau lebih besar dari 26:"))

#+++++24-------------
#memeriksa angka kurang dari 24
iskurangdari = (inputuser <24)

#memeriksa angka lebih dari 26
islebihdari = (inputuser >26)

final = iskurangdari or islebihdari
print("angka yang anda masukan :",final)