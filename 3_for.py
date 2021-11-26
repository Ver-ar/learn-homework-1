"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по количеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

def main():
  sales = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
  
  def count_phone_sold(phone_items_sold):
    items_sold_sum = 0
    for item_sold in phone_items_sold:
      items_sold_sum += item_sold
    return count_phone_sold
  
        
  def count_phone_sold_avg(phone_items_sold):
    items_sold_sum = 0
    for item_sold in phone_items_sold:
      items_sold_sum += item_sold
    return round(items_sold_sum / len(phone_items_sold), 2)
        
  sales_sum = 0
  for phone in sales:
        
    phone_sold = count_phone_sold(phone["items_sold"])
    phone_sold_avg = count_phone_sold_avg(phone["items_sold"])
        

        
    sales_sum += phone_sold()
    sales_sum_avg = round(sales_sum / len(sales), 2)

    print(f'Среднее количество продаж {phone["product"]}: {phone_sold_avg}')
    print(f'Суммарное количество продаж {phone["product"]}: {phone_sold}')        
    
  print(f'Среднее количество всех продаж: {sales_sum}')
  print(f'Суммарное количество всех продаж: {sales_sum_avg}')
    
    
if __name__ == "__main__":
  main()