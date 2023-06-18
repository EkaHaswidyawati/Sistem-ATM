import getpass
#getpass => menerima sebuah kata sandi agar tidak muncul (tidak terlihat)

#membuat list nama pengguna, pin dan saldo bank
nama_user = ['nita', 'eka', 'rara']
password = ['1234', '4321', '1111']
saldo = [1000000, 6000000, 9000000]
jumlah = 0
    
# memeriksa nama pengguna yang dimasukkan
while True:
    user = input('\nMASUKKAN USERNAME: ')
    user = user.lower()
    if user in nama_user:
        if user == nama_user[0]:
            n = 0
        elif user == nama_user[1]:
            n = 1
        else:
            n = 2
        break
    else:
        print('-'*24)
        print('| %-1s |'%('USERNAME TIDAK VALID'))
        print('-'*24)

# comparing pin
while jumlah < 3:
    print('_'*24)
#getpass => menerima sebuah kata sandi agar tidak muncul (tidak terlihat)
    pin = str(getpass.getpass('MASUKKAN PIN: '))
    print('_'*24)
# isdigit => mendeteksi string yang terdiri dari angka saja
    if pin.isdigit():
        if user == 'nita':
            if pin == password[0]:
                break
            else:
                jumlah += 1
                print('-'*19)
                print('| %-2s |'%('PIN TIDAK VALID'))
                print('-'*19)
                print()

        if user == 'eka':
            if pin == password[1]:
                break
            else:
                jumlah += 1
                print('-'*19)
                print('| %-1s |'%('PIN TIDAK VALID'))
                print('-'*19)
                print()
                
        if user == 'rara':
            if pin == password[2]:
                break
            else:
                jumlah += 1
                print('-'*19)
                print('| %-1s |'%('PIN TIDAK VALID'))
                print('-'*19)
                print()

# jika pin yang valid harus keluar atau exit
if jumlah == 3:
    print('*'*38)
    print('3 KALI GAGAL MEMASUKKAN PIN, EXITING\n!!!!!!KARTU ANDA TELAH DIKUNCI!!!!!!')
    print('*'*38)
    exit()

print()
print('*'*25)
print(' '*5, 'ATM ABC', ' '*5)	
print('SELAMAT DATANG',(nama_user[n]))
print('*'*25)

# Menu utama
while True:
    pilihan = input('PILIH DARI OPSI BERIKUT: \n1. Saldo__(S) \n2. Tarik Tunai(T) \n3. Setor Tunai_(ST) \n4. Transfer_(TR) \n5. Exit_(E) \n: ').lower()
    respon = ['s', 't', 'st', 'tr', 'e']
    pilihan = pilihan.lower()
    if pilihan == 's':
# capitalize => Mengubah karakter pertama pada huruf pertama menjadi huruf besar.
        print(str.capitalize(nama_user[n]), 'SALDO ANDA ', saldo[n],'RUPIAH.')

    elif pilihan == 't':
        uang_keluar = int(input('MASUKKAN JUMLAH YANG INGIN ANDA TARIK: '))
        if uang_keluar%50000 != 0:
            print('-'*63)
            print('| JUMLAH YANG INGIN ANDA TARIK HARUS SESUAI DENGAN UANG 50000 |')
            print('-'*63)
        elif uang_keluar > saldo[n]:
            print('-'*30)
            print('| SALDO ANDA TIDAK MENCUKUPI |')
            print('-'*30)
        else:
            saldo[n] = saldo[n] - uang_keluar
            print('SALDO ANDA SEKARANG: ', saldo[n], 'RUPIAH')
            
    elif pilihan == 'st':
        print()
        uang_masuk = int(input('MASUKKAN JUMLAH YANG INGIN ANDA SETOR: '))
        print()
        if uang_masuk%50000 != 0:
            print('---------------------------------------------------------------')
            print('| JUMLAH YANG INGIN ANDA SETOR HARUS SESUAI DENGAN UANG 50000 |')
            print('---------------------------------------------------------------')
        else:
            saldo[n] = saldo[n] + uang_masuk
            print('SALDO ANDA SEKARANG: ', saldo[n], 'RUPIAH')

    elif pilihan == 'tr':
        transfer = int(input('MASUKKAN JUMLAH YANG INGIN ANDA DITRANSFER: '))
        bank = input('MASUKKAN NAMA BANK YANG AKAN DITRANSFER: ')
        norek = input('MASUKKAN NOMOR REKENING YANG AKAN DITRANSFER: ')
        if transfer%10000 != 0:
            print('-'*63)
            print('| JUMLAH YANG INGIN ANDA TRANSFER MINIMAL 10000 |')
            print('-'*63)
        elif transfer > saldo[n]:
            print('-'*30)
            print('| SALDO ANDA TIDAK MENCUKUPI |')
            print('-'*30)
        else:
            saldo[n] = saldo[n] - transfer
            print('TRANSFER KE', bank, 'BERHASIL, SALDO ANDA SEKARANG: ', saldo[n], 'RUPIAH')

    elif pilihan == 'e':
        print('*'*40)
        print(' '*5, 'ANDA TELAH KELUAR DARI AKUN',' '*5)
        print('*'*40)
        exit()
    else:
        print('------------------')
        print('RESPONSE NOT VALID')
        print('------------------')