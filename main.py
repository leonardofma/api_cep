from ctypes import addressof
from email.headerregistry import Address
from traceback import print_tb
from urllib import request
import requests

def main():
    print('iniciando busca')

    cep_input = input('Digite o CEP para consulta: ')

    if len(cep_input) != 8:
        print('CEP invalido')
        exit()

    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))


    address_data = request.json()

    if 'erro' not in address_data:
        print('CEP:{}'.format(address_data['cep']))
        print('Logradouro:{}'.format(address_data['logradouro']))
        print('Complemento:{}'.format(address_data['complemento']))
        print('Bairro:{}'.format(address_data['bairro']))
        print('Cidade:{}'.format(address_data['localidade']))
        print('Estado:{}'.format(address_data['uf']))
    else:
        print(cep_input)    



print(main())