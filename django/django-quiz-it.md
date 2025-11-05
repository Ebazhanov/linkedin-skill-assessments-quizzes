## Django

#### D1. Per memorizzare nella cache l'intero sito per un'applicazione in Django, aggiungi tutte queste impostazioni tranne quale?

- [ ] django.middleware.common.CommonMiddleware
- [ ] django.middleware.cache.UpdateCacheMiddleware
- [ ] django.middleware.cache.FetchFromCacheMiddleware
- [x] django.middleware.cache.AcceleratedCacheMiddleware

**Riferimento:**
Django viene fornito con un robusto sistema di cache che consente di salvare pagine dinamiche, in modo che non debbano essere calcolate per ogni richiesta. Per comodità, Django offre la cache con diversa granularità: dall'intero sito web alle pagine, a parti di pagine, ai risultati delle query del database, a qualsiasi oggetto in memoria. Middleware della cache. Se abilitato, ogni pagina alimentata da Django verrà memorizzata nella cache in base all'URL.

#### D2. In quale linguaggio di programmazione è scritto Django?

- [ ] C++
- [ ] Java
- [x] Python
- [ ] Ruby

#### D3. Per fornire automaticamente un valore per un campo o per eseguire una validazione che richiede l'accesso a più di un singolo campo, dovresti sovrascrivere il metodo `___` nella classe `___`.

- [ ] validate(); Model
- [ ] group(); Model
- [ ] validate(); Form
- [x] clean(); Model

#### D4. Un cliente vuole che il suo sito sia in grado di caricare gli episodi di "Rick & Morty" per numero o per titolo, ad esempio shows/3/3 o shows/picklerick. Quale pattern URL consigli?

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

#### D5. Come determini all'avvio se un pezzo di middleware deve essere utilizzato?

