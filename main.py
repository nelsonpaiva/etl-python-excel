#utilizo a blibioteca do pandas para ler o csv e transformar em dataframe
import pandas as pd 
#fazer o import da própria biblioteca do pandas profiling
from ydata_profiling import ProfileReport

#vou utilizar uma função onde ele usa um método da classe do pandas que lê o dataframe e 
# vai transformar esse csv dentro do meu código python
df = pd.read_csv('data.csv')

#utilizo esses outros dois métodos do python para me mostar um relatório pronto
profile = ProfileReport(df, title='Profiling Report')
profile.to_file("output.html")