# -*- coding: utf-8 -*-
"""ProjetoPandas2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ruFlBBlj2RTRRYaIbwuqMcUyix1jctsN

**Criando colunas numericas**
"""

import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
pd.read_csv(url)
dados = pd.read_csv(url, sep=';')
dados

dados['Valor_por_mes'] = dados['Valor'] + dados['Condominio']
dados.head()

dados['Valor_por ano'] = dados['Valor_por_mes'] * 12 + dados['IPTU']
dados.head()

"""**Criando colunas categoricas**"""

dados['Descricao'] = dados['Tipo'] + ' em ' + dados['Bairro']
dados.head()

dados['Descricao'] = dados['Tipo'] + ' em ' + dados['Bairro'] + ' com ' + \
                    dados['Quartos'].astype(str) + ' quarto(s) ' + \
                    ' e ' + dados['Vagas'].astype(str) + ' vaga(s) de garagem.'
dados.head()

dados['Possui_suite'] = dados['Suites'].apply(lambda x: "Sim" if x > 0 else "Nao")
dados.head()

dados.to_csv('dados_completos_dev.csv', index=False, sep=';')

pd.read_csv('dados_completos_dev.csv', sep=';')