- [x] Solleva MiddlewareNotUsed nella funzione **init** del tuo middleware.
- [ ] Implementa il metodo not_used nella tua classe middleware.
- [ ] Elenca il middleware sotto una voce di django.middleware.IgnoredMiddleware.
- [ ] Scrivi codice per rimuovere il middleware dalle impostazioni in [app]/**init**.py.

#### D6. Come disattivi l'escape HTML automatico di Django per parte di una pagina web?

- [ ] Posiziona quella sezione tra tag di paragrafo contenenti l'interruttore autoescape=off.
- [x] Avvolgi quella sezione tra { percentage mark autoescape off percentage mark} e {percentage mark endautoescape percentage mark} tag.
- [ ] Avvolgi quella sezione tra {percentage mark autoescapeoff percentage mark} e {percentage mark endautoescapeoff percentage mark} tag.
- [ ] Non devi fare nulla: l'autoescape è disattivato per impostazione predefinita.

#### D7. Quale passaggio NON ti aiuterebbe a risolvere l'errore "django-admin: comando non trovato"?

- [ ] Verifica che la cartella bin all'interno della tua directory Django sia nel percorso di sistema.
- [ ] Assicurati di aver attivato l'ambiente virtuale configurato contenente Django.
- [ ] Verifica di aver installato Django.
- [x] Assicurati di aver creato un progetto Django.

#### D8. Ogni volta che un utente viene salvato, il suo quiz_score deve essere ricalcolato. Dove potrebbe essere un luogo ideale per aggiungere questa logica?

- [ ] template
- [x] model
- [ ] database
- [ ] view

#### D9. Qual è il modo corretto per iniziare una classe chiamata "Rainbow" in Python?

- [ ] Rainbow {}
- [ ] export Rainbow:
- [x] class Rainbow:
- [ ] def Rainbow:

#### D10. Hai ereditato un progetto Django e devi farlo funzionare localmente. Viene fornito con un file requirements.txt contenente tutte le sue dipendenze. Quale comando dovresti usare?

- [ ] django-admin startproject requirements.txt
- [ ] python install -r requirements.txt
- [x] pip install -r requirements.txt
- [ ] pip install Django

#### D11. Quale best practice NON è rilevante per le migrazioni?

- [x] Per assicurarti che le tue migrazioni siano aggiornate, dovresti eseguire updatemigrations prima di eseguire i tuoi test.
- [ ] Dovresti fare un backup del database di produzione prima di eseguire una migrazione.
- [ ] Il codice di migrazione dovrebbe essere sotto controllo di versione.
- [ ] Se un progetto ha molti dati, dovresti testare su una copia di staging prima di eseguire la migrazione in produzione.

#### D12. Cosa corrisponderà a questo pattern URL? url(r'^\$', views.hello)

- [ ] una stringa che inizia con la lettera R
- [x] una stringa vuota alla radice del server
- [ ] una stringa contenente ^ e $
- [ ] una stringa vuota ovunque nell'URL

#### D13. Qual è l'ordine tipico di un ciclo di richiesta/risposta HTTP in Django?

- [x] URL > view > template
- [ ] form > model > view
- [ ] template > view > model
- [ ] URL > template > view > model

#### D14. Le viste generiche basate su classi di Django forniscono quali classi che implementano attività comuni di sviluppo web?

- [ ] concrete
- [ ] thread-safe
- [x] astratte
- [ ] dinamiche

#### D15. Quali competenze ti servono per mantenere un insieme di template Django?

- [ ] sintassi dei template
- [x] HTML e sintassi dei template
- [ ] Python, HTML e sintassi dei template
- [ ] Python e sintassi dei template

#### D16. Come definiresti la relazione tra una stella e una costellazione in un modello Django?

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

#### D17. Quale NON è un passaggio valido nella configurazione della tua istanza Django 2.x per servire file statici come immagini o CSS?

- [x] Nel tuo file urls, aggiungi un pattern che include il nome della tua directory statica.
- [ ] Crea una directory chiamata static all'interno della directory della tua app.
- [ ] Crea una directory con il nome dell'app sotto la directory static e posiziona i file statici all'interno.
- [ ] Usa il tag template {percentage mark load static percentage mark}.

#### D18. Qual è il modo corretto per rendere disponibile una variabile a tutti i tuoi template?

- [ ] Imposta una variabile di sessione.
- [ ] Usa una variabile globale.
- [x] Aggiungi un dizionario al contesto del template.
- [ ] Usa RequestContext.

#### D19. Dovresti creare un modello utente personalizzato per nuovi progetti?

- [ ] No. L'uso di un modello utente personalizzato potrebbe danneggiare l'interfaccia admin e alcune app di terze parti.
- [x] Sì. È più facile apportare modifiche una volta che va in produzione.
- [ ] No. La classe models.User integrata di Django è stata provata e testata: non ha senso reinventare la ruota.
- [ ] Sì, poiché non c'è altra opzione.

#### D20. Vuoi creare una pagina che consenta la modifica di due classi connesse da una chiave esterna (ad esempio, una domanda e una risposta che risiedono in tabelle separate). Quale funzionalità Django puoi utilizzare?

- [ ] actions
- [ ] admin
- [ ] mezcal
- [x] inlines

#### D21. Perché i QuerySet sono considerati "pigri"?

- [ ] I risultati di un QuerySet non sono ordinati.
- [x] I QuerySet non creano alcuna attività del database fino a quando non vengono valutati.
- [ ] I QuerySet non caricano oggetti in memoria fino a quando non sono necessari.
- [ ] Utilizzando i QuerySet, non puoi eseguire query più complesse.

#### D22. Ricevi un errore `MultiValueDictKeyError` quando provi ad accedere a un parametro di richiesta con il seguente codice: request.GET['search_term']. Quale soluzione NON ti aiuterà in questo scenario?

- [x] Passa all'uso di POST invece di GET come metodo di richiesta.
- [ ] Assicurati che il campo di input nel tuo modulo sia anch'esso denominato "search_term".
- [ ] Usa il metodo GET di MultiValueDict invece di accedere al dizionario direttamente in questo modo: request.GET.get('search_term', '').
- [ ] Verifica se il parametro search_term è presente nella richiesta prima di tentare di accedervi.

#### D23. Quale funzione della classe Form di Django renderà i campi di un modulo come una serie di tag <p>?

- [ ] show_fields()
- [x] as_p()
- [ ] as_table()
- [ ] fields()

#### D24. Hai trovato un bug in Django e vuoi inviare una patch. Qual è la procedura corretta?

- [ ] Effettua il fork del repository Django su GitHub.
- [ ] Invia una pull request.
- [x] tutte queste risposte.
- [ ] Esegui la suite di test di Django.

#### D25. Django fornisce valori predefiniti ragionevoli per le impostazioni. In quale modulo Python puoi trovare queste impostazioni?

- [ ] `django.utils.default_settings.py`
- [ ] `django.utils.global_settings.py`
- [ ] `django.conf.default_settings.py`
- [x] `django.conf.global_settings.py`

#### D26. Quale nome di variabile è migliore secondo le linee guida PEP 8?

- [ ] numFingers
- [ ] number-of-Fingers
- [x] number_of_fingers
- [ ] finger_num

#### D27. Un progetto ha accumulato 500 migrazioni. Quale linea d'azione perseguiresti?

- [ ] Unisci manualmente i tuoi file di migrazione per ridurre il numero
- [ ] Non preoccuparti del numero
- [ ] Prova a minimizzare il numero di migrazioni
- [x] Usa squashmigrations per ridurre il numero

#### D28. Cosa ti consente un oggetto F() quando lavori con i modelli?

- [x] eseguire operazioni db senza recuperare un oggetto modello
- [ ] definire livelli di isolamento delle transazioni db
- [ ] utilizzare funzioni aggregate più facilmente
- [ ] costruire QuerySet riutilizzabili

#### D29. Quale NON è un tipo di campo Django per contenere interi?

- [ ] SmallIntegerField
- [x] NegativeIntegerField
- [ ] BigAutoField
- [ ] PositiveIntegerField

#### D30. Quale mostrerà la versione attualmente installata?

- [ ] print (django.version)
- [ ] import django django.getVersion()
- [x] import django django.get_version()
- [ ] python -c django --version

#### D31. Dovresti usare il metodo http `___` per leggere i dati e `___` per aggiornare o creare dati

- [ ] READ; WRITE
- [x] GET; POST
- [ ] POST; GET
- [ ] GET; PATCH

#### D32. Quando dovresti utilizzare il metodo POST rispetto a GET per l'invio di dati?

- [ ] quando l'efficienza è importante
- [ ] quando vuoi che i dati vengano memorizzati nella cache
- [ ] quando vuoi utilizzare il tuo browser per aiutare con il debug
- [x] quando i dati nel modulo potrebbero essere sensibili

#### D33. Quando utilizzare il framework dei siti Django?

- [x] se la tua singola installazione alimenta più di un sito
- [ ] se devi servire contenuti statici e dinamici
- [ ] se vuoi che la tua app abbia un nome di dominio completamente qualificato
- [ ] se prevedi più di 10.000 utenti

#### D34. Di quale infrastruttura hai bisogno:

`title=models.charfield(max_length=100, validators=[validate_spelling])`

- [ ] array inizializzato chiamato validators
- [x] un file validators contenente una funzione chiamata validate_spelling importata all'inizio del modello
- [ ] un file validators contenente una funzione chiamata validate importata all'inizio del modello
- [ ] pacchetto spelling importato all'inizio del modello

#### D35. Quale decoratore viene utilizzato per richiedere che una vista accetti solo i metodi get e head?

- [x] require_safe()
- [ ] require_put()
- [ ] require_post()
- [ ] require_get()

#### D36. Come definiresti la relazione tra un libro e un autore - il libro ha un solo autore.

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

#### D37. Cos'è un callable che accetta un valore e solleva un errore se il valore fallisce?

- [x] validator
- [ ] deodorizer
- [ ] mediator
- [ ] espressione regolare

#### D38. Per proteggere un endpoint API, rendendolo accessibile solo agli utenti registrati, puoi sostituire il valore rest_framework.permissions.allowAny nella sezione default_permissions del tuo settings.py con

- [ ] rest_framework.permissions.IsAdminUser
- [x] rest_framework.permissions.IsAuthenticated
- [ ] rest_framework.permissions.IsAuthorized
- [ ] rest_framework.permissions.IsRegistered

#### D39. Quale comando useresti per applicare una migrazione?

- [ ] makemigration
- [ ] update_db
- [ ] applymigration
- [x] migrate

#### D40. Quale tipo di classe consente di convertire QuerySet e istanze di modelli in tipi di dati Python nativi per l'uso nelle API?

- [ ] objectwriters
- [x] serializers
- [ ] picklers
- [ ] viewsets

#### D41. Come dovrebbe finire il codice?

```python
{ percentage if spark >= 50 percentage }
Lots of spark
{percentage elif spark == 42 percentage}
```

- [ ] { percentage else percentage}
- [x] {percentage endif percentage}
- [ ] Niente necessario
- [ ] {percentage end percentage}

#### D42. Quale blocco di codice creerà un serializer?

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

#### D43. Quale classe ti consente di creare automaticamente una classe Serializer con campi e validatori che corrispondono ai campi del tuo modello?

- [x] ModelSerializer
- [ ] Model
- [ ] DataSerializer
- [ ] ModelToSerializer

#### D44. Quale comando per accedere allo strumento admin integrato per la prima volta?

- [ ] django-admin setup
- [ ] django-admin runserver
- [ ] python manage.py createuser
- [x] python manage.py createsuperuser

#### D45. Gli ambienti virtuali sono per la gestione delle dipendenze. Quale granularità funziona meglio?

- [x] dovresti configurare un nuovo virtualenv per ogni progetto Django
- [ ] Non dovrebbero essere usati
- [ ] Usa lo stesso venv per tutto il tuo lavoro Django
- [ ] Usa un nuovo venv per ogni app Django

#### D46. Cosa esegue vari comandi Django come l'avvio di un webserver o la creazione di un'app?

- [ ] migrate.py
- [ ] wsgi.py
- [x] manage.py
- [ ] runserver

#### D47. Cosa suggeriscono le best practice di Django dovrebbe essere "grasso"?

- [x] models
- [ ] controllers
- [ ] programmatori
- [ ] clients

#### D48. Quale NON fa parte della filosofia di design di Django?

- [ ] Accoppiamento lasco
- [ ] Meno codice
- [ ] Sviluppo rapido
- [x] Implicito rispetto all'esplicito

#### D49. Qual è il risultato di questo codice template?

{% raw %}{{"live long and prosper"|truncatewords:3}}{% endraw %}

- [x] live long and ...
- [ ] live long and
- [ ] un errore di compilazione
- [ ] liv

#### D50. Quando questo codice carica i dati in memoria?

```
1 sandwiches = Sandwich.objects.filter(is_vegan=True)
2 for sandwich in sandwiches:
3   print(sandwich.name + " - " + sandwich.spice_level)
```

- [ ] linea 1
- [ ] Dipende da quanti risultati restituisce la query.
- [ ] Dipende dalla cache.
- [x] linea 2

#### D51. Stai costruendo un'applicazione web utilizzando un frontend React e un backend Django. Per cosa dovrai fornire?

- [ ] un server web NGINX
- [ ] un database NoSQL
- [ ] un disco rigido più grande
- [x] middleware CORS

#### D52. Per esporre un modello esistente tramite un endpoint API, cosa devi implementare?

- [ ] una richiesta HTTP
- [ ] un oggetto JSON
- [ ] una query
- [x] un serializer

#### D53. Come impediresti a Django di eseguire operazioni di creazione o eliminazione di tabelle di database tramite migrazioni per un particolare modello?

- [ ] Esegui il comando `migrate` con `--exclude=[nome_modello]`.
- [ ] Sposta la definizione del modello da `models.py` in un file proprio.
- [x] Imposta `managed=False` all'interno del modello.
- [ ] Non eseguire il comando `migrate`.

#### D54. Quale metodo puoi usare per verificare se i dati del modulo sono cambiati quando usi un'istanza del modulo?

- [x] has_changed()
- [ ] its_changed()
- [ ] has_updated()
- [ ] Nessuna di queste

#### D55. Cos'è WSGI?

- [ ] un server
- [x] una specifica di interfaccia
- [ ] un modulo Python
- [ ] un framework

Riferimento:- https://wsgi.tutorial.codepoint.net/intro

#### D56. Quale vista generica dovrebbe essere utilizzata per visualizzare i titoli di tutte le canzoni di Django Reinhardt?

- [ ] DetailView
- [ ] TittleView
- [ ] SongView
- [x] ListView

#### D57. Quale affermazione è più accurata, riguardo all'uso del database SQLite predefinito sulla tua macchina locale/di sviluppo ma Postgres in produzione

- [ ] C'è meno possibilità di introdurre bug poiché SQLite funziona già immediatamente
- [ ] Va bene, devi solo mantenere entrambe le istanze sincronizzate
- [x] È una cattiva idea e potrebbe portare a problemi in futuro
- [ ] È il modo più efficiente per costruire un progetto

#### D58. Perché potresti voler scrivere un Manager di modelli personalizzato?

- [ ] per eseguire query del database
- [ ] per configurare un database per i test
- [x] per modificare il QuerySet iniziale che il Manager restituisce
- [ ] per filtrare i risultati che una query del database restituisce

#### D59. In Django, cosa viene utilizzato per personalizzare i dati inviati ai template?

- [ ] models
- [x] views
- [ ] forms
- [ ] serializers

#### D60. Per completare il condizionale, con cosa dovrebbe finire questo blocco di codice?

```shell
% if sparles >= 50 %
  Lots of sparkles!
% elif sparkles == 42 %
  The answer to life, the universe, and everything!
```

- [x] `% endif %`
- [ ] Non serve altro.
- [ ] `% end%`
- [ ] `% else %`

#### D61. Quando dovresti utilizzare il metodo POST rispetto al metodo GET per l'invio di dati da un modulo?

- [x] quando i dati nel modulo potrebbero essere sensibili
- [ ] quando vuoi che i dati vengano memorizzati nella cache
- [ ] quando vuoi utilizzare il tuo browser per aiutare con il debug
- [ ] quando l'efficienza è importante

#### D62. Cos'è un callable che accetta un valore e solleva un errore se il valore non soddisfa alcuni criteri?

- [ ] mediator
- [x] validator
- [ ] espressione regolare
- [ ] deodorizer

#### D63. Stai caricando un file su Django da un modulo e vuoi salvare il file ricevuto come campo su un oggetto modello. Puoi semplicemente assegnare l'oggetto file da **\_a un campo di tipo\_\_** nel modello.

- [ ] request.META; FileField
- [ ] request.FILES; BLOBField
- [x] request.FILES; FileField
- [ ] request.META.Files; CLOBField

#### D64. Quale modulo Python potrebbe essere utilizzato per memorizzare lo stato corrente di un modello Django in un file?

- [x] pickle
- [ ] struct
- [ ] marshal
- [ ] serialize

#### D65. Per aggiungere una nuova app a un progetto Django esistente, devi modificare la sezione **_ del file _**.

- [ ] ALLOWED_HOSTS; settings.py
- [ ] APPS; manage.py
- [x] INSTALLED_APPS; settings.py
- [ ] TEMPLATES; urls.py

#### D66. Quale NON è un pacchetto di terze parti comunemente utilizzato per l'autenticazione?

- [ ] django-guardian
- [ ] django-rest-auth
- [ ] authtoken
- [x] django-rest-framework-jwt

#### D67. Quale funzione nel pacchetto django.urls può aiutarti a evitare di codificare gli URL generando un URL dato il nome di una vista?

- [ ] get_script_prefix()
- [ ] redirect()
- [x] reverse()
- [ ] resolve()

#### D68. Quale è un metodo di richiesta HTTP fittizio?

- [ ] POST
- [ ] PUT
- [x] PAUSE
- [ ] PATCH

#### D69. Quale funzione helper NON è fornita come parte del pacchetto django.shortcuts? rif-

- [x] render_to_request()
- [ ] render()
- [ ] redirect()
- [ ] get_object_or_404()

[Riferimento](https://docs.djangoproject.com/en/4.0/topics/http/shortcuts/#:~:text=The%20package%20django.,controlled%20coupling%20for%20convenience's%20sake)

#### D70. Quale è un luogo non standard per memorizzare i template?

- [x] al livello radice di un progetto
- [ ] all'interno dell'applicazione
- [ ] nel database
- [ ] su Github

#### D71. Se avessi lasciato fuori 8080 dal comando python manage.py runserver 8080 quale porta userebbe Django come predefinita?

- [ ] 8080
- [ ] 80
- [x] 8000
- [ ] Non riuscirebbe ad avviarsi

#### D72. Quale affermazione sulle app Django è falsa?

- [x] Un'app Django è il contenitore di livello superiore per un'applicazione web alimentata da Django.
- [ ] Le app Django sono piccole librerie progettate per rappresentare un singolo aspetto di un progetto.
- [ ] Ogni app Django dovrebbe fare una cosa, e una cosa sola.
- [ ] Un progetto Django è composto da molte app.

#### D73. Quali caratteri sono illegali nei nomi delle variabili dei template?

- [ ] underscore.
- [ ] lettere maiuscole.
- [x] segni di punteggiatura.
- [ ] numeri.

[Riferimento](https://docs.djangoproject.com/en/4.1/ref/templates/language/#:~:text=Variable%20names%20consist%20of%20any,may%20not%20be%20a%20number.)

#### D74. Quale NON è un tag di chiusura template valido?

- [ ] `% endautoescape %`
- [x] `% endifempty %`
- [ ] `% endcomment %`
- [ ] `% endfilter %`

#### D75. Quando avresti bisogno di usare la funzione di utilità reverse_lazy invece di reverse?

- [ ] quando vuoi fornire un URL inverso come valore predefinito per un parametro nella firma di una funzione
- [x] tutte queste risposte
- [ ] quando vuoi fornire un URL inverso come attributo url di una vista generica basata su classi
- [ ] quando vuoi fornire un URL a un decoratore, come l'argomento login_url per il decoratore permission_required()

#### D76. Qual è lo scopo del file \_\_init\_\_.py?

- [ ] per estendere l'insieme di moduli trovati in un pacchetto
- [ ] per consentire ai moduli compilati di diverse versioni e versioni di Python di coesistere
- [ ] per inizializzare le impostazioni del progetto
- [x] per dichiarare il contenuto della directory come modulo Python

[Riferimento](<https://docs.djangoproject.com/en/4.1/ref/urlresolvers/#:~:text=reverse_lazy()&text=It%20is%20useful%20for%20when,a%20generic%20class%2Dbased%20view>)

#### D77. Quale pacchetto Python può essere utilizzato per modificare i numeri in una forma più leggibile come "1200000" in "1,2 milioni"?

- [ ] black
- [ ] puffer
- [ ] pitch
- [x] humanize

#### D78. Dove troveresti il file settings.py?

- [x] \[projectname\]/settings.py
- [ ] \[projectname\]/\[projectname\]/settings.py
- [ ] \[PYTHON_ROOT\]/settings.py
- [ ] \[DJANGO_ROOT]/settings.py

#### D79. Cosa scriveresti per definire la relazione tra un libro e un autore, assumendo che un libro abbia un solo autore, in un modello Django?

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

#### D80. Quale metodo puoi usare per verificare se i dati del modulo sono stati modificati quando usi un'istanza Form?

- [ ] changed_data()
- [x] has_changed()
- [ ] has_updated()
- [ ] is_modified()

#### D81. Quale affermazione è più accurata, riguardo all'uso del database SQLite predefinito sulla tua macchina locale/di sviluppo ma Postgres in produzione?

- [ ] È il modo più efficiente per costruire un progetto
- [ ] C'è meno possibilità di introdurre bug poiché SQLite funziona già immediatamente
- [x] È una cattiva idea e potrebbe portare a problemi in futuro
- [ ] Va bene, devi solo mantenere entrambe le istanze sincronizzate

#### D82. Come gestisce Django il routing degli URL?

- [ ] utilizzando classi
- [ ] utilizzando funzioni
- [x] utilizzando espressioni regolari
- [ ] utilizzando percorsi fissi

#### D83. Qual è lo scopo del middleware di Django?

- [ ] Per definire lo schema del database
- [ ] Per gestire il routing degli URL
- [x] Per gestire globalmente richieste e risposte HTTP
- [ ] Per creare interfacce utente

[Riferimento](https://medium.com/scalereal/everything-you-need-to-know-about-middleware-in-django-2a3bd3853cd6)

#### D84. Quale delle seguenti affermazioni è vera sul Mapping Relazionale-Oggetti (ORM) di Django?

- [ ] Viene utilizzato per definire il routing degli URL in un'applicazione Django.
- [x] Ti consente di interrogare il database utilizzando codice Python.
- [ ] Viene utilizzato per definire la struttura dei template HTML.
- [ ] È responsabile della gestione dell'autenticazione degli utenti.

#### D85. Quale delle seguenti affermazioni è vera sul campo "many-to-many" di Django in un modello?

- [ ] Viene utilizzato per definire una relazione uno-a-uno tra due modelli.
- [ ] Crea una relazione di chiave esterna tra due modelli.
- [x] Consente di associare più oggetti tra loro.
- [ ] Applica vincoli univoci su un campo.

#### D86. Le viste generiche basate su classi di Django forniscono quali classi che implementano attività comuni di sviluppo web?

- [ ] concrete
- [ ] thread-safe
- [x] astratte
- [ ] dinamiche

#### D87. Quali competenze ti servono per mantenere un insieme di template Django?

- [ ] sintassi dei template
- [x] HTML e sintassi dei template
- [ ] Python, HTML e sintassi dei template
- [ ] Python e sintassi dei template

#### D88. Quale è un luogo non standard per memorizzare i template?

- [x] al livello radice di un progetto
- [ ] all'interno dell'applicazione
- [ ] nel database
- [ ] su Github

#### D89. Se avessi lasciato fuori 8080 dal comando python manage.py runserver 8080 quale porta userebbe Django come predefinita?

- [ ] 8080
- [ ] 80
- [x] 8000
- [ ] Non riuscirebbe ad avviarsi

#### D90. Qual è lo scopo del Mapping Relazionale-Oggetto (ORM) di Django?

- [ ] Per definire il routing degli URL in un'applicazione Django.
- [ ] Per gestire globalmente richieste e risposte HTTP.
- [x] Per mappare oggetti Python su tabelle del database e semplificare le operazioni del database.
- [ ] Per creare interfacce utente.

#### D91. In Django, a cosa si riferisce il termine "migrazione"?

- [ ] Un cambiamento nella configurazione del routing degli URL.
- [x] Il processo di propagazione delle modifiche apportate ai tuoi modelli (aggiunta di un campo, eliminazione di un modello, ecc.) nello schema del database.
- [ ] Un modo per definire middleware personalizzato.
- [ ] Il processo di creazione di template HTML per la tua applicazione.

#### D92. Qual è lo scopo del "contesto" di Django nel contesto del rendering dei template?

- [x] Per passare dati dalle tue viste ai tuoi template in modo che i dati possano essere renderizzati dinamicamente.
- [ ] Per definire pattern URL per la tua applicazione.
- [ ] Per gestire richieste e risposte HTTP.
- [ ] Per creare interfacce utente.

#### D93. Cosa rappresenta la classe Django `QuerySet`?

- [ ] Una classe Python utilizzata per definire il routing degli URL in Django.
- [ ] Una classe per la gestione di richieste e risposte HTTP.
- [x] Una query del database effettuata da Django, rappresentata in Python.
- [ ] Una classe per definire template HTML.

#### D94. In Django, qual è lo scopo del comando di gestione "collectstatic"?

- [ ] Per raccogliere dati utente per l'analisi.
- [ ] Per raccogliere record del database da più fonti.
- [x] Per raccogliere tutti i file statici (CSS, JavaScript, immagini) da ciascuna delle tue applicazioni in un'unica posizione.
- [ ] Per raccogliere log per scopi di debug.

#### D95. Per cosa viene utilizzato il sito Admin di Django?

- [ ] Per gestire l'autenticazione degli utenti.
- [ ] Per definire il routing degli URL per le applicazioni Django.
- [x] Per fornire un'interfaccia admin generata automaticamente per i tuoi modelli.
- [ ] Per scrivere ed eseguire query del database.

#### D96. A cosa si riferisce il "middleware" di Django?

- [ ] Un modo per creare interfacce utente.
- [ ] Una query del database in Django.
- [x] Un modo per elaborare richieste e risposte HTTP globalmente prima che raggiungano la vista o dopo che lasciano la vista.
- [ ] Un modo per configurare il routing degli URL in Django.

#### D97. Qual è lo scopo principale dei "file di migrazione" di Django?

- [x] Per definire e memorizzare le modifiche allo schema del database nel tempo.
- [ ] Per gestire file statici come CSS e JavaScript.
- [ ] Per configurare pattern URL.
- [ ] Per creare template HTML.

#### D98. Quale sistema di autenticazione fornisce Django pronto all'uso?

- [ ] OAuth 2.0
- [x] Autenticazione utente con modelli e viste utente integrati.
- [ ] JWT (JSON Web Tokens)
- [ ] SAML (Security Assertion Markup Language)

#### D99. In Django, a cosa si riferisce il pattern architetturale "Model-View-Controller" (MVC)?

- [ ] Un pattern per definire il routing degli URL.
- [ ] Un pattern per creare template HTML.
- [x] Un pattern che divide l'applicazione in tre componenti interconnessi: Model, View e Controller (Django spesso si riferisce ad esso come MTV, Model-View-Template).
- [ ] Un pattern per l'autenticazione degli utenti.

#### D100. Qual è lo scopo dei "template" di Django?

- [ ] Per definire lo schema del database e le relazioni tra modelli.
- [x] Per definire la struttura e il layout delle pagine HTML da servire all'utente.
- [ ] Per configurare pattern URL per la tua applicazione.
- [ ] Per memorizzare e servire file statici come immagini e JavaScript.

#### D101. Quale metodo ORM di Django viene utilizzato per recuperare un singolo oggetto che corrisponde ai parametri di ricerca forniti?

- [ ] `get_object_or_404()`
- [x] `get()`
- [ ] `filter()`
- [ ] `values()`

#### D102. Qual è lo scopo del metodo `__str__()` in un modello Django?

- [ ] Per definire l'ordinamento predefinito per le istanze del modello
- [x] Per fornire una rappresentazione stringa leggibile dall'uomo dell'istanza del modello
- [ ] Per definire il campo predefinito da utilizzare per le ricerche
- [ ] Per definire il campo di visualizzazione predefinito nell'interfaccia admin di Django

#### D103. Quale metodo ORM di Django viene utilizzato per recuperare un elenco di oggetti che corrispondono ai parametri di ricerca forniti?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [x] `filter()`
- [ ] `values()`

#### D104. Qual è lo scopo del parametro `related_name` nel campo `ForeignKey` di un modello Django?

- [ ] Per definire il nome della relazione inversa sul modello correlato
- [ ] Per definire l'ordinamento predefinito per gli oggetti correlati
- [x] Per definire il nome dell'attributo sul modello correlato che accede all'insieme di oggetti correlati
- [ ] Per definire il nome dell'attributo sul modello corrente che accede all'oggetto correlato

#### D105. Quale metodo ORM di Django viene utilizzato per recuperare un elenco di valori distinti per i campi specificati?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [ ] `filter()`
- [x] `values()`

#### D106. Qual è lo scopo del parametro `unique` in un campo del modello Django?

- [ ] Per definire l'ordinamento predefinito per il campo
- [ ] Per definire il valore predefinito per il campo
- [x] Per garantire che il valore del campo sia univoco in tutte le istanze del modello
- [ ] Per definire la lunghezza massima del campo

#### D107. Quale metodo ORM di Django viene utilizzato per recuperare un singolo oggetto che corrisponde ai parametri di ricerca forniti o solleva un'eccezione `Http404` se nessun oggetto viene trovato?

- [x] `get_object_or_404()`
- [ ] `get()`
- [ ] `filter()`
- [ ] `values()`

#### D108. Qual è lo scopo del parametro `on_delete` nel campo `ForeignKey` di un modello Django?

- [ ] Per definire il valore predefinito per il campo
- [ ] Per definire la lunghezza massima del campo
- [x] Per specificare il comportamento quando l'oggetto referenziato viene eliminato
- [ ] Per definire il nome della relazione inversa sul modello correlato

#### D109. Quale metodo ORM di Django viene utilizzato per eseguire operazioni di aggregazione (ad es. `sum()`, `avg()`, `count()`) su un QuerySet?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [ ] `filter()`
- [x] `aggregate()`

#### D110. Qual è lo scopo del parametro `related_query_name` nel campo `ForeignKey` di un modello Django?

- [ ] Per definire il nome della relazione inversa sul modello correlato
- [x] Per definire il nome dell'attributo sul modello correlato che accede all'insieme di oggetti correlati
- [ ] Per definire l'ordinamento predefinito per gli oggetti correlati
- [ ] Per definire il nome dell'attributo sul modello corrente che accede all'oggetto correlato

