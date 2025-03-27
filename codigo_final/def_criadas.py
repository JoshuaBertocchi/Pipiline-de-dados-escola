# %%
def detecta_codificacao(caminho_diretorio):
    import os  # Importa o módulo os para manipulação de diretórios e arquivos
    import chardet  # Importa chardet para detectar a codificação dos arquivos

    # Percorre todos os arquivos no diretório especificado
    for arquivo in os.listdir(caminho_diretorio):
        # Verifica se o arquivo tem a extensão .csv
        if arquivo.endswith('.csv'):
            caminho_completo = os.path.join(caminho_diretorio, arquivo)  # Obtém o caminho completo do arquivo

            # Detecta a codificação do arquivo
            with open(caminho_completo, 'rb') as f:
                result = chardet.detect(f.read(10000))  # Lê uma parte do arquivo e detecta a codificação
                encoding_detectado = result['encoding']  # Obtém a codificação detectada
                print(f"Convertendo {arquivo} de {encoding_detectado} para UTF-8")

            # Se a codificação não for detectada, assume 'ISO-8859-1' como padrão
            if encoding_detectado is None:
                encoding_detectado = 'ISO-8859-1'

            # Abre o arquivo na codificação detectada e lê o conteúdo
            with open(caminho_completo, 'r', encoding=encoding_detectado, errors='replace') as f:
                conteudo = f.read()

            # Reescreve o conteúdo no mesmo arquivo, mas agora em UTF-8
            with open(caminho_completo, 'w', encoding='utf-8') as f:
                f.write(conteudo)

    print("Todos os arquivos foram convertidos para UTF-8!")  # Mensagem final indicando que o processo terminou



# %%

caminho_diretorio_teste = ('G:/0_Estudos_Analise_de_Dados/07_Projeto/Banco_escola/DADOS_PROJETO/Perfil dos educandos')
caminho_diretorio = ('G:/0_Estudos_Analise_de_Dados/07_Projeto/Banco_escola/DADOS_PROJETO/Escolas')

#def leitura_e_tranformacao_em_df (caminho_diretorio):   

import pandas as pd
import os
import chardet

lista_dfs = []
dicionario_dataframes = {}
contador = 0

for arquivo  in os.listdir(caminho_diretorio):
    # Leitura dos arquivos no caminho_diretorio
    if arquivo.endswith('.csv'):
        print(f'✅ Arquivo .csv encontrado: {arquivo}')
        contador += 1
        caminho_completo = os.path.join(f'{caminho_diretorio}/{arquivo}')
        # Abrindo arquivo e identificando eu Encoding
        with open(caminho_completo, 'rb') as f:
            resultado = chardet.detect(f.read(10000))
            encoding_valor = resultado['encoding'].upper().strip()
            print(f'🌐{arquivo} Possuí decodificador : {encoding_valor}') 
            
        # Tratamento baseado no Encoding 
        if encoding_valor == 'UTF-8' or encoding_valor == 'UTF-8-SIG':
            print(f'O arquivo {arquivo} está no formato UTF-8!')
            df = pd.read_csv(caminho_completo, sep= ';', encoding='utf-8')
            df.columns = df.columns.str.upper()
            print(f'Aquivo  N°: {contador}(UTF-8) Transformado em DF!✅')
            print('🔃 Adicionando o DataFrame na Lista de DFs')
            lista_dfs.append(df) 
            print('Adicionado a lista ✅')
            print('🔃 Adicionando o DataFrame ao dicionário')
            dicionario_dataframes[arquivo] = df 
            print('✅ Adicionado ao dicionário!')
            lista_chaves = list(dicionario_dataframes.keys())
            

        elif encoding_valor == 'ISO-8859-1' or encoding_valor == 'ISO-8859-1':
            print(f'O arquivo {arquivo} está no formato ISO-8859-1!')
            df = pd.read_csv(caminho_completo, sep= ';', encoding='ISO-8859-1')
            print('🔃 Adicionando o DataFrame na Lista de DFs')
            lista_dfs.append(df)
            print('Adicionado a lista ✅')
            print('🔃 Adicionando o DataFrame ao dicionário')
            dicionario_dataframes[arquivo] = df 
            lista_chaves = list(dicionario_dataframes.keys())
            print('✅ Adicionado ao dicionário!')
        else:
            print(f'❌O arquivo {arquivo} está no formato {encoding_valor} e não é compatível com esse código, necessário ter Encoding UTF-8, UTF-8-SIG ou ISO-8859-1!')
    else:
        print(f'❌ Arquivo  {arquivo} não possui o formato compatível com o código. Transforme em CSV.')

print(f'📚 Total de DataFrames adicionados ao Dicionário:{len(dicionario_dataframes.keys())}')
print(f'📚 Total de DataFrames adicionados a Lista:{len(lista_dfs)}')
print(f'N° de DFs:{len(lista_chaves)}.')
print(f'Keys/chaves do dicionário:{lista_chaves}.')
# %%

