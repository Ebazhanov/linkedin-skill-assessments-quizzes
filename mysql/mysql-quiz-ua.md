## MySQL

#### Q1. Коли у вас є підзапит всередині основного запиту, який запит виконується першим?

- [ ] Підзапит ніколи не виконується. Виконується лише основний запит.
- [ ] Вони виконуються одночасно.
- [ ] основний запит
- [x] підзапит

#### Q2. Вам потрібно експортувати всю базу даних, включаючи об'єкти бази даних, а також дані. Яку консольну утиліту ви використовуєте?

- [ ] mysqlexport
- [ ] mysqladmin
- [x] mysqldump
- [ ] mysqld

#### Q3. Потрібно забезпечити точність і надійність даних у базі. Ви призначаєте деякі обмеження для типу даних, які можуть потрапити в таблицю. Які саме обмеження ви призначаєте?

- [ ] на рівні рядка
- [ ] на рівні бази даних
- [x] на рівні стовпця
- [ ] на рівні функції

#### Q4. Який параметр у більшості консольних утиліт MySQL можна використовувати для отримання опису різних параметрів програми?

- [ ] --options
- [ ] ?
- [x] --help
- [ ] -h

#### Q5. MySQL використовує змінні середовища в деяких програмах і консольних операціях. Яка змінна використовується shell для пошуку програм MySQL?

- [ ] DIR
- [ ] HOME
- [x] PATH
- [ ] MYSQL_HOME

#### Q6. Як можна створити збережену процедуру в MySQL?

- [ ] A

```
1 CREATE PROCEDURE P () AS
2 BEGIN
3 END;
```

- [x] B

```
1 CREATE PROCEDURE P ()
2 BEGIN
3 END
```

- [ ] C

```
1 CREATE PROCP
2 BEGIN
3 END;
```

- [ ] D

```
1 CREATE PROC P AS O
2 BEGIN
3 END;
```

#### Q7. Якщо ви створюєте схему таблиці для зберігання оцінок студентів у вигляді літер (A, B, C, D або F), який тип стовпця буде найкращим вибором?

- [x] ENUM
- [ ] OTEXT
- [ ] VARCHAR
- [ ] LONGTEXT

#### Q8. Керівництво попросило вас створити базу даних співробітників. Ви починаєте з таблиці співробітників. Який правильний синтаксис?

- [ ] A

```sql
    CREATE TABLE employee (
    employeeID char(10),
    firstName varchar(50),
    lastName varchar(50),
    phone varchar(20),
    address varchar(50),
    PRIMARY KEY ON employeeID
    );
```

- [ ] B

```sql
    CREATE TABLE employee (
    employeeID char(10),
    firstName varchar(50),
    lastName varchar(50),
    phone varchar(20),
    address varchar(50),
    PRIMARY KEY employeeID
    );
```

- [ ] C

```sql
    CREATE TABLE IF EXISTS employee (
    employeeID char(10),
    firstName varchar(50),
    lastName varchar(50),
    phone varchar(20),
    address varchar(50),
    PRIMARY KEY (employeeID)
    );
```

- [x] D

```sql
    CREATE TABLE IF NOT EXISTS employee (
    employeeID char(10),
    firstName varchar(50),
    lastName varchar(50),
    phone varchar(20),
    address varchar(50),
    PRIMARY KEY (employeeID)
    );
```

#### Q9. Ви працюєте з таблицями, як показано на цій діаграмі. Вам потрібно створити список клієнтів, які придбали певні моделі автомобілів. Яку SQL-умову ви використовуєте?

![mysql Q09](images/mysql_q09.jpg?raw=true)

- [ ] LIKE
- [x] IN
- [ ] BETWEEN
- [ ] HAVING

#### Q10. Який запит НЕ використовується для адміністрування MySQL сервера?

- [ ] USE db
- [x] SELECT column FROM tbl
- [ ] SHOW COLUMNS FROM tbl
- [ ] SHOW TABLES

#### Q11. MySQL сервер може працювати в різних SQL-режимах, залежно від значення системної змінної sql_mode. Який режим змінює синтаксис і поведінку, щоб більше відповідати стандартному SQL?

- [ ] TRADITIONAL
- [x] ANSI
- [ ] MSSQL
- [ ] STRICT

#### Q12. Програми MySQL — це набір консольних утиліт, які надаються з типовими дистрибутивами MySQL. MySQL призначений для роботи з базами даних

- [ ] бази даних і програмування
- [ ] користувачів і адміністраторів
- [x] клієнтів і серверів
- [ ] синтаксису та об'єктів

#### Q13. Яка команда MySQL показує структуру таблиці?

- [ ] INFO table;
- [ ] SHOW table;
- [ ] STRUCTURE table;
- [x] DESCRIBE table;

#### Q14. MySQL використовує безпеку на основі \_ для всіх з'єднань, запитів та інших операцій, які користувачі можуть спробувати виконати. Або Як реалізовані дозволи в MySQL?

- [ ] схема адміністратора
- [ ] зашифровані алгоритми
- [ ] налаштування користувача
- [x] списки контролю доступу

