my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('task4.txt', 'w', encoding='utf-8') as new_block:
    with open('task4.txt', encoding='utf-8') as orig_block:
        new_block.writelines([line.replace(line.split()[0], my_dict.get(line.split()[0])) for line in orig_block])