## MySQL

#### Q1. Wenn Sie eine Unterabfrage innerhalb der Hauptabfrage haben, welche Abfrage wird zuerst ausgeführt?

- [ ] Die Unterabfrage wird nie ausgeführt. Nur die Hauptabfrage wird ausgeführt.
- [ ] Sie werden gleichzeitig ausgeführt
- [ ] die Hauptabfrage
- [x] die Unterabfrage

#### Q2. Sie müssen zusätzlich zu den Daten die gesamte Datenbank einschließlich der Datenbankobjekte exportieren. Welches Befehlszeilentool verwendest du?

- [ ] mysqlexport
- [ ] mysqladmin
- [x] mysqldump
- [ ] mysqld

#### Q3. Sie müssen die Genauigkeit und Zuverlässigkeit der Daten in Ihrer Datenbank sicherstellen. Sie weisen einige Einschränkungen zu, um den Datentyp einzuschränken, der in eine Tabelle aufgenommen werden kann. Welche Art von Einschränkungen weisen Sie zu?

- [ ] Zeilenebene
- [ ] Datenbankebene
- [x] Spaltenebene
- [ ] Funktionsebene

#### Q4. Welche Option der meisten MySQL-Befehlszeilenprogramme kann verwendet werden, um eine Beschreibung der verschiedenen Optionen des Programms zu erhalten?

- [ ] --option
- [ ] ?
- [x] --help
- [ ] -h

#### F5. MySQL verwendet Umgebungsvariablen in einigen Programmen und Befehlszeilenoperationen. Welche Variable wird von der Shell verwendet, um MySQL-Programme zu finden?

- [ ] DIR
- [ ] HOME
- [x] PATH
- [ ] MYSQL_HOME

#### F6. Wie können Sie eine gespeicherte Prozedur in MySQL erstellen?

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

#### F7. Wenn Sie ein Tabellenschema zum Speichern von Schülernoten als Buchstaben (A, B, C, D oder F) erstellen würden, welcher Spaltentyp wäre die beste Wahl?

- [x] ENUM
- [ ] OTEXT
- [ ] VARCHAR
- [ ] LONGTEXT

#### F8. Das Management hat Sie gebeten, eine Mitarbeiterdatenbank aufzubauen. Sie beginnen mit der Mitarbeitertabelle. Was ist die korrekte Syntax?

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

#### F9. Sie arbeiten mit den Tabellen, wie in diesem Diagramm gezeigt. Sie müssen die Liste der Kunden erstellen, die bestimmte Automodelle gekauft haben. Welche SQL-Klausel verwenden Sie?

![mysql Q09](images/mysql_q09.jpg?raw=true)

- [ ] LIKE
- [x] IN
- [ ] BETWEEN
- [ ] HAVING

#### F10. Welche Abfrage würde NICHT zur Verwaltung eines MySQL-Servers verwendet werden?

- [ ] USE db
- [x] SELECT column FROM tbl
- [ ] SHOW COLUMNS FROM tbl
- [ ] SHOW TABLES

#### F11. Der MySQL-Server kann abhängig vom Wert der Systemvariablen sql_mode in verschiedenen SQL-Modi betrieben werden. Welcher Modus ändert Syntax und Verhalten, um mehr mit Standard-SQL übereinzustimmen?

- [ ] TRADITIONAL
- [x] ANSI
- [ ] MSSQL
- [ ] STRICT

#### F12. MySQL-Programme sind eine Reihe von Befehlszeilendienstprogrammen, die mit typischen MySQL-Distributionen bereitgestellt werden. MySQL ist als Datenbank konzipiert.

- [ ] Datenbank und Programmierung
- [ ] Benutzer und Administrator
- [x] Client und Server
- [ ] Syntax und Objekte

#### F13. Welcher MySQL-Befehl zeigt die Struktur einer Tabelle?

- [ ] INFO table;
- [ ] SHOW table;
- [ ] STRUCTURE table;
- [x] DESCRIBE table;

#### F14. MySQL verwendet Sicherheit basierend auf \_ für alle Verbindungen, Abfragen und andere Operationen, die Benutzer versuchen können auszuführen.

- [ ] Administratorschema
- [ ] verschlüsselte Algorithmen
- [ ] Benutzereinstellungen
- [x] Zugriffskontrolllisten

