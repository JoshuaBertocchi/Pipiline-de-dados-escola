# %%
import pandas as pd
import os


diretorio = ('G:/0_Estudos_Analise_de_Dados/07_Projeto/Banco_escola/DADOS_PROJETO/Data/Data/Escolas')
lista_dfs = []
dataframes = {}
contador = 0


for arquivos  in os.listdir(diretorio):
    if arquivos.endswith('.csv'):
        print(f'✅ Arquivo .csv encontrado: {arquivos}')
        try:
            contador += 1
            caminho_completo = os.path.join(f'{diretorio}/{arquivos}')
            df = pd.read_csv(caminho_completo, sep= ';', encoding='utf-8')
            df.columns = df.columns.str.upper()
            
            print(f'Aquivo N°: {contador} Transformado em DF!✅')

            try:
                contador += 1
                print('🔃 Adicionando o DataFrame na Lista de DFs')
                lista_dfs.append(df)
                print('Adicionado a lista ✅')
                dataframes[arquivos] = df # Talvez eu use isso aqui
                print('✅ Adicionado ao dicionário!')
            except Exception as e:
                print(f"❌ Erro!!! Arquivo não pode ser adiciona na lista {arquivos}: {str(e)}")

        except Exception as e:
            print(f"🔥 Erro ao ler {arquivos}: {str(e)}")
    else:
        
        print(f'❌ Arquivo  {arquivos} não possui o formato compatível com o código. Transforme em CSV.')
print(f'📚 Total de DataFrames adicionados ao dicionário:{len(dataframes.keys())}')

# %%
def detecta_codificacao(caminho_diretorio):
    import pandas as pd
    import sqlite3 
    import os
    import chardet
    for arquivo in os.listdir(caminho_diretorio):
        if arquivo.endswith('.csv'):
            caminho_completo = os.path.join(caminho_diretorio, arquivo)

            # Detecta a codificação
            with open(caminho_completo, 'rb') as f:
                result = chardet.detect(f.read(10000))
                encoding_detectado = result['encoding']
                print(f"Convertendo {arquivo} de {encoding_detectado} para UTF-8")

            if encoding_detectado is None:
                encoding_detectado = 'ISO-8859-1'

            # Lê o arquivo na codificação detectada e reescreve em UTF-8
            with open(caminho_completo, 'r', encoding=encoding_detectado, errors='replace') as f:
                conteudo = f.read()

            with open(caminho_completo, 'w', encoding='utf-8') as f:
                f.write(conteudo)

    print("Todos os arquivos foram convertidos para UTF-8!")

detecta_codificacao('G:/0_Estudos_Analise_de_Dados/07_Projeto/Banco_escola/DADOS_PROJETO/Data/Data/Escolas')


# %%
dataframes
# %%
#NOTE SEPARAÇÃO DAS DFs QUE POSSUEM DIFERENÇAS NAS COLUNAS

df_colunas_incorretas = []
df_colunas_corretas = []
contador_dfs_teste = 0
for i in lista_dfs:
    if lista_dfs[0].columns.equals(i.columns):
        contador_dfs_teste += 1
        print(f'🌐Verificando quantidade de colunas: {len(i.columns)}')
        df_colunas_corretas.append(i)
        
        print('✅ Possui colunas iguais!')
    else:
        contador_dfs_teste += 1
        df_colunas_incorretas.append(i)
        print(f'🌐Verificando quantidade de colunas: {len(i.columns)}')
        print(f'❌ DF DIFERENTE :{contador_dfs_teste}')
        #for i in range(len(df_colunas_incorretas)):
            #df_colunas_incorretas[i].columns = df_colunas_incorretas[i].columns.str.upper().str.strip()
            
print('✖️ Valores ✖️')
print(f'🔃 N° de df corretos: {len(df_colunas_corretas)}')
print(f'🔃 N° de df inccoretos: {len(df_colunas_incorretas)}')
# %%
#NOTE SEPARAÇÃO DAS DFs QUE POSSUEM DIFERENÇAS NAS COLUNAS

#NOTE TRATAMENTO INDIVIDUAL DE CADA TABELA 


contador_0 = 0
for idx, df in enumerate(df_colunas_corretas):
    if 'NOMES'not in df.columns:
        print(f'DataFrame {idx}: Não possui a coluna "NOMES"')
    else:
        contador_0 += 1
        df.rename(columns= {'NOMES':'NOMESC'}, inplace = True)
        print(f'DataFrame {idx}: Coluna "NOMES" renomeada para "NOMESC"!')

