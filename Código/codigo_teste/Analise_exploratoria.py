# %%
import pandas as pd

# %%
df_2010 = pd.read_csv('G:/0_Estudos_Analise_de_Dados/07_Projeto/Banco_escola/DADOS_PROJETO/Data/Data/Escolas/escolas-dez-2010.csv', sep= ';')
df_2011 = pd.read_csv('G:/0_Estudos_Analise_de_Dados/07_Projeto/Banco_escola/DADOS_PROJETO/Data/Data/Escolas/escolas-dez-2011.csv', sep= ';')

# %%
import pandas as pd
from ydata_profiling import ProfileReport

caminho_arquivo = ('G:/0_Estudos_Analise_de_Dados/07_Projeto/Banco_escola/DADOS_PROJETO/Data/Data/Escolas/escolas-dez-2011.csv')

df = pd.read_csv(caminho_arquivo, sep= ';')
profile = ProfileReport(df, title="Profiling Report")
profile.to_file('Analise_exploratoria')

# %%
