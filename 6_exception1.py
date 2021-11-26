"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

from typing import MutableMapping

def hello_user():

  try:

    while True:

      question = str(input('Как дела?\n'))

      if question == "Хорошо":
        break

      else:      
        question = str(input('Как дела?\n'))
        
  except KeyboardInterrupt:
    print('Пока!')
  
        
        
if __name__ == "__main__":
  hello_user()