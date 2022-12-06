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

final_sentence = f"In our country, some smartphones are very popular like {brand_name_one}, {brand_name_two}, {brand_name_3}, {brand_name_4},\n{brand_name_5}, {brand_name_6} and etc. These smartphones manufacturer country are {manufacturer_country_one}, the {manufacturer_country_two}, {manufacturer_country_3}, {manufacturer_country_4}, the {manufacturer_country_5},\nand {manufacturer_country_6}. The retail price of these phones, some are reasonable and some have extreme. The {brand_name_one}\nprice is {retail_price_one} which is very extreme for middle and lower-class people, especially for unemployed vagabond-type\npeople like me. Can you imagine {retail_price_one} equal to how much Bangla taka? This is {usd_to_bdt} BDT. I am sure Aouwal vai\nyou are laughing but don't know for buying this type of smartphone I have to go without food for 5 months. On the\nother hand, {brand_name_6} and {brand_name_two} are only made for Taposh Gosh because {retail_price_6} and {retail_price_two} is equal to\n{usd_to_bdt_6} BDT and {usd_to_bdt_two} BDT which is not a Dada-type amount. But {brand_name_4} and {brand_name_5} are reasonable I think.\nThe {retail_price_4} and {retail_price_5} are the prices If I fast for two months I hope I can buy them because {usd_to_bdt_4}\nBDT and  {usd_to_bdt_5} BDT are not giant amounts. But if I work a little harder and go without food for another month,\nI think I can own an {brand_name_3}. The price is only {retail_price_3} which is almost equal to {usd_to_bdt_3} BDT."

print(final_sentence)
