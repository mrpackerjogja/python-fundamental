"""
Semua sintaksis dasar bahasa pemrograman terdiri dari
1. Sekuensial: Langkah berurutan
2. Percabangan: langkah melompat jika kondisi terpenuhi
3. Perulangan: mengulang langkah yang sama berualang kali hingga kondisi terpenuhi
"""
# Sequential
# print('Mom said, "Go to shop"')
# print('Budi replied, "What should i buy in the shop?"')
# print('Mom said again, "Buy one bottle of milk, if there are eggs buy 6 eggs"')
# print('Then Budi going to shop')
# print('Budi start for shoping\n')

# Branching
jumlah_botol_susu = 1
jumlah_telor = 6
print('\nBeli 1 botol susu, kalau nggak ada ya pulang aja. \n'
      'Kalau ada telor beli 6 butir telor, kalau nggak ada telor beli susu aja')
print(f'jumlah botol susu yang tersedia sebanyak: {jumlah_botol_susu}')
print(f'jumlah butir telor yang tersedia sebanyak: {jumlah_telor}')
print('')
if jumlah_botol_susu <= 0:
    print('pulang, tidak jadi beli susu & telur')
else:
    # print('Beli 1 botol susu')
    if jumlah_telor > 5:
        print('Beli 1 botol susu dan 6 butir telur')
    else:
        print('Beli 1 botol susu saja')

if jumlah_botol_susu >= 1:
    # print('Beli 1 botol susu')
    if jumlah_telor > 5:
        print('Beli 1 botol susu dan 6 butir telur')
    else:
        print('beli 1 botol susu saja')
else:
    print('pulang, tidak jadi beli susu & telur')

# virtual environtment - . python-fundamental-new_venv/bin/activate
