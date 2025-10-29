from tabela.tabela import TabelaPb

# tabela = TabelaPb(1, r'\\wsl.localhost\Ubuntu\home\gabriel\wp\   estatistica_basica\Dados_EB.xlsx', sheet_name='Tabela 2.1', sheet_name='Tabela 2.1', header=[1])
tabela = TabelaPb(1, './Dados_EB.xlsx', sheet_name='Tabela 2.1', header=[1])
tabela_2_1 = tabela.tab
tabela_2_2 = tabela.frequencia_proporcao('Grau de Instrução')
tabela_2_4 = tabela.frequencia_variavel_continua('Salario (x Sal Min)', amplitude=4)
pass
