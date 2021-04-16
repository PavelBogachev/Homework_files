from pprint import pprint


def merge_files(names_files):
    list_files = []
    for i, name in enumerate(names_files):
        list_files.append([])
        with open(name, encoding='utf-8') as f:
            lines = f.readlines()
            list_files[i].append(len(lines))
            list_files[i].append({'name': name, 'lines': lines})
    list_files.sort()
    with open('test.txt', 'a', encoding='utf-8') as f:
        for file in list_files:
            f.write(f'{file[1]["name"]}\n')
            f.write(f'{file[0]}\n')
            for line in file[1]['lines']:
                f.write(line)
            f.write('\n')


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    cook_book_dict = get_cook_book()
    for dish in dishes:
        for ingredient in cook_book_dict[dish]:
            if ingredient['ingredient_name'] not in shop_list:
                shop_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                            'quantity': person_count * ingredient['quantity']}
            else:
                shop_list[ingredient['ingredient_name']]['quantity'] += person_count * ingredient['quantity']
    return shop_list


def get_cook_book():
    with open('cook_book.txt',  encoding='utf-8') as f:
        cook_book_dict = {}
        dish = f.readline().strip()
        while dish != '':
            cook_book_dict[dish] = []
            count = int(f.readline().strip())
            for i in range(count):
                ingredient = f.readline().strip()
                first_sep = ingredient.find('|')
                second_sep = ingredient.rfind('|')
                ingredient_name = ingredient[:first_sep].strip()
                quantity = int(ingredient[first_sep + 1: second_sep].strip())
                measure = ingredient[second_sep + 1:].strip()
                ingredient_dict = {'ingredient_name': ingredient_name,
                                   'quantity': quantity,
                                   'measure': measure}
                cook_book_dict[dish].append(ingredient_dict)
            f.readline()
            dish = f.readline().strip()
    return cook_book_dict


def main():
    cook_book_dict = get_cook_book()
    shop_list = get_shop_list_by_dishes(['Фахитос', 'Омлет'], 3)
    pprint(cook_book_dict)
    pprint(shop_list)
    merge_files(['1.txt', '2.txt', '3.txt'])


if __name__ == '__main__':
    main()
