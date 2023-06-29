# flycode_test

Используя фреймворк Django:
 
1. Реализовать сущности авторы, книги, комментарии
1.1 Связь Авторы-Книги (Many-To-Many)
1.2 Реализовать возможность оставлять от имени автора комментарий к книгам.
1.3 В сущность книги обязательно добавить флаг Archived, заархированные книги не выводить в публичной части.
 
2. Реализовать административную часть
a. CRUD операции для авторов и книг
b. вывести список книг с обязательным указанием имени авторов в списке и кол-вом комментариев к этой книге
c. вывести список авторов с указанием кол-ва книг и кол-ва комментариев
 
3. Реализовать публичную часть сайта с отображение авторов и их книг (простой вывод списка на странице)
a. Получение списка книг (только те книги, которые не являются заархивированными)
а.1 Получение списка книг выбранного автора (только те книги, которые не являются заархивированными)
b. Получение конкретной книги 
c. Редактирование книги
d. Изменение флага Archived
e. Удаление книги

4. Реализовать комментарии
а. Создание комментария к книге
b. Изменение комментария
с. Удаление комментария.

Скриншоты приложения в папке Screenshots