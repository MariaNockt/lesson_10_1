import threading
from time import sleep, time

def write_words (word_count, file_name):
    with open(file_name, 'w') as f:
        for i in range(1, word_count + 1):
            f.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

# взятие текущего времени
start_time = time()

# запись функций с аргументами из задачи
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

# взятие текущего времени
end_time = time()
print(f'время выполнения функций: {end_time - start_time} секунд')

# взятие текущего времени для потоков
start_time_threads = time()

# создание потоков
threads = []
threads.append(threading.Thread(target=write_words, args=(10, 'example5.txt')))
threads.append(threading.Thread(target=write_words, args=(30, 'example6.txt')))
threads.append(threading.Thread(target=write_words, args=(200, 'example7.txt')))
threads.append(threading.Thread(target=write_words, args=(100, 'example8.txt')))

# запуск протоколов
for thread in threads:
    thread.start()

# ожидание завершения протоколов
for thread in threads:
    thread.join()

# взятие текущего времени
end_time_threads = time()
print(f'время выполнения протоколов: {end_time_threads - start_time_threads} секунд')