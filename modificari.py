import pandas as pd
CALE_FISIER = r"C:\Users\Krisztian\Probleme\Curs17\Proiect\masini.csv"

def modificare_judet(cale_fisier):
    df = pd.read_csv(cale_fisier)
    df['JUDET'] = df["JUDET"].replace(['DOLJ', 'OLT','GORJ','VALCEA','MEHEDINTI'], 'OLTENIA')
    df.to_csv(cale_fisier, index = False)
    return df

modificare_judet(CALE_FISIER)

def modificare_benzina(cale_fisier):
    df = pd.read_csv(cale_fisier)
    df['VALUE_NAME'] = df["VALUE_NAME"].replace(['BENZINA+E85', 'BENZINA+GNC','BENZINA+GPL','BENZINA+ULEI'], 'BENZINA')
    df.to_csv(cale_fisier, index = False)
    return df

modificare_benzina(CALE_FISIER)