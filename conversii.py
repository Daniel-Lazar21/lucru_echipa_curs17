import csv,json
import pandas as pd
CALE_DIR = "C:/Users/danut/Desktop/pythonProject1/lucru_echipa/"
#conversii 
    #converteste fisierul din csv in json 
    #converteste fisierul in fisier text unde fiecare linie este de tipul "Vehicul de tip <CATEGORIE_NATIONALA> 
    # din judetul <JUDET> marca <MARCA>: <TOTALVEHICULE> <TOTAL
    #converteste un fisier json primit ca parametru in fisier csv (pe caz general)

#converteste fisierul din csv in json  
def csv_to_json(fisier):
    with open(CALE_DIR + fisier,"r") as csv_file:    
        lista_dictionare = list(csv.DictReader(csv_file))
           
        with open(CALE_DIR + "conversie_in_json.json","w") as jsonFile:
            json.dump(lista_dictionare,jsonFile,ensure_ascii=False)
            
#converteste un fisier json primit ca parametru in fisier csv (pe caz general)        
def json_to_csv(fisier):
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
                
                    with open(CALE_DIR+"conversie_in_text.txt","a") as convertText:
                        convertText.write(element)             
                    selectie_categ_nat = selectie_categ_nat.query("MARCA != @marca")         
                selectie_judet = selectie_judet.query("CATEGORIE_NATIONALA != @categ_nat")
            df = df.query("JUDET != @judet")   
                

