d = {'nama':'Karina Muslimah', 'alamat':'Ngawi', 'kodepos':'1974', 'nim':'L200180138', 'prodi':'Infomatika', 'panggil':'Karin'}
def nama():
    'menampilkan data diri masing-masing 1 dari setiap data'
    print 'Nama: ' + d['nama']

def alamat():
    'menampilkan data diri masing-masing 1 dari setiap data'
    print 'Alamat: ' + d['alamat']

def kodepos():
    'menamplkan data diri masing-masing 1 dari setiap data'
    print 'Kode Pos: ' + d['kodepos']

def nim():
    'menampilkan data diri masing-masing 1 dari setiap data'
    print 'NIM: ' + d['nim']

def prodi():
    'menampilkan data diri masing-masing 1 dari setiap  data'
    print 'Prodi: ' + d['prodi']

def panggil():
    'menampilkan data diri masing-masing 1 data diri dari setiap data'
    print 'Nama Panggilan: ' + d['panggil']

def bantuan():
    'menampilkan bantuan'
    print """Pilihan yang tersedia:
b menampilkan bantuan ini
N menampilkan NIM
a menampilkan nama
A menampilkan Alamat
K menampilkan Kode Pos
P menampilkan Prodi
C menampilkan Nama Panggilan
k keluar"""

repeat = True

while repeat:
    x = raw_input('Pilihan Saudara: ')
    if x == 'a':
        nama()
    elif x == 'A':
        alamat()
    elif x == 'K':
        kodepos()
    elif x == 'N':
        nim()
    elif x == 'P':
        prodi()
    elif x == 'C':
        panggil()
    elif x == 'b':
        bantuan()

    elif x == 'k':
        print "Terima Kasih"
        repeat = False
