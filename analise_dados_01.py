# region ENUNCIADOS
#
# # Exercício - Mini Projeto de Análise de Dados
# 
# Vamos fazer um exercício completo de pandas para um miniprojeto de análise de dados.
# 
# Esse exercício vai obrigar a gente a usar boa parte dos conhecimento de pandas e até de outros módulos que 
# já aprendemos ao longo do curso.
# 
# ### O que temos?
# 
# Temos os dados de 2019 de uma empresa de prestação de serviços. 
# 
# - CadastroFuncionarios
# - CadastroClientes
# - BaseServiçosPrestados
# 
# Obs1: Para ler arquivos csv, temos o read_csv
# Obs2: Para ler arquivos xlsx (arquivos em excel normais, que não são padrão csv), temos o read_excel
# 
# ### O que queremos saber/fazer?
# 
# 1. Valor Total da Folha Salarial -> Qual foi o gasto total com salários de funcionários pela empresa?
#     Sugestão: calcule o salário total de cada funcionário, salário + benefícios + impostos, depois some todos os salários   
#     
# 2. Qual foi o faturamento da empresa?
#     Sugestão: calcule o faturamento total de cada serviço e depois some o faturamento de todos
#    
# 3. Qual o % de funcionários que já fechou algum contrato?
#     Sugestão: na base de serviços temos o funcionário que fechou cada serviço. 
#     Mas nem todos os funcionários que a empresa tem já fecharam algum serviço.
#     . Na base de funcionários temos uma lista com todos os funcionários
#     . Queremos calcular Qtde_Funcionarios_Fecharam_Serviço / Qtde_Funcionários_Totais
#     . Para calcular a qtde de funcionários que fecharam algum serviço, use a base de serviços e 
#       conte quantos funcionários tem ali. Mas lembre-se, cada funcionário só pode ser contado uma única vez.
#     Dica: se você aplicar o método .unique() em uma variável que é apenas 1 coluna de um dataframe, 
#           ele vai excluir todos os valores duplicados daquela coluna.
#     Ex: unicos_colunaA = dataframe['colunaA'].unique() te dá como resposta uma lista com todos os 
#           itens da colunaA aparecendo uma única vez. 
#           Todos os valores repetidos da colunaA são excluidos da variável unicos_colunaA 
#   
# 4. Calcule o total de contratos que cada área da empresa já fechou
# 
# 5. Calcule o total de funcionários por área
# 
# 6. Qual o ticket médio mensal (faturamento médio mensal) dos contratos?
#     Dica: .mean() calcula a média -> exemplo: media_colunaA = dataframe['colunaA'].mean()
# 
# Obs: Lembrando as opções mais usuais de encoding:
# encoding='latin1', encoding='ISO-8859-1', encoding='utf-8' ou então encoding='cp1252'
# 
# Observação Importante: Se o seu código der um erro na hora de importar os arquivos:
# - CadastroClientes.csv
# - CadastroFuncionarios.csv
# 
# Use separador ";" (ponto e vírgula) para resolver

###
#endregion

#region IMPORTS
#
import pandas as pd
from IPython.display import display
#
#endregion

#region QUESTÃO 1 - Qual foi o gasto total com salários de funcionários pela empresa?
#
# funcionarios= pd.read_csv(r'CadastroFuncionarios.csv', sep= ';', decimal= ',')
# # funcionarios.info()
# despesa_total= funcionarios['Salario Base'] + funcionarios['Impostos'] + funcionarios['Beneficios'] \
#     + funcionarios['VR'] + funcionarios['VT']
# despesa_total= despesa_total.sum()
# print('Despesa total com funcionários: R${:,.2f}'.format(despesa_total).replace(',', ' '))
# #.format(despesa_total.sum())) 
# #.str.replace(',', ' ')))
#
#endregion

#region QUESTÃO 2 - Qual foi o faturamento da empresa?
#
# servicos= pd.read_excel(r'BaseServiçosPrestados.xlsx')
# clientes= pd.read_csv(r'CadastroClientes.csv', sep=';' , )
# serv_clientes = pd.DataFrame.merge(servicos, clientes, on='ID Cliente')
# # serv_clientes.info()
# serv_clientes['Valor Total por Cliente'] = serv_clientes['Tempo Total de Contrato (Meses)'] * serv_clientes['Valor Contrato Mensal']
# # display(serv_clientes)
# receita_total = serv_clientes['Valor Total por Cliente'].sum()
# print('Receita Total: R${:,.2f}'.format(receita_total).replace(',',' '))
#
#endregion

#region QUESTÃO 3 - Qual o % de funcionários que já fechou algum contrato?
#
# como teste, resolvi trazer no merge() inclusive os funcionarios que não venderam serviço algum para tratar depois.
# o tratamento que deixando o parâmetro how no default (inner) já eliminaria os funcionários que não venderam.
# outra opção seria usar o .fillna(0) no merge(). Para fins de negócio traria distorções que podem ser indicadores de
# produtividade média por exemplo.
# enfim, o intuito aqui é aprender a tratar NULL/NaN

# funcionarios= pd.read_csv(r'CadastroFuncionarios.csv', sep= ';', decimal= ',')
# servicos= pd.read_excel(r'BaseServiçosPrestados.xlsx')

# func_serv= pd.DataFrame.merge(funcionarios, servicos, on= 'ID Funcionário', how= 'outer')#.fillna(0)
# # #func_serv.info()
# # #func_serv.to_csv('teste_func_serv_01.csv', sep= ';')
# func_venderam= func_serv[func_serv['Codigo do Servico'].notnull()]
# func_venderam= len(func_venderam['ID Funcionário'].unique())
# func_venderam= func_venderam/len(funcionarios['ID Funcionário'])
# print(f'Percentual de funcionários que realizaram venda: {func_venderam:.2%}')

#
#endregion

#region QUESTÃO 4 - Calcule o total de contratos que cada área da empresa já fechou
#
# funcionarios = pd.read_csv(r'CadastroFuncionarios.csv', sep= ';')
# vendas = pd.read_excel(r'BaseServiçosPrestados.xlsx')
# func_vendas = pd.DataFrame.merge(funcionarios, vendas, on= 'ID Funcionário')
# # func_vendas.info()
# # func_vendas.to_csv(r'teste_funcionarios_vendas.csv', sep= ';')
#     # pegar quais sao as areas e quantas vezes cada uma delas aparece em vendas_func
# areas = func_vendas['Area'].value_counts()
# print(f'Quantidade de Vendas por Área:\n{areas}')
#
#endregion

#region QUESTÃO 5 - Calcule o total de funcionários por área
#
# funcionarios = pd.read_csv(r'CadastroFuncionarios.csv', sep= ';')
# func_area = funcionarios['Area'].value_counts()
# print(f'Fionários por área:\n{func_area}')
#
#endregion

#region QUESTÃO 6 - Qual o ticket médio mensal (faturamento médio mensal) dos contratos?
#
# clientes = pd.read_csv(r'CadastroClientes.csv', sep= ';')
# clientes.info()
# ticket_medio_mes = clientes['Valor Contrato Mensal'].mean()
# print('Ticket Médio Mensal: R${:,.2f}'.format(ticket_medio_mes).replace(',', ' '))
#
#endregion