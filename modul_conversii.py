import csv
import json
import pandas as pd
CALE_DIR="C:/Users/Laurentiu/Desktop/Pachet"
#conversii 
    #converteste fisierul din csv in json 
def csv_to_json(cale_csv):
    data=[]
    with open(cale_csv+'/masini.csv','r') as csvFile:
        reader=csv.DictReader(csvFile)
        for element in reader:
            data.append(element)
    with open(cale_csv+'/fisier.json','w') as jsonFile:
        json.dump(data,jsonFile)        
        
#converteste fisierul in fisier text unde fiecare linie este de tipul "Vehicul de tip <CATEGORIE_NATIONALA> din judetul <JUDET> marca <MARCA>: <TOTALVEHICULE> <TOTAL
def csv_to_txt(cale_csv):
    with open(cale_csv+'/masini.csv','r') as csvFile,open(cale_csv+'/fisier.txt','w') as txtFile:
        reader = csv.reader(csvFile)
        for index,row in enumerate(reader):
           if(index == 0):
               continue
           txtFile.write(f"Vehiculul de tip {row[2]} din judetul {row[1]},marca {row[5]}:{row[7]}\n")
    
#converteste un fisier json primit ca parametru in fisier csv (pe caz general)
def json_to_csv(cale_json):
    with open(cale_json,'r') as jsonFile, open(cale_json,'w')as csvFile:
        df=pd.read_json(jsonFile)
        df.to_csv(csvFile,index=False)


        
  
        



#calcule
    #calculeaza numarul total de masini din tara 
    #calculeaza numarul total de masini dintr-un judet primit ca parametru
    #calculeaza numarul total de masini dintr-o anumita categorie nationala 
    #calculeaza numarul total de masini in functie de tipul de combustibil pe care il folosesc

#modificare 
   #modificati valorile a.i. toate intrarile care contin denumirea benzina sa ramana cu valoarea benzina 
   #modificati valorile a.i. in locul judetelor "dolj","olt","gorj","valcea","mehedinti" sa apara oltenia 
   #adaugati o coloana care sa contina valoarea "popular" sau "nepopular" in functie de nr de vehicule din acea categorie (un vehicul e popular daca exista mai mult de 100) 