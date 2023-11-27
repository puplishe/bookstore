# About
Данный проект - тестовое задание.
# Запуск
1. Клонировать репозиторий
2. После клонирования репозитория в root директории создать файл и назвать
```.env
    ```
3. Копировать из файла .env.example всё в созданный файл .env
4. Для корректной работы отправки писем, с помощью селери, необходимо поменять 2 следующие строчки на свои данные gmail
EMAIL_HOST_USER = 'YOUR ACCOUNT NAME'
EMAIL_HOST_PASSWORD = 'YOUR PASS'
5. Для запуска приложения прописать
```docker-compose build
  ```
6. После завершения билда проекта прописать
```docker-compose up -d
    ```
7. По завершению можно перейти на http://127.0.0.1:8000/swagger/ , где находится документация к апи и можно протестировать работу
