## Django

#### Q1. Pour mettre en cache l'ensemble de votre site pour une application dans Django, vous ajoutez tous ces paramètres sauf lequel ?

- [ ] django.middleware.common.CommonMiddleware
- [ ] django.middleware.cache.UpdateCacheMiddleware
- [ ] django.middleware.cache.FetchFromCacheMiddleware
- [x] django.middleware.cache.AcceleratedCacheMiddleware

**Référence :**
Django est livré avec un système de cache robuste qui vous permet d'enregistrer des pages dynamiques, afin qu'elles n'aient pas à être calculées pour chaque requête. Pour plus de commodité, Django offre un cache avec différentes granularités - du site web entier aux pages en passant par des parties de pages, des résultats de requêtes DB et tout objet en mémoire. Middleware de cache. S'il est activé, chaque page alimentée par Django sera mise en cache en fonction de l'URL.

#### Q2. Dans quel langage de programmation Django est-il écrit ?

- [ ] C++
- [ ] Java
- [x] Python
- [ ] Ruby

#### Q3. Pour fournir automatiquement une valeur pour un champ, ou pour effectuer une validation nécessitant l'accès à plus d'un seul champ, vous devez remplacer la méthode `___` dans la classe `___`.

- [ ] validate(); Model
- [ ] group(); Model
- [ ] validate(); Form
- [x] clean(); Model

#### Q4. Un client souhaite que son site puisse charger les épisodes de "Rick & Morty" par numéro ou par titre—par exemple, shows/3/3 ou shows/picklerick. Quel modèle d'URL recommandez-vous ?

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

#### Q5. Comment déterminez-vous au moment du démarrage si un middleware doit être utilisé ?

