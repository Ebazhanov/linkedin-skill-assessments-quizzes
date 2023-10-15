## Rust (langage de programmation)

#### Q1. Quel type de conversion préserve la valeur mathématique dans tous les cas ?

- [ ] i64 comme i32
- [ ] utiliser comme u64
- [x] i32 comme i64
- [ ] f64 comme f32

#### Q2. Que représentent les barres verticales ici ?

```rouille
str::thread::spawn(|| {
     println!("LinkedIn");
});
```

- [x] une fermeture
- [ ] un fil
- [ ] un futur
- [ ] un bloc

[référence](https://doc.rust-lang.org/book/ch13-01-closures.html#refactoring-with-closures-to-store-code)

#### Q3. Quel choix n’est pas un type de données scalaire ?

- [ ] entier
- [ ] flotter
- [ ] booléen
- [x] tuple

#### Q4. **\_** ne peut pas être déstructuré.

- [x] Caractéristiques
- [ ] Tuples
- [ ] Énumérations
- [ ] Structures

[référence](https://rust-lang.github.io/rfcs/2909-destructuring-assignment.html)

#### Q5. Quelle commande « cargo » vérifie les erreurs d'un programme sans créer d'exécutable binaire ?

-[ ] cargo --version

- [ ] initialisation du fret
- [ ] construction de marchandises
- [x] contrôle de fret

#### Q6. Le terme _box_ et les expressions associées telles que _boxing a value_ sont souvent utilisés en relation avec la disposition de la mémoire. À quoi _box_ fait-il référence ?

- [ ] Cela crée un pointeur sur le tas qui pointe vers une valeur sur la pile.
- [x] Cela crée un pointeur sur la pile qui pointe vers une valeur sur le tas.
- [ ] Cela crée une garde de mémoire autour des valeurs pour empêcher tout accès illégal.
- [ ] C'est une abstraction qui fait référence à la propriété. Les valeurs « encadrées » sont clairement étiquetées.

#### Q7. Quelle est une autre manière d'écrire « slice » qui produit le même résultat ?

```rouille
...
let s = String::form("bonjour");
laissez tranche = &s[0..2];
```

- [ ] let slice = &s[len + 2];
- [ ] let slice = &s[len - 2];
- [ ] let slice = &s.copy(0..2);
- [x] let slice = &s[..2];

#### Q8. Utiliser l'opérateur `?` à la fin d'une expression équivaut à **\_**.

- [ ] un modèle de correspondance qui se ramifie en Vrai ou Faux
- [ ] appelant ok_error()
- [ ] appelant à la panique !()
- [x] un modèle de correspondance pouvant entraîner un retour anticipé

#### Q9. Quelle est la syntaxe valide pour définir un tableau de valeurs i32 ?

- [ ] Tableau<i32>::with_capacity(10)
- [ ] [i32]
- [ ] Tableau<i32>::new(10)
- [x] [i32; dix]

#### Q10. Quelle syntaxe est requise pour prendre une référence mutable à T, lorsqu'elle est utilisée dans un argument de fonction ?

```rouille
incrément fn (i : T) {
     // corps élidé
}
```

- [ ] \*mut T
- [ ] mut réf T
- [ ] mut&T
- [x] &mut T

#### Q11. Les pointeurs intelligents Rc et Arc assurent le comptage de références. Quelle est l'API permettant d'incrémenter un nombre de références ?

- [ ] .ajouter()
- [ ] .incr()
- [x] .clone()
- [ ] .increment()

[référence](https://doc.rust-lang.org/book/ch15-04-rc.html)

#### Q12. Que se passe-t-il lorsqu'une erreur se produit et est gérée par l'opérateur point d'interrogation (?) ?

- [ ] L'erreur est signalée et l'exécution continue.
- [ ] Une exception est levée. Le(s) effet(s) de l'exception sont définis par l'erreur ! macro.
- [ ] Le programme panique immédiatement.
- [x] Rust tente de convertir l'erreur en type d'erreur de la fonction locale et de la renvoyer sous la forme Result::Err. Si cela échoue, le programme panique.

#### Q13. Quelle syntaxe de commentaire n'est pas légale ?

- [ ] `/*`
- [x] `#`
- [ ] `//!`
- [ ] `//`

#### Q14. Dans les modèles de correspondance, les valeurs sont ignorées avec \_.

- [ ] `.ignorer()`
- [ ] `un trait de soulignement (_)`
- [x] ..
- [ ] sauter

#### Q15. Définir un \_ nécessite un paramètre de durée de vie.

- [ ] fonction qui met fin à la durée de vie d'un de ses arguments
- [x] structure qui contient une référence à une valeur
- [ ] fonction avec un argument générique
- [ ] structure qui contient une référence à une valeur encadrée

[Référence du livre Rust](https://doc.rust-lang.org/book/ch10-03-lifetime-syntax.html#lifetime-annotations-in-struct-definitions)

#### Q16. Quel exemple utilise correctement l'API d'entrée de std::collections::HashMap pour renseigner les décomptes ?

```rouille
utilisez std :: collections :: HashMap ;
fn main() {
     laissez mut counts = HashMap::new();
     let text = "LinkedIn Learning";
     pour c dans text.chars() {
         // Complétez ce bloc
     }
     println!("{:?}", compte);
}
```

- [ ] &timide;

```rouille
pour c dans text.chars() {
     si let Some(count) = &mut counts.get(&c) {
         counts.insert(c, *count + 1);
     } autre {
         counts.insert(c, 1);
     } ;
}
```

- [x] &timide;

```rouille
pour c dans text.chars() {
     let count = counts.entry(c).or_insert(0);
     *compte += 1 ;
}
```

- [ ] &timide;

```rouille
pour c dans text.chars() {
     laissez count = counts.entry(c);
     *compte += 1 ;
}
```

- [ ] &timide;

```rouille
pour c dans text.chars() {
     counts.entry(c).or_insert(0).map(|x| x + 1);
}
```

[référence](https://doc.rust-lang.org/std/collections/hash_map/struct.HashMap.html#method.entry)

#### Q17. Quel fragment n'entraîne pas d'allocation de mémoire lors de l'écriture dans un "fichier" (représenté par un Vec<u8>) ?

```rouille
utilisez std :: collections :: HashMap ;

fn main() -> Résultat<(), Box<dyn std::error::Error>> {
     soit mut v = Vec::<u8>::new();

     laissez a = "LinkedIn" ;
     soit b = 123 ;
     soit c = '🧀';

     // remplace cette ligne

     println!("{:?}", v);

     D'accord(())
}
```

- [x] :

```rouille
écrire!(&mut v, "{}{}{}", a, b, c) ?;
```

- [ ] :

```rouille
v.écrire(a) ?;
v.write(b) ?;
v.write(c) ?;
```

- [ ] :

```rouille

```
