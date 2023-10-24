I've translated the Python programming questions and answers into French:

#### Q1. Qu'est-ce qu'une classe abstraite ?

- [ ] Une classe abstraite est le nom de n'importe quelle classe à partir de laquelle vous pouvez instancier un objet.
- [ ] Les classes abstraites doivent être redéfinies chaque fois qu'un objet en est instancié.
- [ ] Les classes abstraites doivent hériter de classes concrètes.
- [x] Une classe abstraite existe uniquement pour que d'autres classes "concrètes" puissent en hériter.

[Reference](https://www.geeksforgeeks.org/abstract-classes-in-python/)

#### Q2. Que se passe-t-il lorsque vous utilisez la fonction intégrée `any()` sur une liste ?

- [ ] La fonction `any()` retourne toujours un élément au hasard de la liste.
- [x] La fonction `any()` renvoie True si n'importe quel élément de la liste évalue à True. Sinon, elle renvoie False.
- [ ] La fonction `any()` prend en tant qu'arguments la liste à vérifier à l'intérieur et l'élément à vérifier. Si "quelconque" des éléments de la liste correspondent à l'élément à vérifier, la fonction renvoie True.
- [ ] La fonction `any()` retourne une valeur booléenne qui répond à la question "Y a-t-il des éléments dans cette liste ?"

**Exemple**

```python
if any([True, False, False, False]) == True:
    print('Oui, il y a un True')
>>> 'Oui, il y a un True'
```

#### Q3. À quelle structure de données un arbre binaire dégénère-t-il s'il n'est pas correctement équilibré ?

- [x] Liste chaînée
- [ ] File d'attente
- [ ] Ensemble
- [ ] OrderedDict

[Reference](https://www.scaler.com/topics/linked-list/)

#### Q4. Quelle affirmation sur les méthodes statiques est vraie ?

- [ ] Les méthodes statiques sont appelées statiques car elles renvoient toujours `None`.
- [ ] Les méthodes statiques peuvent être liées soit à une classe, soit à une instance d'une classe.
- [x] Les méthodes statiques servent principalement de méthodes utilitaires ou d'aides car elles ne peuvent pas accéder ni modifier l'état d'une classe.
- [ ] Les méthodes statiques peuvent accéder et modifier l'état d'une classe ou d'une instance d'une classe.

[Reference](https://www.geeksforgeeks.org/class-method-vs-static-method-python)

#### Q5. Qu'est-ce que les attributs ?

- [ ] Les attributs sont des versions longues d'une instruction `if/else`, utilisées lors des tests d'égalité entre des objets.
- [x] Les attributs sont une manière de stocker des données ou de décrire un état pour une classe ou une instance d'une classe.
- [ ] Les attributs sont des chaînes de caractères qui décrivent les caractéristiques d'une classe.
- [ ] Les arguments de fonction sont appelés "attributs" dans le contexte des méthodes de classe et des méthodes d'instance.

**Explication:** Les attributs sont définis sous la classe, et les arguments sont utilisés dans les fonctions. Les arguments font généralement référence aux paramètres, tandis que les attributs sont les constructeurs de la classe ou d'une instance de la classe.

#### Q6. Quel est le terme qui décrit ce code ?

`compteur, fruit, prix = (2, 'pomme', 3.5)`

- [ ] Affectation de tuple.
- [x] Dépaquetage de tuple.
- [ ] Correspondance de tuple.
- [ ] Duplication de tuple.

[Reference](https://www.w3schools.com/python/python_tuples_unpack.asp)

#### Q7. Quelle méthode intégrée de liste utiliseriez-vous pour supprimer des éléments d'une liste ?

- [ ] Méthode `.delete()`
- [ ] `pop(my_list)`
- [ ] `del(my_list)`
- [x] Méthode `.pop()`

[Reference](https://www.w3schools.com/python/ref_list_pop.asp)

**Exemple**

```python
my_list = [1, 2, 3]
my_list.pop(0)
my_list
>>> [2, 3]
```

#### Q8. À quoi sert couramment la bibliothèque `sys` de Python ?

- [x] Capturer les arguments de ligne de commande donnés lors de l'exécution d'un fichier.
- [ ] Connecter divers systèmes, tels que relier une interface web, un service d'API, une base de données et une application mobile.
- [ ] Prendre une capture instantanée de tous les packages et bibliothèques de votre environnement virtuel.
- [ ] Analyser l'état de santé de votre écosystème Python tout en étant dans un environnement virtuel.

[Reference](https://docs.python.org/3/library/sys.html)

#### Q9. Quelle est la complexité temporelle de l'accès à une valeur dans un dictionnaire en utilisant sa clé ?

- [ ] O(n), aussi appelé temps linéaire.
- [ ] O(log n), aussi appelé temps logarithmique.
- [ ] O(n^2), aussi appelé temps quadratique.
- [x] O(1), aussi appelé temps constant.

#### Q10. Quelle est la syntaxe correcte pour définir une classe appelée Game, si elle hérite d'une classe parente appelée LogicGame ?

- [x] `class Game(LogicGame): pass`
- [ ] `def Game(LogicGame): pass`
- [ ] `def Game.LogicGame(): pass`
- [ ] `class Game.LogicGame(): pass`

**Explication:** La classe parente dont on hérite est passée en argument à la classe enfant. Par conséquent, la première option est la bonne réponse.

#### Q11. Quel type de données intégré de Python est couramment utilisé pour représenter une pile (stack) ?

- [ ] `set`
- [x] `list`
- [ ] `None`
- [ ] `dictionnaire`
- [ ] `Vous ne pouvez créer une pile qu'à partir de zéro.`

#### Q12. Que retournerait cette expression ?

```python
annees_college = ['Nouvelle', 'Deuxième année', 'Troisième année', 'Quatrième année']
retourne list(enumerate(annees_college, 2019))
```

- [ ] `[('Nouvelle', 2019), ('Deuxième année', 2020), ('Troisième année', 2021), ('Quatrième année', 2022)]`
- [ ] `[(2019,

2020, 2021, 2022), ('Nouvelle', 'Deuxième année', 'Troisième année', 'Quatrième année')]`

- [ ] `[('Nouvelle', 'Deuxième année', 'Troisième année', 'Quatrième année'), (2019, 2020, 2021, 2022)]`
- [x] `[(2019, 'Nouvelle'), (2020, 'Deuxième année'), (2021, 'Troisième année'), (2022, 'Quatrième année')]`

#### Q13. Quel est le but du mot-clé "self" lors de la définition ou de l'appel des méthodes d'instance ?

- [ ] `self` signifie qu'aucun autre argument n'est requis pour être passé à la méthode.
- [ ] Il n'y a pas de véritable objectif pour la méthode `self`. C'est simplement un jargon historique de l'informatique que Python conserve pour rester cohérent avec d'autres langages de programmation.
- [x] `self` fait référence à l'instance dont la méthode a été appelée.
- [ ] `self` fait référence à la classe dont l'objet a été créé en utilisant `self`.

[Reference](https://www.geeksforgeeks.org/self-in-python-class/)

#### Q14. Quelle caractéristique des "namedtuples" n'est PAS exacte ?

- [ ] Vous pouvez attribuer un nom à chacun des membres de la "namedtuple" et y faire référence de cette manière, de la même manière que vous accéderiez aux clés dans un dictionnaire.
- [ ] Chaque membre d'un objet "namedtuple" peut être indexé directement, tout comme dans un tuple régulier.
- [ ] Les "namedtuples" sont aussi efficaces en termes de mémoire que les tuples réguliers.
- [x] Aucune importation n'est nécessaire pour utiliser les "namedtuples" car elles sont disponibles dans la bibliothèque standard.

**Nous devons les importer en utilisant** : `from collections import namedtuple`

#### Q15. Qu'est-ce qu'une méthode d'instance ?

- [x] Les méthodes d'instance peuvent modifier l'état d'une instance ou l'état de sa classe parente.
- [ ] Les méthodes d'instance stockent des données liées à l'instance.
- [ ] Une méthode d'instance est une fonction régulière qui appartient à une classe, mais elle doit renvoyer `None`.
- [ ] Une méthode d'instance est une méthode de classe qui ne prend pas d'arguments.

#### Q16. Quelle déclaration ne décrit PAS le concept de l'encapsulation en programmation orientée objet ?

- [ ] Elle protège les données contre les interférences extérieures.
- [ ] Une classe parente est encapsulée et aucune donnée de la classe parente ne passe à la classe enfant.
- [ ] Elle permet de regrouper les données et les méthodes qui peuvent manipuler ces données en un seul endroit.
- [x] Elle ne permet que les méthodes de modifier les données.

[Reference](https://www.scaler.com/topics/python/encapsulation-in-python/)
