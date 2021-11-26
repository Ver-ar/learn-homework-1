"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


from typing import MutableMapping

def hello_user():

  while True:

    question = str(input('Как дела?\n'))
    if question == "Хорошо":
      break
    else:
      question = str(input('Как дела?\n'))
    
        
if __name__ == "__main__":
  hello_user()