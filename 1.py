hari_pertama = {"keju", "tepung", "garam", "gula", "coklat"}
hari_kedua = {"garam", "gula", "coklat", "kecap"}
hari_kedua.add("keju")
sama = hari_pertama.intersection(hari_kedua)
print("1. barang yang sama:",sorted(sama))
beda1 = hari_pertama.difference(hari_kedua)
print("2. hanya hari pertama:", sorted(beda1))
hari_pertama.remove("garam")
beda2 = hari_kedua.difference(hari_pertama)
print("3. hanya hari kedua:", sorted(beda2))
tidak_sama = hari_pertama.symmetric_difference(hari_kedua)
print("4. barang tidak sama:", sorted(tidak_sama))
print("5. hari pertama:", sorted(hari_pertama))
print("6. hari kedua:", sorted(hari_kedua))