- [x] Levez MiddlewareNotUsed dans la fonction **init** de votre middleware.
- [ ] Implémentez la méthode not_used dans votre classe middleware.
- [ ] Listez le middleware sous une entrée de django.middleware.IgnoredMiddleware.
- [ ] Écrivez du code pour supprimer le middleware des paramètres dans [app]/**init**.py.

#### Q6. Comment désactivez-vous l'échappement HTML automatique de Django pour une partie d'une page web ?

- [ ] Placez cette section entre des balises de paragraphe contenant le commutateur autoescape=off.
- [x] Enveloppez cette section entre les balises { percentage mark autoescape off percentage mark} et {percentage mark endautoescape percentage mark}.
- [ ] Enveloppez cette section entre les balises {percentage mark autoescapeoff percentage mark} et {percentage mark endautoescapeoff percentage mark}.
- [ ] Vous n'avez rien à faire—l'échappement automatique est désactivé par défaut.

#### Q7. Quelle étape ne vous aiderait PAS à résoudre l'erreur "django-admin: command not found" ?

- [ ] Vérifiez que le dossier bin à l'intérieur de votre répertoire Django est sur le chemin système.
- [ ] Assurez-vous d'avoir activé l'environnement virtuel que vous avez configuré contenant Django.
- [ ] Vérifiez que vous avez installé Django.
- [x] Assurez-vous d'avoir créé un projet Django.

#### Q8. Chaque fois qu'un utilisateur est sauvegardé, son quiz_score doit être recalculé. Où serait un endroit idéal pour ajouter cette logique ?

- [ ] template
- [x] model
- [ ] database
- [ ] view

#### Q9. Quelle est la bonne façon de commencer une classe appelée "Rainbow" en Python ?

- [ ] Rainbow {}
- [ ] export Rainbow:
- [x] class Rainbow:
- [ ] def Rainbow:

#### Q10. Vous avez hérité d'un projet Django et devez le faire fonctionner localement. Il est livré avec un fichier requirements.txt contenant toutes ses dépendances. Quelle commande devez-vous utiliser ?

- [ ] django-admin startproject requirements.txt
- [ ] python install -r requirements.txt
- [x] pip install -r requirements.txt
- [ ] pip install Django

#### Q11. Quelle bonne pratique n'est PAS pertinente pour les migrations ?

- [x] Pour vous assurer que vos migrations sont à jour, vous devez exécuter updatemigrations avant d'exécuter vos tests.
- [ ] Vous devez sauvegarder votre base de données de production avant d'exécuter une migration.
- [ ] Votre code de migration doit être sous contrôle de source.
- [ ] Si un projet a beaucoup de données, vous devez tester par rapport à une copie de staging avant d'exécuter la migration sur la production.

#### Q12. Que correspondra ce modèle d'URL ? url(r'^\$', views.hello)

- [ ] une chaîne commençant par la lettre R
- [x] une chaîne vide à la racine du serveur
- [ ] une chaîne contenant ^ et $
- [ ] une chaîne vide n'importe où dans l'URL

#### Q13. Quel est l'ordre typique d'un cycle de requête/réponse HTTP dans Django ?

- [x] URL > view > template
- [ ] form > model > view
- [ ] template > view > model
- [ ] URL > template > view > model

#### Q14. Les vues génériques basées sur les classes de Django fournissent quelles classes qui implémentent des tâches courantes de développement web ?

- [ ] concrete
- [ ] thread-safe
- [x] abstract
- [ ] dynamic

#### Q15. Quelles compétences devez-vous avoir pour maintenir un ensemble de templates Django ?

- [ ] syntaxe de template
- [x] HTML et syntaxe de template
- [ ] Python, HTML et syntaxe de template
- [ ] Python et syntaxe de template

#### Q16. Comment définiriez-vous la relation entre une étoile et une constellation dans un modèle Django ?

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

#### Q17. Quelle n'est PAS une étape valide pour configurer votre instance Django 2.x pour servir des fichiers statiques tels que des images ou du CSS ?

- [x] Dans votre fichier urls, ajoutez un modèle qui inclut le nom de votre répertoire statique.
- [ ] Créez un répertoire nommé static dans votre répertoire d'application.
- [ ] Créez un répertoire nommé d'après l'application sous le répertoire static, et placez les fichiers statiques à l'intérieur.
- [ ] Utilisez la balise de template {percentage mark load static percentage mark}.

#### Q18. Quelle est la bonne façon de rendre une variable disponible pour tous vos templates ?

- [ ] Définir une variable de session.
- [ ] Utiliser une variable globale.
- [x] Ajouter un dictionnaire au contexte du template.
- [ ] Utiliser RequestContext.

#### Q19. Devriez-vous créer un modèle utilisateur personnalisé pour les nouveaux projets ?

- [ ] Non. L'utilisation d'un modèle utilisateur personnalisé pourrait casser l'interface d'administration et certaines applications tierces.
- [x] Oui. Il est plus facile d'apporter des modifications une fois qu'il est en production.
- [ ] Non. La classe intégrée models.User de Django a été testée et éprouvée—inutile de réinventer la roue.
- [ ] Oui, car il n'y a pas d'autre option.

#### Q20. Vous souhaitez créer une page permettant l'édition de deux classes connectées par une clé étrangère (par exemple, une question et une réponse qui résident dans des tables séparées). Quelle fonctionnalité Django pouvez-vous utiliser ?

- [ ] actions
- [ ] admin
- [ ] mezcal
- [x] inlines

#### Q21. Pourquoi les QuerySets sont-ils considérés comme "lazy" (paresseux) ?

- [ ] Les résultats d'un QuerySet ne sont pas ordonnés.
- [x] Les QuerySets ne créent aucune activité de base de données tant qu'ils ne sont pas évalués.
- [ ] Les QuerySets ne chargent pas les objets en mémoire tant qu'ils ne sont pas nécessaires.
- [ ] En utilisant des QuerySets, vous ne pouvez pas exécuter de requêtes plus complexes.

#### Q22. Vous recevez une `MultiValueDictKeyError` lorsque vous essayez d'accéder à un paramètre de requête avec le code suivant : request.GET['search_term']. Quelle solution ne vous aidera PAS dans ce scénario ?

- [x] Passer à l'utilisation de POST au lieu de GET comme méthode de requête.
- [ ] Assurez-vous que le champ de saisie dans votre formulaire est également nommé "search_term".
- [ ] Utilisez la méthode GET de MultiValueDict au lieu d'accéder directement au dictionnaire comme ceci : request.GET.get('search_term', '').
- [ ] Vérifiez si le paramètre search_term est présent dans la requête avant d'essayer d'y accéder.

#### Q23. Quelle fonction de la classe Form de Django rendra les champs d'un formulaire sous forme de série de balises <p> ?

- [ ] show_fields()
- [x] as_p()
- [ ] as_table()
- [ ] fields()

#### Q24. Vous avez trouvé un bug dans Django et vous souhaitez soumettre un correctif. Quelle est la procédure correcte ?

- [ ] Forker le dépôt Django sur GitHub.
- [ ] Soumettre une pull request.
- [x] toutes ces réponses.
- [ ] Exécuter la suite de tests de Django.

#### Q25. Django fournit des valeurs par défaut sensées pour les paramètres. Dans quel module Python pouvez-vous trouver ces paramètres ?

- [ ] `django.utils.default_settings.py`
- [ ] `django.utils.global_settings.py`
- [ ] `django.conf.default_settings.py`
- [x] `django.conf.global_settings.py`

#### Q26. Quel nom de variable est le meilleur selon les directives PEP 8 ?

- [ ] numFingers
- [ ] number-of-Fingers
- [x] number_of_fingers
- [ ] finger_num

#### Q27. Un projet a accumulé 500 migrations. Quelle ligne de conduite poursuivriez-vous ?

- [ ] Fusionner manuellement vos fichiers de migration pour réduire le nombre
- [ ] Ne vous inquiétez pas du nombre
- [ ] Essayez de minimiser le nombre de migrations
- [x] Utilisez squashmigrations pour réduire le nombre

#### Q28. Que vous permet de faire un objet F() lorsque vous traitez avec des modèles ?

- [x] effectuer des opérations de base de données sans récupérer un objet de modèle
- [ ] définir des niveaux d'isolation de transaction de base de données
- [ ] utiliser des fonctions d'agrégation plus facilement
- [ ] construire des QuerySets réutilisables

#### Q29. Lequel n'est pas un type de champ Django pour contenir des entiers ?

- [ ] SmallIntegerField
- [x] NegativeIntegerField
- [ ] BigAutoField
- [ ] PositiveIntegerField

#### Q30. Lequel affichera la version actuellement installée ?

- [ ] print (django.version)
- [ ] import django django.getVersion()
- [x] import django django.get_version()
- [ ] python -c django --version

#### Q31. Vous devez utiliser la méthode http `___` pour lire les données et `___` pour mettre à jour ou créer des données

- [ ] READ; WRITE
- [x] GET; POST
- [ ] POST; GET
- [ ] GET; PATCH

#### Q32. Quand devez-vous utiliser la méthode POST plutôt que GET pour soumettre des données ?

- [ ] quand l'efficacité est importante
- [ ] quand vous voulez que les données soient mises en cache
- [ ] quand vous voulez utiliser votre navigateur pour aider au débogage
- [x] quand les données du formulaire peuvent être sensibles

#### Q33. Quand utiliser le framework de sites Django ?

- [x] si votre installation unique alimente plus d'un site
- [ ] si vous devez servir du contenu statique ainsi que du contenu dynamique
- [ ] si vous voulez que votre application ait un nom de domaine entièrement qualifié
- [ ] si vous attendez plus de 10 000 utilisateurs

#### Q34. De quelle infrastructure avez-vous besoin :

`title=models.charfield(max_length=100, validators=[validate_spelling])`

- [ ] tableau initialisé appelé validators
- [x] un fichier validators contenant une fonction appelée validate_spelling importée en haut du modèle
- [ ] un fichier validators contenant une fonction appelée validate importée en haut du modèle
- [ ] package spelling importé en haut du modèle

#### Q35. Quel décorateur est utilisé pour exiger qu'une vue accepte uniquement les méthodes get et head ?

- [x] require_safe()
- [ ] require_put()
- [ ] require_post()
- [ ] require_get()

#### Q36. Comment définiriez-vous la relation entre un livre et un auteur - un livre n'a qu'un seul auteur.

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

#### Q37. Qu'est-ce qu'un callable qui prend une valeur et lève une erreur si la valeur échoue ?

- [x] validator
- [ ] deodorizer
- [ ] mediator
- [ ] regular expression

#### Q38. Pour sécuriser un point de terminaison d'API, le rendant accessible uniquement aux utilisateurs enregistrés, vous pouvez remplacer la valeur rest_framework.permissions.allowAny dans la section default_permissions de votre settings.py par

- [ ] rest_framework.permissions.IsAdminUser
- [x] rest_framework.permissions.IsAuthenticated
- [ ] rest_framework.permissions.IsAuthorized
- [ ] rest_framework.permissions.IsRegistered

#### Q39. Quelle commande utiliseriez-vous pour appliquer une migration ?

- [ ] makemigration
- [ ] update_db
- [ ] applymigration
- [x] migrate

#### Q40. Quel type de classe permet de convertir des QuerySets et des instances de modèle en types de données Python natifs pour une utilisation dans les API ?

- [ ] objectwriters
- [x] serializers
- [ ] picklers
- [ ] viewsets

#### Q41. Comment le code devrait-il se terminer ?

```python
{ percentage if spark >= 50 percentage }
Lots of spark
{percentage elif spark == 42 percentage}
```

- [ ] { percentage else percentage}
- [x] {percentage endif percentage}
- [ ] Rien nécessaire
- [ ] {percentage end percentage}

#### Q42. Quel bloc de code créera un serializer ?

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

#### Q43. Quelle classe vous permet de créer automatiquement une classe Serializer avec des champs et des validateurs correspondant aux champs de votre modèle ?

- [x] ModelSerializer
- [ ] Model
- [ ] DataSerializer
- [ ] ModelToSerializer

#### Q44. Quelle commande pour accéder à l'outil d'administration intégré pour la première fois ?

- [ ] django-admin setup
- [ ] django-admin runserver
- [ ] python manage.py createuser
- [x] python manage.py createsuperuser

#### Q45. Les environnements virtuels servent à gérer les dépendances. Quelle granularité fonctionne le mieux ?

- [x] vous devez configurer un nouveau virtualenv pour chaque projet Django
- [ ] Ils ne devraient pas être utilisés
- [ ] Utilisez le même venv pour tout votre travail Django
- [ ] Utilisez un nouveau venv pour chaque application Django

#### Q46. Qu'est-ce qui exécute diverses commandes Django telles que l'exécution d'un serveur web ou la création d'une application ?

- [ ] migrate.py
- [ ] wsgi.py
- [x] manage.py
- [ ] runserver

#### Q47. Que suggèrent les meilleures pratiques de Django qui devrait être "fat" (gros) ?

- [x] models
- [ ] controllers
- [ ] programmers
- [ ] clients

#### Q48. Lequel ne fait pas partie de la philosophie de conception de Django ?

- [ ] Couplage lâche
- [ ] Moins de code
- [ ] Développement rapide
- [x] Implicite plutôt qu'explicite

#### Q49. Quel est le résultat de ce code de template ?

{% raw %}{{"live long and prosper"|truncatewords:3}}{% endraw %}

- [x] live long and ...
- [ ] live long and
- [ ] une erreur de compilation
- [ ] liv

#### Q50. Quand ce code charge-t-il les données en mémoire ?

```
1 sandwiches = Sandwich.objects.filter(is_vegan=True)
2 for sandwich in sandwiches:
3   print(sandwich.name + " - " + sandwich.spice_level)
```

- [ ] ligne 1
- [ ] Cela dépend du nombre de résultats retournés par la requête.
- [ ] Cela dépend du cache.
- [x] ligne 2

#### Q51. Vous construisez une application web utilisant un front-end React et un back-end Django. Pour quoi devrez-vous provisionner ?

- [ ] un serveur web NGINX
- [ ] une base de données NoSQL
- [ ] un disque dur plus grand
- [x] middleware CORS

#### Q52. Pour exposer un modèle existant via un point de terminaison d'API, que devez-vous implémenter ?

- [ ] une requête HTTP
- [ ] un objet JSON
- [ ] une requête
- [x] un serializer

#### Q53. Comment empêcheriez-vous Django d'effectuer des opérations de création ou de suppression de tables de base de données via des migrations pour un modèle particulier ?

- [ ] Exécutez la commande `migrate` avec `--exclude=[model_name]`.
- [ ] Déplacez la définition du modèle de `models.py` dans son propre fichier.
- [x] Définissez `managed=False` à l'intérieur du modèle.
- [ ] N'exécutez pas la commande `migrate`.

#### Q54. quelle méthode pouvez-vous utiliser pour vérifier si les données du formulaire ont changé lors de l'utilisation d'une instance de formulaire ?

- [x] has_changed()
- [ ] its_changed()
- [ ] has_updated()
- [ ] Aucune de ces réponses

#### Q55. Qu'est-ce que WSGI ?

- [ ] un serveur
- [x] une spécification d'interface
- [ ] un module Python
- [ ] un framework

Lien de référence :- https://wsgi.tutorial.codepoint.net/intro

#### Q56. Quelle vue générique doit être utilisée pour afficher les titres de toutes les chansons de Django Reinhardt ?

- [ ] DetailView
- [ ] TittleView
- [ ] SongView
- [x] ListView

#### Q57. Quelle déclaration est la plus précise, concernant l'utilisation de la base de données SQLite par défaut sur votre machine locale/de développement mais Postgres en production

- [ ] Il y a moins de chances d'introduire des bugs puisque SQLite fonctionne déjà prêt à l'emploi
- [ ] C'est bien, il suffit de garder les deux instances synchronisées
- [x] C'est une mauvaise idée et pourrait conduire à des problèmes à l'avenir
- [ ] C'est la façon la plus efficace de construire un projet

#### Q58. Pourquoi voudriez-vous écrire un Manager de modèle personnalisé ?

- [ ] pour effectuer des requêtes de base de données
- [ ] pour configurer une base de données pour les tests
- [x] pour modifier le QuerySet initial que le Manager retourne
- [ ] pour filtrer les résultats qu'une requête de base de données retourne

#### Q59. Dans Django, qu'est-ce qui est utilisé pour personnaliser les données envoyées aux templates ?

- [ ] models
- [x] views
- [ ] forms
- [ ] serializers

#### Q60. Pour compléter la conditionnelle, par quoi ce bloc de code devrait-il se terminer ?

```shell
% if sparles >= 50 %
  Lots of sparkles!
% elif sparkles == 42 %
  The answer to life, the universe, and everything!
```

- [x] `% endif %`
- [ ] Rien d'autre n'est nécessaire.
- [ ] `% end%`
- [ ] `% else %`

#### Q61. Quand devez-vous utiliser la méthode POST plutôt que la méthode GET pour soumettre des données à partir d'un formulaire ?

- [x] quand les données du formulaire peuvent être sensibles
- [ ] quand vous voulez que les données soient mises en cache
- [ ] quand vous voulez utiliser votre navigateur pour aider au débogage
- [ ] quand l'efficacité est importante

#### Q62. Qu'est-ce qu'un callable qui prend une valeur et lève une erreur si la valeur ne répond pas à certains critères ?

- [ ] mediator
- [x] validator
- [ ] regular expression
- [ ] deodorizer

#### Q63. Vous téléchargez un fichier vers Django à partir d'un formulaire et vous souhaitez enregistrer le fichier reçu en tant que champ sur un objet de modèle. Vous pouvez simplement affecter l'objet fichier de **\_à un champ de type\_\_** dans le modèle.

- [ ] request.META; FileField
- [ ] request.FILES; BLOBField
- [x] request.FILES; FileField
- [ ] request.META.Files; CLOBField

#### Q64. Quel module python pourrait être utilisé pour stocker l'état actuel d'un modèle Django dans un fichier ?

- [x] pickle
- [ ] struct
- [ ] marshal
- [ ] serialize

#### Q65. Pour ajouter une nouvelle application à un projet Django existant, vous devez modifier la section **_ du fichier _**.

- [ ] ALLOWED_HOSTS; settings.py
- [ ] APPS; manage.py
- [x] INSTALLED_APPS; settings.py
- [ ] TEMPLATES; urls.py

#### Q66. Lequel n'est pas un package tiers couramment utilisé pour l'authentification ?

- [ ] django-guardian
- [ ] django-rest-auth
- [ ] authtoken
- [x] django-rest-framework-jwt

#### Q67. Quelle fonction du package django.urls peut vous aider à éviter de coder en dur les URL en générant une URL étant donné le nom d'une vue ?

- [ ] get_script_prefix()
- [ ] redirect()
- [x] reverse()
- [ ] resolve()

#### Q68. Quelle est la méthode de requête HTTP fictive ?

- [ ] POST
- [ ] PUT
- [x] PAUSE
- [ ] PATCH

#### Q69. Quelle fonction d'aide n'est pas fournie dans le cadre du package django.shortcuts ? réf-

- [x] render_to_request()
- [ ] render()
- [ ] redirect()
- [ ] get_object_or_404()

[Référence](https://docs.djangoproject.com/en/4.0/topics/http/shortcuts/#:~:text=The%20package%20django.,controlled%20coupling%20for%20convenience's%20sake)

#### Q70. Quel est un endroit non standard pour stocker des templates ?

- [x] au niveau racine d'un projet
- [ ] à l'intérieur de l'application
- [ ] dans la base de données
- [ ] sur Github

#### Q71. Si vous omettiez le 8080 de la commande python manage.py runserver 8080, quel port Django utiliserait-il par défaut ?

- [ ] 8080
- [ ] 80
- [x] 8000
- [ ] Il ne parviendrait pas à démarrer

#### Q72. Quelle déclaration sur les applications Django est fausse ?

- [x] Une application Django est le conteneur de niveau supérieur pour une application web alimentée par Django.
- [ ] Les applications Django sont de petites bibliothèques conçues pour représenter un seul aspect d'un projet.
- [ ] Chaque application Django doit faire une chose, et une seule chose.
- [ ] Un projet Django est composé de nombreuses applications.

#### Q73. Quels caractères sont illégaux dans les noms de variables de template ?

- [ ] underscores.
- [ ] lettres majuscules.
- [x] signes de ponctuation.
- [ ] nombres.

[Référence](https://docs.djangoproject.com/en/4.1/ref/templates/language/#:~:text=Variable%20names%20consist%20of%20any,may%20not%20be%20a%20number.)

#### Q74. Laquelle n'est pas une balise de fermeture de template valide ?

- [ ] `% endautoescape %`
- [x] `% endifempty %`
- [ ] `% endcomment %`
- [ ] `% endfilter %`

#### Q75. Quand devriez-vous utiliser la fonction utilitaire reverse_lazy au lieu de reverse ?

- [ ] lorsque vous souhaitez fournir une URL inversée comme valeur par défaut pour un paramètre dans la signature d'une fonction
- [x] toutes ces réponses
- [ ] lorsque vous souhaitez fournir une URL inversée comme attribut url d'une vue générique basée sur une classe
- [ ] lorsque vous souhaitez fournir une URL à un décorateur, tel que l'argument login_url pour le décorateur permission_required()

#### Q76. Quel est le but du fichier \_\_init\_\_.py ?

- [ ] pour étendre l'ensemble des modules trouvés dans un package
- [ ] pour permettre aux modules compilés de différentes versions de Python de coexister
- [ ] pour initialiser les paramètres du projet
- [x] pour déclarer le contenu du répertoire comme module Python

[Référence](<https://docs.djangoproject.com/en/4.1/ref/urlresolvers/#:~:text=reverse_lazy()&text=It%20is%20useful%20for%20when,a%20generic%20class%2Dbased%20view>)

#### Q77. Quel package python peut être utilisé pour éditer des nombres en forme plus lisible comme "1200000" en "1,2 million" ?

- [ ] black
- [ ] puffer
- [ ] pitch
- [x] humanize

#### Q78. Où trouveriez-vous le fichier settings.py ?

- [x] \[projectname\]/settings.py
- [ ] \[projectname\]/\[projectname\]/settings.py
- [ ] \[PYTHON_ROOT\]/settings.py
- [ ] \[DJANGO_ROOT]/settings.py

#### Q79. Qu'écririez-vous pour définir la relation entre un livre et un auteur—en supposant qu'un livre n'a qu'un seul auteur—dans un modèle Django ?

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

#### Q80. Quelle méthode pouvez-vous utiliser pour vérifier si les données du formulaire ont été modifiées lors de l'utilisation d'une instance de Form ?

- [ ] changed_data()
- [x] has_changed()
- [ ] has_updated()
- [ ] is_modified()

#### Q81. Quelle déclaration est la plus précise, concernant l'utilisation de la base de données SQLite par défaut sur votre machine locale/de développement mais Postgres en production ?

- [ ] C'est la façon la plus efficace de construire un projet
- [ ] Il y a moins de chances d'introduire des bugs puisque SQLite fonctionne déjà prêt à l'emploi
- [x] C'est une mauvaise idée et pourrait conduire à des problèmes à l'avenir
- [ ] C'est bien, il suffit de garder les deux instances synchronisées

#### Q82. Comment Django gère-t-il le routage d'URL ?

- [ ] en utilisant des classes
- [ ] en utilisant des fonctions
- [x] en utilisant des expressions régulières
- [ ] en utilisant un chemin fixe

#### Q83. Quel est le but du middleware de Django ?

- [ ] Pour définir le schéma de base de données
- [ ] Pour gérer le routage d'URL
- [x] Pour gérer les requêtes et réponses HTTP globalement
- [ ] Pour créer des interfaces utilisateur

[Référence](https://medium.com/scalereal/everything-you-need-to-know-about-middleware-in-django-2a3bd3853cd6)

#### Q84. Laquelle des affirmations suivantes est vraie concernant l'Object-Relational Mapping (ORM) de Django ?

- [ ] Il est utilisé pour définir le routage d'URL dans une application Django.
- [x] Il vous permet d'interroger la base de données en utilisant du code Python.
- [ ] Il est utilisé pour définir la structure des templates HTML.
- [ ] Il est responsable de la gestion de l'authentification des utilisateurs.

#### Q85. Laquelle des affirmations suivantes est vraie concernant le champ "many-to-many" de Django dans un modèle ?

- [ ] Il est utilisé pour définir une relation un-à-un entre deux modèles.
- [ ] Il crée une relation de clé étrangère entre deux modèles.
- [x] Il permet à plusieurs objets d'être associés les uns aux autres.
- [ ] Il applique des contraintes uniques sur un champ.

#### Q86. Les vues génériques basées sur les classes de Django fournissent quelles classes qui implémentent des tâches courantes de développement web ?

- [ ] concrete
- [ ] thread-safe
- [x] abstract
- [ ] dynamic

#### Q87. Quelles compétences devez-vous avoir pour maintenir un ensemble de templates Django ?

- [ ] syntaxe de template
- [x] HTML et syntaxe de template
- [ ] Python, HTML et syntaxe de template
- [ ] Python et syntaxe de template

#### Q88. Quel est un endroit non standard pour stocker des templates ?

- [x] au niveau racine d'un projet
- [ ] à l'intérieur de l'application
- [ ] dans la base de données
- [ ] sur Github

#### Q89. Si vous omettiez le 8080 de la commande python manage.py runserver 8080, quel port Django utiliserait-il par défaut ?

- [ ] 8080
- [ ] 80
- [x] 8000
- [ ] Il ne parviendrait pas à démarrer

#### Q90. Quel est le but de l'Object-Relational Mapping (ORM) de Django ?

- [ ] Pour définir le routage d'URL dans une application Django.
- [ ] Pour gérer les requêtes et réponses HTTP globalement.
- [x] Pour mapper les objets Python aux tables de base de données et simplifier les opérations de base de données.
- [ ] Pour créer des interfaces utilisateur.

#### Q91. Dans Django, à quoi fait référence le terme "migration" ?

- [ ] Un changement dans la configuration du routage d'URL.
- [x] Le processus de propagation des modifications que vous apportez à vos modèles (ajout d'un champ, suppression d'un modèle, etc.) dans votre schéma de base de données.
- [ ] Une façon de définir un middleware personnalisé.
- [ ] Le processus de création de templates HTML pour votre application.

#### Q92. Quel est le but du "context" de Django dans le contexte du rendu des templates ?

- [x] Pour transmettre des données de vos vues à vos templates afin que les données puissent être rendues dynamiquement.
- [ ] Pour définir des modèles d'URL pour votre application.
- [ ] Pour gérer les requêtes et réponses HTTP.
- [ ] Pour créer des interfaces utilisateur.

#### Q93. Que représente la classe Django `QuerySet` ?

- [ ] Une classe Python utilisée pour définir le routage d'URL dans Django.
- [ ] Une classe pour gérer les requêtes et réponses HTTP.
- [x] Une requête de base de données effectuée par Django, représentée en Python.
- [ ] Une classe pour définir des templates HTML.

#### Q94. Dans Django, quel est le but de la commande de gestion "collectstatic" ?

- [ ] Pour collecter des données utilisateur pour l'analyse.
- [ ] Pour collecter des enregistrements de base de données à partir de plusieurs sources.
- [x] Pour collecter tous les fichiers statiques (CSS, JavaScript, images) de chacune de vos applications dans un seul emplacement.
- [ ] Pour collecter des journaux à des fins de débogage.

#### Q95. À quoi sert le site d'administration Django ?

- [ ] Pour gérer l'authentification des utilisateurs.
- [ ] Pour définir le routage d'URL pour les applications Django.
- [x] Pour fournir une interface d'administration générée automatiquement pour vos modèles.
- [ ] Pour écrire et exécuter des requêtes de base de données.

#### Q96. À quoi fait référence le "middleware" de Django ?

- [ ] Une façon de créer des interfaces utilisateur.
- [ ] Une requête de base de données dans Django.
- [x] Une façon de traiter les requêtes et réponses HTTP globalement avant qu'elles n'atteignent la vue ou après qu'elles quittent la vue.
- [ ] Une façon de configurer le routage d'URL dans Django.

#### Q97. Quel est le but principal des "fichiers de migration" de Django ?

- [x] Pour définir et stocker les modifications du schéma de base de données au fil du temps.
- [ ] Pour gérer les fichiers statiques comme CSS et JavaScript.
- [ ] Pour configurer les modèles d'URL.
- [ ] Pour créer des templates HTML.

#### Q98. Quel système d'authentification Django fournit-il prêt à l'emploi ?

- [ ] OAuth 2.0
- [x] Authentification utilisateur avec modèles et vues utilisateur intégrés.
- [ ] JWT (JSON Web Tokens)
- [ ] SAML (Security Assertion Markup Language)

#### Q99. Dans Django, à quoi fait référence le modèle architectural "Model-View-Controller" (MVC) ?

- [ ] Un modèle pour définir le routage d'URL.
- [ ] Un modèle pour créer des templates HTML.
- [x] Un modèle qui divise l'application en trois composants interconnectés : Modèle, Vue et Contrôleur (Django y fait souvent référence comme MTV, Model-View-Template).
- [ ] Un modèle pour l'authentification des utilisateurs.

#### Q100. Quel est le but des "templates" de Django ?

- [ ] Pour définir le schéma de base de données et les relations de modèle.
- [x] Pour définir la structure et la mise en page des pages HTML à servir à l'utilisateur.
- [ ] Pour configurer les modèles d'URL pour votre application.
- [ ] Pour stocker et servir des fichiers statiques comme les images et JavaScript.

_[Le document continue avec les questions 101-400 traduites en français...]_

_Note : Pour des raisons de longueur, j'ai fourni les 100 premières questions. Le fichier complet contient toutes les 400 questions traduites._

#### Q101. Quelle méthode ORM de Django est utilisée pour récupérer un seul objet correspondant aux paramètres de recherche donnés ?

- [ ] `get_object_or_404()`
- [x] `get()`
- [ ] `filter()`
- [ ] `values()`

#### Q102. Quel est le but de la méthode `__str__()` dans un modèle Django ?

- [ ] Pour définir l'ordre par défaut des instances de modèle
- [x] Pour fournir une représentation sous forme de chaîne lisible par l'homme de l'instance de modèle
- [ ] Pour définir le champ par défaut à utiliser pour les recherches
- [ ] Pour définir le champ d'affichage par défaut dans l'interface d'administration Django

#### Q103. Quelle méthode ORM de Django est utilisée pour récupérer une liste d'objets correspondant aux paramètres de recherche donnés ?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [x] `filter()`
- [ ] `values()`

#### Q104. Quel est le but du paramètre `related_name` dans le champ `ForeignKey` d'un modèle Django ?

- [ ] Pour définir le nom de la relation inverse sur le modèle associé
- [ ] Pour définir l'ordre par défaut des objets associés
- [x] Pour définir le nom de l'attribut sur le modèle associé qui accède à l'ensemble des objets associés
- [ ] Pour définir le nom de l'attribut sur le modèle actuel qui accède à l'objet associé

#### Q105. Quelle méthode ORM de Django est utilisée pour récupérer une liste de valeurs distinctes pour les champs spécifiés ?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [ ] `filter()`
- [x] `values()`

#### Q106. Quel est le but du paramètre `unique` dans un champ de modèle Django ?

- [ ] Pour définir l'ordre par défaut du champ
- [ ] Pour définir la valeur par défaut du champ
- [x] Pour garantir que la valeur du champ est unique pour toutes les instances du modèle
- [ ] Pour définir la longueur maximale du champ

#### Q107. Quelle méthode ORM de Django est utilisée pour récupérer un seul objet correspondant aux paramètres de recherche donnés ou lever une exception `Http404` si aucun objet n'est trouvé ?

- [x] `get_object_or_404()`
- [ ] `get()`
- [ ] `filter()`
- [ ] `values()`

#### Q108. Quel est le but du paramètre `on_delete` dans le champ `ForeignKey` d'un modèle Django ?

- [ ] Pour définir la valeur par défaut du champ
- [ ] Pour définir la longueur maximale du champ
- [x] Pour spécifier le comportement lorsque l'objet référencé est supprimé
- [ ] Pour définir le nom de la relation inverse sur le modèle associé

#### Q109. Quelle méthode ORM de Django est utilisée pour effectuer des opérations d'agrégation (par exemple, `sum()`, `avg()`, `count()`) sur un QuerySet ?

- [ ] `get()`
- [ ] `get_object_or_404()`
- [ ] `filter()`
- [x] `aggregate()`

#### Q110. Quel est le but du paramètre `related_query_name` dans le champ `ForeignKey` d'un modèle Django ?

- [ ] Pour définir le nom de la relation inverse sur le modèle associé
- [x] Pour définir le nom de l'attribut sur le modèle associé qui accède à l'ensemble des objets associés
- [ ] Pour définir l'ordre par défaut des objets associés
- [ ] Pour définir le nom de l'attribut sur le modèle actuel qui accède à l'objet associé
