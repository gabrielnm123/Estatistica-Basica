import pandas as pd
from math import floor

class TabelaPb():
    def __init__(self, *args, type: int=0, sort_values_by_variavel: str=None, sort_values_ascending: bool=True, **kwargs) -> None:
        if type == 0:
            if sort_values_by_variavel:
                self.tab = pd.read_excel(*args, **kwargs).sort_values(by=sort_values_by_variavel, ascending=sort_values_ascending)
            else:
                self.tab = pd.read_excel(*args, **kwargs)
        else:
            self.tab = None    
        if 'Anos' in self.tab.columns and 'Meses' in self.tab.columns:
            self.tab.rename(columns={'Anos': 'Idade'}, inplace=True)
            self.tab['Idade'] = self.tab['Idade'] + self.tab['Meses'] / 12
            self.tab = self.tab.round({'Idade': 2})
            self.tab.drop('Meses', axis=1, inplace=True)

    def frequencia(self, variavel:str, tab: pd.DataFrame=None, sort_values_by_variavel: str=None, sort_values_ascending: bool = True) -> pd.DataFrame:
        tab = tab.sort_values(by=variavel if sort_values_by_variavel == None else sort_values_by_variavel, ascending=sort_values_ascending) if type(tab) == pd.DataFrame else self.tab.sort_values(by=variavel if sort_values_by_variavel == None else sort_values_by_variavel, ascending=sort_values_ascending)
        return pd.DataFrame(tab[variavel].value_counts(sort=False)).reset_index().rename(columns={'count': 'Frequência n_i'}).astype(object)

    def frequencia_proporcao(self, *args, **kwargs) -> pd.DataFrame:
        tab = self.frequencia(*args, **kwargs)
        tab['Proporção f_i'] = tab['Frequência n_i'] / tab['Frequência n_i'].sum()
        return tab
    
    def frequencia_variavel_continua(self, variavel:str, amplitude:int, tab: pd.DataFrame=None, *args, **kwargs) -> pd.DataFrame:
        tab = tab.copy() if type(tab) == pd.DataFrame else self.tab.copy()
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
        return self.frequencia(classes, tab, variavel, *args, **kwargs)
    
class Tabela(TabelaPb):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        if 'N' in self.tab.columns:
            self.tab.drop('N', axis=1, inplace=True)

    def _frequencia(self, *args, **kwargs) -> pd.DataFrame:
        tab = super().frequencia(*args, **kwargs)
        tab['Porcentagem 100 f_i'] = (tab['Frequência n_i'] / tab['Frequência n_i'].sum()) * 100
        return tab

    def frequencia(self, *args, **kwargs) -> pd.DataFrame:
        tab = self._frequencia(*args, **kwargs)
        tab.loc[len(tab)] = ['Total' if index == 0 else round(tab[tab.columns[index]].sum()) for index in range(len(tab.columns))]
        return tab

    def frequencia_proporcao(self, *args, **kwargs) -> pd.DataFrame:
        tab = self._frequencia(*args, **kwargs)
        tab['Proporção f_i'] = tab['Frequência n_i'] / tab['Frequência n_i'].sum()
        tab.loc[len(tab)] = ['Total' if index == 0 else round(tab[tab.columns[index]].sum()) for index in range(len(tab.columns))]
        return tab
