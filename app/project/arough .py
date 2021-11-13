import random


f = open('oldPhones1.txt', 'w', encoding="utf-8")


rowid = '101'
words = ("Adeel", "Shaadab", "Ali, 'faisal", 'ahmed', 'hamood', 'hammad')

account = 0
f = open('me.txt', 'w')

for i in range(10000000):
    f.write(
        f"put 'customers' , '{random.randint(101,2000000000000)}', 'details:{random.choice(words)}', '{random.randint(0,100000000000000)}'\n")


# import json
# import requests

# # url = "https://www.prepostseo.com/apis/checkPlag"


# # data = {"key": "6bca6abc57bc26a95ce2b0e734446979",
# #         'data':
# #         'bIt is also the most successful of hundreds of attempts to create virtual money through the use of cryptography, the science of making and breaking codes. Bitcoin has inspired hundreds of imitators, but it remains the largest cryptocurrency by market capitalization, a distinction it has held throughout its decade-plus history.\r\n\r\n(A general note: According to the Bitcoin Foundation, the word "Bitcoin" is capitalized when it refers to the cryptocurrency as an entity, and it is given as "bitcoin" when it refers to a quantity of the currency or the units themselves. Bitcoin is also abbreviated as BTC. Throughout this article, we will alternate between these usages'}

# # response = requests.post(url=url, data=data).json()
# # for i in response:
# #     print(i)
# # print(response)


# # json_object = json.dumps(response, indent=4)

# # # Writing to sample.json
# # with open("sample.json", "w") as outfile:
# #     outfile.write(json_object)


# with open('my.json', errors='ignore') as jsonfile:
#     response = json.load(jsonfile)

# # print(response)
# print('\n\nplagPercent', response['plagPercent'],
#       '\n\nparaphrasePercent', response['paraphrasePercent'],
#       '\n\nuniquePercent', response['uniquePercent'],
#       '\n\nsources', response['sources']
#       )
# for i in response['sources']:
#     print('\n\n\n\n', i)
#     print('\n\n\n\n percent :', i['percent'])
#     print('\n\n\n\ncount :', i['count'])
