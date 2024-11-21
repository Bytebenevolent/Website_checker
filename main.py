import requests
from pyfiglet import Figlet


FIGLET = Figlet(font = 'bubble')


def main():
    print(FIGLET.renderText("Website checker"))  # Установка шрифта.
    url = ''
    check_website_availability(url)


def check_website_availability(url):
    while True:
        print("Для выхода введите: exit")
        url = input("Введите URL сайта для проверки(пример: https://example.com): ")
        if url == 'exit'.lower():
            print(FIGLET.renderText("Website checker"))
            break
        try:
            response = requests.get(url, timeout = 10)
            if response.status_code == 200:
                print(f"Сайт {url} доступен. Код ответа: {response.status_code}")
            else:
                print(f"Сайт {url} ответил с кодом: {response.status_code}")
        except requests.exceptions.RequestException as exception:
            print(f"Ошибка при попытке доступа к сайту: {url}. Ошибка: {exception}")

 
if __name__ == '__main__':
    main()