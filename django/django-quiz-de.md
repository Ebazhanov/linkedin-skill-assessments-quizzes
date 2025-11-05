## Django

#### F1. Um Ihre gesamte Website für eine Anwendung in Django zu cachen, fügen Sie alle außer welcher dieser Einstellungen hinzu?

- [ ] django.middleware.common.CommonMiddleware
- [ ] django.middleware.cache.UpdateCacheMiddleware
- [ ] django.middleware.cache.FetchFromCacheMiddleware
- [x] django.middleware.cache.AcceleratedCacheMiddleware

**Referenz:**
Django verfügt über ein robustes Cache-System, mit dem Sie dynamische Seiten speichern können, sodass sie nicht für jede Anfrage neu berechnet werden müssen. Aus Bequemlichkeit bietet Django Cache mit unterschiedlicher Granularität – von der gesamten Website über Seiten bis hin zu Teilen von Seiten, DB-Abfrageergebnissen und beliebigen Objekten im Speicher. Cache-Middleware. Wenn aktiviert, wird jede von Django betriebene Seite basierend auf der URL zwischengespeichert.

#### F2. In welcher Programmiersprache ist Django geschrieben?

- [ ] C++
- [ ] Java
- [x] Python
- [ ] Ruby

#### F3. Um automatisch einen Wert für ein Feld bereitzustellen oder eine Validierung durchzuführen, die Zugriff auf mehr als ein einzelnes Feld erfordert, sollten Sie die `___` Methode in der `___` Klasse überschreiben.

- [ ] validate(); Model
- [ ] group(); Model
- [ ] validate(); Form
- [x] clean(); Model

#### F4. Ein Kunde möchte, dass seine Website "Rick & Morty"-Episoden nach Nummer oder Titel laden kann – z.B. shows/3/3 oder shows/picklerick. Welches URL-Muster empfehlen Sie?

- [ ] A

```python
url(r'shows/<int:season>/<int:episode>/', views.episode_number),
url(r'shows/<slug:episode_name>/', views.episode_name)
```

- [x] B

```python
path('shows/<int:season>/<int:episode>/', views.episode_number),
path('shows/<slug:episode_name>/', views.episode_name)
```

- [ ] C

```python
path('shows/<int:season>/<int:episode>', views.episode_number),
path('shows/<slug:episode_name>/', views.episode_number)
```

- [ ] D

```python
url(r'^show/(?P<season>[0-9]+)/(?P<episode>[0-9]+)/$', views.episode_number),
url(r'^show/(?P<episode_name>[\w-]+)/', views.episode_name
```

#### F5. Wie bestimmen Sie beim Start, ob ein Middleware-Element verwendet werden soll?

