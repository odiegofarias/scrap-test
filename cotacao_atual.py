import requests
from parsel import Selector
from time import sleep
import json

"""
    ETAPAS DA APLICAÇÃO:
        V  - Acessar o site e coletar as categorias selecionadas - https://mundofii.com/categorias/
        V  - Com base nas categorias, acessar e pegar o ticker dos fundos imob. Ex: https://mundofii.com/categorias/galpoes-logisticos
        V  - Com base nesses tickers, pegar a cotação atual de cada fundo imob. Ex: https://mundofii.com/fundos/HGLG11
        X   - Salvar em um arquivo separado por categorias
"""

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

categorias = ['hibrido', 'shoppings', 'recebiveis-imobiliarios', 'galpoes-logisticos']
# , 'shoppings', 'recebiveis-imobiliarios', 'galpoes-logisticos'

fundos_imob = dict()

for consulta in range(len(categorias)):
    categoria = categorias[consulta]

    r_get_fundos_por_categoria = requests.get(f'https://mundofii.com/categorias/{categoria}', headers=headers)

    sel = Selector(text=r_get_fundos_por_categoria.text)
    fiis = sel.xpath("//span[@class='fii_siglaCompleta tCor2 claro']/text()").getall()

    fundos_imob[categoria] = fiis

dic = dict()

for chave, valor in fundos_imob.items():
    for ticker in valor:
        
        r = requests.post('https://www.clubefii.com.br/pega_cotacao', headers=headers, data={'cod_neg': ticker})

        """
            - Pegar cotação no mundofii
            # sel = Selector(text=r.text)
            # cotacao_atual = sel.xpath("//span[@class='flash_card--a card noWrap noMargin noPadding 100% th4']/b/text()").get().strip()
        """
        data_json = r.text.split(';')[0][:6]
        cotacao_atual = data_json
        dic[ticker] = cotacao_atual

        print(f'Buscando por: {ticker}')

        sleep(0.5)
        
with open(f'arquivo.json', 'w') as f:
    json.dump(dic, f, indent=4)








        

    
 





            


    
