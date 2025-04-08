#_CARA MENJALANKAN PROGRAM_#
#_Pastikan di PC atau Laptop kalian sudah terinstal python_#
#_Simpan file projek ini di direktori yang mudah di temukan, contoh : (C:\Users\'nama device kalian'\desktop)_#
#_Buka Command Line, lalu pindah ke direktori kalian menyimpan file 'create_gif.py'_#
#______________________cd Desktop________________________#
#_Lalu jalankan  program python3 atau python dan nama file:_#
#_python3 create_gif.py_#
#_Jika tidak bisa di jalankan dan ada error coba gunakan perintah untuk menjalankan program berikut:_#
#_python create_gif.py_#

#_memasukkan imageio.v3 yang sudah di instal dan menamainya di program pyton sebagai iio (singkat dan cepat untuk di tulis)_#
import imageio.v3 as iio

#_me-pic1.png & me-pic2.png ganti dengan foto yang ingin kalian jadikan GIF_#
filenames = ['me-pic1.png', 'me-pic2.png']
images = [ ]

#_perlu membuat perulangan untuk jaga-jaga jika ada banyak gambar_#
#_INPUT_#
for filename in filenames:
  images.append(iio.imread(filename))
  

#_'me.gif' hasil GIF dari 2 foto yang kalian input_#
#_EXPORT_#
iio.imwrite('me.gif', images, duration = 500, loop = 0)