[Довідка](https://dev.mysql.com/doc/refman/8.0/en/security-guidelines.html)

#### Q15. Яка команда MySQL змінює записи даних у таблиці?

- [x] UPDATE
- [ ] MODIFY
- [ ] CHANGE
- [ ] ALTER

#### Q16. Який найкращий тип запиту для перевірки формату електронної пошти в таблиці MySQL?

- [ ] SQL-запит із використанням розділів
- [ ] SQL-запит із використанням IS NULL
- [x] SQL-запит із використанням регулярного виразу
- [ ] SQL-запит із використанням LTRIM або RTRIM

#### Q17. У MySQL запити завжди закінчуються яким символом?

- [ ] розрив рядка
- [ ] двокрапка
- [x] крапка з комою
- [ ] крапка

#### Q18. Як можна видалити запис за допомогою MySQL?

- [ ] DELETE
- [x] DELETE FROM
- [ ] REMOVE
- [ ] REMOVE FROM

#### Q19. Який варіант НЕ є інструкцією для фільтрації даних?

- [x] GROUP BY
- [ ] WHERE
- [ ] LIMIT
- [ ] LIKE

#### Q20. Що повертає наступний SQL-запит?

`SELECT * FROM Employees WHERE EmployeeName LIKE 'a%'`

- [ ] записи в таблиці Employees, де значення в стовпці EmployeeName не містить "a".
- [x] записи в таблиці Employees, де значення в стовпці EmployeeName починається з "a".
- [ ] записи в таблиці Employees, де значення в стовпці EmployeeName містить "a".
- [ ] записи в таблиці Employees, де значення в стовпці EmployeeName закінчується на "a".

#### Q21. У `SELECT * FROM clients;` що представляє clients?

- [ ] SQL-запит
- [ ] SQL-інструкція
- [ ] база даних
- [x] таблиця

#### Q22. Чим MySQL відрізняється від SQL?

- [ ] SQL — це стандартна мова для отримання та маніпулювання даними зі структурованих баз даних. MySQL — це нереляційна система керування базами даних, яка використовується для керування SQL-базами даних.
- [x] SQL — це стандартна мова для отримання та маніпулювання даними зі структурованих баз даних. MySQL — це реляційна система керування базами даних, яка використовується для керування SQL-базами даних.
- [ ] Вони не відрізняються. MySQL і SQL означають одне й те саме.
- [ ] My SQL — це мова, а SQL — це програмне забезпечення.

#### Q23. Якщо потрібно впорядкувати таблицю фільмів за назвою, який запит спрацює?

- [ ] SELECT \* FROM movies GROUP BY name
- [x] SELECT \* FROM movies ORDER BY name
- [ ] SELECT \* FROM movies ORDER TABLE by name
- [ ] SELECT \* FROM movies FILTER BY name

#### Q24. Тригер — це об'єкт бази даних, який асоціюється з таблицею та активується, коли для таблиці відбувається певна подія. Які три події це можуть бути?

- [x] INSERT, UPDATE, DELETE
- [ ] CREATE, ALTER, DROP
- [ ] OPEN, FETCH, CLOSE
- [ ] DECLARE, SET, SELECT

[Довідка](https://dev.mysql.com/doc/refman/5.7/en/triggers.html)

#### Q25. Ви працюєте з дуже великими таблицями у базі даних. Яку SQL-умову ви використовуєте, щоб запобігти надмірно великим результатам запиту?

- [ ] UNIQUE
- [x] LIMIT
- [ ] DISTINCT
- [ ] CONSTRAINT

#### Q26. Який порт типово використовується для MySQL Server?

- [ ] 25
- [ ] 990
- [ ] 0
- [x] 3306

#### Q27. Як можна відфільтрувати дублікати даних під час отримання записів із таблиці?

- [x] DISTINCT
- [ ] WHERE
- [ ] LIMIT
- [ ] AS

#### Q28. У чому різниця між DROP і TRUNCATE?

- [ ] обидва стосуються однієї операції повного видалення таблиці.
- [ ] обидва стосуються однієї операції очищення таблиці, але збереження її визначення.
- [ ] TRUNCATE повністю видаляє таблицю, видаляючи також її визначення. DROP очищає таблицю, але не видаляє визначення.
- [x] DROP повністю видаляє таблицю, видаляючи також її визначення. TRUNCATE очищає таблицю, але не видаляє визначення.

#### Q29. Як вибрати кожен рядок у заданій таблиці під назвою "inventory"?

- [ ] SELECT all FROM inventory;
- [ ] FROM inventory SELECT all;
- [ ] FROM inventory SELECT \*;
- [x] SELECT \* FROM inventory;

#### Q30. У добре спроектованій реляційній базі даних що є в кожній таблиці?

- [ ] набір тригерів
- [ ] послідовне поле id
- [ ] мінімум три стовпці
- [x] первинний ключ

#### Q31. Файли параметрів MySQL надають спосіб вказати часто використовувані параметри, щоб їх не потрібно було вводити в командному рядку щоразу, коли ви запускаєте програму. Яка інша назва файлів параметрів?

- [ ] змінні налаштування
- [x] конфігураційні файли
- [ ] файли довідки
- [ ] усталені налаштування

[Довідка](https://dev.mysql.com/doc/refman/8.0/en/option-files.html)

#### Q32. Після встановлення MySQL може знадобитися ініціалізувати \_, що може бути зроблено автоматично за допомогою деяких методів встановлення MySQL.

- [ ] механізм зберігання
- [ ] облікові записи користувачів
- [ ] таблиці привілеїв
- [x] каталог даних

#### Q33. Вам потрібно експортувати дані з таблиці customers у файл CSV, з заголовками стовпців у першому рядку. Яку умову ви додаєте до вашої команди MySQL?

- [ ] JOIN
- [ ] WITH HEADERS
- [x] UNION
- [ ] WITH COLUMNS

[Зразок](https://stackoverflow.com/questions/5941809/include-headers-when-using-select-into-outfile)

#### Q34. Одна з форм резервного копіювання, реплікація, дозволяє підтримувати ідентичні дані на кількох серверах у конфігурації \_.

- [ ] remote-local (віддалений-локальний)
- [ ] parent-child (батько-дитина)
- [x] master-slave (майстер-слейв)
- [ ] logical-physical (логічний-фізичний)

#### Q35. Яка вимога для використання підзапиту в умові SELECT?

- [ ] підзапит повинен використовувати агрегатну функцію.
- [ ] підзапит повинен посилатися на ту саму таблицю, що й основний запит.
- [x] підзапит повинен повертати одне значення.
- [ ] підзапит повинен повертати принаймні одне значення.

#### Q36. Кожного разу, коли MySQL оновлюється, найкраще виконати mysql_upgrade, який шукає несумісності з оновленим сервером MySQL. Що робить ця команда, якщо знаходить таблицю з можливою несумісністю?

- [x] виконує перевірку таблиці та, якщо виявлено проблеми, намагається відновити таблицю.
- [ ] зупиняється та повідомляє адміністратору сервера, що оновлення не може бути завершено, доки не буде вирішено проблему несумісності.
- [ ] надає повний звіт про специфікації таблиці та несумісності адміністратору сервера.
- [ ] виконує перевірку таблиці та, якщо виявлено проблеми, відображає інформацію для адміністратора сервера, щоб він міг вжити заходів.

#### Q37. Яка команда mysql використовується для перевірки, які облікові записи мають певні привілеї?

- [x] show grants (відображає привілеї та ролі, призначені обліковому запису користувача або ролі MySQL)
- [ ] show privileges (показує список системних привілеїв, які підтримує сервер MySQL)
- [ ] show access
- [ ] show user permissions

#### Q38. Що не може мати тригер, пов'язаний із ним?

- [x] тимчасова таблиця
- [ ] системна таблиця
- [ ] велика таблиця
- [ ] нова таблиця

[Довідка](https://dev.mysql.com/doc/refman/5.7/en/create-trigger.html)

#### Q39. У пізніших версіях MySQL підтримується нативний тип даних json для зберігання документів json. Який недолік мають стовпці json?

- [ ] неефективні для зберігання документів json
- [x] не можуть бути індексовані безпосередньо
- [ ] документи не можуть бути перевірені під час зберігання в стовпцях json
- [ ] не можуть бути нормалізовані

#### Q40. Яке твердження є правильним для наведеної нижче діаграми?

![mysql Q41](images/mysql_q41.jpg?raw=true)

- [ ] carid є первинним ключем для purchases
- [ ] carid є зовнішнім ключем для cars.carid
- [x] customerid є зовнішнім ключем для customers.id
- [ ] customerid є первинним ключем для purchases

#### Q41. Яку команду можна використовувати для завантаження даних із файлу в таблицю?

- [ ] `cat file | mysql`
- [x] `LOAD DATA INFILE`
- [ ] `LOAD DATA LOCAL INFILE`
- [ ] `extended INSERT statement`

#### Q43. Який правильний синтаксис розширеної інструкції вставки?

- [ ] insert into cars (make, model, year) values ('Ford', 'Mustang', 2002)
      ('Mercedes', 'C', 2003)

- [ ] insert into cars (make, model, year) values ('Ford', 'Mustang', 2002)
      values ('Mercedes', 'C', 2003)

- [ ] insert into cars (make, model, year) extended ('Ford', 'Mustang', 2002),
      ('Mercedes', 'C', 2003)

- [x] insert into cars (make, model, year) values ('Ford', 'Mustang', 2002),
      ('Mercedes', 'C', 2003)

#### Q44. Вам потрібно зробити точну копію таблиці з усіма стовпцями та індексами. Як можна отримати всю інформацію, необхідну для цього?

- [ ] create table
- [ ] clone table
- [ ] insert into
- [x] show create table

Зверніть увагу, що питання стосується _отримання_ даних, а не самої операції _дублювання_. І насправді немає необхідності запускати `SHOW CREATE TABLE`. [Щоб дублювати структуру таблиці](https://popsql.com/learn-sql/mysql/how-to-duplicate-a-table-in-mysql), можна використовувати `CREATE TABLE new_table LIKE original_table;`.

#### Q45. вам потрібно зробити вашу систему MySQL захищеною від атак. Що ви _не_ повинні робити?

- [ ] Запускати MySQL сервер як звичайний користувач.
- [ ] Надати привілеї PROCESS або SUPER іншим користувачам.
- [x] Запускати MySQL сервер як користувач unix root.
- [ ] Використовувати стиснутий протокол.

#### Q46. Ви керуєте базою даних із таблицею під назвою customers. Ви створили тимчасову таблицю, також під назвою customers, з якою працюєте протягом сеансу. Вам потрібно створити тимчасову таблицю з іншими специфікаціями. Яку команду потрібно виконати спочатку?

- [ ] `CREATE TEMPORARY TABLE customers;`
- [ ] `DROP TEMP TABLE customers;`
- [ ] `DROP TABLE customers;`
- [x] `DROP TEMPORARY TABLE customers;`

1. [Довідка](https://dev.mysql.com/doc/refman/8.0/en/drop-table.html)
2. [Довідка](https://www.mysqltutorial.org/mysql-temporary-table)

#### Q47. Вам потрібно виконати складний запит із рекурсивними підзапитами, але без створення збереженої процедури або функції. Яку команду або умову ви використовуєте?

- [ ] COLLATE
- [ ] UNION
- [ ] FULL JOIN
- [x] WITH

Це саме те, для чого призначена [умова WITH](https://dev.mysql.com/doc/refman/8.0/en/with.html).

#### Q48. Який варіант не є алгоритмом обробки для представлень бази даних?

- [ ] merge
- [x] updatable
- [ ] temptable
- [ ] undefined

[Довідка](https://dev.mysql.com/doc/refman/8.0/en/view-algorithms.html)

#### Q49. Для чого використовується консольна утиліта MySQL `perror`?

- [ ] для відображення вашої версії MySQL
- [ ] для відображення кодів помилок операційної системи
- [ ] для відображення усталених налаштувань, які містять помилки
- [x] для відображення кодів помилок сховища

Примітка: perror виводить опис для коду помилки системи або для коду помилки [механізму зберігання (обробника таблиць)](<https://dev.mysql.com/doc/refman/5.7/en/perror.html#:~:text=2 perror — Display MySQL Error Message Information,-For most system&text=You can find out what,(table handler) error code>)

#### Q50. Як можна відобразити всі стовпці для заданої таблиці?

- [ ] SHOW table COLUMNS;
- [x] SHOW COLUMNS FROM table;
- [ ] LIST table COLUMNS;
- [ ] SELECT COLUMNS FROM table;

Примітка: `DESCRIBE tablename` є скороченням для цієї команди.

#### Q51. Як можна відобразити повний набір таблиць у поточній вибраній базі даних?

- [ ] SELECT \* FROM DATABASE;
- [x] SHOW TABLES;
- [ ] LIST TABLES;
- [ ] SELECT ALL TABLES;

#### Q52. Який варіант не є однією з інструкцій обслуговування таблиць?

- [ ] CHECK TABLE;
- [x] CREATE TABLE;
- [ ] ANALYZE TABLE;
- [ ] OPTIMIZE TABLE;

#### Q53. У якій таблиці MySQL зберігає паролі для облікових записів користувачів?

- [ ] mysql.accounts;
- [ ] mysql.passwords;
- [ ] mysql.admin;
- [x] mysql.user;

#### Q54. Керівництво попросило вас створити базу даних співробітників. Вам потрібно включити поточну посаду та зарплату кожного співробітника, а також усі попередні посади та зарплати в компанії. Ви вирішуєте використовувати структуру один-до-багатьох: таблицю співробітників з основною інформацією, як-от ім'я та адреса, і таблицю зайнятості з історією посад і зарплат. Ви можете використовувати поле employeeID для їх з'єднання. Що є employment.employeeID прикладом?

- [ ] первинний ключ (primary key);
- [ ] вторинний ключ (secondary key);
- [x] зовнішній ключ (foreign key);
- [ ] альтернативний ключ (alternate key);

#### Q55. У нових версіях MySQL (8.0+), який правильний синтаксис для оголошення CTE (Common Table Expression) (Загального Табличного Виразу)?

- [ ] WITH (SELECT id FROM users) as cte, SELECT ...
- [ ] WITH (SELECT id FROM users) as cte SELECT ...
- [ ] WITH cte as (SELECT id FROM users), SELECT ...
- [x] WITH cte as (SELECT id FROM users) SELECT ...

#### Q56. Яка одна з причин для введення надмірності даних у нормалізований дизайн бази даних?

- [x] щоб зменшити пошкодження даних
- [ ] щоб зменшити обсяг пам'яті
- [x] щоб зробити систему швидшою
- [ ] щоб запобігти аномаліям даних

Примітка: "щоб зробити систему швидшою" також може бути правильним. Наприклад, ми можемо заздалегідь обчислити важкий запит і зберегти його результат у деякому стовпці (використовувати його як кеш). Тому, якщо "система" означає "застосунок, який використовує mysql", то це також правильно.

#### Q57. Наведений нижче фрагмент коду використовується для читання даних із XML-файлу та збереження в таблицю. Яка структура XML \_не\_ підтримується цією інструкцією?

```mysql
LOAD XML LOCAL INFILE 'cars.xml'
INTO TABLE cars
ROWS IDENTIFIED BY `<car>`;
```

- [ ] A

```xml
<car>
   <field name="make"> Lexus </field>
   <field name="model"> IS300 </field>
   <field name="make"> 2016 </field>
</car>
```

- [x] B

```xml
<car name="make"> Dodge </car>
<car name="model"> Ram </car>
<car name="year"> 2000 </car>
```

- [ ] C

```xml
<car make="Ford" model="Mustang" year="2002"/>
```

- [ ] D

```xml
<car year="2010">
    <make>Mercedes</make> <model> C-Class</model>
</car>
```

#### Q58. Ви завантажуєте дані в таблицю. Яку команду можна використовувати, щоб переконатися, що всі дані вставлені, а дублікати рядків відкинуті?

- [x] `INSERT IGNORE`
- [ ] `INSERT UNIQUE`
- [ ] `INSERT INTO`
- [ ] `INSERT DISTINCT`

#### Q59. Яке твердження про оператор `TRUNCATE TABLE` є правильним?

- [ ] Він зупиниться і видасть помилку, коли зустріне рядок, на який посилається рядок у дочірній таблиці.
- [x] Він завжди спочатку видаляє, а потім створює нову таблицю.
- [ ] Він видаляє рядки по одному в таблицях з обмеженнями зовнішнього ключа.
- [x] Він не викликає тригери `DELETE`, пов'язані з таблицею.

Примітка: обидві відповіді правильні - див. [TRUNCATE TABLE Statement](https://dev.mysql.com/doc/refman/8.0/en/truncate-table.html) у довіднику MySQL

#### Q60. Ви працюєте з таблицями, як показано на цій діаграмі. Вам потрібно отримати кількість проданих автомобілів за домашнім штатом кожного клієнта. Як це можна зробити?

![mysql Q61](images/mysql_q61.png?raw=true)

- [ ] `SELECT state, COUNT(*) FROM customers WHERE ID IN (SELECT customerID FROM purchases) GROUP BY state;`
- [ ] `SELECT state, COUNT(*) FROM customers c LEFT JOIN purchases p ON c.ID = p.customerID GROUP BY state;`
- [x] `SELECT state, COUNT(*) FROM customers c, purchases p WHERE c.ID = p.customerID GROUP BY state;`
- [ ] `SELECT state, COUNT(*) FROM customers GROUP BY state;`

Пояснення: Різниця між 2 і 3 полягає в тому, що LEFT JOIN поверне 1 рядок на клієнта перед групуванням. Якщо замінити на RIGHT JOIN, він поверне правильну інформацію.

#### Q61. Під час міграції даних часто виникає потреба видалити дублікати рядків як частину очищення даних. Яке твердження працює найкраще?

- [ ] `DELETE DUPS`
- [ ] `DELETE DISTINCT`
- [x] `DELETE JOIN`
- [ ] `DELETE WITH`

#### Q62. Під час роботи з курсором MySQL, що потрібно додатково оголосити?

- [ ] Значення `DEFAULT`
- [ ] Змінну `RETURN`
- [ ] Процедуру `SQLEXCEPTION`
- [x] Обробник `NOT FOUND`

#### Q63. Який тип резервної копії включає всі зміни, внесені до даних з моменту останнього повного резервного копіювання?

- [ ] знімок (snapshot)
- [ ] логічна (logical)
- [x] диференційна (differential)
- [ ] інкрементна (incremental)

#### Q64. Вам потрібно відновити базу даних MySQL з файлу резервної копії. Яку консольну утиліту ви використовуєте для фактичного імпорту даних після повторного створення бази даних?

- [ ] `mysqld`
- [x] `mysql`
- [ ] `mysqladmin`
- [ ] `mysqldump`

#### Q65. Ви імпортуєте дані у форматі JSON у нову таблицю. Ви запускаєте CREATE TABLE json_data ( city JSON ); і вставляєте рядки в цю таблицю. Який правильний синтаксис для перегляду списку міст?

- [ ] `SELECT city FROM json_data;`
- [x] `SELECT city->>'$.name' city FROM json_data;`
- [ ] `SELECT city.name city FROM json_data;`
- [ ] `SELECT city->'$.name' city FROM json_data;`

Примітка: останній варіант також дійсний, але результати будуть укладені в лапки.

#### Q66. Якщо ви хочете використовувати MyISAM замість InnoDB, яку опцію потрібно вказати в операторі CREATE TABLE?

- [x] ENGINE
- [ ] PARTITION
- [ ] STORAGE
- [ ] TABLESPACE

#### Q67. Ви працюєте з таблицею на цій діаграмі. Ви хочете використовувати повнотекстовий пошук, щоб знайти клієнтів, які живуть на city або на drive. Яка команда для цього?

Назва таблиці: **customers**

| ID   | lastname | firstname | phone        | address             | city        | state | zip   |
| ---- | -------- | --------- | ------------ | ------------------- | ----------- | ----- | ----- |
| A001 | Smith    | Bob       | 212-555-1212 | 1001 1st Street     | New York    | NY    | 10001 |
| A002 | Chang    | John      | 213-555-5678 | 888 Rodeo Drive     | Los Angeles | CA    | 90210 |
| A003 | Smith    | Mary      | 999-999-9999 | 123 Main Street     | Anytown     | VA    | 12345 |
| A004 | Johnson  | Jack      | 312-312-3120 | 1111 Chicago Avenue | Chicago     | IL    | 60606 |
| A005 | Lopez    | Linda     | 737-777-3333 | 123 Main Street     | Austin      | TX    | 73344 |

- [ ] A

```sql
SELECT *
FROM customers
WHERE address MATCH 'Street' OR 'Drive';
```

- [ ] B

```sql
SELECT *
FROM customers
WHERE MATCH(address) IN ('street, drive');
```

- [ ] C

```sql
SELECT *
FROM customers
WHERE address MATCH 'Street' OR address MATCH 'Drive';
```

- [x] D

```sql
SELECT *
FROM customers
WHERE MATCH(address) AGAINST ('street, drive');
```

#### Q68. Який запит виводить список баз даних на поточному сервері?

- [x] SHOW DATABASES;
- [ ] LIST ALL DATABASES;
- [ ] LIST DATABASES;
- [ ] SHOW DB;

#### Q69. Який результат етапу проектування бази даних?

- [ ] всі таблиці, стовпці, типи даних, індекси та їхні зв'язки
- [ ] список сутностей, їхні зв'язки та обмеження
- [ ] всі таблиці та їхні назви, які потрібні для реалізації логічної моделі
- [x] список сутностей, їхні зв'язки, обмеження, типи даних і кардинальності

#### Q70. Який варіант _не_ є дійсною моделлю для параметра збереженої процедури?

- [ ] INOUT
- [ ] IN
- [ ] OUT
- [x] IN OUT

#### Q71. Яка перевага використання тимчасової таблиці замість heap-таблиці?

- [ ] Тимчасова таблиця буде видалена при перезапуску бази даних.
- [ ] Тимчасові таблиці можуть бути спільними між клієнтами, що робить їх більш зручними в групових середовищах розробки.
- [x] Тимчасова таблиця буде видалена, як тільки ваша сесія буде відключена.
- [ ] Створення тимчасової таблиці не вимагає жодних спеціальних привілеїв.

#### Q72. Яка максимальна кількість стовпців може бути використана одним індексом таблиці?

- [ ] 2
- [ ] 4
- [ ] 8
- [x] 16

#### Q73. Яка команда поверне список тригерів у поточній базі даних?

- [ ] `DISPLAY TRIGGERS;`
- [x] `SHOW TRIGGERS;`
- [ ] `SELECT ALL TRIGGERS;`
- [ ] `SELECT * FROM information_schema.triggers;`

#### Q74. Яке твердження є правильним щодо типів даних TIMESTAMP і DATETIME?

- [ ] Значення TIMESTAMP вимагають більше байтів для зберігання, ніж значення DATETIME.
- [ ] TIMESTAMP зберігається без часової зони, а DATETIME зберігається в значеннях UTC.
- [x] TIMESTAMP і DATETIME обидва зберігаються без часової зони.
- [ ] TIMESTAMP зберігається в значеннях UTC, а DATETIME зберігається без часової зони.

#### Q75. Який еквівалент команди mysqladmin reload?

- [ ] `mysqladmin flush-threads`
- [ ] `mysqladmin flush-tables`
- [x] `mysqladmin flush-privileges`
- [ ] `mysqladmin flush-all`

#### Q76. Поясніть аспект безпеки збережених процедур

- [ ] Збережені процедури не є безпечними, оскільки їх можна виконувати з командного рядка як користувач root.
- [ ] Збережені процедури є безпечними, оскільки власник збереженої процедури може вирішити, кому надавати доступ.
- [x] Збережені процедури є безпечними, оскільки застосунки можуть отримати доступ до збережених процедур, але не до жодних базових таблиць.
- [ ] Збережені процедури не є безпечними, оскільки вони можуть виконувати оператори для видалення таблиць або масового видалення даних.

#### Q77. Як би ви отримали дані про всіх клієнтів, у яких не збережено номер телефону?

- [ ] `SELECT * FROM customers WHERE PhoneNumber = NULL;`
- [ ] `SELECT * FROM customers WHERE PhoneNumber IS NOT VALID;`
- [x] `SELECT * FROM customers WHERE PhoneNumber IS NULL;`
- [ ] `SELECT * FROM customers WHERE PhoneNumber IS UNKNOWN;`

#### Q78. На діаграмі нижче поле price оголошено як тип DECIMAL. Яке було б більш ефективне оголошення для цього поля?

![mysql picture](images/mysql_q80.png?raw=true)

- [ ] FLOAT
- [x] DECIMAL(10,2)
- [ ] NUMERIC
- [ ] DOUBLE

#### Q79. Який варіант _не_ є доступним типом рядка для стовпця?

- [ ] `ENUM`
- [ ] `SET`
- [x] `BIT`
- [ ] `CHAR`

Пояснення: BIT не є рядковим типом.

#### Q80. Ця діаграма показує який тип відносин між клієнтами та автомобілями?

![mysql picture](images/mysql_q80.png?raw=true)

- [ ] один-до-багатьох (one-to-many)
- [ ] батько-дитина (parent-child)
- [x] багато-до-багатьох (many-to-many)
- [ ] багато-до-одного (many-to-one)

#### Q81. Збережена процедура — це набір SQL-інструкцій, збережених на сервері, і вона може бути у формі процедури або функції. Яка інструкція не може бути використана всередині збережених процедур?

- [ ] `SELECT`
- [x] `USE`
- [ ] `SET`
- [ ] `DECLARE`

Пояснення: І `SET`, і `DECLARE` використовуються для створення змінних. Довідка: [MySQL STORED PROCEDURE Довідник із прикладами](https://www.softwaretestinghelp.com/mysql-stored-procedure/)

#### Q82. Коли додається новий студент до нової бази даних, ви хочете, щоб нові записи створювалися в пов'язаних таблицях, як-от Exam, Score і Attendance. Як би ви це зробили?

- [x] тригер
- [ ] регулярний вираз
- [ ] подання
- [ ] індекс

#### Q83. На діаграмі нижче поля ID оголошені як тип CHAR замість INT. Яка з можливих причин _не_ є правильною для цього рішення?

![mysql picture](images/mysql_q85.png?raw=true)

- [ ] Поле ID повинно містити літери, а не лише цифри.
- [ ] Ви можете мати послідовний формат у всіх таблицях, які потребують полів ID.
- [ ] Поле ID повинно мати провідні нулі, які тип даних INT би обрізав.
- [x] Тип даних `CHAR(10)` є більш ефективним і економним за місцем.

#### Q84. Чому ви скористалися б загальним виразом таблиці (CTE)?

- [ ] Щоб визначити запити для подальшого повторного використання протягом поточної сесії.
- [ ] Щоб створити тимчасові таблиці, які можна використовувати для попереднього вибору часто використовуваних наборів результатів.
- [ ] Щоб обчислити нове одиничне значення з набору результатів і повернути його до парсера запитів.
- [x] Щоб розбити складні запити та дозволити повторне використання в межах одного запиту.

Пояснення: CTE не створюють тимчасові таблиці, вони працюють лише в межах одного запиту. Довідка: [13.2.15 WITH (Common Table Expressions)](https://dev.mysql.com/doc/refman/8.0/en/with.html).

#### Q85. Який модифікатор опцій вказує програмі не завершувати роботу з помилкою, якщо вона не розпізнає опцію, а замість цього видає попередження?

- [ ] --verbose
- [ ] --skip
- [ ] --skip-error
- [x] --loose

Довідка: [4.2.2.4 Program Option Modifiers](https://dev.mysql.com/doc/refman/8.0/en/option-modifiers.html)

#### Q86. Що повертає цей SQL-запит?

```
SELECT name FROM students WHERE name REGEXP '^to';
```

- [x] всі імена, що починаються з "to", як-от Tommy або Tony
- [ ] всі імена, що містять "to", як-от Roberto і Tommy
- [ ] всі імена без "to", як-от Samantha або Kathryn
- [ ] всі імена, що закінчуються на "to", як-от Roberto

#### Q87. Ви працюєте з таблицями, як показано на діаграмі. Вам потрібно згенерувати список загальних цін для кожної марки та моделі автомобіля, з підсумками для кожної марки та загальним підсумком усіх цін. Яку SQL-інструкцію ви використовуєте?

![mysql picture](images/mysql_q92.png?raw=true)

- [ ] UNION
- [ ] SHOW TOTALS
- [ ] UNION ALL
- [x] WITH ROLLUP

#### Q88. Ліві та праві з'єднання також відомі як \_.

- [ ] Внутрішнє з'єднання (Inner Join)
- [ ] Природне з'єднання (Natural Join)
- [x] Зовнішнє з'єднання (Outer Join)
- [ ] Декартове з'єднання (Cartesian Join)

#### Q89. Який правильний спосіб створення подання бази даних у MySQL?

- [ ] `CREATE VIEW v1 SELECT * FROM t1 WHERE col1 > 10;`
- [ ] `CREATE VIEW v1 AS BEGIN SELECT * FROM t1 END;`
- [ ] `CREATE VIEW v1 BEGIN SELECT * FROM t1 END;`
- [x] `CREATE VIEW v1 AS SELECT * FROM t1;`

#### Q90. Усередині транзакції потрібно виконати кілька операцій. Що ви зробите, якщо під час цієї транзакції станеться виняток?

- [ ] `UNDO`
- [ ] `UNCOMMIT`
- [x] `ROLLBACK`
- [ ] `REVERSE`

#### Q91. Яка функція знаходить поточний час або дату в MySQL?

- [ ] DATE()
- [ ] GETDATE()
- [x] CURDATE()
- [ ] CURRENT()

#### Q92. Яке правильне використання ENUM у MySQL?

- [ ] `Create table size (ENUM ('Small','Medium','Large'));`
- [ ] `Create table ENUM (name ('Small','Medium','Large'));`
- [ ] `Create table size (name: ENUM['Small','Medium','Large']);`
- [x] `Create table size (name ENUM('Small','Medium','Large'));`

#### Q93. Команда mysqldump не може генерувати вихід у форматі **\_**.

- [x] JSON
- [ ] CSV
- [ ] XML
- [ ] TXT

#### Q94. Ви працюєте з таблицями, показаними нижче. Вам потрібно згенерувати список усіх автомобілів, незалежно від того, чи були вони продані. Яка інструкція це виконує?

![mysql picture](images/mysql_q98.png?raw=true)

- [ ] A

```
SELECT cars.*, purchases.date
FROM cars RIGHT JOIN purchases
ON cars.ID = purchases.carID;
```

- [ ] B

```
SELECT cars.*, purchases.date
FROM cars INNER JOIN purchases
ON cars.ID = purchases.carID;
```

- [ ] C

```
SELECT cars.*, purchases.date
FROM cars JOIN purchases
ON cars.ID = purchases.carID;
```

- [x] D

```
SELECT cars.*, purchases.date FROM cars LEFT JOIN purchases ON cars.ID = purchases.carID;
```

#### Q95. Який фрагмент коду зі збереженої процедури слід переписати як оператор CASE?

- [ ] A

```
    IF var1 THEN SET varA = var1;
    ELSEIF var2 THEN SET varA = var2;
    ELSEIF var3 THEN SET varA = var3;
    ELSE SET varA = var4;
    END IF;
```

- [ ] B

```
    IF var1 = var2 THEN SET varA = var1;
    ELSEIF var2 = var3 THEN SET varA = var2;
    ELSEIF var3 = var4 THEN SET varA = var3;
    ELSE SET varA = var4;
    END IF;
```

- [ ] C

```
    IF var1 = 1 THEN SET varA = var1;
    ELSEIF var2 = 2 THEN SET varA = var2;
    ELSEIF var3 = 3 THEN SET varA = var3;
    ELSE SET varA = var4;
    END IF;
```

- [x] D

```
    IF var1 = 1 THEN SET varA = var1;
    ELSEIF var1 = 2 THEN SET varA = var2;
    ELSEIF var1 = 3 THEN SET varA = var3;
    ELSE SET varA = var4;
    END IF;
```

#### Q96. Для чого ви б використовували збережені функції?

- [x] для формул і бізнес-правил, які ви хочете застосувати до стовпців у SQL-запиті
- [ ] для формул і бізнес-правил, які слід застосовувати під час певної події тригера, як-от під час вставок
- [ ] для автоматичної модифікації даних таблиці на основі запиту
- [x] для повторного використання повторюваних запитів

#### Q97. Які кроки потрібно виконати, щоб нормалізувати таблицю з цієї діаграми?

Назва таблиці: superheroes
| name | alias | power1 | power2 | power3 |
| ---- | ----- | ------ | ------ | ------ |
| Superman | Clark Kent | Flight | X-Ray Vision | Super Strength |
| Wonder Woman | Diana Prince | Force Fields | Reflexes | Telepathy |
| Spider-man | Peter Parker | Walcrawling | Web-making | Enhanced Senses |
| Aquaman | Arthur Curry | Underwater Breathing | Enhanced Sight | Stamina |
| Hulk | Bruce Banner | Super Strength | Radiation Immunity | Invulnerability |

- [x] Створити іншу таблицю для пошуку здібностей з полями для коду та опису, а також таблицю зв'язку з іменами супергероїв і кодами здібностей.
- [ ] Додати стовпець до цієї таблиці для ідентифікатора запису та зробити його первинним ключем.
- [ ] Розширити цю таблицю, додавши стовпці "power4", "power5" тощо, щоб дозволити додаткові здібності для кожного супергероя.
- [ ] Перетворити цю таблицю на таблицю з назвою "power" і додати один запис для кожної комбінації супергероя та здібності, загалом 15 записів у цьому прикладі.

#### Q98. Таблиця Item має булеве поле endOfLife і поле makeYear типу YEAR(4). Як можна встановити булеве значення true для всіх елементів, виготовлених до 2019 року?

- [ ] UPSERT Item SET endOfLife = true WHERE makeYear < 2019
- [ ] CHANGE Item SET endOfLife = true WHERE makeYear < 2019
- [ ] ALTER Item SET endOfLife = true WHERE makeYear < 2019
- [x] UPDATE Item SET endOfLife = true WHERE makeYear < 2019

#### Q99. Який варіант є прикладом агрегатної функції?

- [ ] NOW()
- [ ] MID()
- [ ] FORMAT()
- [x] COUNT()

[Довідка](https://www.sqltutorial.org/sql-aggregate-functions/)

#### Q100. Ви працюєте над тригером UPDATE у таблиці employee на цій діаграмі. Як можна отримати доступ до нового значення для адреси всередині тригера?

![mysql picture](images/mysql_q116.png?raw=true)

- [x] Скористатися NEW.address
- [ ] Скористатися INSERTED.address
- [ ] Скористатися DELETED.address
- [ ] Скористатися OLD.address

[Довідка](https://dev.mysql.com/doc/refman/8.0/en/trigger-syntax.html)

#### Q101. Ви працюєте з таблицями, як показано на цій діаграмі. Вам потрібно згенерувати список клієнтів, які придбали певні моделі автомобілів. Яку SQL-інструкцію ви використаєте?

![Q104](https://github.com/Ebazhanov/linkedin-skill-assessments-quizzes/assets/22109189/5c73a5c5-3e8b-4110-8068-dca25b323e57)

- [ ] UNION ALL
- [x] UNION
- [ ] SHOW TOTALS
- [ ] WITH ROLLUP

#### Q102. Як би ви зробили нечутливий до регістру запит у MySQL?

- [ ] `SELECT * FROM customers WHERE UPPEERCASE(LastName) = 'POTTER';`
- [ ] `SELECT * FROM customers WHERE LOWERCASE(LastName) = 'potter';`
- [x] `SELECT * FROM customers WHERE UPPER(LastName) = 'POTTER';`
- [ ] `SELECT * FROM customers WHERE UPPER(LastName) = 'Potter';`

#### Q103. До якої категорії належить ключове слово "COUNT" у MySQL?

- [x] Агрегатні функції
- [ ] Оператори
- [ ] Інструкції
- [ ] Усі згадані

#### Q104. Для чого потрібна інструкція "HAVING" у MySQL?

- [ ] Для фільтрації значень стовпців
- [x] Для фільтрації значень рядків
- [ ] Для фільтрації значень рядків і стовпців
- [ ] Жоден із згаданих

#### Q105. Яка інструкція схожа на інструкцію "HAVING" у MySQL?

- [ ] SELECT
- [ ] FROM
- [x] WHERE
- [ ] Жоден із згаданих

#### Q106. Яким буде результат наступної команди MySQL?

      SELECT emp_id, fname, lname
      FROM employee
      WHERE title=’HEAD TELLER’ AND start_date&gt;2008-11-23;

- [ ] Усі стовпці
- [ ] Лише ті стовпці, які вказані в інструкції "SELECT"
- [x] Стовпці, вказані в інструкції "SELECT", і лише ті рядки, які містять 'HEAD TELLER' як "title"
- [ ] Жоден із згаданих

#### Q107. Чи є помилка в наступній MySQL інструкції?

      SELECT e.emp_id, e.fname,e.lname,d.name
      FROM employee e INNER JOIN department d
      ON e.dept_id=e.dept_id;

- [x] НІ
- [ ] ТАК
- [ ] ЗАЛЕЖИТЬ
- [ ] Жоден з варіантів

#### Q108. Як у MySQL вибрати всі записи з таблиці "Persons", де "LastName" алфавітно знаходиться між (включно) "Hansen" і "Pettersen"?

- [ ] `SELECT LastName>'Hansen' AND LastName<'Pettersen' FROM Persons`
- [x] `SELECT * FROM Persons WHERE LastName BETWEEN 'Hansen' AND 'Pettersen'`
- [ ] `SELECT * FROM Persons WHERE LastName>'Hansen' AND LastName<'Pettersen'`
- [ ] Жоден з варіантів.

[Джерело](https://www.w3schools.com/mysql/mysql_between.asp)

#### Q109. Розгляньте набір відношень, наведених нижче, і SQL-запит, що йде за ними

        Students : (Roll number, Name, Date of birth)
        Courses: (Course number, Course name, instructor)
        Grades: (Roll number, Course number, Grade)
        SELECT DISTINCT Name
        FROM Students, Courses, Grades
        WHERE Students.Roll_number = Grades.Roll_number
        AND Courses.Instructor =Sriram
        AND Courses.Course_number = Grades.Course_number
        AND Grades.Grade = A

(Який набір обчислюється цим запитом?)

- [ ] Імена студентів, які отримали оцінку A з усіх курсів, які викладає Sriram
- [ ] Імена студентів, які отримали оцінку A з усіх курсів
- [x] Імена студентів, які отримали оцінку A хоча б з одного курсу, який викладає Sriram
- [ ] Жоден з варіантів

#### Q110. Ви працюєте з таблицями, показаними нижче. Вам потрібно переконатися, що будь-який запис, доданий до таблиці purchases, містить customerID, який вже існує в таблиці customers, і carID, який вже існує в таблиці cars. Ви вирішуєте використовувати тригер для перевірки. Який тригер ви використовуєте?

![mysql picture](images/mysql_q85.png?raw=true)

- [ ] IF EXISTS
- [ ] CROSS JOIN
- [x] BEFORE INSERT
- [ ] AFTER INSERT

`IF EXISTS` і `CROSS JOIN` не є дійсними для тригера.

#### Q111. Поточні версії MySQL підтримують функцію повнотекстового пошуку на деяких рушіях зберігання як альтернативу використанню оператора LIKE і регулярних виразів. Яку інструкцію ви б виконали, щоб увімкнути повнотекстовий індекс для стовпця description у таблиці Car?

- [x] ALTER TABLE car ADD FULL TEXT(description);
- [ ] MERGE TABLE car ADD FULL TEXT(description)
- [ ] ENABLE FULL TEXT(description) car
- [ ] SEARCH FULL TEXT(description) car

#### Q112. Яку інструкцію ви _не_ використовували б для фільтрації даних?

![image](https://github.com/Ebazhanov/linkedin-skill-assessments-quizzes/assets/22109189/9cb0ae9d-1f6b-4f85-9d2f-44b6a7afd00c)

- [x] GROUP_BY
- [ ] MATCH
- [ ] WHERE
- [ ] LIKE

#### Q113. Який тип JOIN у MySQL повертає всі рядки з лівої таблиці та відповідні рядки з правої таблиці, заповнюючи значеннями NULL, якщо немає відповідності з правого боку?

- [ ] INNER JOIN
- [x] LEFT JOIN (або LEFT OUTER JOIN)
- [ ] RIGHT JOIN (або RIGHT OUTER JOIN)
- [ ] FULL JOIN (або FULL OUTER JOIN)

#### Q114. Що означає SQL у MySQL?

- [x] Structured Query Language
- [ ] Simple Query Language
- [ ] System Query Language
- [ ] Structured Question Language

#### Q115. Яка MySQL інструкція використовується для вибору даних з бази даних?

- [ ] Extract
- [x] select
- [ ] get
- [ ] Open

#### Q116. Яка мета `PRIMARY KEY` у таблиці MySQL?

- [x] Створити унікальний індекс у таблиці
- [ ] Визначити стовпець як ціле число
- [ ] Визначити тип даних стовпця
- [ ] Вказати зовнішній ключ

[Джерело](<https://www.w3schools.com/mysql/mysql_primarykey.asp#:~:text=The%20PRIMARY%20KEY%20constraint%20uniquely,or%20multiple%20columns%20(fields).>)

#### Q117. Який з наступних SQL-запитів є дійсним для вставки нового рядка в таблицю users?

- [x] `INSERT INTO users (name, email) VALUES ('John Doe', 'john.doe@example.com')`
- [ ] `ADD users (name, email) VALUES ('John Doe', 'john.doe@example.com')`
- [ ] `CREATE users (name, email) VALUES ('John Doe', 'john.doe@example.com')`
- [ ] `UPDATE users (name, email) VALUES ('John Doe', 'john.doe@example.com')`

#### Q118. Який з наступних SQL-запитів є дійсним для видалення рядка з id 2 з таблиці users?

- [x] `DELETE FROM users WHERE id = 2`
- [ ] `REMOVE FROM users WHERE id = 2`
- [ ] `DROP users WHERE id = 2`
- [ ] `TRUNCATE users WHERE id = 2`

#### Q119. Програми MySQL — це набір утиліт командного рядка, які надаються з типовими дистрибутивами MySQL. MySQL розроблений як база даних.

- [ ] база даних і програмування
- [ ] користувач і адміністратор
- [x] клієнт і сервер
- [ ] синтаксис і об'єкти

#### Q120. Яка команда MySQL показує структуру таблиці?

- [ ] INFO table;
- [ ] SHOW table;
- [ ] STRUCTURE table;
- [x] DESCRIBE table;

#### Q121. Ліві та праві з'єднання також відомі як \_.

- [ ] Inner Join
- [ ] Natural Join
- [x] Outer Join
- [ ] Cartesian Join

#### Q122. Який правильний спосіб створити представлення бази даних у MySQL?

- [ ] `CREATE VIEW v1 SELECT * FROM t1 WHERE col1 > 10;`
- [ ] `CREATE VIEW v1 AS BEGIN SELECT * FROM t1 END;`
- [ ] `CREATE VIEW v1 BEGIN SELECT * FROM t1 END;`
- [x] `CREATE VIEW v1 AS SELECT * FROM t1;`

#### Q123. У базі даних з таблицею "Students", що містить інформацію про студентів, яка SQL-інструкція використовується для отримання імен усіх студентів, які набрали більше 90 балів на іспитах?

- [ ] A

```
SELECT student_name FROM Students WHERE score > 90;
```

- [x] B

```
SELECT name FROM Students WHERE score > 90;
```

- [ ] C

```
SELECT student_name FROM Students WHERE exam_score > 90;
```

- [ ] D

```
SELECT name FROM Students WHERE exam_score > 90;
```

#### Q124 Яка SQL-команда використовується для отримання даних з бази даних?

- [ ] FETCH
- [ ] SEARCH
- [x] SELECT
- [ ] EXTRACT
