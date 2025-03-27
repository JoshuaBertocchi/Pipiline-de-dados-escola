import pandas as pd
import sqlite3 
import os
import chardet

## Padronizados para utf-8
caminho_diretorio = 'G:/0_Estudos_Analise_de_Dados/07_Projeto/DADOS_PROJETO/Data/Data/Escolas'

def detecta_codificacao(caminho_completo):
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



##Transformando em lista com df

 

def list_dataframes(caminho_diretorio):
    lista_dfs= []

    for arquivo in os.listdir(caminho_diretorio):
        if arquivo.endswith('.csv'):
            caminho_completo = caminho_diretorio + '/' + arquivo
            df = pd.read_csv(caminho_completo, sep=";", encoding='utf-8',  ) 
            lista_dfs.append(df)
        else:
            continue

    return lista_dfs 
        


## Padronizando as colunas



def padroniza_colunas(lista_dfs, colunas_padrao, colunas_para_dropar):
    for df in lista_dfs:
        columns_upper = df.columns.str.upper()  # Converte os nomes das colunas para maiúsculas
        colunas_em_comum = set(colunas_para_dropar) & set(columns_upper)
        
        if len(colunas_em_comum) > 0:
            df.drop(columns=colunas_em_comum, axis=1, inplace=True)
            
            print('Colunas removidas.')
        else:
            print('Colunas não encontradas, já podem ter sido excluidas em uma execução anterior!')
        #df.rename(columns= dict(zip(df.columns, columns_upper)), inplace= True)
        df.columns = df.columns.str.upper()


if __name__ == '__main__':
    
    caminho_diretorio = 'G:/0_Estudos_Analise_de_Dados/07_Projeto/DADOS_PROJETO/Data/Data/Escolas'
    detecta_codificacao(caminho_diretorio)
    lista_dfs = list_dataframes(caminho_diretorio)

    colunas_padrao = [
    "DRE", "CODESC", "TIPOESC", "NOMESC", "NOMESCOFI", "CEU", "DIRETORIA", "SUBPREF",
    "ENDERECO", "NUMERO", "BAIRRO", "CEP", "TEL1", "TEL2", "FAX", "SITUACAO", "CODDIST",
    "DISTRITO", "SETOR", "CODINEP", "CD_CIE", "EH", "FX_ETARIA", "DT_CRIACAO", "ATO_CRIACAO",
    "DOM_CRIACAO", "DT_INI_CONV", "DT_AUTORIZA", "DT_EXTINCAO", "NOME_ANT", "REDE",
    "LATITUDE", "LONGITUDE", "DATABASE"
    ]

    colunas_para_dropar = [
        'T2D3D', 'T2D3D15', 'T2D3D14', 'T2D3D13', 'T2D3D12', 'T2D3D11', 'T2D3D10', 'T2D3D09', 'T2D3D08', 'T2D3D07',
        'DTURNOS', 'DTURNOS15', 'DTURNOS14', 'DTURNOS13', 'DTURNOS12', 'DTURNOS11', 'DTURNOS10', 'DTURNOS09', 'DTURNOS08', 'DTURNOS07',
        'T2D3D16', 'DTURNOS16'
    ]

    padroniza_colunas(lista_dfs, colunas_padrao, colunas_para_dropar)

for i, df in enumerate(lista_dfs, start=1):
    print(f'Tabela {i} tem {len(df.columns)} colunas: {list(df.columns)}')


