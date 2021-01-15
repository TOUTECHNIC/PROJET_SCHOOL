    
print('=================================================\n')
print ('programme de gestion des classes \n')
print('=================================================')

table_note=[]
tabl_dic={}
T_m=[]
def repet ():
    nom=input('taper nom/prenom  eleve :\n')
    while True :
        try:
            NCLASS =int(input('N° DE CLASSEMENT  :\n'))
            #table_note.append(NCLASS)
            break          
        except ValueError:
            print(' entrer un nombre entier 1 ')

    while True :
        try :
            note_1=float(input('TAPER NOTE 1  :\n'))
            #table_note.append(note_1)
            break
        except ValueError:
            print(' entrer un nombre entier 2 \n')
    while True :
        try:
            note_2=float(input('TAPER NOTE 2  :\n'))           
            break                
        except ValueError:
            print(' entrer un nombre entier 1 ') 
    somme=note_1+note_2
    moyen=float(somme/2)
    tabl_dic['  nomcomplet'] = nom
    tabl_dic['   N°Classe'] = NCLASS
    tabl_dic['  note1'] = note_1      
    tabl_dic['  note2'] = note_2
    tabl_dic['  somme'] = somme
    tabl_dic['moyen']= moyen
    table_note.append(tabl_dic)
    T_m.append(moyen) 
def reslt ():
    print(tabl_dic)
    print(tabl_dic.get('nomcomplet'))
    for key,value in tabl_dic.items():
        print(key,value)
        if tabl_dic['  somme'] == 10:
            print(key,value)
    #print(table_note.index(key='moyen'))
def moyan ():
    print('________LES NOTES SUPERIEUR >10____________')
    for i in T_m:
        if i>10 :
            print(i)
    print('________LES NOTES MOIN DE 10 _______________')
    for i in T_m: 
        if i < 10 :
            print (i)
    print('________LES NOTES EGALE = 10 ________________')
    for i in T_m: 
        if i == 10 :
            print (i)
while True :
    choix=str.lower(input('voulez vous repeter Oui/Non \t :\t'))
    print('\n')
    if choix == 'o':
        repet()
        #table_note.append(nom)                          
    elif choix=='p' :
        for i in table_note :
            print('========',[i],"=======")
            print()
    elif choix=='q' : 
        break
    elif choix == 'l':
        reslt()
    else :
        print('*******************\n ERREUR : vous avez 3 choix : \n[o]ajouter \n[q]quitter \n[p] afficher la liste \n***************')