dicionario_dataframes.keys()
dicionario_dataframes.items()

# %%

dicionario_dataframes_incorretos = {}
dicionario_dataframes_corretos = {}
contador_dfs_teste = 0
df_referencia = dicionario_dataframes['escolas-dez-2010.csv']

for chaves, df in dicionario_dataframes.items():
    contador_dfs_teste += 1

    if df.columns.equals(df_referencia.columns):
        print(f'🌐 Verificando {chaves} - Quantidade de colunas: {len(df.columns)}')
        #df_colunas_corretas.append(df)
        dicionario_dataframes_corretos[chaves] = df
        print('✅ Possui colunas iguais!')
    
    else:
        #df_colunas_incorretas.append(df)
        dicionario_dataframes_incorretos[chaves] = df
        print(f'🌐Verificando quantidade de colunas: {len(df.columns)}')
        print(f'❌ DF DIFERENTE :{contador_dfs_teste}')
       
print('✖️ Valores ✖️')
print(f'🔃 N° de df corretos: {len(dicionario_dataframes_corretos)}')
print(f'🔃 N° de df inccoretos: {len(dicionario_dataframes_incorretos)}')
# %%

#NOTE - Tratamento manual (TABELA CORRETAS)

for chave , df in dicionario_dataframes.items():
    dicionario_dataframes[chave].rename(columns = {"NOMES": "NOMESC", 
                                                    "NOMESCOFI": "NOMESCOF",
                                                    "CD_CIE": "CODCIE"}, inplace = True)


# %%
for index , df in dicionario_dataframes_corretos.items():
    print(index, df.columns) 

for index , df in enumerate(dicionario_dataframes_incorretos):
    print('Incorretas',index, df)
# %%
dicionario_dataframes_incorretos['escolasr34dez2017.csv'].columns
# %%
colunas_drop = [
    'T2D3D', 'T2D3D15', 'T2D3D14', 'T2D3D13', 'T2D3D12', 'T2D3D11', 'T2D3D10', 'T2D3D09', 'T2D3D08', 'T2D3D07',
    'DTURNOS', 'DTURNOS15', 'DTURNOS14', 'DTURNOS13', 'DTURNOS12', 'DTURNOS11', 'DTURNOS10', 'DTURNOS09', 'DTURNOS08', 'DTURNOS07',
    'T2D3D', 'T2D3D16', 'T2D3D15', 'T2D3D14', 'T2D3D13', 'T2D3D12', 'T2D3D11', 'T2D3D10', 'T2D3D09', 'T2D3D08', 'T2D3D07',
    'DTURNOS', 'DTURNOS16', 'DTURNOS15', 'DTURNOS14', 'DTURNOS13', 'DTURNOS12', 'DTURNOS11', 'DTURNOS10', 'DTURNOS09', 'DTURNOS08', 'DTURNOS07'
]

dicionario_dataframes_incorretos['escolasr34dez2017.csv'].drop(columns = colunas_drop, inplace = True, errors = 'ignore')
dicionario_dataframes_incorretos['escolasr34.csv'].drop(columns = colunas_drop, inplace = True, errors = 'ignore')
# %%
dicionario_dataframes_incorretos['escolasr34.csv']
# %%
df_correto = dicionario_dataframes_corretos['escolas-dez-2010.csv']
df_incorreto = dicionario_dataframes_incorretos['escolasr34.csv']

cols_df1 = set(df_correto)
cols_df2 = set(df_incorreto)

apenas_df1 = cols_df1 - cols_df2
apenas_df2 = cols_df2 - cols_df1
print(f'Colunas na Tabalea 01{apenas_df1}')
print(f'Colunas na Tabalea 02{apenas_df2}')
# %%


df_referencia = dicionario_dataframes_corretos['escolas-dez-2010.csv']

for chaves, df in dicionario_dataframes.items():
    contador_dfs_teste += 1

    if df.columns.equals(df_referencia.columns):
        print(f'🌐 Verificando {chaves} - Quantidade de colunas: {len(df.columns)}')
        #df_colunas_corretas.append(df)
        dicionario_dataframes_corretos[chaves] = df
        print('✅ Possui colunas iguais!')
    
    else:
        #df_colunas_incorretas.append(df)
        dicionario_dataframes_incorretos[chaves] = df
        print(f'🌐Verificando quantidade de colunas: {len(df.columns)}')
        print(f'❌ DF DIFERENTE :{contador_dfs_teste}')
       
print('✖️ Valores ✖️')
print(f'🔃 N° de df corretos: {len(dicionario_dataframes_corretos)}')
print(f'🔃 N° de df inccoretos: {len(dicionario_dataframes_incorretos)}')
# %%
