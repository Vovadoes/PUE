# Problems of the urban environment

## Красткое описание
Эта программа позволит увидеть на карте концентрацию проблем в регионе.

### Ввод
На ввод программе дается таблица подобная этой. Пример таблицы вы можете найти [тут](./example/input/table).

Адрес обращения	| Дом | Дата | текст обращения
--- | --- | --- | ---
улица Советская | 50А | 05.06.2021 22:08 | Тротуар возле рощи
улица Кукшумская | 9 | 11.06.2021 20:56 | прошу асфальтировать тротуар по улице Кукшумской до ЧЭМК
улица Кадыкова | 18 корп. 1 | 05.06.2021 17:12 | Нужны дополнительные парковочные места..

### Вывод
Программа создаёт [таблицу](Code/output/table) и [базу данных](Code/output/db). Таблицу можни использовать в других проекстах.

### Подробное описание можно почитать [тут](./doc.md).
 ## Установка

 Для того чтобы установить проект нужно установить библиотеки и иметь версию python 3.9.7+

 ### Установка библиотек
 В директории проекта в папке [Hackathon](./Code) лежит текстовый файл [requirements.txt](Code/requirements.txt). Все библиотеки из этого файла можно установить с помощью следующей конструкции: 
```
$ pip install -r requirements.txt
```
Дополнитеьно нужно прописать слудующую сточку:
```
python -m spacy download en_core_web_sm
```

### Python interpreter
Минимально обходимая версия [Python](https://www.python.org/downloads/release/python-397/).

### Запуск
Для запуска перейдите в папку [Hackathon](./Code) и выполните следующую команду:
```
python main.py
```
