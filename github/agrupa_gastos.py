import pandas as pd

def agrupa_gastos(df):

    df = pd.read_csv('raw/gastos-deputados-2018-rj.csv')	

    # agrupa por ano, nome, partido e uf
    print('Agrupando os gastos por deputado...')
    gasto = df.groupby(['numano', 'txnomeparlamentar', 'sguf'])['vlrliquido'].s$
    gasto = gasto.append(gasto.sum(numeric_only=True), ignore_index=True)

    # ordena por maior gasto
    print('Ordenando os gastos...')
    gasto = gasto.sort_values('vlrliquido', ascending=True).reset_index(drop=Tr$

    # salva o csv 
    path = 'gastos-agrupados-2018-rj.csv'
    gasto.to_csv(path)

    print('Tudo pronto! Base salva em {}'.format(path))
    return gasto


if __name__ == '__main__':

    agrupa_gastos('raw/gastos-deputados-2018-rj.csv')
