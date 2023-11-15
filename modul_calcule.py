import pandas as pd
import csv
#calcule
    #calculeaza numarul total de masini din tara 
CALE_DIR="C:/Users/Laurentiu/Desktop/Pachet"
def nr_total_masini(cale):
    suma=0
    df=pd.read_csv(cale+'/masini.csv')
    for element in df['TOTAL_VEHICULE']:
        suma+=element
    print(suma)
    #calculeaza numarul total de masini dintr-un judet primit ca parametru
def nr_total_masini_judet(cale,judet):
    suma=0
    df=pd.read_csv(cale+'/masini.csv')
    rez=df.query('JUDET == @judet') 
    for element in rez["TOTAL_VEHICULE"]:
        suma+=element
    print(suma)         
    #calculeaza numarul total de masini dintr-o anumita categorie nationala 
def nr_total_masini_categorie_nationala(cale,categorie):
    suma=0
    df=pd.read_csv(cale+'/masini.csv')
    rez=df.query("CATEGORIE_NATIONALA == @categorie")   
   
    for element in rez["TOTAL_VEHICULE"]:
        suma+=element
    print(suma)
     
    #calculeaza numarul total de masini in functie de tipul de combustibil pe care il folosesc
def nr_total_masini_combustibil(cale,combustibil):
    suma=0
    df=pd.read_csv(cale+'/masini.csv')
    rez=df.query("VALUE_NAME == @combustibil")   
    for element in rez["TOTAL_VEHICULE"]:
        suma+=element
    print(suma)



#modificare 
   #modificati valorile a.i. toate intrarile care contin denumirea benzina sa ramana cu valoarea benzina 
   #modificati valorile a.i. in locul judetelor "dolj","olt","gorj","valcea","mehedinti" sa apara oltenia 
   #adaugati o coloana care sa contina valoarea "popular" sau "nepopular" in functie de nr de vehicule din acea categorie (un vehicul e popular daca exista mai mult de 100) 