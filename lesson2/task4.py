user_words = input("Введите несколько слов, разделенных пробелами: ")
a = user_words.split(' ')
for i, el in enumerate(a, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{i}. - {el}")