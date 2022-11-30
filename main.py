from functions import *

beolvasas()
valasztas=''
while valasztas!=0:
    valasztas=menu()
    if valasztas=='1':
        uj_jarmu()
    elif valasztas=='2':
        jarmu_torol()
    elif valasztas=='3':
       szabadhely()
    elif valasztas=='4':
        cssz_szama()
    elif valasztas=='5':
        tankok_szama()
    elif valasztas=='6':
        tartalom()