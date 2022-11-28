from os import system
from data import *

filename='jarmuvek.csv'

def menu():
    system('cls')
    print('----------MENÜ----------')
    print('0-Kilépés')
    print('1-Jármű beléptetése')
    print('2-Jármű kiléptetése')
    print('3-Szabad helyek száma')
    print('4-Páncélozott csapatszállítók száma')
    print('5-Tankok száma')
    print('6-Teljes hangár tartalma')
    return input('Választás: ')

def beolvasas():
    file=open(filename, 'r', encoding='utf-8')
    for jarmu in file:
        darabolt=jarmu.strip().split(';')
        jarmuvek.append(darabolt[0])
        meret.append(int(darabolt[1]))
    file.close()  

def tartalom():
    system('cls')
    print('----------HANGÁR----------')  
    for item in jarmuvek:
        print(f'\t{item}')
    input('Tovább...') 

def mentes_veg(jarmu, meret):
    file=open(filename, 'a', encoding='utf-8')
    file.write(f'\n{jarmu};{meret}')   
    file.close

def uj_jarmu():
    system('cls')
    print('----------ÚJ JÁRMŰ----------')
    ujJarmu=input('Jármű neve: ') 
    ujMeret=int(input('Jármű mérete(1-Csapatszállító, 2-Tank): '))
    if szabadhely()>2:
        jarmuvek.append(ujJarmu)
        meret.append(ujMeret)   
        mentes_veg(ujJarmu, ujMeret)
        input('Sikeres felvétel...')
    elif szabadhely()>1 and ujMeret==2:
        print('Több tank már nem fér a hangárba')
    elif szabadhely()==0:
        print()    
            

def sorszamozas():
    for i in range(len(jarmuvek)):  
        print(f'\t{i+1}. {jarmuvek[i]}')

def jarmu_torol():
    system('cls')
    print('----------JÁRMŰ TÖRLÉSE----------')    
    sorszamozas()
    sorszam=int(input('Melyik jármű hagyta el a hangárt? Kérem adja meg a sorszámát:'))
    jarmuvek.pop(sorszam-1)
    meret.pop(sorszam-1)
    mentes()
    input('Sikeres törlés...')

def mentes():
    file=open(filename, 'w', encoding='utf-8')
    for i in range(len(jarmuvek)):
        file.write(f'{jarmuvek[i]};{meret[i]}')
        if i<len(meret)-1:
            file.write('\n')
    file.close() 

ferohely=40
foglalthely=0

def osszegzes(szam):
    for i in meret:
        szam+=i
    return szam       

def szabadhely():
    system("cls")
    print('----------SZABAD HELYEK----------')
    szabad=ferohely-osszegzes(foglalthely)
    print(f'\nA szabad helyek száma:{szabad}')
    input('Tovább...')        
  
                 
