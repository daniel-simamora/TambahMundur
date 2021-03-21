'''
Soal: 
Membuat function tambahMundur(x,y) yang menjumlahkan kebalikan dari 2 angka,
dan membaliknya lagi. 
Angka tidak boleh string, float, negatif, dan lebih dari 359999.
Menghilangkan angka 0 di depan angka bukan 0.
'''

def tambahMundur(x,y):
    print('Masukkan angka 1 :',x)
    print('Masukkan angka 2 :',y)
    
    # Function tambahMundur() ini saya buat di dalam infinite loop
    # Supaya ketika try/except bisa langsung keluar dari program 
    # Dan juga harus break ketika memenuhi kondisi yang tidak diinginkan (string, float, negatif, >359999)
    while True: 
        try:
            # Mencoba apakah kedua angka tersebut ada yang string
            int(x)
            int(y)
        except:
            # Jika salah satunya adalah string, maka akan error, lalu pada except langsung break out of loop
            print('Invalid Input!')
            print() #Space kosong
            break
        
        # Selanjutnya, adalah conditional statements:

        # Mencoba apakah angka lebih dari 359999:
        # Karena saya menggunakan 'or', maka jika 1 saja sudah memenuhi, pasti dijalankan
        if (x > 359999) or (y > 359999):
            print('Invalid Input!')
            print() #Space kosong
            break
            
        # Mencoba salah satu angka tersebut adalah float:
        # Saya menggunakan 'is' ketimbang '=='
        # Karena 'is' bernilai True jika type dan nilanya sama
        # Sedangkan'==' bernilai True jika hanya nilainya yang sama 
        elif (x is float(x)) or (y is float(x)):
            print('Invalid Input!')
            print() #Space kosong
            break
            
        # Mencoba apakah salah satu angka bernilai negatif:
        elif (x < 0) or (y < 0):
            print('Invalid Input!')
            print() #Space kosong
            break
            
        # Jika semua conditional statements di atas tidak dipenuhi,
        # Maka kedua angka sudah memenuhi syarat untuk dilakukan TambahMundur
        else:
            # Karena angka bertipe integer, maka saya akan mengubahnya menjadi str(),
            # Kemudian di-reverse dengan index [::-1]
            xx = str(x)[::-1]
            yy = str(y)[::-1]

            # Terlihat bahwa nilai xx dan yy masih dalam tipe string,
            # Maka supaya bisa dihitung, saya ubah dahulu menjadi int(xx) dan int(yy)
            # Kemudian karena hasil perhitungannya perlu dibalik lagi, 
            # saya harus mengubahnya menjadi string lagi, dan di-index oleh [::-1]
            # Kemudian, jika hasilnya memiliki angka 0 di depan angka bukan 0,
            # maka 0 tersebut akan dihilangkan dengan cara membuatnya menjadi integer kembali
            hasil = int(str(int(xx) + int(yy))[::-1])
            print('Hasil tambah mundurnya :',hasil)
            print() #Space kosong
            break
            
    
# TESTING:

# 1. Kedua angka memenuhi syarat:
tambahMundur(1234,5678)
tambahMundur(4358,754)
tambahMundur(1200,5) # Menghilangkan angka 0 di depan
tambahMundur(532,52) # Menghilangkan angka 0 di depan
tambahMundur(24,1)

# 2. Salah satu angka ada yang bertipe string:
tambahMundur(24,'oi')
tambahMundur('abcedfg','oi')


# 3. Salah satu angka ada yang bertipe float
tambahMundur(23.4,100)
tambahMundur(29.41,30.0)

# 4. Salah satu angka negatif
tambahMundur(-200,9)
tambahMundur(-120,-9.23)

# 5. Salah satu angka lebih besar dari 359999
tambahMundur(100,25000000)
tambahMundur(360000,500000)
