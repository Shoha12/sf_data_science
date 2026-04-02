import numpy as np

def random_predict(number:int= 1) -> int:
  """Рандомно угадываем число за меньше чем 20 попыток 

  Args:
      number (int, optional): Загаданное число . Defaults to 1.

  Returns:
      int: Число попыток
  """
  
  count = 0 
  low = 1 # нижняя граница диапазона поиска
  high = 100 # верхняя граница диапазона поиска
  
  while True:
    count += 1
    predict = (low + high) // 2 # берём середину диапазона
    if number > predict:
      low = predict + 1
    elif number < predict:
      high = predict - 1
    else:
      break # число найдено
  
  return count

print(f'Количество попыток: {random_predict()}')


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
score_game(random_predict)