
def litre (l):
lb=int(input('litre de : \t'))
cl=l/lb
return cl

def to_mille (km):
mille=km/1.6
return mille
k=int(input('taper un'))
convert=to_mille(k)

def g():
a=int(input('nb'))
b=int(input('nb'))
c=a*b
print(c)

def pls ():
a=int(input('nb'))
b=int(input('nb'))
c=a+b
print(c)

def total_l ():
choix_3= input( ' votre choix [g_h]')
if choix_3 == 'g':
    g()
if choix == 'h':
    def h():
        CH= input(' choix int / float ')
        if CH== 'i' :
            pls()
        if CH == 'f':
            a=float(input('nb'))
            b=float(input('nb'))
            c=a+b
            print(c)
    h()
while True :
choix = input(' continue --> [o]oui / non ')
if choix == 'o':
    choix2=input(' votre choix [l] litre , [k]kilometre,[c] clacule')

    if choix2=='l':
        print(litre(13))
    if choix2=='k':
        print(convert)
    if choix2 == 'c':
        total_l()

if choix == 'n':
    break




