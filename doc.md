# Подробное описание
## Ввод
Для того чтобы сформировать таблицу или базу данных необходимо запустить программу и нажать на кнопку "Загрузить таблицу".

Появиться новое окно и котором можно выбрать:
- Создать таблицу
- Создать базу данных
По желанию можно выбрать два пункта или ничего не выбирать.

### Создать таблицу
Если будет выбран этот пункт, то при нажатии на кнопку "Загрузить" надо будет указать путь к таблице в виде:

Адрес обращения | Дом | Дата | текст обращения
--- | --- | --- | ---
улица Советская | 50А | 05.06.2021 22:08 | Тротуар возле рощи
улица Кукшумская | 9 | 11.06.2021 20:56 | прошу асфальтировать тротуар по улице Кукшумской до ЧЭМК
улица Кадыкова | 18 корп. 1 | 05.06.2021 17:12 | Нужны дополнительные парковочные места..

Автоматически будет сформирована [таблица]() вида:

Пусто | коорд1 | коорд2 | улица | дом | дата | глав_параметр | под_параметр | проблема
--- | ---  | --- | --- | --- | --- | --- | --- | ---
0 | 56,12152155 | 47,46414201 | улица Советская | 50А | 2021-06-05 22:08:11 | дороги и транспорт | дорога | Тротуар возле рощи
1 | 56,08734805 | 47,27399759 | улица Кукшумская | 9 | 2021-06-11 20:56:03 | дороги и транспорт | дорога | прошу асфальтировать тротуар по улице Кукшумской до ЧЭМК
2 | 56,0915768 | 47,4856415 | улица Ольдеевская | 74 | 2021-06-12 22:02:42 | дороги и транспорт | дорога | Нужна нам всем жителям деревни Дорога!!
3 | 56,1245246 | 47,25269426 | проспект Ленина | 25 | 2021-06-07 18:55:59 | содержание двора | парковочное место | Навести порядок и обустроить место для ТБО.

Если хотите чтобы при создать таблицы старые данные не стирались, то переименуйте текущую таблицу.

### Создать базу данных
Если будет выбран этот пункт, то при нажатии на кнопку "Загрузить" надо будет указать путь к одной из таблицы уже созданной этой программой или таблицу с такими же полями.

При запуске программы если база данных не найдена, она будет создана автоматически.

Автоматически новые поля будут добавлены в базу данных.

Чтобы появились новые категории перезапустите программу.

### Создать таблицу и базу данных

Выбрать таблицу такого же вида как в подпункте. Создать таблицу.

Автоматически будут созданы таблица и база данных.

## Вывод
При нажатии на кнопку "Показать карту" на карте будут показаны категории, выбранные в главном меню. 

Если поставить галочку "Все", то будут показаны абсолютно все проблемы.

- В первом комбо боксе выбирается главный критерий. 
- Во втором комбо боксе выбирается второстепенный критерий.
