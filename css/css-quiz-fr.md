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

#### Q16. Lorsque des éléments se chevauchent, ils sont ordonnés sur l'axe z (c'est-à-dire quel élément en couvre un autre). La propriété z-index peut être utilisée pour spécifier l'ordre z des éléments chevauchants. Quel ensemble d'affirmations concernant la propriété z-index est vrai ?

- [x] Les valeurs de z-index plus élevées apparaissent au-dessus des éléments avec une valeur de z-index inférieure. Des nombres négatifs et positifs peuvent être utilisés. z-index ne peut être utilisé que sur des éléments positionnés.
- [ ] Les valeurs de z-index plus faibles apparaissent au-dessus des éléments avec une valeur de z-index plus élevée. Des nombres négatifs et positifs peuvent être utilisés. z-index doit également être utilisé avec des éléments positionnés.
- [ ] Les valeurs de z-index plus élevées apparaissent au-dessus des éléments avec une valeur de z-index inférieure. Seuls des nombres positifs peuvent être utilisés. z-index doit également être utilisé avec des éléments positionnés.
- [ ] Les valeurs de z-index plus faibles apparaissent au-dessus des éléments avec une valeur de z-index plus élevée. Des nombres négatifs et positifs peuvent être utilisés. z-index peut être utilisé avec ou sans éléments positionnés.

**Note :** une alternative à la question ci-dessous.

#### Q17. Lorsque des éléments à l'intérieur d'un conteneur se chevauchent, la propriété z-index peut être utilisée pour indiquer comment ces éléments sont empilés les uns sur les autres. Quel ensemble d'affirmations est vrai ?

- [x] A

```
  1. Les valeurs de z-index plus élevées apparaissent au-dessus des éléments avec une valeur de z-index inférieure.
  2. Des nombres négatifs et positifs peuvent être utilisés.
  3. La propriété z-index peut être utilisée uniquement sur des éléments positionnés.
```

- [ ] B

```
  1. Les valeurs de z-index plus faibles apparaissent au-dessus des éléments avec une valeur de z-index plus élevée.
  2. Des nombres négatifs et positifs peuvent être utilisés.
  3. La propriété z-index peut être utilisée avec ou sans éléments positionnés.
```

- [ ] C

```
  1. Les valeurs de z-index plus faibles apparaissent au-dessus des éléments avec une valeur de z-index plus élevée.
  2. Des nombres négatifs et positifs peuvent être utilisés.
  3. La propriété z-index doit également être utilisée avec des éléments positionnés.
```

- [ ] D

```
  1. Les valeurs de z-index plus élevées apparaissent au-dessus des éléments avec une valeur de z-index inférieure.
  2. Seuls des nombres positifs peuvent être utilisés.
  3. La propriété z-index doit également être utilisée avec des éléments positionnés.
```

**Note :** une alternative à la question ci-dessous.

#### Q18. Quelle est la différence entre les paramètres line-height suivants ?

```css
line-height: 20px;
line-height: 2;
```

- [x] La valeur de 20px définira la hauteur de ligne à 20px. La valeur de 2 définira la hauteur de ligne à deux fois la taille de police correspondante.
- [ ] La valeur de 20px définira la hauteur de ligne à 20px. La valeur de 2 n'est pas valide.
- [ ] La valeur de 20px définira la hauteur de ligne à 20px. La valeur de 2 se traduira par une valeur par défaut de 2px.
- [ ] La valeur de 20px définira la hauteur de ligne à 20px. La valeur de 2 définira la hauteur de ligne à 20 % de la taille de police correspondante.

#### Q19. Dans l'exemple suivant, quelle couleur sera appliquée au paragraphe un et au paragraphe deux ?

```HTML
<section>
  <p>paragraphe un</p>
</section>

<p>paragraphe deux</p>
```

```css
section p {
  color: red;
}
section + p {
  color: blue;
}
```

- [ ] Le paragraphe un sera en bleu, et le paragraphe deux sera en rouge.
- [ ] Les deux paragraphes seront en bleu.
- [x] Le paragraphe un sera en rouge, et le paragraphe deux sera en bleu.
- [ ] Les deux paragraphes seront en rouge.

#### Q20. Quelles sont trois manières valides d'ajouter du CSS à une page HTML ?

- [ ] A

```
  1. Externe ; le CSS est écrit dans un fichier séparé.
  2. En ligne ; le CSS est ajouté dans la balise <head> de la page HTML.
  3. Interne ; le CSS est inclus dans les balises HTML.
```

- [ ] B

```
  1. Externe ; le CSS est écrit dans un fichier séparé et est lié à l'élément <header> du fichier HTML.
  2. En ligne ; le CSS est ajouté à la balise HTML.
  3. Interne ; le CSS est inclus dans l'élément <header> du fichier HTML.
```

- [ ] C

