# Продажи

# Дана база данных о продажах некоторого интернет-магазина. Каждая строка
# входного файла представляет собой запись вида.

# Покупатель товар количество, где
# - Покупатель — имя покупателя (строка без пробелов),
# - товар — название товара (строка без пробелов),
# - количество — количество приобретенных единиц товара.
#
# Создайте список всех покупателей, а для каждого покупателя подсчитайте
# количество приобретенных им единиц каждого вида товаров.

# Вводятся сведения о покупках в указанном формате.
#
# Выведите список всех покупателей в лексикографическом порядке, после имени
# каждого покупателя выведите двоеточие, затем выведите список названий всех
# приобретенных данным покупателем товаров в лексикографическом порядке, после
# названия каждого товара выведите количество единиц товара, приобретенных
# данным покупателем. Информация о каждом товаре выводится в отдельной строке.


customerDict = dict()
tempDict = customerDict
inFile = open("input.txt", "r", encoding='utf-8')
for line in inFile:
    saleData = line.split()
    # print(saleData)
    customer = saleData[0]
    if customer in customerDict:
        # goods, count = saleData[1], saleData[2]
        customerDict[customer][saleData[1]] = \
            customerDict[customer].get(saleData[1], 0) + int(saleData[2])
    else:
        customerDict[customer] = {saleData[1]: int(saleData[2])}
# print(customerDict)
inFile.close()
# print(customerDict)
for customer in customerDict:
    print(customer, ":", sep="")
    goodsList = list()
    for goods in customerDict[customer]:
        goodsList.append((goods, customerDict[customer][goods]))
    goodsList.sort()
    for goods in goodsList:
        print(*goods)
