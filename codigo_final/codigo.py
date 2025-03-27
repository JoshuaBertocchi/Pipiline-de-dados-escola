#%%
import pandas as pd
import os
import chardet



#%%
def unif_df (caminho_diretorio, caminho_arquivo_referencia):
    contador = 0
    dicionario_dataframes = {}
    if caminho_arquivo_referencia is not None:
        with open(caminho_arquivo_referencia, 'rb') as f:
            resultado = chardet.detect(f.read(10000))
            encoding_valor = resultado['encoding'].upper().strip()
            print(f'🌐 Arquivo Referência possuí decodificador : {encoding_valor} {caminho_arquivo_referencia}')
        df_ref = pd.read_csv(caminho_arquivo_referencia,sep= ';', encoding=encoding_valor)
        print(f'🌐Arquivo referência foi transformado em DF')
        return df_ref
    else:
        print('Caminho is None')

    for arquivo in os.listdir(caminho_diretorio):
        if caminho_diretorio is not None:
            if arquivo.endswith('.csv'):
                print(f'✅ Arquivo .csv encontrado: {arquivo}')
                contador += 1
                caminho_completo = os.path.join(f'{caminho_diretorio}/{arquivo}')
                # Abrindo arquivo e identificando eu Encoding
                with open(caminho_completo, 'rb') as f:
                    resultado = chardet.detect(f.read(10000))
                    encoding_valor = resultado['encoding'].upper().strip()
                    print(f'🌐{arquivo} Possuí decodificador : {encoding_valor}')

                df = pd.read_csv(caminho_completo, sep= ';', encoding= encoding_valor)
                df.columns = df.columns.str.upper()
                print(f'Aquivo  N°: {contador} Transformado em DF!✅')
                print('🔃 Adicionando o DataFrame ao dicionário')
                dicionario_dataframes[arquivo] = df 
                print('✅ Adicionado ao dicionário!')  
            else:
                print(f'❌ Arquivo  {arquivo} não possui o formato compatível com o código. Transforme em CSV.')
        else: 
            print('Caminho is None')
    print(f'🐍 Total de dicionários: {contador}')  
    return dicionario_dataframes


#%%


caminho_diretorio = 'G:/0_Estudos_Analise_de_Dados/07_Projeto/Projeto_escola_py/DADOS_PROJETO/Escolas'
caminho_arquivo_referencia = 'G:/0_Estudos_Analise_de_Dados/07_Projeto/Projeto_escola_py/DADOS_PROJETO/Escolas/escolas-dez-2010.csv'

arquivo_referencia = unif_df(None,caminho_arquivo_referencia)
print(arquivo_referencia)

#%%

dicionario_df = unif_df(caminho_diretorio , None)

#%%
def analise_colunas (dicionario_dataframes, df_referencia):
    contador_dfs = 0
    dicionario_dataframes_incorretos = {}
    dicionario_dataframes_corretos = {}
    for chaves, df in dicionario_dataframes.items():
        contador_dfs += 1

        if df.columns.equals(df_referencia.columns):
            print(f'🌐 Verificando {chaves} - Quantidade de colunas: {len(df.columns)}')
            dicionario_dataframes_corretos[chaves] = df
            print('✅ Possui colunas iguais!')
        
        else:
            dicionario_dataframes_incorretos[chaves] = df
            print(f'🌐Verificando quantidade de colunas: {len(df.columns)}')
            print(f'❌ DF DIFERENTE :{contador_dfs}')
        
    print('✖️ Valores ✖️')
    print(f'🔃 N° de df corretos: {len(dicionario_dataframes_corretos)}')
    print(f'🔃 N° de df inccoretos: {len(dicionario_dataframes_incorretos)}')
            
#%%

