## CSS

#### Q1. Parmi ces sélecteurs, quel sélecteur a la spécificité la plus élevée pour la sélection de l'élément de lien d'ancre ?

```css
ul li a
a
.example a
div a
```

- [x] `.example a`
- [ ] `div a`
- [ ] `a`
- [ ] `ul li a`

#### Q2. En utilisant un sélecteur d'attribut, comment sélectionneriez-vous un élément `<a>` avec un attribut "title" ?

- [x] `a[title]{...}`
- [ ] `a > title {...}`
- [ ] `a.title {...}`
- [ ] `a=title {...}`

**Remarque:** une alternative à la question ci-dessous.

#### Q3. Quel est le sélecteur CSS pour une balise `<a>` contenant l'attribut title ?

- [x] `a[title]`
- [ ] `a > title`
- [ ] `a=title`
- [ ] `a.title`

**Remarque:** une alternative à la question ci-dessus.

#### Q4. CSS Grid et Flexbox deviennent de plus en plus populaires pour créer des mises en page de page. Cependant, les flottants sont toujours couramment utilisés, en particulier lors de la manipulation d'une base de code plus ancienne ou si vous devez prendre en charge des versions plus anciennes des navigateurs. Quelles sont deux techniques valides utilisées pour effacer les flottants ?

- [ ] Utiliser le "clearfix hack" sur l'élément flottant et ajouter un flottement à l'élément parent.
- [ ] Utiliser la propriété overflow sur l'élément flottant ou le "clearfix hack" sur l'élément flottant ou parent.
- [ ] Utiliser le "clearfix hack" sur l'élément flottant ou la propriété overflow sur l'élément parent.
- [x] Utiliser le "clearfix hack" sur l'élément parent ou utiliser la propriété overflow avec une valeur autre que "visible".

#### Q5. Quel(s) élément(s) correspondent aux sélecteurs suivants ?

```css
1) .nav {
  ...;
}
2) nav {
  ...;
}
3) #nav {
  ...;
}
```

- [ ] A

```
  1. Un élément avec un ID "nav"
  2. Un élément nav
  3. Un élément avec une classe "nav"
```

- [ ] B `Ils ciblent tous le même élément nav.`
- [x] C

```
  1. Un élément avec une classe "nav"
  2. Un élément nav
  3. Un élément avec un ID "nav"
```

- [ ] D

```
  1. Un élément avec une classe "nav"
  2. Un élément nav
  3. Un div avec un ID "nav"
```

#### Q6. Lors de l'ajout de styles de transparence, quelle est la différence entre l'utilisation de la propriété opacity et de la propriété background avec une valeur `rgba()` ?

- [ ] L'opacité spécifie le niveau de transparence des éléments enfants. L'arrière-plan avec une valeur `rgba()` applique la transparence uniquement à la couleur de fond.
- [ ] L'opacité applique la transparence uniquement à la couleur de fond. L'arrière-plan avec une valeur `rgba()` spécifie le niveau de transparence d'un élément dans son ensemble, y compris son contenu.
- [x] L'opacité spécifie le niveau de transparence d'un élément, y compris son contenu. L'arrière-plan avec une valeur `rgba()` applique la transparence uniquement à la couleur de fond.
- [ ] L'opacité applique la transparence aux éléments parents et enfants. L'arrière-plan avec une valeur `rgba()` spécifie le niveau de transparence de l'élément parent uniquement.

#### Q7. Qu'est-ce qui est vrai des éléments de bloc et d'éléments en ligne ?

- [ ] Par défaut, les éléments de bloc ont la même hauteur et largeur que le conteneur de contenu entre leurs balises ; les éléments en ligne s'étendent sur toute la largeur de leur conteneur.
- [x] Par défaut, les éléments de bloc s'étendent sur toute la largeur de leur conteneur ; les éléments en ligne ont la même hauteur et largeur que le contenu contenu entre leurs balises.
- [ ] Un élément `<nav>` est un exemple d'élément en ligne. `<header>` est un exemple d'élément de bloc.
- [ ] Un `<span>` est un exemple d'élément de bloc. `<div>` est un exemple d'élément en ligne.

#### Q8. CSS Grid a introduit une nouvelle unité de longueur, fr, pour créer des pistes de grille flexibles. En vous référant à l'exemple de code ci-dessous, quelles seront les largeurs des trois colonnes ?

