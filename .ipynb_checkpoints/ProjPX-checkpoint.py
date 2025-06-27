import plotly.express as px
import pandas as pd
#GRAFICO DE LINHAS
dados_x=[ '2018' , '2019','2020' , '2021']
dados_y = [10, 20, 5, 35]

fig = px.line(x = dados_x, y =dados_y, title = "Vendas X Ano", height= 400, width = 1000)
fig.update_yaxes(title= 'Vendas',title_font_color ='red', ticks= 'outside', tickfont_color='yellow')
fig.show()
#GRAFICO DE PIZZA
dados_x=[ '2018' , '2019','2020' , '2021']
dados_y = [10, 20, 5, 35]

fig = px.pie(names = dados_x, values=dados_y, width = 300 , height = 300)
fig.show()
#GRAFICO DE BARRAS
dados_x=[ '2018' , '2019','2020' , '2021']
dados_y = [10, 20, 5, 35]

fig = px.bar ( x = dados_x, y = dados_y,width = 700 , height = 300 )
fig.show()
#IMPORTANDO A TABELA PARA ANALISE
df_cronograma = pd.read_excel('Tarefas.xlsx')
display (df_cronograma)
#TRANSFORMANDO OS DADOS EM GRAFICOS
fig = px.timeline(df_cronograma, x_start="Início", x_end="Fim", y="Tarefa")
fig.update_yaxes(autorange="reversed")
fig.show()