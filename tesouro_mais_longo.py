import requests
import json


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

r = requests.get('https://www.tesourodireto.com.br/json/br/com/b3/tesourodireto/service/api/treasurybondsinfo.json', headers=headers)

data = json.loads(r.text)

tesouro_mais_longo = data['response']['TrsrBdTradgList'][51]['TrsrBd']['anulInvstmtRate']
print(tesouro_mais_longo)

