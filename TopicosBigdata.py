
import pandas as pd
pd.options.display.float_format = "{:,.2f}".format

tabelaResultado = pd.DataFrame()
tabela = pd.read_csv("large.csv", chunksize=10000)
for parte in tabela:
    colunas = ["Amount Received", "Receiving Currency", "Amount Paid"]
    chunk_filtrado = parte[colunas]
    resumo = chunk_filtrado.groupby("Receiving Currency", as_index=False).sum()
    tabelaResultado = pd.concat([tabelaResultado, resumo])

tabelaResultado = tabelaResultado.groupby("Receiving Currency", as_index=False).sum()
print(tabelaResultado)