#importação das bibliotecas
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters
np.float = float
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean data
limiteBaixo = df['value'].quantile(0.025) 
limiteAlto = df['value'].quantile(0.975)
    # Seleciona os valores maiores que o limite baixo e menores que o limite e retorna como o novo dataset
df = df[(df['value'] >= limiteBaixo) & (df['value'] <= limiteAlto)] 

def draw_line_plot():
    # Draw line plot
    df_glinha = df.copy()
        #Cria a figura e o eixo delimitando o tamanho
    fig, ax = plt.subplots(figsize=(20,6))
        #Desenha a linha
    ax.plot(df_glinha.index, df_glinha['value'], linewidth=1, color='purple')
        #Define o título e nomes dos eixos
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    
    #Cria duas colunas: ano e mês
    df_bar['ano'] = df_bar.index.year
    df_bar['mes'] = df_bar.index.month

    # Draw bar plot
    media = df_bar.groupby(['ano','mes'])['value'].mean()
    tabela= media.unstack(level='mes') # organiza a tabela em linhas=anos e colunas=meses
    tabela[range(1,13)] #Reordena as colunas para garantir meses de 1 até 12
    fig,ax = plt.subplots(figsize=(12,8)) #cria a figura e define o tamanho
    barras = tabela.plot(kind='bar', ax=ax)
    #define o nome dos eixos
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    nomes_mes = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    legenda = ax.legend(title='Months', labels=nomes_mes)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    meses_abrev = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    fig,(ax1, ax2) = plt.subplots(1, 2, figsize=(22,6)) #cria a figura e define o tamanho
    #Boxplot 1 - por ano
    sns.boxplot(data=df_box, x='year', y='value', ax=ax1)
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Page Views")
    #Boxplot 2 - por mês
    sns.boxplot(data=df_box, x='month', y='value', ax=ax2, order=meses_abrev)
    ax2.set_title("Month-wise Box Plot (Seasonality)")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
