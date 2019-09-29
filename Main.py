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

# $ Fungsi-Fungsi
def startgame():
    return [0,10,0]

def printState(hygiene,energy,fun):
    print(" /--Condition------\ ")
    if (hygiene<10):
        print(" | Hygiene = " + str(hygiene) + "     | ")
    else:
        print(" | Hygiene = " + str(hygiene) + "    | ")
    if (energy<10):
        print(" | Energy  = " + str(energy) + "     | ")
    else:
        print(" | Energy  = " + str(energy) + "    | ")
    if (fun<10):
        print(" | Fun     = " + str(fun) + "     | ")
    else:
        print(" | Fun     = " + str(fun) + "       ")
    print(" \-----------------/ ")

def menang(hygiene,energy,fun):
    return (hygiene == 15) and (energy == 15) and (fun == 15)
    
def kalah(hygiene,energy,fun):
    return (hygiene == 0) and (energy == 0) and (fun == 0)

def changeState(condition,awal,akhir):
    if (awal == akhir):
        print("Aksi tidak valid!")
        return condition
    else:
        currstate = akhir
        idx = int(table[table["Current State"]==akhir].index[0])
        condition[0] = table.at[idx,"Hygiene"]
        condition[1] = table.at[idx,"Energy"]
        condition[2] = table.at[idx,"Fun"]
        return condition



# $ MAIN PROGRAM

# * Welcome
print("[] ========================================== []")
print("||   Selamat datang di                        ||")
print("||             Simulasi Kehidupan Sederhana   ||")
print("[] ========================================== []")
print("")

# * Start Game
cond = startgame()
currstate = "q8"
printState(cond[0],cond[1],cond[2])
print(currstate)

# * Start Loop
while (not(menang(cond[0],cond[1],cond[2])) or not(kalah(cond[0],cond[1],cond[2]))):
    print("")
    aksi = str(input("Masukkan aksi yang akan dilakukan: "))
    #newstate = readAction(aksi)
    #changeState(currstate,newstate)
    cond = changeState(cond,currstate,"q32")
    printState(cond[0],cond[1],cond[2])

 
#while (not(menang()) and not(kalah())) :
