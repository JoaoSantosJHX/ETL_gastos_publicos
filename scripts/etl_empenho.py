import pandas as pd

# Caminho do arquivo CSV
caminho_arquivo = 'dados/20250101_Despesas_Empenho.csv'

# Leitura com delimitador e enconding apropriados
df = pd.read_csv(caminho_arquivo, sep=';', encoding='latin1')

# Limpar espaços e aspas das colunas
df.columns = df.columns.str.strip().str.replace('"', '')

# Conversão da data
df['Data Emissão'] = pd.to_datetime(df['Data Emissão'], errors='coerce', dayfirst=True)

# Conversão dos valores (removendo pontos de milhar e vírgulas decimais)
df['Valor do Empenho Convertido pra R$'] = (
    df['Valor do Empenho Convertido pra R$'].astype(str)
    .str.replace('.','',regex=False)
    .str.replace(',','.',regex=False)
    .astype(float)
)

# Criação da coluna ano-mês para análise temporal
df['ano-mes'] = df['Data Emissão'].dt.to_period('M').astype(str)

# Agrupamento por órgão superior, categoria e mês
resumo = (
    df.groupby(['ano-mes', 'Órgão Superior', 'Categoria de Despesa'])['Valor do Empenho Convertido pra R$']
    .sum()
    .reset_index()
    .rename(columns={'Valor do Empenho Convertido pra R$': 'Valor_empenhado'})
)

# Exportação para análise no Power BI
resumo.to_csv('export/empenhos_tratados.csv', index=False, sep=';', encoding='utf-8')

print("✅ ETL finalizado com sucesso! Arquivo exportado para 'export/empenhos_tratados.csv'")