from tabela.tabela import Tabela
import pandas as pd

tabela = Tabela(pd.read_excel(r'\\wsl.localhost\Ubuntu\home\gabriel\wp\estatistica_basica\Dados_EB.xlsx', sheet_name='Tabela 2.1', header=[1]))
tabela = Tabela(pd.read_excel('./Dados_EB.xlsx', sheet_name='Tabela 2.1', header=[1]))
tabela_2_1 = tabela.tab.copy()
tabela_2_2 = tabela.frequencia_proporcao('Grau de Instrução')
tabela_2_4 = tabela.frequencia_variavel_continua('Salario (x Sal Min)', amplitude=4)
pass
