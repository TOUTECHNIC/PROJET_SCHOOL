print (' programme de gestion ')
print('______________________')

id=1
Note=[]
def repet ():
    n=int(input('nombre eleve add'))
    for i in range (0,n) :
        #id=int(input('id eleve\t:'))
        nom=input('nom eleve\t:')
        classe=int(input('classe eleve\t:'))
        Note.append(id=+1)
        Note.append(nom)
        Note.append(classe)
        print(Note)

def percourir ():
    for i in Note :
        print(i)
while True:
    choix=input('vous voulez ajouter un eleve?\n[oui=o],[non=n] --> : ')
    if choix=='o': 
        repet()         
    if choix=='n':
        break
#termin=input('Nombre eleve ajouté')  