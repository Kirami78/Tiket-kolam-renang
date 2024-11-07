print("Program penghitung harga tiket wahana renang")
Masukan = str(input("Masukan jenis pengunjung (dewasa/anak) : ")).lower()
if Masukan == "dewasa" :
    Hari = str(input("Masukan hari : ")).lower()
    if Hari == "sabtu" or Hari == "minggu" :
        Harga = 35000
        print(f"Harga tiket untuk dewasa pada hari {Hari} adalah : Rp.{Harga + 15000}")
    else :
        print(f"Harga tiket untuk dewasa pada hari {Hari} adalah : Rp.{Harga}")
else :
    Hari = str(input("Masukan hari : ")).lower()
    if Hari == "sabtu" or Hari == "minggu" :
        Harga1 = 15000
        print(f"Harga tiket untuk dewasa pada hari {Hari} adalah : Rp.{Harga1 + 15000}")
    else :
        print(f"Harga tiket untuk dewasa pada hari {Hari} adalah : Rp.{Harga1}")




