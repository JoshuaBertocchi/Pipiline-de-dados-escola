#%%

from codigo import unif_df


#%%

caminho_arquivo_referencia = 'G:/0_Estudos_Analise_de_Dados/07_Projeto/Projeto_escola_py/DADOS_PROJETO/Escolas/escolas-dez-2010.csv'

arquivo_referencia = unif_df(None,caminho_arquivo_referencia)
arquivo_referencia

# %%


caminho_diretorio = 'G:/0_Estudos_Analise_de_Dados/07_Projeto/Projeto_escola_py/DADOS_PROJETO/Escolas'

dicionario_df = unif_df(caminho_diretorio , None)
dicionario_df
# %%
