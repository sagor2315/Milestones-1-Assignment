mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    'exchnage_rate': 103.25
}

#Xiaomi Note 5 is a smartphone made in China with a price tag of 300 USD, which
# is nearly equal to 30975 Bangladeshi Taka.

for mobile in mobile_data.get('data'):
    brand_name = mobile.get('name')
    retail_price = mobile.get('price')
    manufec_country = mobile.get('made')
    exchange_rate = mobile_data.get('exchnage_rate')
    usd_string_to_digit = float(mobile.get('price').replace('USD',''))
    usd_to_bdt = usd_string_to_digit * exchange_rate
    sentence = f'{brand_name} is a smartphone made in {manufec_country} with a price tag of {retail_price},\nwhich is nearly equal to {usd_to_bdt} BDT Bangladeshi Taka.\n'
    print(sentence)
