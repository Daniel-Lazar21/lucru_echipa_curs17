import csv,json
import pandas as pd
CALE_DIR = "C:/Users/danut/Desktop/pythonProject1/lucru_echipa/"
#conversii 
    #converteste fisierul din csv in json 
    #converteste fisierul in fisier text unde fiecare linie este de tipul "Vehicul de tip <CATEGORIE_NATIONALA> 
    # din judetul <JUDET> marca <MARCA>: <TOTALVEHICULE> <TOTAL
    #converteste un fisier json primit ca parametru in fisier csv (pe caz general)

 
def csv_to_json(fisier):
    
    with open(CALE_DIR + fisier,"r") as csv_file:    
        myreader = list(csv.DictReader(csv_file))
           
        with open(CALE_DIR + "conversie_in_json.json","w") as jsonFile:
            json.dump(myreader,jsonFile,ensure_ascii=False)
        
#csv_to_json("masini.csv")
def json_to_csv(fisier):
    with open(CALE_DIR + fisier) as jsonFile:
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
    
def conversie_in_txt(fisier):
    with open(CALE_DIR + fisier,"r") as csvFile:
        df = pd.read_csv(csvFile)
        print(df.query("index == 2"))
        lista_judete = [ ]
        for judet in df["JUDET"]:
            if judet not in lista_judete:
                lista_categ_nat = [ ]
                for categ_nat in df["CATEGORIE_NATIONALA"]:
                    if categ_nat not in  lista_categ_nat:
                        lista_marci = [ ]
                        for marca in df["MARCA"]:
                            if marca not in lista_marci:
                                selectie = df.query("JUDET == @judet and CATEGORIE_NATIONALA == @categ_nat and MARCA == @marca")

                                total_vehicule = selectie["TOTAL_VEHICULE"].sum()
                                if total_vehicule != 0:
                                #print(selectie)
                                    element = f"Vehicul de tip {categ_nat} din judetul {judet} marca {marca} : {total_vehicule} \n"
                                    with open(CALE_DIR+"conversie_in_text.txt","a") as convertText:
                                        convertText.write(element)
                                #total_vehicule = selectie["TOTAL_VEHICULE"].sum()
                            lista_marci.append(marca)
                    lista_categ_nat.append(categ_nat)
            lista_judete.append(judet)
                

conversie_in_txt("masini.csv")  