# %%
colunas_drop = [
    'T2D3D', 'T2D3D15', 'T2D3D14', 'T2D3D13', 'T2D3D12', 'T2D3D11', 'T2D3D10', 'T2D3D09', 'T2D3D08', 'T2D3D07',
    'DTURNOS', 'DTURNOS15', 'DTURNOS14', 'DTURNOS13', 'DTURNOS12', 'DTURNOS11', 'DTURNOS10', 'DTURNOS09', 'DTURNOS08', 'DTURNOS07',
    'T2D3D', 'T2D3D16', 'T2D3D15', 'T2D3D14', 'T2D3D13', 'T2D3D12', 'T2D3D11', 'T2D3D10', 'T2D3D09', 'T2D3D08', 'T2D3D07',
    'DTURNOS', 'DTURNOS16', 'DTURNOS15', 'DTURNOS14', 'DTURNOS13', 'DTURNOS12', 'DTURNOS11', 'DTURNOS10', 'DTURNOS09', 'DTURNOS08', 'DTURNOS07'
]
df_colunas_incorretas[5].drop(columns = colunas_drop, inplace = True, errors  = 'ignore')
df_colunas_incorretas[4].drop(columns = colunas_drop, inplace = True, errors  = 'ignore')

df_colunas_incorretas[3].rename(columns= {'NOMES':'NOMESC'}, inplace = True)
df_colunas_incorretas[3].rename(columns= {'FX_ETARIA.1':'FX_ETARIA',                                           
                                          'DESLOC' : 'NOMESCOFI'}, inplace = True) #'CDIST':'CODDIST'
df_colunas_incorretas[0].rename(columns={'DOC_CRIACAO': 'DOM_CRIACAO',
                                         'DT_EXTINTAO' : 'DT_EXTINCAO'}, inplace = True)
df_colunas_incorretas[1].rename(columns={'DT_EXTINTAO' : 'DT_EXTINCAO'}, inplace = True)
#df_colunas_incorretas[4].rename(columns = {'CODCIE':'CODDIST'}, inplace = True)


# %%
#LINK - COMPARADOR DE COLUNAS
df_correto = df_final
df_incorreto = df_colunas_incorretas[5]

cols_df1 = set(df_correto)
cols_df2 = set(df_incorreto)

apenas_df1 = cols_df1 - cols_df2
apenas_df2 = cols_df2 - cols_df1
print(f'Colunas na Tabalea 01{apenas_df1}')
print(f'Colunas na Tabalea 02{apenas_df2}')
# #LINK - COMPARADOR DE COLUNAS
# %%

df_colunas_incorretas[4].columns.tolist()
#df_colunas_incorretas[4]['CODDIST']

# %%
#NOTE UNINDO AS LISTAS 

uniao_lista_01 = pd.concat(df_colunas_corretas, axis= 0, ignore_index= True)
uniao_lista_01.shape
# %%

for df in df_colunas_incorretas:
    
    colunas = df.columns.tolist()
    colunas.sort()
    print(colunas)
#%% 


df_colunas_incorretas[3].shape

# %%
todos_dfs = []
for df in df_colunas_incorretas + df_colunas_corretas:
    df_resetado = df.reset_index(drop=True)  # Remove o índice antigo
    todos_dfs.append(df_resetado)

# Concatena todos os DataFrames
df_final = pd.concat(todos_dfs, axis=0, ignore_index=True)


#%%
#NOTE - #Verificando Dicionário
dataframes.values()
dataframes.keys()
dataframes.items()
#NOTE -

#%%
#Percorre cada DataFrame na lista e mostra suas colunas
for idx, df in enumerate(df_colunas_incorretas):
    print(f"\n📊 DataFrame {idx + 1} de {len(lista_dfs)}")
    print("Colunas:", df.columns.tolist())  # Lista das colunas
    print("Número de linhas:", len(df))
    print(f"Isna: {df.isna().sum()}")
    print("-" * 50)
# %%

#NOTE - Código criação Analise Exploratória
from ydata_profiling import ProfileReport
profile = ProfileReport(df_final, title="Profiling Report")
profile.to_file('Analise_exploratoria')
#NOTE - Código criação Analise Exploratória