- [x] Lösen Sie MiddlewareNotUsed in der **init** Funktion Ihrer Middleware aus.
- [ ] Implementieren Sie die not_used Methode in Ihrer Middleware-Klasse.
- [ ] Listen Sie die Middleware unter einem Eintrag von django.middleware.IgnoredMiddleware auf.
- [ ] Schreiben Sie Code, um die Middleware aus den Einstellungen in [app]/**init**.py zu entfernen.

#### F6. Wie schalten Sie Djangos automatisches HTML-Escaping für einen Teil einer Webseite aus?

- [ ] Platzieren Sie diesen Abschnitt zwischen Absatz-Tags, die den autoescape=off Schalter enthalten.
- [x] Umschließen Sie diesen Abschnitt zwischen { percentage mark autoescape off percentage mark} und {percentage mark endautoescape percentage mark} Tags.
- [ ] Umschließen Sie diesen Abschnitt zwischen {percentage mark autoescapeoff percentage mark} und {percentage mark endautoescapeoff percentage mark} Tags.
- [ ] Sie müssen nichts tun – Autoescaping ist standardmäßig deaktiviert.

#### F7. Welcher Schritt würde NICHT helfen, den Fehler "django-admin: command not found" zu beheben?

- [ ] Überprüfen Sie, ob sich der bin-Ordner in Ihrem Django-Verzeichnis in Ihrem Systempfad befindet.
- [ ] Stellen Sie sicher, dass Sie die virtuelle Umgebung aktiviert haben, die Django enthält.
- [ ] Überprüfen Sie, ob Sie Django installiert haben.
- [x] Stellen Sie sicher, dass Sie ein Django-Projekt erstellt haben.

#### F8. Jedes Mal, wenn ein Benutzer gespeichert wird, muss sein quiz_score neu berechnet werden. Wo wäre ein idealer Ort, um diese Logik hinzuzufügen?

- [ ] Template
- [x] Model
- [ ] Datenbank
- [ ] View

#### F9. Was ist der richtige Weg, um eine Klasse namens "Rainbow" in Python zu beginnen?

- [ ] Rainbow {}
- [ ] export Rainbow:
- [x] class Rainbow:
- [ ] def Rainbow:

#### F10. Sie haben ein Django-Projekt geerbt und müssen es lokal zum Laufen bringen. Es kommt mit einer requirements.txt-Datei, die alle Abhängigkeiten enthält. Welchen Befehl sollten Sie verwenden?

- [ ] django-admin startproject requirements.txt
- [ ] python install -r requirements.txt
- [x] pip install -r requirements.txt
- [ ] pip install Django

#### F11. Welche Best Practice ist NICHT relevant für Migrationen?

- [x] Um sicherzustellen, dass Ihre Migrationen auf dem neuesten Stand sind, sollten Sie updatemigrations ausführen, bevor Sie Ihre Tests ausführen.
- [ ] Sie sollten Ihre Produktionsdatenbank sichern, bevor Sie eine Migration ausführen.
- [ ] Ihr Migrationscode sollte unter Versionskontrolle stehen.
- [ ] Wenn ein Projekt viele Daten hat, sollten Sie gegen eine Staging-Kopie testen, bevor Sie die Migration in der Produktion ausführen.

#### F12. Was wird dieses URL-Muster matchen? url(r'^\$', views.hello)

- [ ] eine Zeichenkette, die mit dem Buchstaben R beginnt
- [x] eine leere Zeichenkette im Server-Root
- [ ] eine Zeichenkette, die ^ und $ enthält
- [ ] eine leere Zeichenkette überall in der URL

#### F13. Was ist die typische Reihenfolge eines HTTP-Anfrage/Antwort-Zyklus in Django?

- [x] URL > View > Template
- [ ] Form > Model > View
- [ ] Template > View > Model
- [ ] URL > Template > View > Model

#### F14. Djangos klassenbasierte generische Views bieten welche Klassen, die gängige Webentwicklungsaufgaben implementieren?

- [ ] konkrete
- [ ] thread-sichere
- [x] abstrakte
- [ ] dynamische

#### F15. Welche Fähigkeiten benötigen Sie, um eine Reihe von Django-Templates zu pflegen?

- [ ] Template-Syntax
- [x] HTML und Template-Syntax
- [ ] Python, HTML und Template-Syntax
- [ ] Python und Template-Syntax

#### F16. Wie würden Sie die Beziehung zwischen einem Stern und einer Konstellation in einem Django-Model definieren?

- [x] A

```python
class Star(models.Model):
name = models.CharField(max_length=100)
class Constellation(models.Model):
stars = models.ManyToManyField(Star)
```

- [ ] B

```python
class Star(models.Model):
constellation = models.ForeignKey(Constellation, on_delete=models.CASCADE)
class Constellation(models.Model):
stars = models.ForeignKey(Star, on_delete=models.CASCADE)
```

- [ ] C

```python
class Star(models.Model):
name = models.CharField(max_length=100)
class Constellation(models.Model):
stars = models.OneToManyField(Star)
```

- [ ] D

```python
class Star(models.Model):
constellation = models.ManyToManyField(Constellation)
class Constellation(models.Model):
name = models.CharField(max_length=100)
```

#### F17. Was ist KEIN gültiger Schritt bei der Konfiguration Ihrer Django 2.x-Instanz zum Bereitstellen von statischen Dateien wie Bildern oder CSS?

- [x] Fügen Sie in Ihrer urls-Datei ein Muster hinzu, das den Namen Ihres statischen Verzeichnisses enthält.
- [ ] Erstellen Sie ein Verzeichnis namens static in Ihrem App-Verzeichnis.
- [ ] Erstellen Sie ein Verzeichnis mit dem Namen der App unter dem statischen Verzeichnis und platzieren Sie statische Dateien darin.
- [ ] Verwenden Sie das Template-Tag {percentage mark load static percentage mark}.

#### F18. Was ist der richtige Weg, um eine Variable für alle Ihre Templates verfügbar zu machen?

- [ ] Setzen Sie eine Sitzungsvariable.
- [ ] Verwenden Sie eine globale Variable.
- [x] Fügen Sie dem Template-Kontext ein Dictionary hinzu.
- [ ] Verwenden Sie RequestContext.

#### F19. Sollten Sie für neue Projekte ein benutzerdefiniertes Benutzermodell erstellen?

- [ ] Nein. Die Verwendung eines benutzerdefinierten Benutzermodells könnte die Admin-Oberfläche und einige Drittanbieter-Apps beschädigen.
- [x] Ja. Es ist einfacher, Änderungen vorzunehmen, sobald es in Produktion geht.
- [ ] Nein. Djangos integrierte models.User-Klasse wurde getestet – es macht keinen Sinn, das Rad neu zu erfinden.
- [ ] Ja, da es keine andere Option gibt.

#### F20. Sie möchten eine Seite erstellen, die das Bearbeiten von zwei Klassen ermöglicht, die durch einen Fremdschlüssel verbunden sind (z.B. eine Frage und Antwort, die in separaten Tabellen gespeichert sind). Welche Django-Funktion können Sie verwenden?

- [ ] Actions
- [ ] Admin
- [ ] Mezcal
- [x] Inlines

#### F21. Warum werden QuerySets als "lazy" betrachtet?

- [ ] Die Ergebnisse eines QuerySet sind nicht sortiert.
- [x] QuerySets erstellen keine Datenbankaktivität, bis sie ausgewertet werden.
- [ ] QuerySets laden Objekte erst in den Speicher, wenn sie benötigt werden.
- [ ] Mit QuerySets können Sie keine komplexeren Abfragen ausführen.

#### F22. Sie erhalten einen `MultiValueDictKeyError` beim Versuch, auf einen Anfrageparameter mit folgendem Code zuzugreifen: request.GET['search_term']. Welche Lösung wird Ihnen in diesem Szenario NICHT helfen?

- [x] Wechseln Sie zur Verwendung von POST anstelle von GET als Anfragemethode.
- [ ] Stellen Sie sicher, dass das Eingabefeld in Ihrem Formular ebenfalls "search_term" heißt.
- [ ] Verwenden Sie die GET-Methode von MultiValueDict, anstatt direkt auf das Dictionary zuzugreifen: request.GET.get('search_term', '').
- [ ] Überprüfen Sie, ob der search_term-Parameter in der Anfrage vorhanden ist, bevor Sie versuchen, darauf zuzugreifen.

#### F23. Welche Funktion der Django Form-Klasse rendert die Felder eines Formulars als Serie von <p>-Tags?

- [ ] show_fields()
- [x] as_p()
- [ ] as_table()
- [ ] fields()

#### F24. Sie haben einen Fehler in Django gefunden und möchten einen Patch einreichen. Was ist das korrekte Verfahren?

- [ ] Forken Sie das Django-Repository auf GitHub.
- [ ] Reichen Sie einen Pull-Request ein.
- [x] All diese Antworten.
- [ ] Führen Sie Djangos Testsuite aus.

#### F25. Django liefert sinnvolle Standardwerte für Einstellungen. In welchem Python-Modul finden Sie diese Einstellungen?

- [ ] `django.utils.default_settings.py`
- [ ] `django.utils.global_settings.py`
- [ ] `django.conf.default_settings.py`
- [x] `django.conf.global_settings.py`

#### F26. Welcher Variablenname ist laut PEP 8-Richtlinien am besten?

- [ ] numFingers
- [ ] number-of-Fingers
- [x] number_of_fingers
- [ ] finger_num

#### F27. Ein Projekt hat 500 Migrationen angesammelt. Welche Vorgehensweise würden Sie verfolgen?

- [ ] Führen Sie Ihre Migrationsdateien manuell zusammen, um die Anzahl zu reduzieren
- [ ] Machen Sie sich keine Sorgen über die Anzahl
- [ ] Versuchen Sie, die Anzahl der Migrationen zu minimieren
- [x] Verwenden Sie squashmigrations, um die Anzahl zu reduzieren

#### F28. Was ermöglicht Ihnen ein F()-Objekt beim Umgang mit Models?

- [x] DB-Operationen ohne Abrufen eines Modellobjekts durchführen
- [ ] DB-Transaktions-Isolationsstufen definieren
- [ ] Aggregatfunktionen einfacher verwenden
- [ ] Wiederverwendbare QuerySets erstellen

#### F29. Welcher ist kein Django-Feldtyp zum Speichern von Ganzzahlen?

- [ ] SmallIntegerField
- [x] NegativeIntegerField
- [ ] BigAutoField
- [ ] PositiveIntegerField

#### F30. Was zeigt die aktuell installierte Version?

- [ ] print (django.version)
- [ ] import django django.getVersion()
- [x] import django django.get_version()
- [ ] python -c django --version

#### F31. Sie sollten die HTTP-Methode `___` verwenden, um Daten zu lesen, und `___`, um Daten zu aktualisieren oder zu erstellen

- [ ] READ; WRITE
- [x] GET; POST
- [ ] POST; GET
- [ ] GET; PATCH

#### F32. Wann sollten Sie die POST-Methode anstelle von GET zum Übermitteln von Daten verwenden?

- [ ] Wenn Effizienz wichtig ist
- [ ] Wenn Sie möchten, dass die Daten gecacht werden
- [ ] Wenn Sie Ihren Browser zum Debuggen verwenden möchten
- [x] Wenn die Daten im Formular sensibel sein könnten

#### F33. Wann sollten Sie das Django Sites-Framework verwenden?

- [x] Wenn Ihre einzelne Installation mehr als eine Website betreibt
- [ ] Wenn Sie statische sowie dynamische Inhalte bereitstellen müssen
- [ ] Wenn Sie möchten, dass Ihre App einen vollqualifizierten Domainnamen hat
- [ ] Wenn Sie mehr als 10.000 Benutzer erwarten

#### F34. Welche Infrastruktur benötigen Sie:

`title=models.charfield(max_length=100, validators=[validate_spelling])`

- [ ] Initialisiertes Array namens validators
- [x] Eine Validators-Datei mit einer Funktion namens validate_spelling, die am Anfang des Models importiert wird
- [ ] Eine Validators-Datei mit einer Funktion namens validate, die am Anfang des Models importiert wird
- [ ] Spelling-Paket, das am Anfang des Models importiert wird

#### F35. Welcher Decorator wird verwendet, um zu verlangen, dass eine View nur die GET- und HEAD-Methoden akzeptiert?

- [x] require_safe()
- [ ] require_put()
- [ ] require_post()
- [ ] require_get()

#### F36. Wie würden Sie die Beziehung zwischen einem Buch und einem Autor definieren – ein Buch hat nur einen Autor.

```python
class Author (models.model):
book=models.foreignkey(Book,on_delete=models.cascade)
class Book(models.model):
name=models.charfield(max_length=100)
```

- [x] A

```python
class Author (models.model):
name=models.charfield(max_length=100)
class Book(models.model):
author=models.foreignkey(Author,on_delete=models.cascade)
```

- [ ] B

```python
class Author (models.model):
name=models.charfield(max_length=100)
class Book(models.model):
author=models.foreignkey(Author)
```

- [ ] C

```python
class Author (models.model):
name=models.charfield(max_length=100)
class Book(models.model):
author=models.foreignkey(Author,on_delete=models.cascade)
```

- [ ] D

```python
class Author (models.model):
name=models.charfield(max_length=100)
class Book(models.model):
author=Author.name
```

#### F37. Was ist ein Callable, das einen Wert nimmt und einen Fehler auslöst, wenn der Wert fehlschlägt?

- [x] Validator
- [ ] Deodorizer
- [ ] Mediator
- [ ] Regulärer Ausdruck

#### F38. Um einen API-Endpunkt zu sichern und ihn nur für registrierte Benutzer zugänglich zu machen, können Sie den Wert rest_framework.permissions.allowAny im Abschnitt default_permissions Ihrer settings.py ersetzen durch

- [ ] rest_framework.permissions.IsAdminUser
- [x] rest_framework.permissions.IsAuthenticated
- [ ] rest_framework.permissions.IsAuthorized
- [ ] rest_framework.permissions.IsRegistered

#### F39. Welchen Befehl würden Sie verwenden, um eine Migration anzuwenden?

- [ ] makemigration
- [ ] update_db
- [ ] applymigration
- [x] migrate

#### F40. Welcher Klassentyp ermöglicht es, QuerySets und Modellinstanzen in native Python-Datentypen zur Verwendung in APIs zu konvertieren?

- [ ] objectwriters
- [x] serializers
- [ ] picklers
- [ ] viewsets

#### F41. Wie sollte der Code enden?

```python
{ percentage if spark >= 50 percentage }
Lots of spark
{percentage elif spark == 42 percentage}
```

- [ ] { percentage else percentage}
- [x] {percentage endif percentage}
- [ ] Nichts erforderlich
- [ ] {percentage end percentage}

#### F42. Welcher Codeblock erstellt einen Serializer?

```python
from rest_framework import serializers
from .models import Planet
```

- [x] A

```python
class PlanetSerializer(serializers.ModelSerializer):
class Meta:
model=Planet
fields=('name','position', 'mass', 'rings')
```

- [ ] B

```python
from rest_framework import serializers
from .models import Planet
class PlanetSerializer():
class Meta:
fields=('name','position', 'mass', 'rings')
model=Planet
```

- [ ] C

```python
from django.db import serializers
from .models import Planet
class PlanetSerializer(serializers.ModelSerializer):
fields=('name','position', 'mass', 'rings')
model=Sandwich
```

- [ ] D

```python
from django.db import serializers
from .models import Planet
class PlanetSerializer(serializers.ModelSerializer):
class Meta:
fields=('name')
model=Planet
```

#### F43. Welche Klasse ermöglicht es Ihnen, automatisch eine Serializer-Klasse mit Feldern und Validatoren zu erstellen, die den Feldern Ihres Models entsprechen?

- [x] ModelSerializer
- [ ] Model
- [ ] DataSerializer
- [ ] ModelToSerializer

#### F44. Welcher Befehl für den ersten Zugriff auf das integrierte Admin-Tool?

- [ ] django-admin setup
- [ ] django-admin runserver
- [ ] python manage.py createuser
- [x] python manage.py createsuperuser

#### F45. Virtuelle Umgebungen dienen der Verwaltung von Abhängigkeiten. Welche Granularität funktioniert am besten?

- [x] Sie sollten für jedes Django-Projekt eine neue virtualenv einrichten
- [ ] Sie sollten nicht verwendet werden
- [ ] Verwenden Sie dieselbe venv für alle Ihre Django-Arbeiten
- [ ] Verwenden Sie eine neue venv für jede Django-App

#### F46. Was führt verschiedene Django-Befehle aus, wie das Ausführen eines Webservers oder das Erstellen einer App?

- [ ] migrate.py
- [ ] wsgi.py
- [x] manage.py
- [ ] runserver

#### F47. Was sollte laut Django Best Practice "fett" sein?

- [x] Models
- [ ] Controller
- [ ] Programmierer
- [ ] Clients

#### F48. Was ist NICHT Teil von Djangos Design-Philosophie?

- [ ] Lose Kopplung
- [ ] Weniger Code
- [ ] Schnelle Entwicklung
- [x] Implizit über explizit

#### F49. Was ist das Ergebnis dieses Template-Codes?

{% raw %}{{"live long and prosper"|truncatewords:3}}{% endraw %}

- [x] live long and ...
- [ ] live long and
- [ ] Ein Kompilierungsfehler
- [ ] liv

#### F50. Wann lädt dieser Code Daten in den Speicher?

```
1 sandwiches = Sandwich.objects.filter(is_vegan=True)
2 for sandwich in sandwiches:
3   print(sandwich.name + " - " + sandwich.spice_level)
```

- [ ] Zeile 1
- [ ] Es hängt davon ab, wie viele Ergebnisse die Abfrage zurückgibt.
- [ ] Es hängt vom Cache ab.
- [x] Zeile 2

#### F51. Sie erstellen eine Webanwendung mit einem React-Frontend und einem Django-Backend. Wofür müssen Sie bereitstellen?

- [ ] Einen NGINX-Webserver
- [ ] Eine NoSQL-Datenbank
- [ ] Eine größere Festplatte
- [x] CORS-Middleware

#### F52. Um ein vorhandenes Model über einen API-Endpunkt verfügbar zu machen, was müssen Sie implementieren?

- [ ] Eine HTTP-Anfrage
- [ ] Ein JSON-Objekt
- [ ] Eine Abfrage
- [x] Einen Serializer

#### F53. Wie würden Sie Django daran hindern, Datenbanktabellen-Erstellungs- oder Löschoperationen über Migrationen für ein bestimmtes Model durchzuführen?

- [ ] Führen Sie den `migrate`-Befehl mit `--exclude=[model_name]` aus.
- [ ] Verschieben Sie die Modelldefinition aus `models.py` in eine eigene Datei.
- [x] Setzen Sie `managed=False` im Model.
- [ ] Führen Sie den `migrate`-Befehl nicht aus.

#### F54. Welche Methode können Sie verwenden, um zu überprüfen, ob sich Formulardaten geändert haben, wenn Sie eine Formularinstanz verwenden?

- [x] has_changed()
- [ ] its_changed()
- [ ] has_updated()
- [ ] Keine davon

#### F55. Was ist WSGI?

- [ ] Ein Server
- [x] Eine Schnittstellenspezifikation
- [ ] Ein Python-Modul
- [ ] Ein Framework

Referenzlink: https://wsgi.tutorial.codepoint.net/intro

#### F56. Welche generische View sollte zur Anzeige der Titel aller Django Reinhardt-Songs verwendet werden?

- [ ] DetailView
- [ ] TittleView
- [ ] SongView
- [x] ListView

#### F57. Welche Aussage ist am genauesten in Bezug auf die Verwendung der Standard-SQLite-Datenbank auf Ihrer lokalen/Entwicklungsmaschine, aber Postgres in der Produktion?

- [ ] Es besteht eine geringere Chance, Fehler einzuführen, da SQLite bereits out of the box funktioniert
- [ ] Es ist in Ordnung, Sie müssen nur beide Instanzen synchronisiert halten
- [x] Es ist eine schlechte Idee und könnte in Zukunft zu Problemen führen
- [ ] Es ist der effizienteste Weg, ein Projekt zu erstellen

#### F58. Warum möchten Sie möglicherweise einen benutzerdefinierten Model Manager schreiben?

- [ ] Um Datenbankabfragen durchzuführen
- [ ] Um eine Datenbank zum Testen einzurichten
- [x] Um das anfängliche QuerySet zu ändern, das der Manager zurückgibt
- [ ] Um die Ergebnisse zu filtern, die eine Datenbankabfrage zurückgibt

#### F59. Was wird in Django verwendet, um die Daten anzupassen, die an die Templates gesendet werden?

- [ ] Models
- [x] Views
- [ ] Forms
- [ ] Serializers

#### F60. Um die Bedingung zu vervollständigen, womit sollte dieser Codeblock enden?

```shell
% if sparles >= 50 %
  Lots of sparkles!
% elif sparkles == 42 %
  The answer to life, the universe, and everything!
```

- [x] `% endif %`
- [ ] Nichts anderes wird benötigt.
- [ ] `% end%`
- [ ] `% else %`

#### F61. Wann sollten Sie die POST-Methode anstelle der GET-Methode zum Übermitteln von Daten aus einem Formular verwenden?

- [x] Wenn die Daten im Formular sensibel sein könnten
- [ ] Wenn Sie möchten, dass die Daten gecacht werden
- [ ] Wenn Sie Ihren Browser zum Debuggen verwenden möchten
- [ ] Wenn Effizienz wichtig ist

#### F62. Was ist ein Callable, das einen Wert nimmt und einen Fehler auslöst, wenn der Wert einige Kriterien nicht erfüllt?

- [ ] Mediator
- [x] Validator
- [ ] Regulärer Ausdruck
- [ ] Deodorizer

#### F63. Sie laden eine Datei von einem Formular zu Django hoch und möchten die empfangene Datei als Feld auf einem Modellobjekt speichern. Sie können das Dateiobjekt einfach von **\_** einem Feld vom Typ \_\_\*\* im Model zuweisen.

- [ ] request.META; FileField
- [ ] request.FILES; BLOBField
- [x] request.FILES; FileField
- [ ] request.META.Files; CLOBField

#### F64. Welches Python-Modul könnte verwendet werden, um den aktuellen Zustand eines Django-Models in einer Datei zu speichern?

- [x] pickle
- [ ] struct
- [ ] marshal
- [ ] serialize

#### F65. Um eine neue App zu einem bestehenden Django-Projekt hinzuzufügen, müssen Sie den **\_-Abschnitt der \_**-Datei bearbeiten.

- [ ] ALLOWED_HOSTS; settings.py
- [ ] APPS; manage.py
- [x] INSTALLED_APPS; settings.py
- [ ] TEMPLATES; urls.py

#### F66. Was ist kein häufig verwendetes Drittanbieter-Paket für die Authentifizierung?

- [ ] django-guardian
- [ ] django-rest-auth
- [ ] authtoken
- [x] django-rest-framework-jwt

#### F67. Welche Funktion im django.urls-Paket kann Ihnen helfen, hardcodierte URLs zu vermeiden, indem sie eine URL bei gegebenem Namen einer View generiert?

- [ ] get_script_prefix()
- [ ] redirect()
- [x] reverse()
- [ ] resolve()

#### F68. Welche ist eine fiktive HTTP-Anfragemethode?

- [ ] POST
- [ ] PUT
- [x] PAUSE
- [ ] PATCH

#### F69. Welche Hilfsfunktion wird NICHT als Teil des django.shortcuts-Pakets bereitgestellt?

- [x] render_to_request()
- [ ] render()
- [ ] redirect()
- [ ] get_object_or_404()

[Referenz](https://docs.djangoproject.com/en/4.0/topics/http/shortcuts/#:~:text=The%20package%20django.,controlled%20coupling%20for%20convenience's%20sake)

#### F70. Was ist ein nicht standardmäßiger Ort zum Speichern von Templates?

- [x] Auf der Root-Ebene eines Projekts
- [ ] Innerhalb der Anwendung
- [ ] In der Datenbank
- [ ] Auf Github

#### F71. Wenn Sie die 8080 aus dem Befehl python manage.py runserver 8080 weglassen würden, welchen Port würde Django standardmäßig verwenden?

- [ ] 8080
- [ ] 80
- [x] 8000
- [ ] Es würde nicht starten

#### F72. Welche Aussage über Django-Apps ist falsch?

- [x] Eine Django-App ist der Container auf oberster Ebene für eine von Django betriebene Webanwendung.
- [ ] Django-Apps sind kleine Bibliotheken, die einen einzelnen Aspekt eines Projekts darstellen sollen.
- [ ] Jede Django-App sollte eine Sache und nur eine Sache tun.
- [ ] Ein Django-Projekt besteht aus vielen Apps.

#### F73. Welche Zeichen sind in Template-Variablennamen illegal?

- [ ] Unterstriche.
- [ ] Großbuchstaben.
- [x] Satzzeichen.
- [ ] Zahlen.

[Referenz](https://docs.djangoproject.com/en/4.1/ref/templates/language/#:~:text=Variable%20names%20consist%20of%20any,may%20not%20be%20a%20number.)

#### F74. Was ist kein gültiges schließendes Template-Tag?

- [ ] `% endautoescape %`
- [x] `% endifempty %`
- [ ] `% endcomment %`
- [ ] `% endfilter %`

#### F75. Wann müssten Sie die reverse_lazy-Hilfsfunktion anstelle von reverse verwenden?

- [ ] Wenn Sie eine Reverse-URL als Standardwert für einen Parameter in der Signatur einer Funktion bereitstellen möchten
- [x] Alle diese Antworten
- [ ] Wenn Sie eine Reverse-URL als url-Attribut einer klassenbasierten generischen View bereitstellen möchten
- [ ] Wenn Sie eine URL für einen Decorator bereitstellen möchten, wie das login_url-Argument für den permission_required()-Decorator

#### F76. Was ist der Zweck der \_\_init\_\_.py-Datei?

- [ ] Den Satz der in einem Paket gefundenen Module zu erweitern
- [ ] Kompilierte Module aus verschiedenen Versionen und Versionen von Python zu koexistieren
- [ ] Projekteinstellungen zu initialisieren
- [x] Den Verzeichnisinhalt als Python-Modul zu deklarieren

[Referenz](<https://docs.djangoproject.com/en/4.1/ref/urlresolvers/#:~:text=reverse_lazy()&text=It%20is%20useful%20for%20when,a%20generic%20class%2Dbased%20view>)

#### F77. Welches Python-Paket kann verwendet werden, um Zahlen in besser lesbare Form zu bearbeiten, wie "1200000" zu "1.2 Million"?

- [ ] black
- [ ] puffer
- [ ] pitch
- [x] humanize

#### F78. Wo würden Sie die settings.py-Datei finden?

- [x] \[projektname\]/settings.py
- [ ] \[projektname\]/\[projektname\]/settings.py
- [ ] \[PYTHON_ROOT\]/settings.py
- [ ] \[DJANGO_ROOT]/settings.py

#### F79. Was würden Sie schreiben, um die Beziehung zwischen einem Buch und einem Autor zu definieren – vorausgesetzt, ein Buch hat nur einen Autor – in einem Django-Model?

- [x] A

```python
class Author (models.Model):
  name = models. CharField (max_length=100)
class Book(models .Model):
  author = models. ForeignKey (Author, on_delete=models. CASCADE)
```

- [ ] B

```python
class Author (models.Model):
  name = models. CharField(max length=100)
class Book(models .Model):
  author = models. ForeignKey (Author)
```

- [ ] C

```python
class Author (models .Model):
  name = models.CharField (max_length=100)
class Book (models .Author) :
  author = Author. name
```

- [ ] D

```python
class Author (models. Model):
  book = models. ForeignKey (Book, on_delete=models.CASCADE)
class Book(models.Model):
  name = models. CharField (max length=100)
```

#### F80. Welche Methode können Sie verwenden, um zu überprüfen, ob sich Formulardaten geändert haben, wenn Sie eine Form-Instanz verwenden?

- [ ] changed_data()
- [x] has_changed()
- [ ] has_updated()
- [ ] is_modified()

#### F81. Welche Aussage ist am genauesten in Bezug auf die Verwendung der Standard-SQLite-Datenbank auf Ihrer lokalen/Entwicklungsmaschine, aber Postgres in der Produktion?

- [ ] Es ist der effizienteste Weg, ein Projekt zu erstellen
- [ ] Es besteht eine geringere Chance, Fehler einzuführen, da SQLite bereits out of the box funktioniert
- [x] Es ist eine schlechte Idee und könnte in Zukunft zu Problemen führen
- [ ] Es ist in Ordnung, Sie müssen nur beide Instanzen synchronisiert halten

#### F82. Wie handhabt Django URL-Routing?

- [ ] Durch Verwendung von Klassen
- [ ] Durch Verwendung von Funktionen
- [x] Durch Verwendung von regulären Ausdrücken
- [ ] Durch Verwendung von festen Pfaden

#### F83. Was ist der Zweck von Djangos Middleware?

- [ ] Das Datenbankschema zu definieren
- [ ] URL-Routing zu verwalten
- [x] HTTP-Anfragen und -Antworten global zu verarbeiten
- [ ] Benutzeroberflächen zu erstellen

[Referenz](https://medium.com/scalereal/everything-you-need-to-know-about-middleware-in-django-2a3bd3853cd6)

#### F84. Was trifft auf Djangos Object-Relational Mapping (ORM) zu?

- [ ] Es wird verwendet, um URL-Routing in einer Django-Anwendung zu definieren.
- [x] Es ermöglicht Ihnen, die Datenbank mit Python-Code abzufragen.
- [ ] Es wird verwendet, um die Struktur von HTML-Templates zu definieren.
- [ ] Es ist für die Verwaltung der Benutzerauthentifizierung verantwortlich.

#### F85. Was trifft auf Djangos "many-to-many"-Feld in einem Model zu?

- [ ] Es wird verwendet, um eine Eins-zu-Eins-Beziehung zwischen zwei Models zu definieren.
- [ ] Es erstellt eine Fremdschlüsselbeziehung zwischen zwei Models.
- [x] Es ermöglicht, dass mehrere Objekte miteinander verknüpft werden.
- [ ] Es erzwingt eindeutige Einschränkungen für ein Feld.

#### F86. Djangos klassenbasierte generische Views bieten welche Klassen, die gängige Webentwicklungsaufgaben implementieren?

- [ ] Konkrete
- [ ] Thread-sichere
- [x] Abstrakte
- [ ] Dynamische

#### F87. Welche Fähigkeiten benötigen Sie, um eine Reihe von Django-Templates zu pflegen?

- [ ] Template-Syntax
- [x] HTML und Template-Syntax
- [ ] Python, HTML und Template-Syntax
- [ ] Python und Template-Syntax

#### F88. Was ist ein nicht standardmäßiger Ort zum Speichern von Templates?

- [x] Auf der Root-Ebene eines Projekts
- [ ] Innerhalb der Anwendung
- [ ] In der Datenbank
- [ ] Auf Github

#### F89. Wenn Sie die 8080 aus dem Befehl python manage.py runserver 8080 weglassen würden, welchen Port würde Django standardmäßig verwenden?

- [ ] 8080
- [ ] 80
- [x] 8000
- [ ] Es würde nicht starten

#### F90. Was ist der Zweck von Djangos Object-Relational Mapping (ORM)?

- [ ] URL-Routing in einer Django-Anwendung zu definieren.
- [ ] HTTP-Anfragen und -Antworten global zu verarbeiten.
- [x] Python-Objekte auf Datenbanktabellen abzubilden und Datenbankoperationen zu vereinfachen.
- [ ] Benutzeroberflächen zu erstellen.

#### F91. Was bedeutet der Begriff "Migration" in Django?

- [ ] Eine Änderung in der URL-Routing-Konfiguration.
- [x] Der Prozess der Weitergabe von Änderungen, die Sie an Ihren Models vornehmen (Hinzufügen eines Felds, Löschen eines Models usw.), in Ihr Datenbankschema.
- [ ] Eine Möglichkeit, benutzerdefinierte Middleware zu definieren.
- [ ] Der Prozess der Erstellung von HTML-Templates für Ihre Anwendung.

#### F92. Was ist der Zweck von Djangos "context" im Kontext des Renderns von Templates?

- [x] Daten von Ihren Views an Ihre Templates zu übergeben, damit die Daten dynamisch gerendert werden können.
- [ ] URL-Muster für Ihre Anwendung zu definieren.
- [ ] HTTP-Anfragen und -Antworten zu verwalten.
- [ ] Benutzeroberflächen zu erstellen.

#### F93. Was repräsentiert die Django `QuerySet`-Klasse?

- [ ] Eine Python-Klasse zur Definition des URL-Routings in Django.
- [ ] Eine Klasse zur Verwaltung von HTTP-Anfragen und -Antworten.
- [x] Eine von Django durchgeführte Datenbankabfrage, dargestellt in Python.
- [ ] Eine Klasse zur Definition von HTML-Templates.

#### F94. Was ist der Zweck des "collectstatic"-Verwaltungsbefehls in Django?

- [ ] Benutzerdaten für Analysen zu sammeln.
- [ ] Datenbankdatensätze aus mehreren Quellen zu sammeln.
- [x] Alle statischen Dateien (CSS, JavaScript, Bilder) aus jeder Ihrer Anwendungen an einem einzigen Ort zu sammeln.
- [ ] Protokolle zum Debuggen zu sammeln.

#### F95. Wofür wird die Django Admin-Site verwendet?

- [ ] Zur Verwaltung der Benutzerauthentifizierung.
- [ ] Zur Definition des URL-Routings für Django-Anwendungen.
- [x] Zur Bereitstellung einer automatisch generierten Admin-Oberfläche für Ihre Models.
- [ ] Zum Schreiben und Ausführen von Datenbankabfragen.

#### F96. Worauf bezieht sich Djangos "Middleware"?

- [ ] Eine Möglichkeit, Benutzeroberflächen zu erstellen.
- [ ] Eine Datenbankabfrage in Django.
- [x] Eine Möglichkeit, HTTP-Anfragen und -Antworten global zu verarbeiten, bevor sie die View erreichen oder nachdem sie die View verlassen haben.
- [ ] Eine Möglichkeit, URL-Routing in Django zu konfigurieren.

#### F97. Was ist der Hauptzweck von Djangos "Migrationsdateien"?

- [x] Änderungen am Datenbankschema im Laufe der Zeit zu definieren und zu speichern.
- [ ] Statische Dateien wie CSS und JavaScript zu verwalten.
- [ ] URL-Muster zu konfigurieren.
- [ ] HTML-Templates zu erstellen.

#### F98. Welches Authentifizierungssystem bietet Django out of the box?

- [ ] OAuth 2.0
- [x] Benutzerauthentifizierung mit integrierten Benutzermodellen und Views.
- [ ] JWT (JSON Web Tokens)
- [ ] SAML (Security Assertion Markup Language)

#### F99. Worauf bezieht sich das architektonische Muster "Model-View-Controller" (MVC) in Django?

- [ ] Ein Muster zur Definition des URL-Routings.
- [ ] Ein Muster zur Erstellung von HTML-Templates.
- [x] Ein Muster, das die Anwendung in drei miteinander verbundene Komponenten unterteilt: Model, View und Controller (Django bezeichnet es oft als MTV, Model-View-Template).
- [ ] Ein Muster für die Benutzerauthentifizierung.

#### F100. Was ist der Zweck von Djangos "Templates"?

- [ ] Datenbankschema und Modellbeziehungen zu definieren.
- [x] Die Struktur und das Layout von HTML-Seiten zu definieren, die dem Benutzer bereitgestellt werden.
- [ ] URL-Muster für Ihre Anwendung zu konfigurieren.
- [ ] Statische Dateien wie Bilder und JavaScript zu speichern und bereitzustellen.

#### F101. Welche Django ORM-Methode wird verwendet, um ein einzelnes Objekt abzurufen, das den angegebenen Lookup-Parametern entspricht?

- [ ] `get_object_or_404()`
- [x] `get()`
- [ ] `filter()`
- [ ] `values()`

#### F102. Was ist der Zweck der `__str__()`-Methode in einem Django-Model?

- [ ] Die Standardsortierung für Modellinstanzen zu definieren
- [x] Eine für Menschen lesbare String-Darstellung der Modellinstanz bereitzustellen
- [ ] Das Standardfeld zu definieren, das für Lookups verwendet werden soll
- [ ] Das Standard-Anzeigefeld in der Django-Admin-Oberfläche zu definieren

#### F103. Welche Django ORM-Methode wird verwendet, um eine Liste von Objekten abzurufen, die den angegebenen Lookup-Parametern entsprechen?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [x] `filter()`
- [ ] `values()`

#### F104. Was ist der Zweck des `related_name`-Parameters in einem Django-Models `ForeignKey`-Feld?

- [ ] Den Namen der umgekehrten Beziehung im zugehörigen Model zu definieren
- [ ] Die Standardsortierung für die zugehörigen Objekte zu definieren
- [x] Den Namen des Attributs im zugehörigen Model zu definieren, das auf die Menge der zugehörigen Objekte zugreift
- [ ] Den Namen des Attributs im aktuellen Model zu definieren, das auf das zugehörige Objekt zugreift

#### F105. Welche Django ORM-Methode wird verwendet, um eine Liste eindeutiger Werte für die angegebenen Felder abzurufen?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [ ] `filter()`
- [x] `values()`

#### F106. Was ist der Zweck des `unique`-Parameters in einem Django-Modellfeld?

- [ ] Die Standardsortierung für das Feld zu definieren
- [ ] Den Standardwert für das Feld zu definieren
- [x] Sicherzustellen, dass der Wert des Feldes über alle Instanzen des Models eindeutig ist
- [ ] Die maximale Länge des Feldes zu definieren

#### F107. Welche Django ORM-Methode wird verwendet, um ein einzelnes Objekt abzurufen, das den angegebenen Lookup-Parametern entspricht, oder eine `Http404`-Ausnahme auszulösen, wenn kein Objekt gefunden wird?

- [x] `get_object_or_404()`
- [ ] `get()`
- [ ] `filter()`
- [ ] `values()`

#### F108. Was ist der Zweck des `on_delete`-Parameters in einem Django-Models `ForeignKey`-Feld?

- [ ] Den Standardwert für das Feld zu definieren
- [ ] Die maximale Länge des Feldes zu definieren
- [x] Das Verhalten festzulegen, wenn das referenzierte Objekt gelöscht wird
- [ ] Den Namen der umgekehrten Beziehung im zugehörigen Model zu definieren

#### F109. Welche Django ORM-Methode wird verwendet, um Aggregationsoperationen (z.B. `sum()`, `avg()`, `count()`) auf einem QuerySet durchzuführen?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [ ] `filter()`
- [x] `aggregate()`

#### F110. Was ist der Zweck des `related_query_name`-Parameters in einem Django-Models `ForeignKey`-Feld?

- [ ] Den Namen der umgekehrten Beziehung im zugehörigen Model zu definieren
- [x] Den Namen des Attributs im zugehörigen Model zu definieren, das auf die Menge der zugehörigen Objekte zugreift
- [ ] Die Standardsortierung für die zugehörigen Objekte zu definieren
- [ ] Den Namen des Attributs im aktuellen Model zu definieren, das auf das zugehörige Objekt zugreift

#### F111. Welche Django ORM-Methode wird verwendet, um ein neues Objekt zu erstellen und in der Datenbank zu speichern?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [x] `save()`
- [ ] `create()`

#### F112. Was ist der Zweck des `default`-Parameters in einem Django-Modellfeld?

- [ ] Die maximale Länge des Feldes zu definieren
- [x] Den Standardwert für das Feld anzugeben
- [ ] Den Namen der umgekehrten Beziehung im zugehörigen Model zu definieren
- [ ] Sicherzustellen, dass der Wert des Feldes über alle Instanzen des Models eindeutig ist

#### F113. Welche Django ORM-Methode wird verwendet, um eine Liste von Objekten abzurufen, die den angegebenen Lookup-Parametern entsprechen, und sie als Liste von Dictionaries zurückzugeben?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [ ] `filter()`
- [x] `values()`

#### F114. Was ist der Zweck des `null`-Parameters in einem Django-Modellfeld?

- [ ] Die maximale Länge des Feldes zu definieren
- [ ] Sicherzustellen, dass der Wert des Feldes über alle Instanzen des Models eindeutig ist
- [x] Anzugeben, ob das Feld einen Null-Wert haben darf
- [ ] Den Standardwert für das Feld zu definieren

#### F115. Welche Django ORM-Methode wird verwendet, um eine Liste von Objekten abzurufen, die den angegebenen Lookup-Parametern entsprechen, und sie nach einem oder mehreren Feldern zu sortieren?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [x] `order_by()`
- [ ] `values()`

#### F116. Was ist der Zweck des `verbose_name`-Parameters in einem Django-Modellfeld?

- [ ] Die Standardsortierung für das Feld zu definieren
- [ ] Die maximale Länge des Feldes zu definieren
- [x] Einen für Menschen lesbaren Namen für das Feld bereitzustellen
- [ ] Sicherzustellen, dass der Wert des Feldes über alle Instanzen des Models eindeutig ist

#### F117. Welche Django ORM-Methode wird verwendet, um eine Liste von Objekten abzurufen, die den angegebenen Lookup-Parametern entsprechen, und bestimmte Objekte auszuschließen?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [x] `exclude()`
- [ ] `values()`

#### F118. Was ist der Zweck des `on_delete`-Parameters in einem Django-Models `OneToOneField`?

- [ ] Die Standardsortierung für die zugehörigen Objekte zu definieren
- [ ] Den Namen der umgekehrten Beziehung im zugehörigen Model zu definieren
- [x] Das Verhalten festzulegen, wenn das referenzierte Objekt gelöscht wird
- [ ] Den Namen des Attributs im zugehörigen Model zu definieren, das auf die Menge der zugehörigen Objekte zugreift

#### F119. Welche Django ORM-Methode wird verwendet, um eine Liste von Objekten abzurufen, die den angegebenen Lookup-Parametern entsprechen, und sie als Liste von Tupeln zurückzugeben?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [ ] `filter()`
- [x] `values_list()`

#### F120. Was ist der Zweck des `unique_together`-Parameters in einer Django-Model-Meta-Klasse?

- [ ] Die Standardsortierung für das Model zu definieren
- [ ] Die maximale Länge der Felder zu definieren
- [x] Sicherzustellen, dass die Kombination der angegebenen Felder über alle Instanzen des Models eindeutig ist
- [ ] Den Namen der umgekehrten Beziehung im zugehörigen Model zu definieren

#### F121. Welche Django ORM-Methode wird verwendet, um eine Liste von Objekten abzurufen, die den angegebenen Lookup-Parametern entsprechen, und sie als Liste von Modellinstanzen zurückzugeben?

- [x] `all()`
- [ ] `get()`
- [ ] `get_object_or_404()`
- [ ] `values()`

#### F122. Was ist der Zweck des `blank`-Parameters in einem Django-Modellfeld?

- [ ] Den Standardwert für das Feld zu definieren
- [x] Anzugeben, ob das Feld leer gelassen werden darf
- [ ] Sicherzustellen, dass der Wert des Feldes über alle Instanzen des Models eindeutig ist
- [ ] Die maximale Länge des Feldes zu definieren

#### F123. Welche Django ORM-Methode wird verwendet, um eine Liste von Objekten abzurufen, die den angegebenen Lookup-Parametern entsprechen, und sie als Liste von Dictionaries mit den angegebenen Feldern zurückzugeben?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [ ] `filter()`
- [x] `values()`

#### F124. Was ist der Zweck des `default`-Parameters in einem Django-Models `ForeignKey`-Feld?

- [ ] Den Namen der umgekehrten Beziehung im zugehörigen Model zu definieren
- [x] Den Standardwert für das Feld anzugeben
- [ ] Sicherzustellen, dass der Wert des Feldes über alle Instanzen des Models eindeutig ist
- [ ] Die maximale Länge des Feldes zu definieren

#### F125. Welche Django ORM-Methode wird verwendet, um eine Liste von Objekten abzurufen, die den angegebenen Lookup-Parametern entsprechen, und sie als Liste von Tupeln mit den angegebenen Feldern zurückzugeben?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [ ] `filter()`
- [x] `values_list()`

#### F126. Was ist der Zweck des `editable`-Parameters in einem Django-Modellfeld?

- [ ] Die Standardsortierung für das Feld zu definieren
- [ ] Sicherzustellen, dass der Wert des Feldes über alle Instanzen des Models eindeutig ist
- [x] Anzugeben, ob das Feld in Admin-Oberflächen zur Bearbeitung angezeigt werden soll
- [ ] Die maximale Länge des Feldes zu definieren

#### F127. Welche Django ORM-Methode wird verwendet, um eine Liste von Objekten abzurufen, die den angegebenen Lookup-Parametern entsprechen, und sie als Liste von Modellinstanzen mit den angegebenen Feldern zurückzugeben?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [x] `values()`
- [ ] `values_list()`

#### F128. Was ist der Zweck des `choices`-Parameters in einem Django-Modellfeld?

- [ ] Die Standardsortierung für das Feld zu definieren
- [x] Eine Reihe von Auswahlmöglichkeiten für das Feld anzugeben
- [ ] Sicherzustellen, dass der Wert des Feldes über alle Instanzen des Models eindeutig ist
- [ ] Die maximale Länge des Feldes zu definieren

#### F129. Welche Django ORM-Methode wird verwendet, um eine Liste von Objekten abzurufen, die den angegebenen Lookup-Parametern entsprechen, und sie als Liste von Tupeln mit den angegebenen Feldern in einer bestimmten Reihenfolge zurückzugeben?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [ ] `values()`
- [x] `values_list()`

#### F130. Was ist der Zweck des `db_index`-Parameters in einem Django-Modellfeld?

- [ ] Die Standardsortierung für das Feld zu definieren
- [x] Einen Datenbankindex für das Feld zu erstellen
- [ ] Sicherzustellen, dass der Wert des Feldes über alle Instanzen des Models eindeutig ist
- [ ] Die maximale Länge des Feldes zu definieren

#### F131. Welche Django ORM-Methode wird verwendet, um eine Liste von Objekten abzurufen, die den angegebenen Lookup-Parametern entsprechen, und sie als Liste von Modellinstanzen mit den angegebenen Feldern zurückzugeben?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [x] `values()`
- [ ] `values_list()`

#### F132. Was ist der Zweck der Parameter `unique_for_date`, `unique_for_month` und `unique_for_year` in einem Django-Modellfeld?

- [ ] Die Standardsortierung für das Feld zu definieren
- [x] Sicherzustellen, dass der Wert des Feldes für das angegebene Datum, den Monat oder das Jahr eindeutig ist
- [ ] Einen Datenbankindex für das Feld zu erstellen
- [ ] Die maximale Länge des Feldes zu definieren

#### F133. Welche Django ORM-Methode wird verwendet, um eine Liste von Objekten abzurufen, die den angegebenen Lookup-Parametern entsprechen, und sie als Liste von Tupeln mit den angegebenen Feldern in einer bestimmten Reihenfolge zurückzugeben?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [ ] `values()`
- [x] `values_list()`

#### F134. Was ist der Zweck des `help_text`-Parameters in einem Django-Modellfeld?

- [ ] Die Standardsortierung für das Feld zu definieren
- [x] Zusätzliche Informationen über das Feld bereitzustellen, die in Admin-Oberflächen angezeigt werden
- [ ] Sicherzustellen, dass der Wert des Feldes über alle Instanzen des Models eindeutig ist
- [ ] Die maximale Länge des Feldes zu definieren

#### F135. Welche Django ORM-Methode wird verwendet, um eine Liste von Objekten abzurufen, die den angegebenen Lookup-Parametern entsprechen, und sie als Liste von Modellinstanzen mit den angegebenen Feldern zurückzugeben?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [x] `values()`
- [ ] `values_list()`

#### F136. Was ist der Zweck des `verbose_name_plural`-Parameters in einer Django-Model-Meta-Klasse?

- [ ] Die Standardsortierung für das Model zu definieren
- [ ] Einen Datenbankindex für das Model zu erstellen
- [x] Einen für Menschen lesbaren Plural-Namen für das Model bereitzustellen
- [ ] Sicherzustellen, dass die Kombination der angegebenen Felder über alle Instanzen des Models eindeutig ist

#### F137. Welche Django ORM-Methode wird verwendet, um eine Liste von Objekten abzurufen, die den angegebenen Lookup-Parametern entsprechen, und sie als Liste von Tupeln mit den angegebenen Feldern in einer bestimmten Reihenfolge zurückzugeben?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [ ] `values()`
- [x] `values_list()`

#### F138. Was ist der Zweck der Parameter `auto_now` und `auto_now_add` in einem Django-Model-`DateField` oder `DateTimeField`?

- [ ] Die Standardsortierung für das Feld zu definieren
- [x] Das Feld automatisch auf das aktuelle Datum/die aktuelle Uhrzeit zu setzen, wenn das Objekt gespeichert oder erstellt wird
- [ ] Sicherzustellen, dass der Wert des Feldes über alle Instanzen des Models eindeutig ist
- [ ] Die maximale Länge des Feldes zu definieren

#### F139. Welche Django ORM-Methode wird verwendet, um eine Liste von Objekten abzurufen, die den angegebenen Lookup-Parametern entsprechen, und sie als Liste von Modellinstanzen mit den angegebenen Feldern zurückzugeben?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [x] `values()`
- [ ] `values_list()`

#### F140. Was ist der Zweck des `related_name`-Parameters in einem Django-Models `ManyToManyField`?

- [ ] Die Standardsortierung für die zugehörigen Objekte zu definieren
- [x] Den Namen des Attributs im zugehörigen Model zu definieren, das auf die Menge der zugehörigen Objekte zugreift
- [ ] Sicherzustellen, dass die Kombination der angegebenen Felder über alle Instanzen des Models eindeutig ist
- [ ] Die maximale Länge des Feldes zu definieren

#### F141. Welche Django ORM-Methode wird verwendet, um eine Liste von Objekten abzurufen, die den angegebenen Lookup-Parametern entsprechen, und sie als Liste von Tupeln mit den angegebenen Feldern in einer bestimmten Reihenfolge zurückzugeben?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [ ] `values()`
- [x] `values_list()`

#### F142. Was ist der Zweck des `on_delete`-Parameters in einem Django-Models `ManyToManyField`?

- [ ] Die Standardsortierung für die zugehörigen Objekte zu definieren
- [ ] Den Namen des Attributs im zugehörigen Model zu definieren, das auf die Menge der zugehörigen Objekte zugreift
- [x] Das Verhalten festzulegen, wenn das referenzierte Objekt gelöscht wird
- [ ] Die maximale Länge des Feldes zu definieren

#### F143. Welche Django ORM-Methode wird verwendet, um eine Liste von Objekten abzurufen, die den angegebenen Lookup-Parametern entsprechen, und sie als Liste von Modellinstanzen mit den angegebenen Feldern zurückzugeben?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [x] `values()`
- [ ] `values_list()`

#### F144. Was ist der Zweck des `default`-Parameters in einem Django-Models `ManyToManyField`?

- [ ] Die Standardsortierung für die zugehörigen Objekte zu definieren
- [x] Den Standardwert für das Feld anzugeben
- [ ] Sicherzustellen, dass die Kombination der angegebenen Felder über alle Instanzen des Models eindeutig ist
- [ ] Die maximale Länge des Feldes zu definieren

#### F145. Welche Django ORM-Methode wird verwendet, um eine Liste von Objekten abzurufen, die den angegebenen Lookup-Parametern entsprechen, und sie als Liste von Tupeln mit den angegebenen Feldern in einer bestimmten Reihenfolge zurückzugeben?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [ ] `values()`
- [x] `values_list()`

#### F146. Was ist der Zweck des `null`-Parameters in einem Django-Models `ForeignKey`-Feld?

- [ ] Die Standardsortierung für die zugehörigen Objekte zu definieren
- [x] Anzugeben, ob das Feld einen Null-Wert haben darf
- [ ] Sicherzustellen, dass die Kombination der angegebenen Felder über alle Instanzen des Models eindeutig ist
- [ ] Die maximale Länge des Feldes zu definieren

#### F147. Welche Django ORM-Methode wird verwendet, um eine Liste von Objekten abzurufen, die den angegebenen Lookup-Parametern entsprechen, und sie als Liste von Modellinstanzen mit den angegebenen Feldern zurückzugeben?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [x] `values()`
- [ ] `values_list()`

#### F148. Was ist der Zweck des `db_column`-Parameters in einem Django-Modellfeld?

- [ ] Die Standardsortierung für das Feld zu definieren
- [x] Den Namen der Datenbankspalte für das Feld anzugeben
- [ ] Sicherzustellen, dass der Wert des Feldes über alle Instanzen des Models eindeutig ist
- [ ] Die maximale Länge des Feldes zu definieren

#### F149. Welche Django ORM-Methode wird verwendet, um eine Liste von Objekten abzurufen, die den angegebenen Lookup-Parametern entsprechen, und sie als Liste von Tupeln mit den angegebenen Feldern in einer bestimmten Reihenfolge zurückzugeben?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [ ] `values()`
- [x] `values_list()`

#### F150. Was ist der Zweck des `db_table`-Parameters in einer Django-Model-Meta-Klasse?

- [ ] Die Standardsortierung für das Model zu definieren
- [x] Den Namen der Datenbanktabelle anzugeben

#### F151. Welches Django-Formularfeld wird verwendet, um zu validieren, dass die Eingabe eines Benutzers eine gültige E-Mail-Adresse ist?

- [ ] EmailField
- [x] EmailField
- [ ] CharField(validators=[validate_email])
- [ ] EmailInput

#### F152. Was ist der Zweck der Verwendung der `is_valid()`-Methode bei einem Django-Formular?

- [ ] Zu prüfen, ob das Formular abgeschickt wurde
- [ ] Die Formulardaten in der Datenbank zu speichern
- [x] Die Formulardaten zu validieren und zu prüfen, ob sie korrekt sind
- [ ] Das Formular-HTML zu rendern

#### F153. Wann würden Sie ein `ModelForm` anstelle eines regulären Django-`Form` verwenden?

- [ ] Wenn Sie ein Formular erstellen möchten, das nicht an ein Datenbankmodell gebunden ist
- [ ] Wenn Sie benutzerdefinierte Validierungsregeln zu Ihrem Formular hinzufügen möchten
- [ ] Wenn Sie das Formular mit einem benutzerdefinierten Template rendern möchten
- [x] Wenn Sie ein Formular erstellen möchten, das direkt an ein Datenbankmodell gebunden ist

#### F154. Wie können Sie das Rendering eines Django-Formularfelds anpassen?

- [ ] Durch Überschreiben der `as_p()`-Methode des Formulars
- [ ] Durch Erstellen einer benutzerdefinierten Formularfeld-Klasse
- [x] Durch Verwendung des `widgets`-Parameters bei der Definition des Formularfelds
- [ ] Durch Ändern des Templates, das das Formular rendert

#### F155. Was ist der Zweck des `cleaned_data`-Dictionaries in einem Django-Formular?

- [ ] Es enthält die rohen, nicht validierten Daten, die vom Benutzer übermittelt wurden
- [ ] Es enthält die HTML-escaped Formulardaten
- [x] Es enthält die validierten und bereinigten Daten aus dem Formular
- [ ] Es enthält die Standardwerte für die Formularfelder

#### F156. Wie können Sie benutzerdefinierte Validierungsregeln zu einem Django-Formularfeld hinzufügen?

- [ ] Durch Überschreiben der `clean()`-Methode des Formulars
- [ ] Durch Hinzufügen eines `validators`-Parameters zur Formularfelddefinition
- [x] Durch sowohl Überschreiben der `clean()`-Methode als auch Hinzufügen eines `validators`-Parameters
- [ ] Durch Erstellen einer benutzerdefinierten Formularfeld-Klasse und Hinzufügen der Validierungslogik dort

#### F157. Was ist der Zweck des `form.is_bound`-Attributs in einem Django-Formular?

- [ ] Es zeigt an, ob das Formular abgeschickt wurde
- [x] Es zeigt an, ob das Formular mit Daten abgeschickt wurde
- [ ] Es zeigt an, ob das Formular in der Datenbank gespeichert wurde
- [ ] Es zeigt an, ob das Formular auf der Seite gerendert wurde

#### F158. Wie können Sie die HTML-Ausgabe eines Django-Formularfelds anpassen?

- [ ] Durch Überschreiben der `as_p()`, `as_ul()` oder `as_table()`-Methoden des Formulars
- [ ] Durch Erstellen einer benutzerdefinierten Widget-Klasse und Verwendung in der Formularfelddefinition
- [x] Durch sowohl Überschreiben der Formularfeld-Rendering-Methoden als auch Verwendung benutzerdefinierter Widgets
- [ ] Durch Ändern des Templates, das das Formular rendert

#### F159. Was ist der Zweck des `required`-Parameters bei der Definition eines Django-Formularfelds?

- [ ] Er setzt den Standardwert des Feldes
- [ ] Er fügt dem Feld benutzerdefinierte Validierungslogik hinzu
- [x] Er macht das Feld erforderlich, damit das Formular gültig ist
- [ ] Er ändert das HTML-Rendering des Feldes

#### F160. Wie können Sie benutzerdefinierte Fehlermeldungen zu einem Django-Formularfeld hinzufügen?

- [ ] Durch Setzen des `error_messages`-Parameters bei der Definition des Formularfelds
- [ ] Durch Überschreiben der `clean()`-Methode des Formulars und Auslösen eines `ValidationError`
- [x] Durch Verwendung sowohl des `error_messages`-Parameters als auch Überschreiben der `clean()`-Methode
- [ ] Durch Ändern des Templates, das das Formular rendert

#### F161. Was ist der Zweck des `label`-Parameters bei der Definition eines Django-Formularfelds?

- [ ] Er setzt den Standardwert des Feldes
- [x] Er setzt den Label-Text, der für das Feld angezeigt wird
- [ ] Er fügt dem Feld benutzerdefinierte Validierungslogik hinzu
- [ ] Er ändert das HTML-Rendering des Feldes

#### F162. Wie können Sie die Ausgangsdaten in einem Django-Formular vorab ausfüllen?

- [ ] Durch Setzen des `initial`-Parameters bei der Definition der Formularfelder
- [ ] Durch Übergeben der Ausgangsdaten als Teil der `request.POST`-Daten
- [x] Durch Übergeben der Ausgangsdaten als `data`-Parameter beim Erstellen der Formularinstanz
- [ ] Durch Überschreiben der `get_initial()`-Methode der Formularklasse

#### F163. Was ist der Zweck des `widget`-Parameters bei der Definition eines Django-Formularfelds?

- [ ] Er setzt den Standardwert des Feldes
- [ ] Er fügt dem Feld benutzerdefinierte Validierungslogik hinzu
- [x] Er gibt das HTML-Widget an, das zum Rendern des Feldes verwendet werden soll
- [ ] Er ändert den Label-Text, der für das Feld angezeigt wird

#### F164. Wie können Sie die HTML-Attribute eines Django-Formularfelds anpassen?

- [ ] Durch Setzen des `attrs`-Parameters bei der Definition des Formularfelds
- [ ] Durch Überschreiben der `as_widget()`-Methode des Formularfelds
- [x] Durch Verwendung sowohl des `attrs`-Parameters als auch Überschreiben von `as_widget()`
- [ ] Durch Ändern des Templates, das das Formular rendert

#### F165. Was ist der Zweck des `help_text`-Parameters bei der Definition eines Django-Formularfelds?

- [ ] Er setzt den Standardwert des Feldes
- [x] Er bietet zusätzlichen erklärenden Text für das Feld
- [ ] Er fügt dem Feld benutzerdefinierte Validierungslogik hinzu
- [ ] Er ändert das HTML-Rendering des Feldes

#### F166. Wie können Sie benutzerdefinierte Validierungslogik zu einem Django-Formularfeld hinzufügen?

- [ ] Durch Setzen des `validators`-Parameters bei der Definition des Formularfelds
- [ ] Durch Überschreiben der `clean()`-Methode des Formularfelds
- [x] Durch Verwendung sowohl des `validators`-Parameters als auch Überschreiben von `clean()`
- [ ] Durch Ändern des Templates, das das Formular rendert

#### F167. Was ist der Zweck des `required`-Parameters bei der Definition eines Django-Formularfelds?

- [ ] Er setzt den Standardwert des Feldes
- [ ] Er fügt dem Feld benutzerdefinierte Validierungslogik hinzu
- [x] Er macht das Feld erforderlich, damit das Formular gültig ist
- [ ] Er ändert das HTML-Rendering des Feldes

#### F168. Wie können Sie die für ein Django-Formularfeld angezeigten Fehlermeldungen anpassen?

- [ ] Durch Setzen des `error_messages`-Parameters bei der Definition des Formularfelds
- [ ] Durch Überschreiben der `clean()`-Methode des Formularfelds und Auslösen eines `ValidationError`
- [x] Durch Verwendung sowohl des `error_messages`-Parameters als auch Überschreiben von `clean()`
- [ ] Durch Ändern des Templates, das das Formular rendert

#### F169. Was ist der Zweck des `label`-Parameters bei der Definition eines Django-Formularfelds?

- [ ] Er setzt den Standardwert des Feldes
- [x] Er setzt den Label-Text, der für das Feld angezeigt wird
- [ ] Er fügt dem Feld benutzerdefinierte Validierungslogik hinzu
- [ ] Er ändert das HTML-Rendering des Feldes

#### F170. Wie können Sie die Ausgangsdaten in einem Django-Formular vorab ausfüllen?

- [ ] Durch Setzen des `initial`-Parameters bei der Definition der Formularfelder
- [ ] Durch Übergeben der Ausgangsdaten als Teil der `request.POST`-Daten
- [x] Durch Übergeben der Ausgangsdaten als `data`-Parameter beim Erstellen der Formularinstanz
- [ ] Durch Überschreiben der `get_initial()`-Methode der Formularklasse

#### F171. Was ist der Zweck des `widget`-Parameters bei der Definition eines Django-Formularfelds?

- [ ] Er setzt den Standardwert des Feldes
- [ ] Er fügt dem Feld benutzerdefinierte Validierungslogik hinzu
- [x] Er gibt das HTML-Widget an, das zum Rendern des Feldes verwendet werden soll
- [ ] Er ändert den Label-Text, der für das Feld angezeigt wird

#### F172. Wie können Sie die HTML-Attribute eines Django-Formularfelds anpassen?

- [ ] Durch Setzen des `attrs`-Parameters bei der Definition des Formularfelds
- [ ] Durch Überschreiben der `as_widget()`-Methode des Formularfelds
- [x] Durch Verwendung sowohl des `attrs`-Parameters als auch Überschreiben von `as_widget()`
- [ ] Durch Ändern des Templates, das das Formular rendert

#### F173. Was ist der Zweck des `help_text`-Parameters bei der Definition eines Django-Formularfelds?

- [ ] Er setzt den Standardwert des Feldes
- [x] Er bietet zusätzlichen erklärenden Text für das Feld
- [ ] Er fügt dem Feld benutzerdefinierte Validierungslogik hinzu
- [ ] Er ändert das HTML-Rendering des Feldes

#### F174. Wie können Sie benutzerdefinierte Validierungslogik zu einem Django-Formularfeld hinzufügen?

- [ ] Durch Setzen des `validators`-Parameters bei der Definition des Formularfelds
- [ ] Durch Überschreiben der `clean()`-Methode des Formularfelds
- [x] Durch Verwendung sowohl des `validators`-Parameters als auch Überschreiben von `clean()`
- [ ] Durch Ändern des Templates, das das Formular rendert

#### F175. Was ist der Zweck des `max_length`-Parameters bei der Definition eines Django-CharField-Formularfelds?

- [ ] Er setzt den Standardwert des Feldes
- [ ] Er fügt dem Feld benutzerdefinierte Validierungslogik hinzu
- [x] Er begrenzt die maximale Länge der Benutzereingabe
- [ ] Er ändert das HTML-Rendering des Feldes

#### F176. Wie können Sie die für ein Django-Formularfeld angezeigten Fehlermeldungen anpassen?

- [ ] Durch Setzen des `error_messages`-Parameters bei der Definition des Formularfelds
- [ ] Durch Überschreiben der `clean()`-Methode des Formularfelds und Auslösen eines `ValidationError`
- [x] Durch Verwendung sowohl des `error_messages`-Parameters als auch Überschreiben von `clean()`
- [ ] Durch Ändern des Templates, das das Formular rendert

#### F177. Was ist der Zweck des `required`-Parameters bei der Definition eines Django-Formularfelds?

- [ ] Er setzt den Standardwert des Feldes
- [ ] Er fügt dem Feld benutzerdefinierte Validierungslogik hinzu
- [x] Er macht das Feld erforderlich, damit das Formular gültig ist
- [ ] Er ändert das HTML-Rendering des Feldes

#### F178. Wie können Sie die Ausgangsdaten in einem Django-Formular vorab ausfüllen?

- [ ] Durch Setzen des `initial`-Parameters bei der Definition der Formularfelder
- [ ] Durch Übergeben der Ausgangsdaten als Teil der `request.POST`-Daten
- [x] Durch Übergeben der Ausgangsdaten als `data`-Parameter beim Erstellen der Formularinstanz
- [ ] Durch Überschreiben der `get_initial()`-Methode der Formularklasse

#### F179. Was ist der Zweck des `widget`-Parameters bei der Definition eines Django-Formularfelds?

- [ ] Er setzt den Standardwert des Feldes
- [ ] Er fügt dem Feld benutzerdefinierte Validierungslogik hinzu
- [x] Er gibt das HTML-Widget an, das zum Rendern des Feldes verwendet werden soll
- [ ] Er ändert den Label-Text, der für das Feld angezeigt wird

#### F180. Wie können Sie die HTML-Attribute eines Django-Formularfelds anpassen?

- [ ] Durch Setzen des `attrs`-Parameters bei der Definition des Formularfelds
- [ ] Durch Überschreiben der `as_widget()`-Methode des Formularfelds
- [x] Durch Verwendung sowohl des `attrs`-Parameters als auch Überschreiben von `as_widget()`
- [ ] Durch Ändern des Templates, das das Formular rendert

#### F181. Was ist der Zweck des `help_text`-Parameters bei der Definition eines Django-Formularfelds?

- [ ] Er setzt den Standardwert des Feldes
- [x] Er bietet zusätzlichen erklärenden Text für das Feld
- [ ] Er fügt dem Feld benutzerdefinierte Validierungslogik hinzu
- [ ] Er ändert das HTML-Rendering des Feldes

#### F182. Wie können Sie benutzerdefinierte Validierungslogik zu einem Django-Formularfeld hinzufügen?

- [ ] Durch Setzen des `validators`-Parameters bei der Definition des Formularfelds
- [ ] Durch Überschreiben der `clean()`-Methode des Formularfelds
- [x] Durch Verwendung sowohl des `validators`-Parameters als auch Überschreiben von `clean()`
- [ ] Durch Ändern des Templates, das das Formular rendert

#### F183. Was ist der Zweck des `max_length`-Parameters bei der Definition eines Django-CharField-Formularfelds?

- [ ] Er setzt den Standardwert des Feldes
- [ ] Er fügt dem Feld benutzerdefinierte Validierungslogik hinzu
- [x] Er begrenzt die maximale Länge der Benutzereingabe
- [ ] Er ändert das HTML-Rendering des Feldes

#### F184. Wie können Sie die für ein Django-Formularfeld angezeigten Fehlermeldungen anpassen?

- [ ] Durch Setzen des `error_messages`-Parameters bei der Definition des Formularfelds
- [ ] Durch Überschreiben der `clean()`-Methode des Formularfelds und Auslösen eines `ValidationError`
- [x] Durch Verwendung sowohl des `error_messages`-Parameters als auch Überschreiben von `clean()`
- [ ] Durch Ändern des Templates, das das Formular rendert

#### F185. Was ist der Zweck des `required`-Parameters bei der Definition eines Django-Formularfelds?

- [ ] Er setzt den Standardwert des Feldes
- [ ] Er fügt dem Feld benutzerdefinierte Validierungslogik hinzu
- [x] Er macht das Feld erforderlich, damit das Formular gültig ist
- [ ] Er ändert das HTML-Rendering des Feldes

#### F186. Wie können Sie die Ausgangsdaten in einem Django-Formular vorab ausfüllen?

- [ ] Durch Setzen des `initial`-Parameters bei der Definition der Formularfelder
- [ ] Durch Übergeben der Ausgangsdaten als Teil der `request.POST`-Daten
- [x] Durch Übergeben der Ausgangsdaten als `data`-Parameter beim Erstellen der Formularinstanz
- [ ] Durch Überschreiben der `get_initial()`-Methode der Formularklasse

#### F187. Was ist der Zweck des `widget`-Parameters bei der Definition eines Django-Formularfelds?

- [ ] Er setzt den Standardwert des Feldes
- [ ] Er fügt dem Feld benutzerdefinierte Validierungslogik hinzu
- [x] Er gibt das HTML-Widget an, das zum Rendern des Feldes verwendet werden soll
- [ ] Er ändert den Label-Text, der für das Feld angezeigt wird

#### F188. Wie können Sie die HTML-Attribute eines Django-Formularfelds anpassen?

- [ ] Durch Setzen des `attrs`-Parameters bei der Definition des Formularfelds
- [ ] Durch Überschreiben der `as_widget()`-Methode des Formularfelds
- [x] Durch Verwendung sowohl des `attrs`-Parameters als auch Überschreiben von `as_widget()`
- [ ] Durch Ändern des Templates, das das Formular rendert

#### F189. Was ist der Zweck des `help_text`-Parameters bei der Definition eines Django-Formularfelds?

- [ ] Er setzt den Standardwert des Feldes
- [x] Er bietet zusätzlichen erklärenden Text für das Feld
- [ ] Er fügt dem Feld benutzerdefinierte Validierungslogik hinzu
- [ ] Er ändert das HTML-Rendering des Feldes

#### F190. Wie können Sie benutzerdefinierte Validierungslogik zu einem Django-Formularfeld hinzufügen?

- [ ] Durch Setzen des `validators`-Parameters bei der Definition des Formularfelds
- [ ] Durch Überschreiben der `clean()`-Methode des Formularfelds
- [x] Durch Verwendung sowohl des `validators`-Parameters als auch Überschreiben von `clean()`
- [ ] Durch Ändern des Templates, das das Formular rendert

#### F191. Was ist der Zweck des `max_length`-Parameters bei der Definition eines Django-CharField-Formularfelds?

- [ ] Er setzt den Standardwert des Feldes
- [ ] Er fügt dem Feld benutzerdefinierte Validierungslogik hinzu
- [x] Er begrenzt die maximale Länge der Benutzereingabe
- [ ] Er ändert das HTML-Rendering des Feldes

#### F192. Wie können Sie die für ein Django-Formularfeld angezeigten Fehlermeldungen anpassen?

- [ ] Durch Setzen des `error_messages`-Parameters bei der Definition des Formularfelds
- [ ] Durch Überschreiben der `clean()`-Methode des Formularfelds und Auslösen eines `ValidationError`
- [x] Durch Verwendung sowohl des `error_messages`-Parameters als auch Überschreiben von `clean()`
- [ ] Durch Ändern des Templates, das das Formular rendert

#### F193. Was ist der Zweck des `required`-Parameters bei der Definition eines Django-Formularfelds?

- [ ] Er setzt den Standardwert des Feldes
- [ ] Er fügt dem Feld benutzerdefinierte Validierungslogik hinzu
- [x] Er macht das Feld erforderlich, damit das Formular gültig ist
- [ ] Er ändert das HTML-Rendering des Feldes

#### F194. Wie können Sie die Ausgangsdaten in einem Django-Formular vorab ausfüllen?

- [ ] Durch Setzen des `initial`-Parameters bei der Definition der Formularfelder
- [ ] Durch Übergeben der Ausgangsdaten als Teil der `request.POST`-Daten
- [x] Durch Übergeben der Ausgangsdaten als `data`-Parameter beim Erstellen der Formularinstanz
- [ ] Durch Überschreiben der `get_initial()`-Methode der Formularklasse

#### F195. Was ist der Zweck des `widget`-Parameters bei der Definition eines Django-Formularfelds?

- [ ] Er setzt den Standardwert des Feldes
- [ ] Er fügt dem Feld benutzerdefinierte Validierungslogik hinzu
- [x] Er gibt das HTML-Widget an, das zum Rendern des Feldes verwendet werden soll
- [ ] Er ändert den Label-Text, der für das Feld angezeigt wird

#### F196. Wie können Sie die HTML-Attribute eines Django-Formularfelds anpassen?

- [ ] Durch Setzen des `attrs`-Parameters bei der Definition des Formularfelds
- [ ] Durch Überschreiben der `as_widget()`-Methode des Formularfelds
- [x] Durch Verwendung sowohl des `attrs`-Parameters als auch Überschreiben von `as_widget()`
- [ ] Durch Ändern des Templates, das das Formular rendert

#### F197. Was ist der Zweck des `help_text`-Parameters bei der Definition eines Django-Formularfelds?

- [ ] Er setzt den Standardwert des Feldes
- [x] Er bietet zusätzlichen erklärenden Text für das Feld
- [ ] Er fügt dem Feld benutzerdefinierte Validierungslogik hinzu
- [ ] Er ändert das HTML-Rendering des Feldes

#### F198. Wie können Sie benutzerdefinierte Validierungslogik zu einem Django-Formularfeld hinzufügen?

- [ ] Durch Setzen des `validators`-Parameters bei der Definition des Formularfelds
- [ ] Durch Überschreiben der `clean()`-Methode des Formularfelds
- [x] Durch Verwendung sowohl des `validators`-Parameters als auch Überschreiben von `clean()`
- [ ] Durch Ändern des Templates, das das Formular rendert

#### F199. Was ist der Zweck des `max_length`-Parameters bei der Definition eines Django-CharField-Formularfelds?

- [ ] Er setzt den Standardwert des Feldes
- [ ] Er fügt dem Feld benutzerdefinierte Validierungslogik hinzu
- [x] Er begrenzt die maximale Länge der Benutzereingabe
- [ ] Er ändert das HTML-Rendering des Feldes

#### F200. Wie können Sie die für ein Django-Formularfeld angezeigten Fehlermeldungen anpassen?

#### F351. Welche Django Middleware-Klasse ist für die Handhabung des CSRF-Schutzes verantwortlich?

- [ ] CsrfViewMiddleware
- [x] CsrfViewMiddleware
- [ ] CSRFProtectionMiddleware
- [ ] DjangoCSRFMiddleware

#### F352. Was ist der Zweck der `settings.CACHES`-Konfiguration in Django?

- [ ] Die Standarddatenbank zu konfigurieren, die von der Anwendung verwendet wird
- [ ] Das E-Mail-Backend zu konfigurieren, das von der Anwendung verwendet wird
- [x] Das Cache-Backend zu konfigurieren, das von der Anwendung verwendet wird
- [ ] Das Authentifizierungs-Backend zu konfigurieren, das von der Anwendung verwendet wird

#### F353. Welchen Django-Modell-Feldtyp sollten Sie verwenden, um eine große Menge an Textdaten zu speichern?

- [ ] CharField
- [ ] TextField
- [x] TextField
- [ ] LargeTextField

#### F354. Wie können Sie einen Django-Verwaltungsbefehl aus Ihrem Python-Code heraus ausführen?

- [ ] Mit der `os.system()`-Funktion
- [ ] Mit der `subprocess.call()`-Funktion
- [x] Mit der `call_command()`-Funktion
- [ ] Mit der `django.core.management.execute_from_command_line()`-Funktion

#### F355. Was ist der Zweck der `signal.dispatch()`-Methode in Django?

- [ ] Ein Signal manuell auszulösen
- [x] Ein Signal an alle registrierten Empfänger zu senden
- [ ] Einen Signal-Empfänger zu registrieren
- [ ] Einen Signal-Empfänger abzumelden

#### F356. Welcher Django-View-Funktions-Decorator wird verwendet, um den CSRF-Schutz für eine View zu aktivieren?

- [ ] `@login_required`
- [ ] `@require_http_methods`
- [x] `@csrf_protect`
- [ ] `@ensure_csrf_cookie`

#### F357. Was ist der Zweck des `content_type`-Parameters in der `django.http.HttpResponse`-Klasse?

- [ ] Die Zeichenkodierung der Antwort festzulegen
- [x] Den MIME-Typ der Antwort festzulegen
- [ ] Den HTTP-Statuscode der Antwort festzulegen
- [ ] Den Content-Length-Header der Antwort festzulegen

#### F358. Was ist der Zweck des `@transaction.atomic()`-Decorators in Django?

- [ ] Sicherzustellen, dass eine View-Funktion asynchron ausgeführt wird
- [x] Sicherzustellen, dass eine Reihe von Datenbankoperationen als einzelne Transaktion ausgeführt werden
- [ ] Sicherzustellen, dass eine View-Funktion nur von einem einzelnen Benutzer gleichzeitig ausgeführt wird
- [ ] Sicherzustellen, dass eine View-Funktion nur von einem Benutzer mit den erforderlichen Berechtigungen ausgeführt wird

#### F359. Was ist der Zweck der `settings.ALLOWED_HOSTS`-Konfiguration in Django?

- [ ] Die erlaubten HTTP-Methoden für die Anwendung zu konfigurieren
- [ ] Die erlaubten Dateitypen für Datei-Uploads zu konfigurieren
- [x] Die erlaubten Hostnamen für die Anwendung zu konfigurieren
- [ ] Die erlaubten IP-Adressen für die Anwendung zu konfigurieren

#### F360. Wie können Sie einen benutzerdefinierten Django-Verwaltungsbefehl erstellen?

- [ ] Durch Erstellen eines Python-Moduls mit einer `main()`-Funktion
- [ ] Durch Erstellen eines Python-Moduls mit einer `handle()`-Funktion
- [x] Durch Erstellen einer Python-Klasse, die von `django.core.management.BaseCommand` erbt
- [ ] Durch Erstellen einer Python-Funktion mit dem `@django.core.management.command`-Decorator

#### F361. Was ist der Zweck der `settings.CACHES`-Konfiguration in Django?

- [ ] Die Standarddatenbank zu konfigurieren, die von der Anwendung verwendet wird
- [ ] Das E-Mail-Backend zu konfigurieren, das von der Anwendung verwendet wird
- [x] Das Cache-Backend zu konfigurieren, das von der Anwendung verwendet wird
- [ ] Das Authentifizierungs-Backend zu konfigurieren, das von der Anwendung verwendet wird

#### F362. Wie können Sie Djangos Caching-Framework verwenden, um eine View-Funktion zu cachen?

- [ ] Durch Dekorieren der View-Funktion mit dem `@cache_page()`-Decorator
- [x] Durch Dekorieren der View-Funktion mit dem `@cache_page()`-Decorator
- [ ] Durch Aufrufen der `cache.set()`-Methode in der View-Funktion
- [ ] Durch Konfigurieren der `settings.CACHES`-Einstellung und Aufrufen von `cache.get()` in der View-Funktion

#### F363. Was ist der Zweck der `signal.disconnect()`-Methode in Django?

- [ ] Ein Signal manuell auszulösen
- [ ] Ein Signal an alle registrierten Empfänger zu senden
- [ ] Einen Signal-Empfänger zu registrieren
- [x] Einen Signal-Empfänger abzumelden

#### F364. Was ist der Zweck der `settings.DEBUG`-Konfiguration in Django?

- [ ] Den CSRF-Schutz für die Anwendung zu aktivieren oder zu deaktivieren
- [x] Den Debug-Modus für die Anwendung zu aktivieren oder zu deaktivieren
- [ ] Das Caching für die Anwendung zu aktivieren oder zu deaktivieren
- [ ] Das Logging für die Anwendung zu aktivieren oder zu deaktivieren

#### F365. Wie können Sie den Django-Test-Client verwenden, um eine Benutzeranmeldung zu simulieren?

- [ ] Durch Aufrufen der `client.login()`-Methode mit den Anmeldedaten des Benutzers
- [ ] Durch Setzen der `settings.AUTH_USER_MODEL`-Konfiguration
- [x] Durch Aufrufen der `client.force_login()`-Methode mit dem Benutzerobjekt
- [ ] Durch Setzen des `request.user`-Attributs im Testfall

#### F366. Was ist der Zweck der `settings.MIDDLEWARE`-Konfiguration in Django?

- [ ] Die Standarddatenbank zu konfigurieren, die von der Anwendung verwendet wird
- [x] Die Middleware-Klassen zu konfigurieren, die von der Anwendung verwendet werden
- [ ] Das Caching-Backend zu konfigurieren, das von der Anwendung verwendet wird
- [ ] Das Authentifizierungs-Backend zu konfigurieren, das von der Anwendung verwendet wird

#### F367. Wie können Sie Djangos Caching-Framework verwenden, um die Antwort einer View-Funktion zu cachen?

- [ ] Durch Dekorieren der View-Funktion mit dem `@cache_page()`-Decorator
- [x] Durch Dekorieren der View-Funktion mit dem `@cache_page()`-Decorator
- [ ] Durch Aufrufen der `cache.set()`-Methode in der View-Funktion
- [ ] Durch Konfigurieren der `settings.CACHES`-Einstellung und Aufrufen von `cache.get()` in der View-Funktion

#### F368. Was ist der Zweck der `settings.CSRF_TRUSTED_ORIGINS`-Konfiguration in Django?

- [ ] Die erlaubten Hostnamen für die Anwendung zu konfigurieren
- [x] Die vertrauenswürdigen Ursprungs-Domains für den CSRF-Schutz zu konfigurieren
- [ ] Die erlaubten Dateitypen für Datei-Uploads zu konfigurieren
- [ ] Die erlaubten IP-Adressen für die Anwendung zu konfigurieren

#### F369. Wie können Sie den Django-Test-Client verwenden, um eine POST-Anfrage mit Formulardaten zu simulieren?

- [ ] Durch Aufrufen der `client.post()`-Methode mit den Formulardaten als Dictionary
- [ ] Durch Setzen des `request.POST`-Attributs im Testfall
- [x] Durch Aufrufen der `client.post()`-Methode mit den Formulardaten als Dictionary
- [ ] Durch Aufrufen der `client.request()`-Methode mit den Formulardaten als Dictionary

#### F370. Was ist der Zweck der `django.core.mail.send_mail()`-Funktion?

- [ ] Einen Dateianhang zu senden
- [ ] Eine HTML-E-Mail zu senden
- [x] Eine Klartext-E-Mail zu senden
- [ ] Eine mehrteilige E-Mail zu senden

#### F371. Wie können Sie Djangos `@login_required`-Decorator verwenden, um den Zugriff auf eine View-Funktion einzuschränken?

- [ ] Durch Dekorieren der View-Funktion mit dem `@login_required`-Decorator
- [x] Durch Dekorieren der View-Funktion mit dem `@login_required`-Decorator
- [ ] Durch Aufrufen der `request.user.is_authenticated`-Methode in der View-Funktion
- [ ] Durch Setzen der `settings.LOGIN_URL`-Konfiguration

#### F372. Was ist der Zweck der `settings.STATIC_ROOT`-Konfiguration in Django?

- [ ] Das Verzeichnis zu konfigurieren, aus dem statische Dateien bereitgestellt werden
- [x] Das Verzeichnis zu konfigurieren, in dem statische Dateien für die Bereitstellung gesammelt werden
- [ ] Das Verzeichnis zu konfigurieren, in dem hochgeladene Mediendateien gespeichert werden
- [ ] Das Verzeichnis zu konfigurieren, in dem sich der Django-Anwendungscode befindet

#### F373. Wie können Sie den Django-Test-Client verwenden, um eine Benutzerabmeldung zu simulieren?

- [ ] Durch Aufrufen der `client.logout()`-Methode
- [x] Durch Aufrufen der `client.session.flush()`-Methode
- [ ] Durch Setzen des `request.user`-Attributs auf `AnonymousUser`
- [ ] Durch Setzen der `settings.LOGOUT_URL`-Konfiguration

#### F374. Was ist der Zweck der `settings.EMAIL_BACKEND`-Konfiguration in Django?

- [ ] Die Standarddatenbank zu konfigurieren, die von der Anwendung verwendet wird
- [ ] Das Cache-Backend zu konfigurieren, das von der Anwendung verwendet wird
- [x] Das E-Mail-Backend zu konfigurieren, das von der Anwendung verwendet wird
- [ ] Das Authentifizierungs-Backend zu konfigurieren, das von der Anwendung verwendet wird

#### F375. Wie können Sie den Django-Test-Client verwenden, um eine Benutzeranmeldung mit einem bestimmten Benutzerobjekt zu simulieren?

- [ ] Durch Aufrufen der `client.login()`-Methode mit den Anmeldedaten des Benutzers
- [ ] Durch Setzen der `settings.AUTH_USER_MODEL`-Konfiguration
- [x] Durch Aufrufen der `client.force_login()`-Methode mit dem Benutzerobjekt
- [ ] Durch Setzen des `request.user`-Attributs im Testfall

#### F376. Was ist der Zweck der `settings.MEDIA_ROOT`-Konfiguration in Django?

- [ ] Das Verzeichnis zu konfigurieren, aus dem statische Dateien bereitgestellt werden
- [ ] Das Verzeichnis zu konfigurieren, in dem statische Dateien für die Bereitstellung gesammelt werden
- [x] Das Verzeichnis zu konfigurieren, in dem hochgeladene Mediendateien gespeichert werden
- [ ] Das Verzeichnis zu konfigurieren, in dem sich der Django-Anwendungscode befindet

#### F377. Wie können Sie den Django-Test-Client verwenden, um eine GET-Anfrage mit Abfrageparametern zu simulieren?

- [ ] Durch Aufrufen der `client.post()`-Methode mit den Abfrageparametern als Dictionary
- [ ] Durch Setzen des `request.GET`-Attributs im Testfall
- [x] Durch Aufrufen der `client.get()`-Methode mit den Abfrageparametern als Dictionary
- [ ] Durch Aufrufen der `client.request()`-Methode mit den Abfrageparametern als Dictionary

#### F378. Was ist der Zweck der `settings.SECRET_KEY`-Konfiguration in Django?

- [ ] Die Standarddatenbank zu konfigurieren, die von der Anwendung verwendet wird
- [ ] Das Cache-Backend zu konfigurieren, das von der Anwendung verwendet wird
- [ ] Das E-Mail-Backend zu konfigurieren, das von der Anwendung verwendet wird
- [x] Den geheimen Schlüssel zu konfigurieren, der für kryptographische Signaturen verwendet wird

#### F379. Wie können Sie den Django-Test-Client verwenden, um eine Benutzeranmeldung mit einem bestimmten Benutzerobjekt zu simulieren?

- [ ] Durch Aufrufen der `client.login()`-Methode mit den Anmeldedaten des Benutzers
- [ ] Durch Setzen der `settings.AUTH_USER_MODEL`-Konfiguration
- [x] Durch Aufrufen der `client.force_login()`-Methode mit dem Benutzerobjekt
- [ ] Durch Setzen des `request.user`-Attributs im Testfall

#### F380. Was ist der Zweck der `settings.LOGGING`-Konfiguration in Django?

- [ ] Die Standarddatenbank zu konfigurieren, die von der Anwendung verwendet wird
- [ ] Das Cache-Backend zu konfigurieren, das von der Anwendung verwendet wird
- [x] Die Logging-Einstellungen für die Anwendung zu konfigurieren
- [ ] Das E-Mail-Backend zu konfigurieren, das von der Anwendung verwendet wird

#### F381. Wie können Sie den Django-Test-Client verwenden, um eine POST-Anfrage mit Dateidaten zu simulieren?

- [ ] Durch Aufrufen der `client.post()`-Methode mit den Dateidaten als Dictionary
- [ ] Durch Setzen des `request.FILES`-Attributs im Testfall
- [x] Durch Aufrufen der `client.post()`-Methode mit den Dateidaten als Dictionary
- [ ] Durch Aufrufen der `client.request()`-Methode mit den Dateidaten als Dictionary

#### F382. Was ist der Zweck der `settings.SECURE_BROWSER_XSS_FILTER`-Konfiguration in Django?

- [ ] Die erlaubten Hostnamen für die Anwendung zu konfigurieren
- [ ] Die vertrauenswürdigen Ursprungs-Domains für den CSRF-Schutz zu konfigurieren
- [x] Den X-XSS-Protection HTTP-Header für Cross-Site-Scripting-Schutz zu aktivieren
- [ ] Die erlaubten Dateitypen für Datei-Uploads zu konfigurieren

#### F383. Wie können Sie den Django-Test-Client verwenden, um eine Benutzerabmeldung zu simulieren?

- [ ] Durch Aufrufen der `client.logout()`-Methode
- [x] Durch Aufrufen der `client.session.flush()`-Methode
- [ ] Durch Setzen des `request.user`-Attributs auf `AnonymousUser`
- [ ] Durch Setzen der `settings.LOGOUT_URL`-Konfiguration

#### F384. Was ist der Zweck der `settings.SECURE_SSL_REDIRECT`-Konfiguration in Django?

- [ ] Die erlaubten Hostnamen für die Anwendung zu konfigurieren
- [x] HTTPS-Weiterleitung für die Anwendung zu aktivieren
- [ ] Die vertrauenswürdigen Ursprungs-Domains für den CSRF-Schutz zu konfigurieren
- [ ] Die erlaubten Dateitypen für Datei-Uploads zu konfigurieren

#### F385. Wie können Sie den Django-Test-Client verwenden, um eine GET-Anfrage mit Abfrageparametern zu simulieren?

- [ ] Durch Aufrufen der `client.post()`-Methode mit den Abfrageparametern als Dictionary
- [ ] Durch Setzen des `request.GET`-Attributs im Testfall
- [x] Durch Aufrufen der `client.get()`-Methode mit den Abfrageparametern als Dictionary
- [ ] Durch Aufrufen der `client.request()`-Methode mit den Abfrageparametern als Dictionary

#### F386. Was ist der Zweck der `settings.SECURE_HSTS_SECONDS`-Konfiguration in Django?

- [ ] Die erlaubten Hostnamen für die Anwendung zu konfigurieren
- [x] Den HTTP Strict Transport Security (HSTS)-Header zu aktivieren
- [ ] Die vertrauenswürdigen Ursprungs-Domains für den CSRF-Schutz zu konfigurieren
- [ ] Die erlaubten Dateitypen für Datei-Uploads zu konfigurieren

#### F387. Wie können Sie den Django-Test-Client verwenden, um eine POST-Anfrage mit Dateidaten zu simulieren?

- [ ] Durch Aufrufen der `client.post()`-Methode mit den Dateidaten als Dictionary
- [ ] Durch Setzen des `request.FILES`-Attributs im Testfall
- [x] Durch Aufrufen der `client.post()`-Methode mit den Dateidaten als Dictionary
- [ ] Durch Aufrufen der `client.request()`-Methode mit den Dateidaten als Dictionary

#### F388. Was ist der Zweck der `settings.SECURE_REFERRER_POLICY`-Konfiguration in Django?

- [ ] Die erlaubten Hostnamen für die Anwendung zu konfigurieren
- [ ] Den HTTP Strict Transport Security (HSTS)-Header zu aktivieren
- [x] Den Referrer-Policy HTTP-Header für Referrer-Policy-Durchsetzung zu konfigurieren
- [ ] Die erlaubten Dateitypen für Datei-Uploads zu konfigurieren

#### F389. Wie können Sie den Django-Test-Client verwenden, um eine POST-Anfrage mit Formulardaten zu simulieren?

- [ ] Durch Aufrufen der `client.post()`-Methode mit den Formulardaten als Dictionary
- [ ] Durch Setzen des `request.POST`-Attributs im Testfall
- [x] Durch Aufrufen der `client.post()`-Methode mit den Formulardaten als Dictionary
- [ ] Durch Aufrufen der `client.request()`-Methode mit den Formulardaten als Dictionary

#### F390. Was ist der Zweck der `settings.STATIC_URL`-Konfiguration in Django?

- [ ] Das Verzeichnis zu konfigurieren, aus dem statische Dateien bereitgestellt werden
- [ ] Das Verzeichnis zu konfigurieren, in dem statische Dateien für die Bereitstellung gesammelt werden
- [x] Das URL-Präfix für die Bereitstellung statischer Dateien zu konfigurieren
- [ ] Das Verzeichnis zu konfigurieren, in dem hochgeladene Mediendateien gespeichert werden

#### F391. Wie können Sie den Django-Test-Client verwenden, um eine Benutzeranmeldung mit einem bestimmten Benutzerobjekt zu simulieren?

- [ ] Durch Aufrufen der `client.login()`-Methode mit den Anmeldedaten des Benutzers
- [ ] Durch Setzen der `settings.AUTH_USER_MODEL`-Konfiguration
- [x] Durch Aufrufen der `client.force_login()`-Methode mit dem Benutzerobjekt
- [ ] Durch Setzen des `request.user`-Attributs im Testfall

#### F392. Was ist der Zweck der `settings.MEDIA_URL`-Konfiguration in Django?

- [ ] Das Verzeichnis zu konfigurieren, aus dem statische Dateien bereitgestellt werden
- [ ] Das Verzeichnis zu konfigurieren, in dem statische Dateien für die Bereitstellung gesammelt werden
- [x] Das URL-Präfix für die Bereitstellung von Mediendateien zu konfigurieren
- [ ] Das Verzeichnis zu konfigurieren, in dem hochgeladene Mediendateien gespeichert werden

#### F393. Wie können Sie den Django-Test-Client verwenden, um eine Benutzerabmeldung zu simulieren?

- [ ] Durch Aufrufen der `client.logout()`-Methode
- [x] Durch Aufrufen der `client.session.flush()`-Methode
- [ ] Durch Setzen des `request.user`-Attributs auf `AnonymousUser`
- [ ] Durch Setzen der `settings.LOGOUT_URL`-Konfiguration

#### F394. Was ist der Zweck der `settings.CSRF_COOKIE_SECURE`-Konfiguration in Django?

- [ ] Die erlaubten Hostnamen für die Anwendung zu konfigurieren
- [x] Das Secure-Flag für das CSRF-Cookie zu aktivieren
- [ ] Die vertrauenswürdigen Ursprungs-Domains für den CSRF-Schutz zu konfigurieren
- [ ] Die erlaubten Dateitypen für Datei-Uploads zu konfigurieren

#### F395. Wie können Sie den Django-Test-Client verwenden, um eine GET-Anfrage mit Abfrageparametern zu simulieren?

- [ ] Durch Aufrufen der `client.post()`-Methode mit den Abfrageparametern als Dictionary
- [ ] Durch Setzen des `request.GET`-Attributs im Testfall
- [x] Durch Aufrufen der `client.get()`-Methode mit den Abfrageparametern als Dictionary
- [ ] Durch Aufrufen der `client.request()`-Methode mit den Abfrageparametern als Dictionary

#### F396. Was ist der Zweck der `settings.CSRF_COOKIE_HTTPONLY`-Konfiguration in Django?

- [ ] Die erlaubten Hostnamen für die Anwendung zu konfigurieren
- [ ] Das Secure-Flag für das CSRF-Cookie zu aktivieren
- [x] Das HttpOnly-Flag für das CSRF-Cookie zu aktivieren
- [ ] Die vertrauenswürdigen Ursprungs-Domains für den CSRF-Schutz zu konfigurieren

#### F397. Wie können Sie den Django-Test-Client verwenden, um eine POST-Anfrage mit Dateidaten zu simulieren?

- [ ] Durch Aufrufen der `client.post()`-Methode mit den Dateidaten als Dictionary
- [ ] Durch Setzen des `request.FILES`-Attributs im Testfall
- [x] Durch Aufrufen der `client.post()`-Methode mit den Dateidaten als Dictionary
- [ ] Durch Aufrufen der `client.request()`-Methode mit den Dateidaten als Dictionary

#### F398. Was ist der Zweck der `settings.SECURE_CONTENT_TYPE_NOSNIFF`-Konfiguration in Django?

- [ ] Die erlaubten Hostnamen für die Anwendung zu konfigurieren
- [ ] Das Secure-Flag für das CSRF-Cookie zu aktivieren
- [x] Den X-Content-Type-Options-Header zu aktivieren
- [ ] Die vertrauenswürdigen Ursprungs-Domains für den CSRF-Schutz zu konfigurieren
