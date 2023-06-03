""" игра компьютер угадывает число рандомно"""
import numpy as np

def random_predict(number=1) -> int:
    """_summary_

    Args:
        num (int, optional): заданное число. Defaults to 1.

    Returns:
        int: число попыток
    """
    count=0
    while True:
        numr=np.random.randint(0, 100)
        count+=1
        if numr == number:
            return count


def score_game(random_predict) ->int:
    """среднее число

    Args:
        random_predict (int): на входе рандомное число от 0 до 100

    Returns:
        int: среднее значение от попыток
    """
    count_ls=[]
    np.random.seed(1)
    random_array=  np.random.randint(0,100,size=(1800))
    for nummer in random_array:
        count_ls.append(random_predict(nummer))
    score = int(np.mean(count_ls))
    return score   
if __name__ == "__main__":
    print(score_game(random_predict))     