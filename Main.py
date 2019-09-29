'''
Kelompok King Kong Bray
Anggota kelompok:
- Gregorius Jovan Kresnadi    - 13518135
- Radhinansyah Hemsa Ghaida   - 13518087

Nama program : Simulator Kehidupan Sederhana

Deskripsi program:
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
'''
# $ Import library
import pandas as pd
table = pd.read_csv("Transition Table.csv")
 
# $ Global Variables
hyg = 0
ene = 10
fun = 0

# $ Fungsi-Fungsi
def startgame():
    hygiene = 0
    energy = 10
    fun = 0

def printState(hygiene,energy,fun):
    print(" /--Condition------\ ")
    if (hygiene<10):
        print(" | Hygiene = " + str(hygiene) + "     | ")
    else:
        print(" | Hygiene =" + str(hygiene) + "     | ")
    if (energy<10):
        print(" | Energy  = " + str(energy) + "    | ")
    else:
        print(" | Energy  = " + str(energy) + "    | ")
    if (fun<10):
        print(" | Fun     = " + str(fun) + "     | ")
    else:
        print(" | Fun     = " + str(fun) + "       ")
    print(" \-----------------/ ")

def menang(hygiene,energy,fun):
    if
    
def kalah(hygiene,energy,fun):
    if

def readState(hygiene,energy,fun):



# $ MAIN PROGRAM

# * Welcome
print("[] ========================================== []")
print("||   Selamat datang di                        ||")
print("||             Simulasi Kehidupan Sederhana   ||")
print("[] ========================================== []")
print("")

# * Start Game
startgame()
printState(hyg,ene,fun)

 
#while (not(menang()) and not(kalah())) :
