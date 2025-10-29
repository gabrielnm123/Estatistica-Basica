import pandas as pd
from math import floor

class TabelaPb():
    def __init__(self, tab: pd.DataFrame) -> None:
        self.tab = tab.copy()
        if 'Anos' in self.tab.columns and 'Meses' in self.tab.columns:
            self.tab['Idade'] = self.tab['Anos'] + self.tab['Meses'] / 12
            colunas = self.tab.columns.to_list()
            colunas.insert(colunas.index('Anos'), colunas.pop())
            colunas.remove('Anos')
            colunas.remove('Meses')
            self.tab = self.tab[colunas]

    def frequencia(self, variavel:str, tab: pd.DataFrame=None) -> pd.DataFrame:
        tab = tab if type(tab) == pd.DataFrame else self.tab.copy()
        return pd.DataFrame(tab[variavel].value_counts()).reset_index().rename(columns={'count': 'Frequência n_i'})

    def frequencia_proporcao(self, variavel:str) -> pd.DataFrame:
        tabela_freq = self.frequencia(variavel)
        total = tabela_freq['Frequência n_i'].sum()
        tabela_freq['Proporção f_i'] = tabela_freq['Frequência n_i'] / total
        return tabela_freq.copy()
    
    def frequencia_variavel_continua(self, variavel:str, amplitude:int) -> pd.DataFrame:
        tab = self.tab.copy()
        variavel_dados = tab[variavel].to_list()
        variavel_dados.sort()
        variavel_min = floor(variavel_dados[0])
        variavel_max = variavel_min + amplitude
        classes = f'Classes de {variavel}'
        while not (variavel_min > variavel_dados[-1]):
            classe = f'[{variavel_min}, {variavel_max})'
            for valor in variavel_dados:
                if variavel_min <= valor < variavel_max:
                    tab.loc[tab[variavel] == valor, classes] = classe
            variavel_min = variavel_max
            variavel_max += amplitude
        return self.frequencia(classes, tab)
    
class Tabela(TabelaPb):
    def __init__(self, tab: pd.DataFrame) -> None:
        super().__init__(tab)

class Teste(pd):
    def __init__(self) -> None:
        # a alteração do __init__ tem que vim antes do super().__init__() ou depois
        super().__init__()

    def teste(self, dados: dict) -> dict:
        return dados