```css
.grid {
  display: grid;
  width: 500px;
  grid-template-columns: 50px 1fr 2fr;
}
```

- [ ] La première colonne aura une largeur de 50px. La deuxième colonne fera 50px de large et la troisième colonne fera 100px de large.
- [x] La première colonne aura une largeur de 50px. La deuxième colonne fera 150px de large et la troisième colonne fera 300px de large.
- [ ] La première colonne aura une largeur de 50px. La deuxième colonne fera 300px de large et la troisième colonne fera 150px de large.
- [ ] La première colonne aura une largeur de 50px. La deuxième colonne fera 500px de large et la troisième colonne fera 1000px de large.

**Remarque:** une alternative à la question ci-dessous.

#### Q9. Si la largeur du conteneur est de 500 pixels, quelle sera la largeur des trois colonnes dans cette disposition ?

`.grid { display: grid; grid-template-columns: 50px 1fr 2fr; }`

- [x] 50px, 150px, 300px
- [ ] 50px, 200px, 300px
- [ ] 50px, 100px, 200px
- [ ] 50px, 50px, 100px

**Remarque:** une alternative à la question ci-dessus.

#### Q10. À quoi sert la propriété line-height ?

- [x] pour contrôler la hauteur de l'es

pace entre deux lignes de contenu

- [ ] pour contrôler la hauteur de l'espace entre les éléments de titre
- [ ] pour contrôler la hauteur de la taille des caractères
- [ ] pour contrôler la largeur de l'espace entre les caractères

#### Q11. Trois de ces choix sont vrais concernant les sélecteurs de classe. Lequel n'est pas vrai ?

- [ ] Plusieurs classes peuvent être utilisées dans le même élément.
- [ ] La même classe peut être utilisée plusieurs fois par page.
- [ ] Les sélecteurs de classe commencent par un point initial.
- [x] Les classes peuvent être utilisées plusieurs fois par page, mais pas au sein du même élément.

**Remarque:** une alternative à la question ci-dessous.

#### Q12. Qu'est-ce qui n'est pas vrai à propos des sélecteurs de classe ?

- [x] Une seule valeur de classe peut être attribuée à un élément.
- [ ] Un élément peut avoir plusieurs valeurs de classe.
- [ ] Les sélecteurs de classe sont précédés d'un point.
- [ ] Plus d'un élément peut avoir la même valeur de classe.

#### Q13. Il existe de nombreuses propriétés qui peuvent être utilisées pour aligner des éléments et créer des mises en page de page, telles que float, position, flexbox et grid. Parmi ces quatre propriétés, laquelle devrait être utilisée pour aligner une barre de navigation globale qui reste fixe en haut de la page ?

- [x] position
- [ ] flexbox
- [ ] grid
- [ ] float

#### Q14. Dans l'exemple abrégé ci-dessous, quelles propriétés de fond individuelles sont représentées ?

```css
background: blue url(image.jpg) no-repeat scroll 0px 0px;
```

- [x] A

```css
background-color: blue;
background-image: url(image.jpg);
background-repeat: no-repeat;
background-attachment: scroll;
background-position: 0px 0px;
```

- [ ] B

```css
background-color: blue;
background-img: url(image.jpg);
background-repeat: no-repeat;
background-scroll: scroll;
background-size: 0px 0px;
```

- [ ] C

```css
background-color: blue;
background-src: url(image.jpg);
background-repeat: no-repeat;
background-wrap: scroll;
background-position: 0px 0px;
```

- [ ] D

```css
background-color: blue;
background-src: url(image.jpg);
background-repeat: no-repeat;
background-scroll: scroll;
background-position: 0px 0px;
```

#### Q15. Dans cet exemple, selon les règles de cascade et de spécificité, quelle couleur aura le lien ?

```css
.example {
  color: yellow;
}
ul li a {
  color: blue;
}
ul a {
  color: green;
}
a {
  color: red;
}
```

```html
<ul>
  <li><a href="#" class="example">lien</a></li>
  <li>élément de liste</li>
  <li>élément de liste</li>
</ul>
```

- [ ] vert
- [x] jaune
- [ ] bleu
- [ ] rouge
