import csv
import json
import pandas as pd
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
        
#converteste fisierul in fisier text unde fiecare linie este de tipul "Vehicul de tip <CATEGORIE_NATIONALA> din judetul <JUDET> 
#marca <MARCA>: <TOTALVEHICULE> <TOTAL
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

#!!!AM adaugat aceasta functie pentru ca nu sunt sigur daca prima varianta ,pe care am facut-o si eu intial, este
#corecta din mai multe motive cum ar fi repetitia unor linii!!!
#converteste fisierul in fisier text unde fiecare linie este de tipul "Vehicul de tip <CATEGORIE_NATIONALA> 
# din judetul <JUDET> marca <MARCA>: <TOTALVEHICULE> <TOTAL    
def afisare_txt(fisier):
    with open(CALE_DIR + fisier,"r") as csvFile:
        df = pd.read_csv(csvFile)

        while df["JUDET"].empty == False:
            judet = list(df["JUDET"])[0]
            selectie_judet = df.query("JUDET == @judet")
                
            while selectie_judet["CATEGORIE_NATIONALA"].empty == False:
                categ_nat = list(selectie_judet["CATEGORIE_NATIONALA"])[0]        
                selectie_categ_nat = selectie_judet.query("CATEGORIE_NATIONALA == @categ_nat")
                
                while selectie_categ_nat["MARCA"].empty == False:
                    marca = list(selectie_categ_nat["MARCA"])[0]                 
                    selectie_marca = selectie_categ_nat.query("MARCA == @marca")
                    total_vehicule = selectie_marca["TOTAL_VEHICULE"].sum()            
                    element = f"Vehicul de tip {categ_nat} din judetul {judet} marca {marca} : {total_vehicule} \n"
                
                    with open(CALE_DIR+"afisare_text.txt","a") as convertText:
                        convertText.write(element)             
                    selectie_categ_nat = selectie_categ_nat.query("MARCA != @marca")         
                selectie_judet = selectie_judet.query("CATEGORIE_NATIONALA != @categ_nat")
            df = df.query("JUDET != @judet")   
            
#converteste un fisier json primit ca parametru in fisier csv (pe caz general) 
#!!!Am adaugat aceasta functie pt ca functia json_to_csv dadea o eroare si nu putea fi folosita!!!    
def json_to_csv_v2(fisier):
    with open(CALE_DIR + fisier,'r') as jsonFile:
        jsondata = json.load(jsonFile)
        with open(CALE_DIR + 'conversie_json_in_csv.csv', 'w',newline="") as csvFile:
            csv_writer = csv.writer(csvFile)
            count = 0
            for dictionar in jsondata:
                if count == 0:
                    header = dictionar.keys()
                    csv_writer.writerow(header)
                    count += 1
                csv_writer.writerow(dictionar.values())