```
  1. Externe ; le CSS est écrit dans un fichier séparé et est lié à l'élément <head> du fichier HTML.
  2. Interne ; le CSS est inclus dans l'élément <header> du fichier HTML.
  3. En ligne ; le CSS est ajouté à la balise HTML.
```

- [x] D

```


  1. Externe ; le CSS est écrit dans un fichier séparé et est lié à l'élément <head> du fichier HTML.
  2. En ligne ; le CSS est ajouté à la balise HTML.
  3. Interne ; le CSS est inclus dans l'élément <head> du fichier HTML.
```

#### Q21. Quelle affirmation est vraie concernant le format d'image SVG ?

- [ ] Le CSS peut être appliqué aux SVG, mais JavaScript ne le peut pas.
- [ ] Les SVG fonctionnent mieux pour créer des graphiques 3D.
- [x] Les SVG peuvent être créés comme des graphiques vectoriels ou codés à l'aide d'éléments spécifiques aux SVG tels que <svg>, <line> et <ellipse>.
- [ ] Les SVG sont un langage de balisage basé sur HAML pour créer des graphiques vectoriels.

#### Q22. Dans l'exemple ci-dessous, quand la couleur rose sera-t-elle appliquée à l'élément ancre ?

```css
a:active {
  color: pink;
}
```

- [ ] La couleur du lien s'affichera en rose après avoir été cliquée ou lorsque la souris survole le lien.
- [ ] La couleur du lien s'affichera en rose au survol de la souris.
- [x] La couleur du lien s'affichera en rose pendant que le lien est cliqué, avant que le clic de la souris soit relâché.
- [ ] La couleur du lien s'affichera en rose avant d'avoir été cliquée.

#### Q23. Pour changer la couleur d'un SVG à l'aide de CSS, quelle propriété est utilisée ?

- [ ] Utilisez background-fill pour définir la couleur à l'intérieur de l'objet et stroke ou border pour définir la couleur de la bordure.
- [ ] La couleur ne peut pas être modifiée avec CSS.
- [ ] Utilisez fill ou background pour définir la couleur à l'intérieur de l'objet et stroke pour définir la couleur de la bordure.
- [x] Utilisez fill pour définir la couleur à l'intérieur de l'objet et stroke pour définir la couleur de la bordure.

#### Q24. Lorsque vous utilisez position: fixed, l'élément sera toujours positionné par rapport à quoi ?

- [ ] à l'élément le plus proche avec position: relative
- [x] à la fenêtre d'affichage
- [ ] à l'élément parent
- [ ] à l'élément de conteneur

#### Q25. Par défaut, une image d'arrière-plan se répétera \_

- [ ] uniquement si la propriété background-repeat est définie sur repeat
- [x] indéfiniment, verticalement et horizontalement
- [ ] indéfiniment sur l'axe horizontal uniquement
- [ ] une fois, sur les axes x et y

#### Q26. Lors de l'utilisation de media queries, les types de média sont utilisés pour cibler une catégorie de périphérique. Quel choix liste les types de média valides actuels ?

- [ ] imprimer, écran, auditif
- [ ] imprimer, écran, télévision
- [x] imprimer, écran, vocal
- [ ] imprimer, vocal, dispositif

#### Q27. Comment pouvez-vous rendre la première lettre de chaque paragraphe de la page en rouge ?

- [x] p::first-letter { color: red; }
- [ ] p:first-letter { color: red; }
- [ ] first-letter::p { color: red; }
- [ ] first-letter:p { color: red; }

#### Q28. Dans cet exemple, quel est le sélecteur, la propriété et la valeur ?

```css
p {
  color: #000000;
}
```

- [ ] A

```
  "p" est le sélecteur
  "#000000" est la propriété
  "couleur" est la valeur
```

- [x] B

```
  "p" est le sélecteur
  "couleur" est la propriété
  "#000000" est la valeur
```

- [ ] C

```
  "couleur" est le sélecteur
  "#000000" est la propriété
  "#p" est la valeur
```

- [ ] D

```
  "couleur" est le sélecteur
  "p" est la propriété
  "#000000" est la valeur
```

#### Q29. Sur quoi est basée l'unité rem ?

- [ ] L'unité rem est relative à la taille de police de l'élément p.
- [ ] Vous devez définir la valeur de l'unité rem en écrivant une déclaration telle que rem { font-size: 1px ; }.
- [ ] L'unité rem est relative à la taille de police de l'élément contenant (parent).
- [x] L'unité rem est relative à la taille de police de l'élément racine de la page.

#### Q30. Quel choix donnerait à un élément de bloc des coins arrondies ?

- [ ] `corner-radius: 10px ;`
- [ ] `border-corner: 10px ;`
- [ ] `corner-curve: 10px ;`
- [x] `border-radius: 10px ;`

[Documentation officielle :](https://www.w3schools.com/css/css3_borders.asp)
