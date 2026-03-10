import pandas as pd
import numpy as np

# 1. Simulação de Dados "Sujos" (O que acontece no mundo real)
data = {
    'ID': [1, 2, 3, 4, 5],
    'Nome_Ativo': ['Bitcoin', 'Ethereum', None, 'Cardano ', 'Solana'], # Note o espaço em 'Cardano '
    'Preco_USD': ['65000', '3500.50', '0', '0.45', '140.00'], # Preços como Texto
    'Data_Coleta': ['2026-03-09', '2026-03-09', '2026-03-09', '2026/03/09', '09-03-2026'] # Datas bagunçadas
}

df = pd.DataFrame(data)
print("📌 Dados Brutos (Sujos):")
print(df)
print("-" * 30)

# 2. PROCESSO DE EVOLUÇÃO (Transformação)
def limpar_dados_mercado(df_raw):
    df_limpo = df_raw.copy()
    
    # A. Corrigindo Tipos: Transformando Preço de Texto para Float
    df_limpo['Preco_USD'] = pd.to_numeric(df_limpo['Preco_USD'])
    
    # B. Padronizando Texto: Removendo espaços em branco e tratando nulos
    df_limpo['Nome_Ativo'] = df_limpo['Nome_Ativo'].str.strip()
    df_limpo['Nome_Ativo'] = df_limpo['Nome_Ativo'].fillna('Nao Identificado')
    
    # C. Normalizando Datas: Transformando tudo para o padrão AAAA-MM-DD
    df_limpo['Data_Coleta'] = pd.to_datetime(df_limpo['Data_Coleta'], dayfirst=False, errors='coerce').dt.strftime('%Y-%m-%d')
    
    return df_limpo

# 3. EXECUTANDO A LIMPEZA
df_final = limpar_dados_mercado(df)

print("✅ Dados Processados e Limpos (Log de Evolução - Yasmin Lopes):")
print(df_final)

# Mensagem final para o Log
print("\n[Log]: Desafio de Data Cleaning concluído com sucesso por Yasmin Lopes.")
