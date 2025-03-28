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


lista_50= [1,2,3,4,5,6,7,8,1,1,1,1,2,2,2,2,3,5,1,3,10,23]
lista = []


for index, valores in enumerate(lista_50):
    if valores == 
    print(index, valores)



# %%
lista
# %%
# Lista de exemplo (você pode mudar esses valores)
lista = [1, 2, 3, 2, 5, 3, 4]

# Dicionário para guardar onde cada número aparece
posicoes_dos_numeros = {}

# Percorre a lista e guarda as posições de cada número
for posicao, numero in enumerate(lista):
    if numero not in posicoes_dos_numeros:
        posicoes_dos_numeros[numero] = []  # Cria uma lista vazia para o número
    posicoes_dos_numeros[numero].append(posicao)  # Adiciona a posição

# Mostra os resultados
print("Análise da lista:", lista)
print("\nPosições de cada número:")
for numero, posicoes in posicoes_dos_numeros.items():
    print(f"Número {numero} aparece nas posições: {posicoes}")

# Verifica quais números se repetem
print("\nValores que se repetem:")
tem_repetido = False
for numero, posicoes in posicoes_dos_numeros.items():
    if len(posicoes) > 1:  # Se o número aparece em mais de uma posição
        print(f"→ Número {numero} aparece {len(posicoes)} vezes, nas posições: {posicoes}")
        tem_repetido = True

if not tem_repetido:
    print("Nenhum valor se repete na lista.")