goods = []
while input("Добавить новые товары? ") == 'Да':
    number = int(input("Введите количество товара: "))
    features = {}
    feature_key = input("Введите название товара: ")
    feature_value = input("Введите цену товара: ")
    feature_unit = input("Введите единицу измерения количества")
    features[feature_key] = feature_value
    goods.append(tuple([number, features]))
print(goods)
analitic = {}
for good in goods:
    for feature_key, feature_value in good[1].items():
        if feature_key in analitic:
            analitic[feature_key].append(feature_value, feature_unit)
        else:
         analitic[feature_key] = [feature_value, feature_unit]
print(analitic)