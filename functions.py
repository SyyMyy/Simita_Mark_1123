from os import system

def menu():
    system('cls')
    print('----------MENÜ----------')
    print('0-Kilépés')
    print('1-Jármű beléptetése')
    print('2-Jármű kiléptetése')
    print('3-Szabad helyek száma')
    print('4-Páncélozott csapatszállítók száma')
    print('5-Tankok száma')
    return input('Választás: ')