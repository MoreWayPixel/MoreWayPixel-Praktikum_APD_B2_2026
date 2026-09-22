harga_skincare = [35000, 42000, 50000, 55000, 68000, 70000]
ongkir = 12000
total_pengeluaran = harga_skincare[0] + harga_skincare[1] + harga_skincare[2] + harga_skincare[3] + harga_skincare[4] + harga_skincare[5] + ongkir

rata_rata = total_pengeluaran / len(harga_skincare)
nim = 57
bolean = nim < rata_rata

konversi_jpy = 0.0094
total_jpy = total_pengeluaran * konversi_jpy
slice_skincare = harga_skincare[-4:-1]

total_rp = f"{total_pengeluaran:,}".replace(",", ".")
ongkir_rp = f"{ongkir:,}".replace(",", ".")
rata_rp = f"{rata_rata:,.2f}".replace(".", "X").replace(",", ".").replace("X", ",")
jpy_str = f"{total_jpy:,.2f}".replace(".", "X").replace(",", ".").replace("X", ",")

print("=== Struk Pembelian Mba Jennie ===")
print(f"{'Daftar Harga Skincare':<23} : {harga_skincare}")
print(f"{'Ongkos Kirim':<23} : Rp {ongkir_rp:>10}")
print(f"{'Total Pengeluaran':<23} : Rp {total_rp:>10}")
print(f"{'Rata-rata Harga':<23} : Rp {rata_rp:>10}")
print(f"{'NIM':<23} : {nim}")
print(f"{'Status (NIM < Rata2)':<23} : {bolean}")
print(f"{'Total Pengeluaran JPY':<23} : ¥  {jpy_str:>10}")
print(f"{'Slice Negatif (3 s/d 5)':<23} : {slice_skincare}")