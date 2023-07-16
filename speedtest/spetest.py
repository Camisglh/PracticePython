# установка библиотек
# pip install speedtest-cli
import speedtest

s = speedtest.Speedtest()

print("Подключение к серверам...")
s.get_servers() # получить список серверов
print("Выбор лучшего сервера...")
s.get_best_server() # выбрать лучший сервер

print("Выполняется тест скорости загрузки...")
download_speed = s.download() # получить скорость загрузки

print("Выполняется тест скорости отдачи...")
upload_speed = s.upload() # получить скорость отдачи

print(f"Скорость загрузки: {download_speed / 1024 / 1024:.2f} Mbit/s")
print(f"Скорость отдачи: {upload_speed / 1024 / 1024:.2f} Mbit/s")