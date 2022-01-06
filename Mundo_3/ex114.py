"""
Exercício Python 114:
Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
"""
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('O Site Pudim não está disponível!')
else:
    print('O Site Pudim está disponível!')
    print(site.read())
