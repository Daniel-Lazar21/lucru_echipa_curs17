import csv
import pandas as pd

#afisari:
    #afiseaza toate masinile dintr-un judet anume 
def afisare_masini_judet_anume(cale,judet):
    df = pd.read_csv(cale+'/masini.csv')
    rez= df.query("JUDET == @judet")
    print(rez)   
    
#afiseaza toate masinile dintr-o categorie anume 
def afisare_masini_categorie_anume(cale,categorie):
    df = pd.read_csv(cale+'/masini.csv')
    #am modificat linia  'rez = df[categorie]' deoarece dadea o eroare plus ca asa selectam toata coloana si daca 
    #ziceam ca vreau toate autobuzele imi dadea eroare pentru ca autobuze nu apare in header-ul fisierului masini.csv
    rez = df.query("CATEGORIE_NATIONALA == @categorie")
    print(rez)    
    
#afiseaza toate masinile care sunt mai multe de 10
def afisare_numar_masini_10(cale):
    df = pd.read_csv(cale+'/masini.csv')
    rez = df.query('TOTAL_VEHICULE > 10 ')
    rez=rez.query("CATEGORIE_NATIONALA == 'AUTOTURISM'")
    print(rez)
