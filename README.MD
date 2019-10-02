# Tubes1TBFO_13518135_13518087 -- Simulasi The Sims
Program ini adalah contoh pengaplikasian tabel transisi DFA untuk membuat sebuah game sederhana

## Instalasi Program
Program ini dibuat menggunakan bahasa pemrograman python oleh karena itu dibutuhkan bahasa pemrograman python versi 3. Python dapat diunduh melalui https://www.python.org/downloads/
Setelah Python diinstall, bukalah terminal komputer dan ketikkan "pip install Pandas" untuk mengunduh library Pandas. Pandas diperlukan untuk membaca file Transition Table.csv yang berisi Tabel Transisi DFA.

### Cara Menjalankan Kode Program
Untuk menjalankan program, buka terminal komputer Anda dan pergi ke directory di mana program di simpan. Kemudian silakan ketikkan perintah seperti di bawah ini:

'''bash
C:\Users\<user>\Documents\Tubes1TBFO_13518135_13518087>
# py main.py
[] ========================================== []
||    Selamat datang di                       ||
||            Simulasi Kehidupan Sederhana    ||
[] ========================================== []
||                 List Aksi                  ||
[] ========================================== []
||  1. Tidur Siang .................. E + 10  ||
||  2. Tidur Malam .................. E + 15  ||
||  3. Makan Hamburger .............. E +  5  ||
||  4. Makan Pizza .................. E + 10  ||
||  5. Makan Steak and Beans ........ E + 15  ||
||  6. Minum Air .................... H -  5  ||
||  7. Minum Kopi ................... H -  5  ||
||                                    E +  5  ||
||  8. Minum Jus .................... H -  5  ||
||                                    E + 10  ||
||  9. Buang Air Kecil .............. H +  5  ||
|| 10. Buang Air Besar .............. H + 10  ||
||                                    E -  5  ||
|| 11. Bersosialisasi ke Kafe ....... H -  5  ||
||                                    E - 10  ||
||                                    F + 15  ||
|| 12. Bermain Media Sosial ......... E - 10  ||
||                                    F + 10  ||
|| 13. Bermain Komputer ............. E - 10  ||
||                                    F + 15  ||
|| 14. Mandi ........................ H + 15  ||
||                                    E -  5  ||
|| 15. Cuci Tangan .................. H +  5  ||
|| 16. Mendengarkan Musik di Radio .. E -  5  ||
||                                    F + 10  ||
|| 17. Membaca Koran ................ E -  5  ||
||                                    F +  5  ||
|| 18. Membaca Novel ................ E -  5  ||
||                                    F + 10  ||
[] ========================================== []

 /--Condition------\
 | Hygiene = 0     |
 | Energy  = 10    |
 | Fun     = 0     |
 \-----------------/

Mau ngapain bray?? :
'''
Jika program berhasil dijalankan, maka akan muncul menu utama program seperti di atas.

## Deskripsi Program
Program yang mensimulasikan game The Sims, dengan beberapa simplifikasi
Salah satunya adalah atribut sebagai berikut:
- Hygiene, gabungan dari atribut Hygiene dan Bladder dalam The Sims
- Energy, gabungan dari atribut Energy dan Hunger dalam The Sims
- Fun, gabungan dari atribut Fun dan Social dalam The Sims
Permainan ini dimulai dengan atribut sebagai berikut:
Hygiene: 0
Energy : 10
Fun    : 0
Lalu, permainan bekerja dengan cara menginput aksi yang ingin dilakukan
untuk mengubah atribut-atribut tersebut. Permainan dimenangkan saat
ketiga atribut bernilai 15, dan kalah jika ketiga atribut bernilai 0

## Cara Menggunakan Program
Ketika program dijalankan, maka menu list aksi akan muncul, dan akan diminta sebuah input aksi. Untuk memainkan gamenya silakan ketikkan aksi sesuai di list yang tertera.

### Kontributor
Program dibuat untuk memenuhi salah satu Tugas Besar IF2124 Teori Bahasa Formal dan Otomata ITB. Adapun pembuat dari program ini adalah :

* Radhinansyah Hemsa Ghaida / 1651s8087
* Gregorius Jovan Kresnadi  / 13518135

