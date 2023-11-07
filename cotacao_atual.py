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

dic = dict()

fundos_imobiliarios = ['ALZR11', 'KNRI11', 'HGLG11', 'HGCR11', 'BTLG11', 'BRCO11', 'HGRU11' ,'HGBS11' ,'TRXF11', 'AFHI11', 'HSML11', 'BTAL11', 'TGAR11', 'KNSC11', 'VGHF11', 'CPTS11', 'PATL11']

# for chave, valor in fundos_imob.items():
for ativo in fundos_imobiliarios:
    
    r = requests.post('https://www.clubefii.com.br/pega_cotacao', headers=headers, data={'cod_neg': ativo})

    """
        - Pegar cotação no mundofii
        # sel = Selector(text=r.text)
        # cotacao_atual = sel.xpath("//span[@class='flash_card--a card noWrap noMargin noPadding 100% th4']/b/text()").get().strip()
    """
    data_json = r.text.split(';')[0][:6]
    cotacao_atual = data_json
    dic[ativo] = cotacao_atual

    print(f'Buscando por: {ativo}')

    sleep(0.5)
    
with open(f'arquivo.json', 'w') as f:
    json.dump(dic, f, indent=4)
    f.write(agora)








        

    
 





            


    
