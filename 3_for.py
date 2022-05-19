""" student Mikhail Korotkov

Домашнее задание №1

Цикл for: Продажи товаров


* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

products = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]


def number_of_sales(sales):
    all_sales = 0
    if isinstance(sales, list):
        for sale in sales:
            all_sales += sale
    else:
        all_sales += sales
    return all_sales

def average_number_of_sales(all_sales, total_sales):
    average_sales = all_sales / total_sales
    return average_sales


def main():

    all_sales = 0

    for product in products:
        product['all_sales'] = number_of_sales(product['items_sold'])
        product['average_sales'] = average_number_of_sales(product['all_sales'], len(product['items_sold']))
        print(f"товар: {product['product']}, всего продано: {product['all_sales']}, среднее количество продаж: {product['average_sales']}")
    
    for product in products:
        all_sales += number_of_sales(product['all_sales'])

    average_sales = average_number_of_sales(all_sales, len(products[0]['items_sold']))
    
    print(f"Всего продано со склада: {all_sales}, Среднее количество продаж за месяц: {average_sales}")
    
if __name__ == "__main__":
    main()
