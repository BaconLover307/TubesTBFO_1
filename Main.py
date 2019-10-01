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
# $ ====================== Import library ======================
import pandas as pd
table = pd.read_csv("Transition Table.csv")
 
# $ ====================== Global Variables ======================
aksi = ''
state = ''
currstate = ''
newstate = ''

# $ ====================== Fungsi-Fungsi ======================
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
        print(" | Fun     = " + str(fun) + "    | ")
    print(" \-----------------/ ")

def menang(hygiene,energy,fun):
    return (hygiene == 15) and (energy == 15) and (fun == 15)
    
def kalah(hygiene,energy,fun):
    return (hygiene == 0) and (energy == 0) and (fun == 0)

def readAction(aksi,currstate):
    try:
        idx = int(table[table['Current State']==currstate].index[0]) 
        newstate = table.at[idx, aksi]
        return newstate
    except:
        print("Kamu ngapain mas!? Gabisa ngetik ya?!")
        return currstate
    finally:
        pass

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

# $ ====================== MAIN PROGRAM ======================
# * Welcome
print("[] ========================================== []")
print("||    Selamat datang di                       ||")
print("||            Simulasi Kehidupan Sederhana    ||")
print("[] ========================================== []")
print("||                 List Aksi                  ||")
print("[] ========================================== []")
print("||  1. Tidur Siang .................. E + 10  ||")
print("||  2. Tidur Malam .................. E + 15  ||")
print("||  3. Makan Hamburger .............. E +  5  ||")
print("||  4. Makan Pizza .................. E + 10  ||")
print("||  5. Makan Steak and Beans ........ E + 15  ||")
print("||  6. Minum Air .................... H -  5  ||")
print("||  7. Minum Kopi ................... H -  5  ||")
print("||                                    E +  5  ||")
print("||  8. Minum Jus .................... H -  5  ||")
print("||                                    E + 10  ||")
print("||  9. Buang Air Kecil .............. H +  5  ||")
print("|| 10. Buang Air Besar .............. H + 10  ||")
print("||                                    E -  5  ||")
print("|| 11. Bersosialisasi ke Kafe ....... H -  5  ||")
print("||                                    E - 10  ||")
print("||                                    F + 15  ||")
print("|| 12. Bermain Media Sosial ......... E - 10  ||")
print("||                                    F + 10  ||")
print("|| 13. Bermain Komputer ............. E - 10  ||")
print("||                                    F + 15  ||")
print("|| 14. Mandi ........................ H + 15  ||")
print("||                                    E -  5  ||")
print("|| 15. Cuci Tangan .................. H +  5  ||")
print("|| 16. Mendengarkan Musik di Radio .. E -  5  ||")
print("||                                    F + 10  ||")
print("|| 17. Membaca Koran ................ E -  5  ||")
print("||                                    F +  5  ||")
print("|| 18. Membaca Novel ................ E -  5  ||")
print("||                                    F + 10  ||")
print("[] ========================================== []")
print("")

# * Start Game
cond = startgame()
currstate = "q8"
printState(cond[0],cond[1],cond[2])

# * Start Loop
while (not(menang(cond[0],cond[1],cond[2])) and not(kalah(cond[0],cond[1],cond[2]))):
    print("")
    aksi = str(input("Mau ngapain bray?? : "))
    newstate = readAction(aksi,currstate)
    cond = changeState(cond,currstate,newstate)
    currstate = newstate
    print("")
    printState(cond[0],cond[1],cond[2])

# * Game Selesai
if (menang(cond[0],cond[1],cond[2])):
    print("")
    print(" __     ______  _    _  __          _______ _   _  ")
    print(" \ \   / / __ \| |  | | \ \        / /_   _| \ | | ")
    print("  \ \_/ / |  | | |  | |  \ \  /\  / /  | | |  \| | ")
    print("   \   /| |  | | |  | |   \ \/  \/ /   | | | . ` | ")
    print("    | | | |__| | |__| |    \  /\  /   _| |_| |\  | ")
    print("    |_|  \____/ \____/      \/  \/   |_____|_| \_| ")
    print("[]================================================[]")
    print("||  Pesan Sponsor:                                ||")
    print("||                   Sehat bet idup lo brayyy :)  ||")
    print("[]================================================[]")
    
if (kalah(cond[0],cond[1],cond[2])):
    print("")
    print(" __   _______ _   _   _     _____ _____ _____  ")
    print(" \ \ / /  _  | | | | | |   |  _  /  ___|  ___|")
    print("  \ V /| | | | | | | | |   | | | \ `--.| |__   ")
    print("   \ / | | | | | | | | |   | | | |`--. \  __|  ")
    print("   | | \ \_/ / |_| | | |___\ \_/ /\__/ / |___  ")
    print("   \_/  \___/ \___/  \_____/\___/\____/\____/ ")
    print("[]============================================[]")
    print("||  Pesan Sponsor:                            ||")
    print("||            Telah berpulang seorang sim :(  ||")
    print("[]============================================[]")

print("")
print("")
print('[]---------------------------------------------[]');
print('||    Terima kasih telah memainkan             ||');
print("||             Simulasi Kehidupan Sederhana    ||")
print('[]---------------------------------------------[]');
 