[Referenz](https://dev.mysql.com/doc/refman/8.0/en/security-guidelines.html)

#### F15. Welcher MySQL-Befehl modifiziert Datensätze in einer Tabelle?

- [x] UPDATE
- [ ] MODIFY
- [ ] CHANGE
- [ ] ALTER

#### F16. Was ist die beste Art von Abfrage, um das Format einer E-Mail-Adresse in einer MySQL-Tabelle zu validieren?

- [ ] eine SQL-Abfrage mit Partitionen
- [ ] eine SQL-Abfrage mit IS NULL
- [x] eine SQL-Abfrage mit einem regulären Ausdruck
- [ ] eine SQL-Abfrage mit LTRIM oder RTRIM

#### F17. In MySQL folgt auf Abfragen immer welches Zeichen?

- [ ] Zeilenumbruch
- [ ] Doppelpunkt
- [x] Semikolon
- [ ] Raute

#### Q18. Wie können Sie einen Datensatz mit MySQL entfernen?

- [ ] DELETE
- [x] DELETE FROM
- [ ] REMOVE
- [ ] REMOVE FROM

#### Q19. Welche Auswahl ist KEINE Anweisung, die Sie zum Filtern von Daten verwenden würden?

- [x] GROUP BY
- [ ] WHERE
- [ ] LIMIT
- [ ] LIKE

#### Q20. Was gibt die folgende SQL-Anweisung zurück?

`SELECT * FROM Employees WHERE EmployeeName LIKE 'a%'`

- [ ] Es wird in der Tabelle „Employees“ aufgezeichnet, wo der Wert in der Spalte „EmployeeName“ kein „a“ enthält.
- [x] Es wird in der Employees-Tabelle aufgezeichnet, wo der Wert in der EmployeeName-Spalte mit "a" beginnt.
- [ ] Es wird in der Tabelle „Employees“ aufgezeichnet, wo der Wert in der Spalte „EmployeeName“ ein „a“ hat.
- [ ] Es wird in der Employees-Tabelle aufgezeichnet, wo der Wert in der EmployeeName-Spalte mit "a" endet.

#### F21. Was steht in „SELECT \* FROM clients;“ für „clients“?

- [ ] eine SQL-Abfrage
- [ ] eine SQL-Anweisung
- [ ] eine Datenbank
- [x] eine Tabelle

#### F22. Wie unterscheidet sich MySQL von SQL?

- [ ] SQL ist eine Standardsprache zum Abrufen und Bearbeiten von Daten aus strukturierten Datenbanken. MySQL ist ein nichtrelationales Datenbankverwaltungssystem, das zur Verwaltung von SQL-Datenbanken verwendet wird.
- [x] SQL ist eine Standardsprache zum Abrufen und Bearbeiten von Daten aus strukturierten Datenbanken. MySQL ist ein relationales Datenbankverwaltungssystem, das zur Verwaltung von SQL-Datenbanken verwendet wird.
- [ ] Sie unterscheiden sich nicht. MySQL und SQL beziehen sich auf dasselbe.
- [ ] My SQL ist eine Sprache und SQL ist eine Softwareanwendung.

#### F23. Welche Abfrage funktioniert, wenn Sie eine Tabelle mit Filmen nach Namen bestellen müssen?

- [ ] SELECT \* FROM movies GROUP BY name
- [x] SELECT \* FROM movies ORDER BY name
- [ ] SELECT \* FROM movies ORDER TABLE by name
- [ ] SELECT \* FROM movies FILTER BY name

#### Q24. Ein Trigger ist ein Datenbankobjekt, das einer Tabelle zugeordnet ist und aktiviert wird, wenn ein bestimmtes Ereignis für die Tabelle eintritt. Welche drei Ereignisse sind das?

- [x] INSERT, UPDATE, DELETE
- [ ] CREATE, ALTER, DROP
- [ ] OPEN, FETCH, CLOSE
- [ ] DECLARE, SET, SELECT

[Referenz](https://dev.mysql.com/doc/refman/5.7/en/triggers.html)

#### F25. Sie arbeiten mit sehr großen Tabellen in Ihrer Datenbank. Welche SQL-Klausel verwenden Sie, um übermäßig große Abfrageergebnisse zu verhindern?

- [ ] UNIQUE
- [x] LIMIT
- [ ] DISTINCT
- [ ] CONSTRAINT

#### F26. Was ist der Standardport für MySQL Server?

- [ ] 25
- [ ] 990
- [ ] 0
- [x] 3306

#### F27. Wie können Sie doppelte Daten filtern, während Sie Datensätze aus einer Tabelle abrufen?

- [x] DISTINCT
- [ ] WHERE
- [ ] LIMIT
- [ ] AS

#### F28. Was ist der Unterschied zwischen DROP und TRUNCATE?

- [ ] Sie beziehen sich beide auf denselben Vorgang des vollständigen Löschens der Tabelle.
- [ ] Sie beziehen sich beide auf denselben Vorgang des Löschens der Tabelle, behalten aber ihre Definition bei.
- [ ] TRUNCATE löscht die Tabelle vollständig und entfernt auch ihre Definition. DROP löscht die Tabelle, löscht aber nicht die Definition.
- [x] DROP löscht die Tabelle vollständig und entfernt auch ihre Definition. TRUNCATE löscht die Tabelle, löscht aber nicht die Definition.

#### Q29. Wie wählen Sie jede Zeile in einer bestimmten Tabelle mit dem Namen "Inventar" aus?

- [ ] SELECT all FROM inventory;
- [ ] FROM inventory SELECT all;
- [ ] FROM inventory SELECT \*;
- [x] SELECT \* FROM inventory;

#### Q30. Was hat jede Tabelle in einer effizient gestalteten relationalen Datenbank?

- [ ] Satz von Triggern
- [ ] sequentielles ID-Feld
- [ ] mindestens drei Spalten
- [x] Primärschlüssel

#### F31. MySQL-Optionsdateien bieten eine Möglichkeit, häufig verwendete Optionen anzugeben, sodass sie nicht jedes Mal, wenn Sie ein Programm ausführen, in die Befehlszeile eingegeben werden müssen. Was ist ein anderer Name für die Optionsdateien?

- [ ] variable Einstellungen
- [x] Konfigurationsdateien
- [ ] Hilfedateien
- [ ] Standardeinstellungen

[Referenz](https://dev.mysql.com/doc/refman/8.0/en/option-files.html)

#### F32. Nach der Installation von MySQL kann es erforderlich sein, \_ zu initialisieren, was bei einigen MySQL-Installationsmethoden automatisch erfolgen kann.

- [ ] Speicher-Engine
- [ ] Benutzerkonten
- [ ] Grant-Tabellen
- [x] Datenverzeichnis

#### F33. Sie müssen die Daten in der Kundentabelle in eine CSV-Datei exportieren, mit Spaltenüberschriften in der ersten Zeile. Welche Klausel fügen Sie Ihrem MySQL-Befehl hinzu?

- [ ] JOIN
- [ ] WITH HEADERS
- [x] UNION
- [ ] WITH COLUMNS

[Beispiel](https://stackoverflow.com/questions/5941809/include-headers-when-using-select-into-outfile)

#### Q34. Eine Form der Sicherung, die Replikation, ermöglicht es Ihnen, identische Daten auf mehreren Servern als \_ Konfiguration zu verwalten.

- [ ] remote-local
- [ ] parent-child
- [x] master-slave
- [ ] logical-physical

#### F35. Was ist die Voraussetzung für die Verwendung einer Unterabfrage in der SELECT-Klausel?

- [ ] Die Unterabfrage muss eine Aggregatfunktion verwenden.
- [ ] Die Unterabfrage muss auf dieselbe Tabelle verweisen wie die Hauptabfrage.
- [x] Die Unterabfrage muss einen einzelnen Wert zurückgeben.
- [ ] Die Unterabfrage muss mindestens einen Wert zurückgeben.

#### F36. Jedes Mal, wenn MySQL aktualisiert wird, ist es am besten, mysql_upgrade auszuführen, das nach Inkompatibilitäten mit dem aktualisierten MySQL-Server sucht. Was macht dieser Befehl, wenn er eine Tabelle mit einer möglichen Inkompatibilität findet?

- [x] Es führt eine Tabellenprüfung durch und versucht, falls Probleme gefunden werden, eine Tabellenreparatur.
- [ ] Es stoppt und benachrichtigt den Serveradministrator, dass das Upgrade nicht abgeschlossen werden kann, bis das Inkompatibilitätsproblem behoben ist.
- [ ] stellt dem Serveradministrator einen vollständigen Bericht der Tabellenspezifikationen und der Inkompatibilitäten bereit.
- [ ] Es führt eine Tabellenprüfung durch und zeigt, wenn Probleme gefunden werden, die Informationen an, damit der Serveradministrator Maßnahmen ergreifen kann.

#### F37. Welche MySQL-Anweisung wird verwendet, um zu überprüfen, welche Konten bestimmte Berechtigungen haben?

- [x] show grants (zeigt die Privilegien und Rollen an, die einem MySQL-Benutzerkonto oder einer MySQL-Rolle zugewiesen sind)
- [ ] showprivilegien (zeigt die Liste der Systemprivilegien, die der MySQL-Server unterstützt)
- [ ] Zugriff anzeigen
- [ ] Benutzerberechtigungen anzeigen

#### F38. Womit kann kein Auslöser verknüpft werden?

- [x] temporary table
- [ ] system table
- [ ] large table
- [ ] new table

[Referenz](https://dev.mysql.com/doc/refman/5.7/en/create-trigger.html)

#### Q39. Spätere Versionen von MySQL unterstützen den nativen JSON-Datentyp zum Speichern von JSON-Dokumenten. Was ist ein Nachteil von JSON-Spalten?

- [ ] ineffizient zum Speichern von JSON-Dokumenten
- [x] kann nicht direkt indiziert werden
- [ ] Dokumente können nicht validiert werden, wenn sie in json-Spalten gespeichert sind
- [ ] kann nicht normalisiert werden

#### Q40. Welche Aussage trifft auf das folgende Diagramm zu?

![mysql Q41](images/mysql_q41.jpg?raw=true)

- [ ] carid ist der Primärschlüssel für Käufe
- [ ] carid ist der Fremdschlüssel für cars.carid
- [x] Kunden-ID ist der Fremdschlüssel für Kunden-ID
- [ ] Kunden-ID ist der Primärschlüssel für Käufe

#### F41. Mit welcher Anweisung können Sie Daten aus einer Datei in die Tabelle laden?

- [ ] `cat file | mysql`
- [x] `LOAD DATA INFILE`
- [ ] `LOAD DATA LOCAL INFILE`
- [ ] `extended INSERT statement`

#### F42. Sie arbeiten mit den Tabellen, wie in diesem Diagramm gezeigt. Sie müssen sicherstellen, dass jeder zur Tabelle „Einkäufe“ hinzugefügte Datensatz aus einer Kunden-ID besteht, die bereits in der Tabelle „Kunden“ vorhanden ist, und einer Fahrzeug-ID, die bereits in der Tabelle „Autos“ vorhanden ist. Sie entscheiden sich, einen Trigger für die Validierung zu verwenden. Welches verwendest du?

![mysql Q43](images/mysql_q85.jpg?raw=true)

- [ ] `AFTER INSERT`
- [x] `BEFORE INSERT`
- [ ] `CROSS JOIN`
- [ ] `IF EXISTS`

`IF EXISTS` und `CROSS JOIN` sind für einen Trigger nicht gültig.

#### F43. Welches ist die korrekte Syntax einer erweiterten Einfügeanweisung?

- [ ] insert into cars (make, model, year) values ('Ford', 'Mustang', 2002)
      ('Mercedes', 'C', 2003)

- [ ] insert into cars (make, model, year) values ('Ford', 'Mustang', 2002)
      values ('Mercedes', 'C', 2003)

- [ ] insert into cars (make, model, year) extended ('Ford', 'Mustang', 2002),
      ('Mercedes', 'C', 2003)

- [x] insert into cars (make, model, year) values ('Ford', 'Mustang', 2002),
      ('Mercedes', 'C', 2003)

#### Q44. Sie müssen eine exakte Kopie einer Tabelle mit allen Spalten und Indizes erstellen. Wie können Sie alle Informationen erhalten, die Sie benötigen, um dies zu erreichen?

- [ ] create table
- [ ] clone table
- [ ] insert into
- [x] show create table

Beachten Sie, dass es bei der Frage um das _Bekommen_ der Daten geht und nicht um die \_Duplizierungsoperation selbst. Und tatsächlich besteht überhaupt keine Notwendigkeit, `SHOW CREATE TABLE` auszuführen. [Um die Tabelle zu duplizieren](https://popsql.com/learn-sql/mysql/how-to-duplicate-a-table-in-mysql) Struktur können Sie `CREATE TABLE new_table LIKE original_table;`.

#### F45. sie müssen ihr mysql-system gegen angreifer sichern. Was sollst du _nicht_ tun?

- [ ] MySQL-Server als normaler Benutzer ausführen.
- [ ] Gewähren Sie anderen Benutzern das PROCESS- oder SUPER-Privileg.
- [x] Führen Sie den MySQL-Server als Unix-Root-Benutzer aus.
- [ ] Verwenden Sie das komprimierte Protokoll.

#### F46. Sie verwalten eine Datenbank mit einer Tabelle „Kunden“. Sie haben eine temporäre Tabelle, auch "Kunden" genannt, erstellt, mit der Sie für die Dauer Ihrer Sitzung arbeiten. Sie müssen die temporäre Tabelle mit anderen Spezifikationen neu erstellen. Welchen Befehl müssen Sie zuerst ausführen?

- [ ] `CREATE TEMPORARY TABLE customers;`
- [ ] `DROP TEMP TABLE Kunden;`
- [ ] `DROP TABLE Kunden;`
- [x] `DROP TEMPORARY TABLE customers;`

1. [Referenz](https://dev.mysql.com/doc/refman/8.0/en/drop-table.html)
2. [Referenz](https://www.mysqltutorial.org/mysql-temporary-table)

#### F47. Sie müssen eine komplexe Abfrage mit rekursiven Unterabfragen ausführen, ohne jedoch eine gespeicherte Prozedur oder eine Funktion zu erstellen. Welchen Befehl oder welche Klausel verwenden Sie?

- [ ] COLLATE
- [ ] UNION
- [ ] FULL JOIN
- [x] WITH

Genau dafür ist [WITH-Klausel](https://dev.mysql.com/doc/refman/8.0/en/with.html) konzipiert

#### F48. Welche Wahl ist kein Verarbeitungsalgorithmus für Datenbankansichten?

- [ ] merge
- [x] updatable
- [ ] temptable
- [ ] undefined

[Referenz](https://dev.mysql.com/doc/refman/8.0/en/view-algorithms.html)

#### F49. Wofür wird das MySQL-Befehlszeilendienstprogramm „perror“ verwendet?

- [ ] um Ihre MySQL-Version anzuzeigen
- [ ] um Betriebssystem-Fehlercodes anzuzeigen
- [ ] um fehlerhafte Standardeinstellungen anzuzeigen
- [x] um Speicherfehlercodes anzuzeigen

Hinweis: perror gibt eine Beschreibung für einen Systemfehlercode oder für einen Fehlercode einer Speicher-Engine (Tabellenhandler) aus -
[link](<https://dev.mysql.com/doc/refman/5.7/en/perror.html#:~:text=2%20perror%20%E2%80%94%20Display%20MySQL%20Error% 20Message%20Information,-For%20most%20system&text=You%20can%20find%20out%20what,(table%20handler)%20error%20code>)

#### Q50. Wie können Sie alle Spalten für eine bestimmte Tabelle auflisten?

- [ ] SHOW table COLUMNS;
- [x] SHOW COLUMNS FROM table;
- [ ] LIST table COLUMNS;
- [ ] SELECT COLUMNS FROM table;

Hinweis: `DESCRIBE tablename` ist eine Abkürzung für diesen Befehl

#### F51. Wie würden Sie den vollständigen Tabellensatz in der aktuell ausgewählten Datenbank auflisten?

- [ ] SELECT \* FROM DATABASE;
- [x] SHOW TABLES;
- [ ] LIST TABLES;
- [ ] SELECT ALL TABLES;

#### F52. Welche Auswahl gehört nicht zu den Tabellenpflegeanweisungen?

- [ ] CHECK TABLE;
- [x] CREATE TABLE;
- [ ] ANALYZE TABLE;
- [ ] OPTIMIZE TABLE;

#### F53. In welcher Tabelle speichert MySQL Passwörter für Benutzerkonten?

- [ ] mysql.accounts;
- [ ] mysql.passwords;
- [ ] mysql.admin;
- [x] mysql.user;

#### F54. Das Management hat Sie gebeten, eine Mitarbeiterdatenbank aufzubauen. Sie müssen die aktuelle Position und das Gehalt jedes Mitarbeiters sowie alle früheren Positionen und Gehälter im Unternehmen angeben. Sie entscheiden sich für eine Eins-zu-Viele-Struktur: eine Mitarbeitertabelle mit den wichtigsten Informationen wie Name und Adresse und eine Beschäftigungstabelle mit Positions- und Gehaltshistorie. Sie können das Feld employeeID verwenden, um sie zu verbinden. Wofür ist Employment.employeeID ein Beispiel?

- [ ] Primärschlüssel;
- [ ] Sekundärschlüssel;
- [x] Fremdschlüssel;
- [ ] Alternativschlüssel;

#### F55. Was ist in neueren Versionen von MySQL (8.0+) die korrekte Syntax, um einen CTE (Common Table Expression) zu deklarieren?

- [ ] WITH (SELECT id FROM users) as cte, SELECT ...
- [ ] WITH (SELECT id FROM users) as cte SELECT ...
- [ ] WITH cte as (SELECT id FROM users), SELECT ...
- [x] WITH cte as (SELECT id FROM users) SELECT ...

#### F56. Was ist ein Grund, Datenredundanz in ein normalisiertes Datenbankdesign einzuführen?

- [x] um die Beschädigung von Daten zu reduzieren
- [ ] um den Speicherplatz zu reduzieren
- [x] um das System schneller zu machen
- [ ] um Datenanomalien zu vermeiden

Hinweis: "um das System schneller zu machen" kann auch richtig sein. Zum Beispiel können wir eine schwere Abfrage im Voraus berechnen und ihr Ergebnis in einer Spalte speichern (als Cache verwenden). Wenn also "System" "Anwendung, die mysql verwendet" bedeutet, dann ist es auch richtig.

#### F57. Das folgende Code-Snippet wird verwendet, um Daten aus einer XML-Datei in eine Tabelle einzulesen. Welche XML-Struktur wird von der Anweisung \_nicht\_ unterstützt?

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

#### F58. Sie laden Daten in eine Tabelle. Mit welchem ​​Befehl können Sie sicherstellen, dass alle Daten eingefügt und doppelte Zeilen verworfen werden?

- [x] `INSERT IGNORE`
- [ ] `INSERT UNIQUE`
- [ ] `INSERT INTO`
- [ ] `INSERT DISTINCT`

#### F59. Welche Aussage über die `TRUNCATE TABLE`-Anweisung ist richtig?

- [ ] Es stoppt und gibt einen Fehler aus, wenn es auf eine Zeile trifft, die von einer Zeile in einer untergeordneten Tabelle referenziert wird.
- [x] Es wird immer zuerst gelöscht und dann eine neue Tabelle neu erstellt.
- [ ] Es löscht Zeilen nacheinander in Tabellen mit Fremdschlüsseleinschränkungen.
- [x] Es ruft die der Tabelle zugeordneten `DELETE`-Trigger nicht auf.

Hinweis: Beide Antworten sind richtig – siehe [TRUNCATE TABLE Statement](https://dev.mysql.com/doc/refman/8.0/en/truncate-table.html) im MySQL-Handbuch

#### Q60. Sie arbeiten mit den Tabellen, wie in diesem Diagramm gezeigt. Sie müssen die Anzahl der verkauften Autos pro Heimatstaat des Wohnsitzes jedes Kunden erhalten. Wie können Sie dies erreichen?

![mysql Q61](images/mysql_q61.png?raw=true)

- [ ] `SELECT state, COUNT(*) FROM customers WHERE ID IN (SELECT customerID FROM purchases) GROUP BY state;`
- [ ] `SELECT state, COUNT(*) FROM customers c LEFT JOIN purchases p ON c.ID = p.customerID GROUP BY state;`
- [x] `SELECT state, COUNT(*) FROM customers c, purchases p WHERE c.ID = p.customerID GROUP BY state;`
- [ ] `SELECT state, COUNT(*) FROM customers GROUP BY state;`

Erläuterung: Der Unterschied zwischen 2 und 3 besteht darin, dass LEFT JOIN vor der Gruppierung 1 Zeile pro Kunde zurückgibt. Wenn es durch RIGHT JOIN ersetzt würde, würde es die richtigen Informationen zurückgeben.

#### F61. Bei der Datenmigration müssen häufig doppelte Zeilen im Rahmen der Datenbereinigung gelöscht werden. Welche Aussage funktioniert am besten?

- [ ] `DELETE DUPS`
- [ ] `DELETE DISTINCT`
- [x] `DELETE JOIN`
- [ ] `DELETE WITH`

#### F62. Was müssen Sie bei der Arbeit mit dem MySQL-Cursor außerdem deklarieren?

- [ ] `DEFAULT` value
- [ ] `RETURN` variable
- [ ] `SQLEXCEPTION` routine
- [x] `NOT FOUND` handler

#### F63. Welcher Sicherungstyp umfasst alle Änderungen, die an den Daten vorgenommen wurden, seit die letzte vollständige Sicherung durchgeführt wurde?

- [ ] snapshot
- [ ] logical
- [x] differential
- [ ] incremental

#### F64. Sie müssen eine MySQL-Datenbank aus einer Sicherungsdatei wiederherstellen. Welches Befehlszeilentool verwenden Sie für den eigentlichen Datenimport, nachdem Sie die Datenbank neu erstellt haben?

- [ ] `mysqld`
- [x] `mysql`
- [ ] `mysqladmin`
- [ ] `mysqldump`

#### F65. Sie importieren Daten als JSON in eine neue Tabelle. Sie führen CREATE TABLE json_data ( city JSON ) aus; und Zeilen in diese Tabelle einfügen. Was ist die korrekte Syntax, um die Liste der Städte anzuzeigen?

- [ ] `SELECT city FROM json_data;`
- [x] `SELECT city->>'$.name' city FROM json_data;`
- [ ] `SELECT city.name city FROM json_data;`
- [ ] `SELECT city->'$.name' city FROM json_data;`

Hinweis: Die letzte Option ist auch gültig, aber die Ergebnisse werden in Anführungszeichen gesetzt

#### F66. Wenn Sie MyISAM anstelle von InnoDB verwenden möchten, welche Option müssen Sie in der CREATE TABLE-Anweisung angeben?

- [x] ENGINE
- [ ] PARTITION
- [ ] STORAGE
- [ ] TABLESPACE

#### F67. Sie arbeiten mit der Tabelle in diesem Diagramm. Sie möchten mit der Volltextsuche die Kunden finden, die in einer Straße oder Einfahrt wohnen. Wie lautet der Befehl dazu?

Table name: **customers**

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

#### F68. Welche Abfrage listet die Datenbanken auf dem aktuellen Server auf?

- [x] SHOW DATABASES;
- [ ] LIST ALL DATABASES;
- [ ] LIST DATABASES;
- [ ] SHOW DB;

#### F69. Was ist das Ergebnis der Datenbankentwurfsphase?

- [ ] alle Tabellen, Spalten, Datentypen, Indizes und ihre Beziehungen
- [ ] eine Liste von Entitäten, ihrer Beziehung und Einschränkungen
- [ ] alle Tabellen und deren Namen, die zur Implementierung des logischen Modells benötigt werden
- [x] eine Liste von Entitäten, ihrer Beziehung, Beschränkungen, Datentypen und Kardinalitäten

#### Q70. Welche Wahl ist _kein_ gültiges Modell für einen gespeicherten Prozedurparameter?

- [ ] INOUT
- [ ] IN
- [ ] OUT
- [x] IN OUT

#### F71. Welchen Vorteil bietet die Verwendung einer temporären Tabelle anstelle einer Heap-Tabelle?

- [ ] Die temporäre Tabelle wird gelöscht, wenn die Datenbank neu gestartet wird.
- [ ] Temporäre Tabellen können von Clients gemeinsam genutzt werden, wodurch sie in Gruppenentwicklungsumgebungen besser verwendbar sind.
- [x] Die temporäre Tabelle wird gelöscht, sobald Ihre Sitzung getrennt wird.
- [ ] Das Erstellen einer temporären Tabelle erfordert keine besonderen Berechtigungen.

#### F72. Welches ist ein gültiger Konstruktor für eine Klasse namens User?

- [ ] `public construct User() {}`
- [x] `public User() {}`
- [ ] `public instance User() {}`
- [ ] `public init User() {}`

#### Q73. Was ist die maximale Anzahl von Spalten, die von einem einzelnen Tabellenindex verwendet werden können?

- [ ] 2
- [ ] 4
- [ ] 8
- [x] 16

#### Q74. Welcher Befehl gibt eine Liste von Triggern in der aktuellen Datenbank zurück?

- [ ] `DISPLAY TRIGGERS;`
- [x] `SHOW TRIGGERS;`
- [ ] `SELECT ALL TRIGGERS;`
- [ ] `SELECT * FROM information_schema.triggers;`

#### Q75. Welche Aussage zu den Datentypen TIMESTAMP und DATETIME ist richtig?

- [ ] TIMESTAMP-Werte benötigen mehr Bytes zum Speichern als DATETIME-Werte.
- [ ] TIMESTAMP wird ohne Zeitzone gespeichert und DATETIME wird in UTC-Werten gespeichert.
- [x] TIMESTAMP und DATETIME werden beide ohne Zeitzone gespeichert.
- [ ] TIMESTAMP wird in UTC-Werten gespeichert und DATETIME wird ohne Zeitzone gespeichert.

#### F76. Was ist das Äquivalent zum Befehl mysqladmin reload?

- [ ] `mysqladmin flush-threads`
- [ ] `mysqladmin flush-tables`
- [x] `mysqladmin flush-privileges`
- [ ] `mysqladmin flush-all`

#### F77. Erklären Sie den Sicherheitsaspekt gespeicherter Prozeduren

- [ ] Gespeicherte Prozeduren sind nicht sicher, da sie von der Befehlszeile als Root-Benutzer ausgeführt werden können
- [ ] Stored Procedures sind sicher, da der Eigentümer der Stored Procedure entscheiden kann, wem Zugriff gewährt wird
- [x] Gespeicherte Prozeduren sind sicher, da Anwendungen Zugriff auf gespeicherte Prozeduren und nicht auf zugrunde liegende Tabellen gewährt werden kann
- [ ] Gespeicherte Prozeduren sind nicht sicher, da sie Anweisungen ausführen können, um Tabellen zu löschen oder Daten massenweise zu löschen

#### F78. Wie würden Sie Daten zu allen Kunden abrufen, bei denen keine Telefonnummer gespeichert ist?

- [ ] `SELECT * FROM customers WHERE PhoneNumber = NULL;`
- [ ] `SELECT * FROM customers WHERE PhoneNumber IS NOT VALID;`
- [x] `SELECT * FROM customers WHERE PhoneNumber IS NULL;`
- [ ] `SELECT * FROM customers WHERE PhoneNumber IS UNKNOWN;`

#### Q79. Im folgenden Diagramm ist das Preisfeld als Typ DECIMAL deklariert. Was wäre eine effizientere Deklaration für dieses Feld?

![Mysql-Bild](images/mysql_q80.png?raw=true)

- [ ] FLOAT
- [x] DECIMAL(10,2)
- [ ] NUMERIC
- [ ] DOUBLE

#### F80. Welche Option ist „kein“ verfügbarer Zeichenfolgentyp für eine Spalte?

- [ ] `ENUM`
- [ ] `SET`
- [x] `BIT`
- [ ] `CHAR`

Erläuterung: BIT ist kein String-Typ

#### F81. Dieses Diagramm zeigt, welche Art von Beziehung zwischen Kunden und Autos?

![Mysql-Bild](images/mysql_q80.png?raw=true)

- [ ] one-to-many
- [ ] parent-child
- [x] many-to-many
- [ ] many-to-one

#### Q82. Eine gespeicherte Routine ist ein Satz von SQL-Anweisungen, die auf dem Server gespeichert sind und entweder als Prozedur oder als Funktion vorliegen. Welche Anweisung kann nicht in gespeicherten Routinen verwendet werden?

- [ ] `SELECT`
- [x] `USE`
- [ ] `SET`
- [ ] `DECLARE`

Erläuterung: Sowohl `SET` als auch `DECLARE` werden verwendet, um Variablen zu erstellen. Referenz: [Tutorial zu MySQL STORED PROCEDURE mit Beispielen](https://www.softwaretestinghelp.com/mysql-stored-procedure/)

#### F83. Wenn ein neuer Student zu einer neuen Datenbank hinzugefügt wird, möchten Sie, dass neue Datensätze in den zugehörigen Tabellen wie Prüfung, Ergebnis und Anwesenheit erstellt werden. Wie würden Sie dies erreichen?

- [x] trigger
- [ ] regular expression
- [ ] view
- [ ] index

#### F84. Im folgenden Diagramm sind die ID-Felder als Typ CHAR statt INT deklariert. Was ist KEIN möglicher Grund für diese Entscheidung?

![Mysql-Bild](images/mysql_q85.png?raw=true)

- [ ] Das ID-Feld muss Buchstaben und nicht nur Zahlen enthalten.
- [ ] Sie können ein konsistentes Format für alle Tabellen haben, die ID-Felder erfordern.
- [ ] Das ID-Feld muss führende Nullen haben, die der INT-Datentyp abschneiden würde.
- [x] Der Datentyp `CHAR(10)` ist effizienter und platzsparender.

#### F85. Warum sollten Sie einen allgemeinen Tabellenausdruck (CTE) verwenden?

- [ ] Zum Definieren von Abfragen zur späteren Wiederverwendung für die Dauer der aktuellen Sitzung
- [ ] Zum Erstellen temporärer Tabellen, die zur Vorauswahl häufig verwendeter Ergebnismengen verwendet werden können.
- [ ] Um einen neuen Einzelwert aus einer Ergebnismenge zu berechnen und an den Abfrageparser zurückzugeben.
- [x] Um komplexe Abfragen aufzuschlüsseln und die Wiederverwendung innerhalb einer Abfrage zu ermöglichen.

Erläuterung: CTEs erstellen keine temporären Tabellen, sie funktionieren nur innerhalb einer einzelnen Abfrage. Referenz: [13.2.15 WITH (Common Table Expressions)](https://dev.mysql.com/doc/refman/8.0/en/with.html).

#### F86. Welcher Optionsmodifikator weist ein Programm an, nicht mit einem Fehler zu beenden, wenn es die Option nicht erkennt, sondern stattdessen eine Warnung auszugeben?

- [ ] --verbose
- [ ] --skip
- [ ] --skip-error
- [x] --loose

Referenz: [4.2.2.4 Program Option Modifiers](https://dev.mysql.com/doc/refman/8.0/en/option-modifiers.html)

#### F87. Was gibt diese SQL-Anweisung zurück?

```
SELECT name FROM students WHERE name REGEXP '^to';
```

- [x] alle Namen, die mit „to“ beginnen, wie z. B. Tommy oder Tony
- [ ] alle Namen mit "to", wie Roberto und Tommy
- [ ] Alle Namen ohne "to", wie Samantha oder Kathryn
- [ ] alle Namen, die mit „to“ enden, wie z. B. Roberto

#### Q88. Sie arbeiten mit den Tabellen wie in der Abbildung dargestellt. Sie müssen die Liste der Gesamtpreise für jede Automarke und jedes Automodell erstellen, mit Zwischensummen für jede Marke und der Gesamtsumme aller Preise. Welche SQL-Klausel verwenden Sie?

![Mysql-Bild](images/mysql_q92.png?raw=true)

- [ ] UNION
- [ ] SHOW TOTALS
- [ ] UNION ALL
- [x] WITH ROLLUP

#### Q89. Die Left- und Right-Joins werden auch als \_ bezeichnet.

- [ ] Inner Join
- [ ] Natural Join
- [x] Outer Join
- [ ] Cartesian Join

#### Q90. Was ist der gültige Weg, um eine Datenbankansicht in MySQL zu erstellen?

- [ ] `CREATE VIEW v1 SELECT * FROM t1 WHERE col1 > 10;`
- [ ] `CREATE VIEW v1 AS BEGIN SELECT * FROM t1 END;`
- [ ] `CREATE VIEW v1 BEGIN SELECT * FROM t1 END;`
- [x] `CREATE VIEW v1 AS SELECT * FROM t1;`

#### Q91. Wie werden Berechtigungen in MySQL implementiert?

- [ ] encrypted algorithms
- [x] access control lists
- [ ] user settings
- [ ] administrator schema

#### Q92. Innerhalb einer Transaktion müssen mehrere Operationen durchgeführt werden. Was würden Sie tun, wenn während dieser Transaktion eine Ausnahme auftritt?

- [ ] `UNDO`
- [ ] `UNCOMMIT`
- [x] `ROLLBACK`
- [ ] `REVERSE`

#### Q93. Welche Funktion findet die aktuelle Uhrzeit oder das Datum in MySQL?

- [ ] DATE()
- [ ] GETDATE()
- [x] CURDATE()
- [ ] CURRENT()

#### Q94. Was ist die korrekte Verwendung von ENUM in MySQL?

- [ ] `Create table size (ENUM ('Small','Medium','Large'));`
- [ ] `Create table ENUM (name ('Small','Medium','Large'));`
- [ ] `Create table size (name: ENUM['Small','Medium','Large']);`
- [x] `Create table size (name ENUM('Small','Medium','Large'));`

#### Q95. Der mysqldump-Befehl kann keine Ausgabe in **\_** generieren.

- [x] JSON
- [ ] CSV
- [ ] XML
- [ ] TXT

#### Q96. Sie arbeiten mit den unten gezeigten Tabellen. Sie müssen die Liste aller Autos erstellen, unabhängig davon, ob sie verkauft wurden oder nicht. Welche Aussage leistet das?

![Mysql-Bild](images/mysql_q98.png?raw=true)

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

#### Q97. Welcher Codeausschnitt aus einer gespeicherten Prozedur sollte als CASE-Anweisung umgeschrieben werden?

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

#### Q98. Warum würden Sie gespeicherte Funktionen verwenden?

- [ ] für Formeln und Geschäftsregeln, die Sie auf Spalten in einer SQL-Abfrage anwenden möchten
- [x] für Formeln und Geschäftsregeln, die auf ein bestimmtes Triggerereignis angewendet werden sollen, z. B. auf Einfügungen
- [ ] zum automatischen Ändern der Daten einer Tabelle basierend auf einer Abfrage
- [ ] zur Wiederverwendung wiederkehrender Abfragen

#### Q99. Welche Schritte müssen Sie unternehmen, um die Tabelle aus diesem Diagramm zu normalisieren?

Tabellenname: Superhelden
| Name | Pseudonym | Leistung1 | Leistung2 | Macht3 |
| ---- | ----- | ------ | ------ | ------ |
| Übermensch | Clark Kent | Flug | Röntgenblick | Superstärke |
| Wunderfrau | Diana Prinz | Kraftfelder | Reflexe | Telepathie |
| Spiderman | Peter Parker | Walkriechen | Web-Making | Verbesserte Sinne |
| Aquaman | Arthur Curry | Unterwasseratmung | Verbesserte Sicht | Ausdauer |
| Hulk | Bruce-Banner | Superstärke | Strahlenimmunität | Unverwundbarkeit |

- [x] Erstellen Sie eine weitere Tabelle zum Nachschlagen von Kräften mit Feldern für Code und Beschreibung sowie eine Verbindungstabelle mit Superheldennamen und Kraftcodes.
- [ ] Fügen Sie dieser Tabelle eine Spalte hinzu, die als Datensatzkennung dient, und machen Sie sie zum Primärschlüssel.
- [ ] Erweitern Sie diese Tabelle um zusätzliche Spalten "power4", "power5" und so weiter, um zusätzliche Kräfte für jeden Superhelden zu ermöglichen.
- [ ] Konvertieren Sie diese Tabelle so, dass sie eine Spalte mit dem Namen "Power" hat, und fügen Sie einen Datensatz für jede Superhelden-Power-Kombination hinzu, für insgesamt 15 Datensätze in diesem Beispiel.

#### Q100. Was ist ein gültiger Weg, um eine Datenbankansicht in MySQL zu erstellen?

- [ ] 1 CREATE VIEW v1 2 SELECT \* FROM t1 3 WHERE col1 &gt; 10;
- [ ] 1 CREATE VIEW v1 2 BEGIN 3 SELECT \* FROM t1 4 END
- [ ] 1 CREATE VIEW v1 AS 2 SELECT \* FROM t1;
- [ ] 1 CREATE VIEW v1 AS 2 BEGIN 3 SELECT \* FROM t1 4 END;

#### Q101. Eine Tabelle Item hat ein boolesches Feld endOfLife und ein makeYear-Feld vom Typ YEAR(4). Wie können Sie den booleschen Wert für alle Artikel, die vor 2019 hergestellt wurden, auf wahr setzen?

- [ ] UPSERT Item SET endOfLife = true WHERE makeYear < 2019
- [ ] CHANGE Item SET endOfLife = true WHERE makeYear < 2019
- [ ] ALTER Item SET endOfLife = true WHERE makeYear < 2019
- [x] UPDATE Item SET endOfLife = true WHERE makeYear < 2019

#### Q102. Welche Auswahl ist ein Beispiel für eine Aggregatfunktion?Welche Auswahl ist ein Beispiel für eine Aggregatfunktion?

- [ ] NOW()
- [ ] MID()
- [ ] FORMAT()
- [x] COUNT()

[Referenz](https://www.sqltutorial.org/sql-aggregate-functions/)

#### Q103. In diesem Diagramm arbeiten Sie am UPDATE-Trigger in der Mitarbeitertabelle. Wie können Sie auf den neuen Wert für die Adresse innerhalb des Triggers zugreifen?

![Mysql-Bild](images/mysql_q103.png?raw=true)

- [x] Use NEW.address
- [ ] Use INSERTED.address
- [ ] Use DELETED.address
- [ ] USE OLD.address

[Referenz](https://dev.mysql.com/doc/refman/8.0/en/trigger-syntax.html)

#### Q104. Sie arbeiten mit den Tabellen, wie in diesem Diagramm gezeigt. Sie müssen die Liste der Kunden erstellen, die bestimmte Automodelle gekauft haben. Welche SQL-Klausel verwenden Sie?

- [ ] UNION ALL
- [x] UNION
- [ ] SHOW TOTALS
- [ ] WITH ROLLUP

#### Q105. Sie verwalten eine Datenbank mit einer Tabelle namens „Kunden“. Sie haben eine temporäre Tabelle, auch "Kunden" genannt, erstellt, mit der Sie für die Dauer Ihrer Sitzung arbeiten. Sie müssen die temporäre Tabelle mit anderen Spezifikationen neu erstellen. Welchen Befehl müssen Sie zuerst ausführen?

- [ ] `CREATE TEMPORARY TABLE customers;`
- [ ] `DROP TEMP TABLE customers;`
- [ ] `DROP TEMPORARY TABLE customers;`
- [x] `DROP TABLE customers;`

#### Q106. Wie würden Sie in MySQL eine Abfrage ohne Berücksichtigung der Groß-/Kleinschreibung erstellen?

- [ ] `SELECT * FROM customers WHERE UPPEERCASE(LastName) = 'POTTER';`
- [ ] `SELECT * FROM customers WHERE LOWERCASE(LastName) = 'potter';`
- [x] `SELECT * FROM customers WHERE UPPER(LastName) = 'POTTER';`
- [ ] `SELECT * FROM customers WHERE UPPER(LastName) = 'Potter';`

#### Q107. Zu welchen Kategorien in Mysql gehört das Schlüsselwort "COUNT"?

- [x] Aggregatfunktionen
- [ ] Operatoren
- [ ] Klauseln
- [ ] Alle genannten

#### Q108. Welche der folgenden gehört zu einer "Aggregatfunktion"?

- [x] COUNT
- [ ] UPPER
- [ ] LOWER
- [ ] Alle genannten

#### Q109. Was bedeutet die "HAVING"-Klausel in MySQL?

- [ ] Um die Spaltenwerte herauszufiltern
- [x] Zum Herausfiltern der Zeilenwerte
- [ ] Zum Herausfiltern der Zeilen- und Spaltenwerte
- [ ] Keine der genannten

#### Q110. Welche Klausel ähnelt der "HAVING"-Klausel in Mysql?

- [ ] SELECT
- [ ] FROM
- [x] WHERE
- [ ] Keine der genannten

#### Q111. Was wird die Ausgabe des folgenden MySQL-Befehls sein?

      SELECT emp_id, fname, lname
      FROM employee
      WHERE title=’HEAD TELLER’ AND start_date&gt;2008-11-23;

- [ ] Alle Spalten
- [ ] Nur die Spalten, die mit der "SELECT"-Klausel erwähnt werden
- [x] Spaltenerwähnung mit "SELECT"-Klausel und nur die Zeilen, die "HEAD TELLER" als "title" enthalten
- [ ] Keine der genannten

#### Q112. Gibt es einen Fehler in der folgenden MySQL-Anweisung?

      SELECT e.emp_id, e.fname,e.lname,d.name
      FROM employee e INNER JOIN department d
      ON e.dept_id=e.dept_id;

- [x] NEIN
- [ ] JAWOHL
- [ ] Abhängig
- [ ] Keine der genannten

#### Q113. Spätere Versionen von MySQL unterstützen den nativen JSON-Datentyp zum Speichern von JSON-Dokumenten. Was ist ein Nachteil von JSON-Spalten?

- [ ] JSON-Spalten können nicht normalisiert werden.
- [x] JSON-Spalten können nicht direkt indiziert werden.
- [ ] JSON-Spalten sind zum Speichern von JSON-Dokumenten ineffizient.
- [ ] JSON-Dokumente können nicht validiert werden, wenn sie in JSON-Spalten gespeichert sind.

#### Q114. Wie wählen Sie mit MySQL alle Datensätze aus einer Tabelle mit dem Namen "Personen" aus, in der der "Nachname" alphabetisch zwischen (und einschließlich) "Hansen" und "Pettersen" steht?

- [ ] `SELECT LastName>'Hansen' AND LastName<'Pettersen' FROM Persons`
- [x] `SELECT * FROM Persons WHERE LastName BETWEEN 'Hansen' AND 'Pettersen'`
- [ ] `SELECT * FROM Persons WHERE LastName>'Hansen' AND LastName<'Pettersen'`
- [ ] `Keines der oben genannten.`

[Referenz](https://www.w3schools.com/mysql/mysql_between.asp)

#### Q115. Betrachten Sie den unten angegebenen Satz von Beziehungen und die folgende SQL-Abfrage

        Students : (Roll number, Name, Date of birth)
        Courses: (Course number, Course name, instructor)
        Grades: (Roll number, Course number, Grade)
        SELECT DISTINCT Name
        FROM Students, Courses, Grades
        WHERE Students.Roll_number = Grades.Roll_number
        AND Courses.Instructor =Sriram
        AND Courses.Course_number = Grades.Course_number
        AND Grades.Grade = A

(Welche der folgenden Mengen wird durch die obige Abfrage berechnet?)

- [ ] Namen von Schülern, die in allen von Sriram unterrichteten Kursen eine A-Note erhalten haben
- [ ] Namen der Studenten, die in allen Kursen eine A-Note erhalten haben
- [x] Namen von Studenten, die in mindestens einem der von Sriram unterrichteten Kurse eine A-Note erhalten haben
- [ ] Nichts des oben Genannten
