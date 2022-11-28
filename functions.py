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
    file.readline()
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

def mentes(jarmu, meret):
    file=open(filename, 'a', encoding='utf-8')
    file.write(f'\n{jarmu};{meret}')   
    file.close

def uj_jarmu():
    system('cls')
    print('----------ÚJ JÁRMŰ----------')
    ujJarmu=input('Jármű neve: ') 
    ujMeret=int(input('Jármű mérete(1-Csapatszállító, 2-Tank): '))
    jarmuvek.append(ujJarmu)
    meret.append(ujMeret)   
    mentes(ujJarmu, ujMeret)
    input('Sikeres felvétel...')
