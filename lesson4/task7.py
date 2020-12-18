def fact_gen(number):
    fact_num = 1
    if number ==0:
        yield f'{number}! = 1'
    for i in range(1, number + 1):
        fact_num *= i
        yield  f'{i}! = {fact_num}'

for el in fact_gen(int(input("Факториал: "))):
    print(el)