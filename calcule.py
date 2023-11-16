#calcule
import os
import csv
#calculeaza numarul total de masini din tara
FILE_PATH="/Users/mihaiapostolescu/Projects/Python/curs-17/"

def read_csv(filename):
    with open(FILE_PATH+filename,'r') as file:
        reader = csv.reader(file)
        returnable=list(reader)
        return returnable

def nrTotalMasini():
    csvFile=read_csv("masini.csv")
    count=0
    nr_Total_Masini=0
    for line in csvFile:
        if count!=0:
            nr_Total_Masini = nr_Total_Masini + int(line[7])
        count+=1
    print(nr_Total_Masini)

# nrTotalMasini()

def nrTotalMasiniPeJudet(judet):
    csvFile=read_csv("masini.csv")
    count=0
    nr_Total_Masini=0
    for line in csvFile:
        if count!=0 and line[1]==judet:
            nr_Total_Masini = nr_Total_Masini + int(line[7])
        count+=1
    print(nr_Total_Masini)
# nrTotalMasiniPeJudet("ARAD")

def nrTotalMasiniPeCategorie(categorie):
    csvFile=read_csv("masini.csv")
    count=0
    nr_Total_Masini=0
    for line in csvFile:
        if count!=0 and str(line[3]).replace(" ","")==categorie:
            nr_Total_Masini = nr_Total_Masini + int(line[7])
        count+=1
    print(nr_Total_Masini)

# nrTotalMasiniPeCategorie("M3")

def nrTotalMasiniPeCombustibil(combustibil):
    csvFile=read_csv("masini.csv")
    count=0
    nr_Total_Masini=0
    for line in csvFile:
        if count!=0 and str(line[6]).replace(" ","")==combustibil:
            nr_Total_Masini = nr_Total_Masini + int(line[7])
        count+=1
    print(nr_Total_Masini)

# nrTotalMasiniPeCombustibil("MOTORINA")