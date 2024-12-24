from time import sleep

from tqdm import tqdm

if __name__ == '__main__':
    for i in tqdm(range(2000), desc='Прогресс-бар'):
        sleep(0.003)
    for i in tqdm(range(1000), desc='Второй'):
        sleep(0.001)

