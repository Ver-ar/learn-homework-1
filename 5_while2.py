"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

questions_and_answers = {"Как дела?": "Хорошо", "Что делаешь?": "Программирую","А вчера что делал?": "Отдыхал","Как настроение?": "Отличное","Когда восстание машин?": "Не знаю, меня не позвали("}

def ask_user(answers_dict):

  while True:  

    question = str(input("Спрашивай!\n"))

    if question in answers_dict:
      print(answers_dict.get(question), '\n' )
    
    elif question == ("Пока!"):
      break

    else:
      print("Спроси что-нибудь другое\n")
      continue

if __name__ == "__main__":
    ask_user(questions_and_answers)
