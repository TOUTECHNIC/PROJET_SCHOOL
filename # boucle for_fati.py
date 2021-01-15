# boucle for
li=[]
def pls ():
    nb=int(input('taper nombre eleve : \t'))
    for i in range (0,nb):
        j=0
        j=j+1
        li.append(i)
        nom=input('votre nom :\t')
        li.append(nom)
        note1=float(input('1ER EVALUATION : \t'))
        li.append(note1)
        note2=float(input('2EME EVALUATION : \t'))
        li.append(note2)
        resulte=(note1+note2)/2
        li.append(resulte)
        print(li)       
pls()

while True :
    choix=input('vous voules chercher par id \t :')
    if choix== 'o':
        chercher = int(input('chercher un id : \t'))
        if chercher in li :
            id=li.index(chercher)
            jsq=id+4
            print(li[id:jsq])
        else :
            print (' n\'existe pas ')
    if choix== 'n':
        break

'''
# python haking certificat ethical hacker
def selection ():
    choix= input('votre choix [v]Vente _ [a]Achat : \t')
    if choix is 'v':
        facture()
    elif choix is 'a':
        pass
selection()

def facture ():
    print('============ facturatio =============\n\n')
    while True :
        n= int(input('nombre du produit _ [0]quitter: \t'))
        if n == 0 :
            break
        else:
            for i in range (0,n):
                while True :
                    try :
                        id = int(input('id : \t'))
                        break
                    except ValueError :
                        print('taper un nombre entier')
                while True :
                    try:
                        qte=int(input('quantite : \n'))
                        break
                    except:
                        print('entrer quantite nombre entire ')
                while True :
                    try :
                        prix= float(input('prix unitaire : \n'))
                        break
                    except :
                        print('entrer un nombre entire ')
                prix_t= float(qte*prix)
                print (' prix total = '+str(prix_t)+' DH')
facture()
'''