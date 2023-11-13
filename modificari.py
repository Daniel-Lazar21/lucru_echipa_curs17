import pandas as pd
CALE_FISIER = r"C:\Users\Krisztian\Probleme\Curs17\Proiect\masini.csv"

def modificare_judet(cale_fisier):
    df = pd.read_csv(cale_fisier)
    df['JUDET'] = df["JUDET"].replace(['DOLJ', 'OLT','GORJ','VALCEA','MEHEDINTI'], 'OLTENIA')
    df.to_csv(cale_fisier, index = False)
    return df

modificare_judet(CALE_FISIER)