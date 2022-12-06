import random
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
#  For Sentence One
brand_name_one = mobile_data.get('data')[0].get('name')
manufacturer_country_one = mobile_data.get('data')[0].get('made')
retail_price_one = mobile_data.get('data')[0].get('price')
conv_retail_price_one_to_int = int(retail_price_one.replace('USD',''))
usd_to_bdt = mobile_data.get('exchnage_rate') * conv_retail_price_one_to_int

#  For Sentence Two
brand_name_two = mobile_data.get('data')[1].get('name')
manufacturer_country_two = mobile_data.get('data')[1].get('made')
retail_price_two = mobile_data.get('data')[1].get('price')
conv_retail_price_two_to_int = int(retail_price_two.replace('USD',''))
usd_to_bdt_two = mobile_data.get('exchnage_rate') * conv_retail_price_two_to_int

#  For Sentence Three
brand_name_3 = mobile_data.get('data')[2].get('name')
manufacturer_country_3 = mobile_data.get('data')[2].get('made')
retail_price_3 = mobile_data.get('data')[2].get('price')
conv_retail_price_3_to_int = float(retail_price_3.replace('USD',''))
usd_to_bdt_3 = mobile_data.get('exchnage_rate') * conv_retail_price_3_to_int

#  For Sentence Four
brand_name_4 = mobile_data.get('data')[3].get('name')
manufacturer_country_4 = mobile_data.get('data')[3].get('made')
retail_price_4 = mobile_data.get('data')[3].get('price')
conv_retail_price_4_to_int = float(retail_price_4.replace('USD',''))
usd_to_bdt_4 = mobile_data.get('exchnage_rate') * conv_retail_price_4_to_int

#  For Sentence Five
brand_name_5 = mobile_data.get('data')[4].get('name')
manufacturer_country_5 = mobile_data.get('data')[4].get('made')
retail_price_5 = mobile_data.get('data')[4].get('price')
conv_retail_price_5_to_int = int(retail_price_5.replace('USD',''))
usd_to_bdt_5 = mobile_data.get('exchnage_rate') * conv_retail_price_5_to_int

#  For Sentence Six
brand_name_6 = mobile_data.get('data')[5].get('name')
manufacturer_country_6 = mobile_data.get('data')[5].get('made')
retail_price_6 = mobile_data.get('data')[5].get('price')
conv_retail_price_6_to_int = int(retail_price_6.replace('USD',''))
usd_to_bdt_6 = mobile_data.get('exchnage_rate') * conv_retail_price_6_to_int

sentence_one = [
    f'{brand_name_one} is made in {manufacturer_country_one}.The price is {retail_price_one} which is almost equal to {usd_to_bdt} BDT',
    f'{manufacturer_country_one} is the manufacturer of {brand_name_one}. In bangla taka {usd_to_bdt} BDT is actual price which is equal to {retail_price_one}',
    f'{manufacturer_country_one} is the place where {brand_name_one} manufacture. In {usd_to_bdt} BDT or {brand_name_one} is the retail price.'
]

sentence_two = [
    f'{brand_name_two} is made in {manufacturer_country_two}. The price is {retail_price_two} which is\nalmost equal to {usd_to_bdt_two} BDT',
    f'{brand_name_two} is not a Bangladeshi smartphone cause it is manufactured by {manufacturer_country_two}. The retail price is {retail_price_two} if you convert to Bangla taka then it will be {usd_to_bdt_two} BDT.',
    f'{brand_name_3} is made in {manufacturer_country_3}. The price is {retail_price_3} which is almost equal to {usd_to_bdt_3} BDT',

    f'{brand_name_4} is made in {manufacturer_country_4}. The price is {retail_price_4} which is almost equal to {usd_to_bdt_4} BDT',

    f'{brand_name_5} is made in {manufacturer_country_5}. The price is {retail_price_5} which is almost equal to {usd_to_bdt_5} BDT',

    f'{brand_name_6} is made in {manufacturer_country_6}. The price is {retail_price_6} which is\nalmost equal to {usd_to_bdt_6} BDT']

sentence_1 = random.choice(sentence_one)
sentence_2 = random.choice(sentence_two)

full_sentence = f'{sentence_2} {sentence_1}'
print(full_sentence)
