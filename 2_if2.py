"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():
  while True:

    first_line = input('Введите первую строку: ')
    second_line = input('Введите вторую строку: ')
    

    try:
      first_line = str(first_line)
      second_line = str(second_line)
        
      def comparsions(first_line, second_line):
        if first_line == second_line:
          return '1'
        elif first_line != second_line and len(first_line) >= len(second_line):
          return '2'
        elif first_line != second_line and second_line == 'learn':
          return '3'
            
      print(comparsions(first_line, second_line))
      
    except ValueError:
      print('0')
      continue

    
if __name__ == "__main__":
  main()