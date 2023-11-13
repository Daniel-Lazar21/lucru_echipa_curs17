import csv,json
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
    myfile = [ ]
    with open(CALE_DIR + fisier,"r") as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
           
            element = f"Vehicul de tip {row[2]} din judetul {row[1]} marca {row[4]} : {row[7]} \n"
            with open(CALE_DIR+"conversie_in_text.txt","a") as convertText:
                convertText.write(element)
                

json_to_csv("conversie_in_json.json")  