import csv
import pandas as pd
CALE_DIR="C:/Users/Laurentiu/Desktop/Pachet"


#afisari:
    #afiseaza toate masinile dintr-un judet anume 
def afisare_masini_judet_anume(cale,judet):
    df = pd.read_csv(cale+'/masini.csv')
    rez= df.query("JUDET == @judet")
    print(rez)   
    #afiseaza toate masinile dintr-o categorie anume 
def afisare_masini_categorie_anume(cale,categorie):
    df = pd.read_csv(cale+'/masini.csv')
    rez= df[categorie]
    print(rez)    
    #afiseaza toate masinile care sunt mai multe de 10
def afisare_numar_masini_10(cale):
    df = pd.read_csv(cale+'/masini.csv')
    rez = df.query('TOTAL_VEHICULE > 10 ')
    rez=rez.query("CATEGORIE_NATIONALA == 'AUTOTURISM'")
    print(rez)

afisare_numar_masini_10(CALE_DIR)    
    
#conversii 
    #converteste fisierul din csv in json 
    #converteste fisierul in fisier text unde fiecare linie este de tipul "Vehicul de tip <CATEGORIE_NATIONALA> din judetul <JUDET> marca <MARCA>: <TOTALVEHICULE> <TOTAL
    #converteste un fisier json primit ca parametru in fisier csv (pe caz general)

#calcule
    #calculeaza numarul total de masini din tara 
    #calculeaza numarul total de masini dintr-un judet primit ca parametru
    #calculeaza numarul total de masini dintr-o anumita categorie nationala 
    #calculeaza numarul total de masini in functie de tipul de combustibil pe care il folosesc

#modificare 
   #modificati valorile a.i. toate intrarile care contin denumirea benzina sa ramana cu valoarea benzina 
   #modificati valorile a.i. in locul judetelor "dolj","olt","gorj","valcea","mehedinti" sa apara oltenia 
   #adaugati o coloana care sa contina valoarea "popular" sau "nepopular" in functie de nr de vehicule din acea categorie (un vehicul e popular daca exista mai mult de 100) 