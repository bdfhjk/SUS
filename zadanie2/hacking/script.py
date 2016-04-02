import sys
import pandas as pd
df       = pd.read_csv('banking.csv')
final_df = pd.read_csv('test.csv')

final_df_sorted = [pd.DataFrame()]*100
df_sorted = [pd.DataFrame]*100

for i, dd in final_df.groupby('wiek'):
    final_df_sorted[i] = dd

for i, dd in df.groupby('age'):
    df_sorted[i] = dd
    

for i in range(17, 98):
    sys.stderr.write(str(i) + '\n')
    for numer, kolumna in final_df_sorted[i].iterrows():
        for index, row in df_sorted[i].iterrows():
            if  row['y'] == 1 and \
                row['age'] == kolumna['wiek'] and \
                row['default'] == kolumna['debet'] and \
                row['housing'] == kolumna['hipoteka'] and \
                row['cons_conf_idx'] == kolumna['CCI'] and \
                row['job'] == kolumna['zawod'] and \
                row['marital'] == kolumna['stan_cywilny'] and \
                row['education'] == kolumna['wyksztalcenie'] and \
                row['loan'] == kolumna['pozyczka'] and \
                row['pdays'] == kolumna['przerwa'] and \
                row['emp_var_rate'] == kolumna['zmiennosc_zatrudnienia'] and \
                row['previous'] == kolumna['poprzednie'] and \
                row['poutcome'] == kolumna['poprzedni_wynik'] and \
                row['campaign'] == kolumna['liczba_kontaktow'] and \
                row['cons_price_idx'] == kolumna['CPI'] and \
                row['euribor3m'] == kolumna['EURIBOR3M'] and \
                row['nr_employed'] == kolumna['wskaznik_zatrudnienia']:
                    print kolumna['id_klienta'] 
