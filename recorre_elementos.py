import json
import requests


print('Ingresar seller_id: ')
seller_id = input()
r = requests.get('https://api.mercadolibre.com/sites/MLA/search?seller_id='+seller_id)
packages_json = r.json()


f = open('log', 'w')

f.write('Item ID: \n')
for x in packages_json['results']:
    f.write(x['id']+'\n')

f.write('Item title: \n')
for x in packages_json['results']:
    f.write(x['title']+'\n')

f.write('Category id: \n')
for x in packages_json['results']:
    f.write(x['category_id']+'\n')

f.close()
