import pandas as pd
from sklearn.naive_bayes import GaussianNB
import variaveis

atributos = variaveis.atributos
resultados = variaveis.resultados

modelo = GaussianNB()
modelo.fit(atributos, resultados)

print('TRIAGEM CORONA VIRUS')
print('Responda as perguntas com 0 para  não e 1 para sim')

febre = int(input("Febre? "))
cansaco = int(input("Cansaço? "))
tosse = int(input("Tosse Seca? "))
espirro = int(input("Espirro? "))
dorCorpo = int(input("Dor no Corpo? "))
corizando = int(input("Corizando? "))
dorGarganta = int(input("Dor na Garganta? "))
diarreia = int(input("Diarreia? "))
dorCabeca = int(input("Dor de Cabeça? "))
faltaAr = int(input("Falta de Ar? "))

dadosColetados = [febre,cansaco,tosse,espirro,dorCorpo,corizando,dorGarganta,
diarreia,dorCabeca,faltaAr]

novos = dadosColetados


resposta = modelo.predict([novos])

if resposta == 1 :
    print('Resultado: ')
    print('Recomenda-se fazer o teste de corona vírus')
else:
    print('Resultado: ')
    print('Paciente não apresenta sintomas de corona vírus')
