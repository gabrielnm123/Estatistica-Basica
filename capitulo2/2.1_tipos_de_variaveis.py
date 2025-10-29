import pandas as pd
import numpy as np

# Cada linha da matriz corresponde a uma unidade de investigação (por exemplo, uma unidade amostral) e cada coluna, a uma variável, que corresponde à realização de uma característica.

# Importar os dados do Excel. 
tab21 = pd.read_excel('./Dados_EB.xlsx', sheet_name='Tabela 2.1', header=[0, 1]) # Importa as duas primeiras linhas como cabeçalho

# Limpeza de dados
level0_labels = tab21.columns.get_level_values(0).to_list() # Nível Pai
level1_labels = tab21.columns.get_level_values(1).to_list() # Nível Filho

for i in range(len(level0_labels)):
    if level1_labels[i] not in ['Anos', 'Meses']:
        level0_labels[i] = level1_labels[i] # Copia o nome do nível filho para o nível pai
        level1_labels[i] = None # Limpa o nível filho

tab21.columns = pd.MultiIndex.from_arrays([level0_labels, level1_labels]) # Atualiza o cabeçalho
del(level0_labels, level1_labels, i) # Limpa o ambiente

# Visualizar as linhas, selecionando a coluna nan.
print(tab21['Estado Civil'][np.nan])

# Podemos facilmente saber quais são as variáveis importadas por meio do comando
print(tab21.columns)

# Variáveis qualitativas são aquelas que expressam uma qualidade ou característica, não podendo ser medidas numericamente.
    # Nominais: não possuem uma ordem intrínseca (por exemplo, cor dos olhos, estado civil).
    # Ordinais: possuem uma ordem intrínseca (por exemplo, nível de escolaridade, classe social).
# Variáveis quantitativas são aquelas que expressam uma quantidade, podendo ser medidas numericamente.
    # Discretas: assumem valores inteiros (por exemplo, número de filhos, número de carros).
    # Contínuas: podem assumir qualquer valor dentro de um intervalo (por exemplo, altura, peso, temperatura).
