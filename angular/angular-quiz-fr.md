## Angulaire

#### Q1. Quel est le but du décorateur ViewChild dans cette classe de composants ?

```ts
@Component({
    ...
    template: '<p #bio></p>'
})
export class UserDetailsComponent {
    @ViewChild('bio') bio;
}
```

- \[x] Il permet d’accéder à partir de la classe de composants à l’objet ElementRef pour le `<p>` qui a la variable de référence du modèle bio dans la vue du modèle du composant.
- \[ ] Il indique que le `<p>` doit être rendu en tant qu’enfant de la vue parent qui utilise ce composant.
- \[ ] Il fait le `<p>` dans le modèle prend en charge la projection de contenu.
- \[ ] Il fait le `<p>` visible dans le rendu final. Si le #bio a été utilisé dans le modèle et que le @ViewChild n’a pas été utilisé dans la classe, Angular masque automatiquement le `<p>` qui a #bio dessus.

[DigitalOcean - viewchild-access-component](https://www.digitalocean.com/community/tutorials/angular-viewchild-access-component)

#### Q2. Quelle méthode est utilisée pour connecter un FormControl à un élément d’entrée DOM natif dans des formulaires réactifs ?

- \[ ] Ajoutez le nom de chaîne donné au FormControl à un attribut nommé controls sur le <form> pour indiquer les champs qu’il doit inclure.
- \[ ] Utilisez la syntaxe de liaison entre crochets autour de l’attribut value sur l’élément DOM et définissez-la comme égale à une instance de FormControl.
- \[x] Utilisez la directive formControlName et définissez la valeur égale au nom de chaîne donné au FormControl.
- \[ ] Utilisez le nom de chaîne donné au FormControl comme valeur pour l’attribut ID de l’élément DOM.

[Angular.io - Groupes de formulaires réactifs](https://angular.io/guide/reactive-forms#creating-nested-form-groups)

#### Q3. Quelle est la différence entre le `paramMap` et l' `queryParamMap` sur l' `ActivatedRoute` classe?

- \[ ] Le paramMap est un littéral d’objet des paramètres dans le chemin d’URL d’un itinéraire. La requêteParamMap est un observable de ces mêmes paramètres.
- \[ ] Le paramMap est un Observable qui contient les valeurs de paramètre qui font partie du chemin d’URL d’un itinéraire. QueryParamMap est une méthode qui prend un tableau de clés et est utilisée pour trouver des paramètres spécifiques dans le paramMap.
- \[ ] paramMap est le nom hérité d’Angular 3. Le nouveau nom est queryParamMap.
- \[x] Les deux sont des observables contenant des valeurs de la chaîne d’URL de l’itinéraire demandé. Le paramMap contient les valeurs de paramètre qui se trouvent dans le chemin d’accès à l’URL et le queryParamMap contient les paramètres de requête d’URL.

[StackOverflow](https://stackoverflow.com/a/49617621)

#### Q4. Sur la base de l’utilisation suivante du canal asynchrone et en supposant que le champ de classe utilisateurs est un Observable, combien d’abonnements aux utilisateurs Observable sont effectués ?

```html
<h2>Names</h2>
<div *ngFor="let user of users | async">{{ user.name }}</div>
<h2>Ages</h2>
<div *ngFor="let user of users | async">{{ user.age }}</div>
<h2>Genders</h2>
<div *ngFor="let user of users | async">{{ user.gender }}</div>
```

- \[ ] Aucune. Le canal asynchrone ne s’abonne pas automatiquement.
- \[ ] Aucune. La syntaxe du modèle n’est pas correcte.
- \[x] Trois. Il y en a un pour chaque canal asynchrone.
- \[ ] Un. Le canal asynchrone met en cache observables par type interne.

[UltimateCourses](https://ultimatecourses.com/blog/angular-ngfor-async-pipe)

#### Q5. Comment utiliser HttpClient pour envoyer une requête POST à un point de terminaison à partir d’une fonction addOrder dans cet OrderService ?

```ts
export class OrderService {
  constructor(private httpClient: HttpClient) {}

  addOrder(order: Order) {
    // Missing line
  }
}
```

- \[ ] this.httpClient.url(this.orderUrl).post(order);
- \[ ] this.httpClient.send(this.orderUrl, ordre);
- \[ ] this.httpClient.post<Order>(this.orderUrl, commande);
- \[x] this.httpClient.post<Order>(this.orderUrl, order).subscribe();

[Angular.io - Envoi de données au serveur](https://angular.io/guide/http#sending-data-to-a-server)

#### Q6. Dans quel cas la méthode RouterModule.forRoot est-elle utilisée ?

- \[ ] Enregistrement de tous les fournisseurs que vous avez l’intention d’utiliser dans les composants routés.
- \[x] Enregistrement des définitions d’itinéraire au niveau de l’application racine.
- \[ ] Indiquant qu’Angular devrait encourager vos itinéraires pour réussir.
- \[ ] Déclarer que vous avez l’intention d’utiliser le routage uniquement au niveau racine.

[O ' REILLY](https://www.oreilly.com/library/view/switching-to-angular/9781788620703/c9e90774-0e10-410b-bd20-d3e9e0b8d117.xhtml)

#### Q7. Sur quels éléments DOM ce sélecteur de métadonnées de composant correspondra-t-il ?

```ts
@Component({
    selector: 'app-user-card',
    . . .
})
```

- \[ ] Tout élément avec l’attribut app-user-card, tel que `<div app-user-card></div>`.
- \[ ] La première instance de `<app-user-card></app-user-card>`.
- \[x] Toutes les instances de `<app-user-card></app-user-card>`.
- \[ ] Toutes les instances de `<user-card></user-card>`.

[Angular.io - Métadonnées de composant](https://angular.io/guide/architecture-components#component-metadata)

#### Q8. Quelle est la syntaxe de modèle correcte pour utiliser la directive structurelle ngFor intégrée pour afficher une liste de productNames ?

- \[ ]

```html
<ul>
  <li [ngFor]="let productName of productNames">{{ productName }}</li>
</ul>
```

- \[ ]

```html
<ul>
  <li ngFor="let productName of productNames">{{ productName }}</li>
</ul>
```

- \[x]

```html
<ul>
  <li *ngFor="let productName of productNames">{{ productName }}</li>
</ul>
```

- \[ ]

```html
<ul>
  <? for productName in productNames { ?>
  <li>{{ productName }}</li>
  <? } ?>
</ul>
```

[Angular.io- Directives structurelles](https://angular.io/guide/built-in-directives#listing-items-with-ngfor)

#### Q9. Quelles sont les propriétés de métadonnées des deux décorateurs de composants utilisées pour configurer les styles CSS d’un composant ?

- \[ ] viewEncapsulation et viewEncapsulationFiles.
- \[ ] Il n’y en a qu’un et c’est la propriété nommée css.
- \[ ] css et cssUrl.
- \[x] styles et styleUrls.

[Angular.io - Styles de composants](https://angular.io/guide/component-styles)

#### Q10. Avec la classe de composant suivante, quelle syntaxe de modèle utiliseriez-vous dans le modèle pour afficher la valeur du champ de classe de titre ?

```ts
@Component({
  selector: 'app-title-card',
  template: '',
})
class TitleCardComponent {
  title = 'User Data';
}
```

- \[ ] `{{ 'title' }}`
- \[x] `{{ title }}`
- \[ ] `[title]`
- \[ ] Un champ de classe ne peut pas être affiché dans un modèle via la syntaxe du modèle.

[Angular.io - Interpolation de chaîne ou Interpolation de texte](https://angular.io/guide/interpolation)

#### Q11. Quel est le but de la méthode valueChanges sur un FormControl ?

- \[ ] Il est utilisé pour configurer les valeurs autorisées pour le contrôle.
- \[ ] Il est utilisé pour changer la valeur d’un contrôle en une nouvelle valeur. Vous appelez cette méthode et transmettez la nouvelle valeur pour le champ de formulaire. Il prend même en charge la transmission d’un tableau de valeurs qui peuvent être définies au fil du temps.
- \[ ] Il renvoie un booléen en fonction de si la valeur du contrôle est différente de la valeur avec laquelle il a été initialisé.
- \[x] Il s’agit d’un observable qui émet chaque fois que la valeur du contrôle change, de sorte que vous pouvez réagir à de nouvelles valeurs et prendre des décisions logiques à ce moment-là.

[Angular.io - Affichage d’une valeur de contrôle de](https://angular.io/guide/reactive-forms#displaying-a-form-control-value)

#### Q12. Quelle directive est utilisée pour lier un `<a>` balise au routage ?

- \[ ] routeTo
- \[x] routeurLien
- \[ ] routePath
- \[ ] appLink

[Angular.io - RouterLink](https://angular.io/api/router/RouterLink#description)

#### Q13. À quoi sert le décorateur de sortie dans cette classe de composants ?

```ts
@Component({
    selector: 'app-shopping-cart',
    . . .
})
export class ShoppingCartComponent {
    @Output() itemTotalChanged = new EventEmitter();
}
```

- \[ ] Il fait le `itemTotalChanged` champ de classe public.
- \[ ] Il permet de lier des valeurs au `itemTotalChanged` champ de classe, comme ceci : `<app-shopping-cart [itemTotalChanged]="newTotal"></app-shopping-cart>`.
- \[x] Il fournit un moyen de lier des événements au `itemTotalChanged` champ de classe, comme ceci : `<app-shopping-cart (itemTotalChanged)="logNewTotal($event)"></app-shopping-cart>`.
- \[ ] C’est simplement un moyen de mettre un commentaire devant un champ de classe pour la documentation.

[Angular.io - Envoi de données au composant parent](https://angular.io/guide/inputs-outputs#sending-data-to-a-parent-component)

#### Q14. Quelle est la différence entre ces deux exemples de balisage pour la gestion conditionnelle de l’affichage ?

```html
<div *ngIf="isVisible">Active</div>
<div [hidden]="!isVisible">Active</div>
```

- \[ ] Le `ngIf` est un raccourci pour l’autre exemple. Lorsque Angular traite cette directive, il écrit un élément div dans le DOM avec la propriété masquée.
- \[ ] Ils sont fondamentalement les mêmes.
- \[x] Le `ngIf` ne restitue pas le div dans le DOM si l’expression est false. Le `hidden` l’utilisation de la propriété masque le contenu div dans la fenêtre d’affichage du navigateur, mais le div se trouve toujours dans le DOM.
- \[ ] Le `ngIf` est valide, mais l’utilisation de l' `hidden` la propriété est incorrecte et génère une erreur.

[StackOverflow](https://stackoverflow.com/a/39778145)

#### Q15. Comment désactiver le bouton d’envoi lorsque le formulaire contient des erreurs dans cet exemple de formulaires pilotés par modèle ?

```html
<form #userForm="ngForm">
  <input type="text" ngModel name="firstName" required />
  <input type="text" ngModel name="lastName" required />
  <button (click)="submit(userForm.value)">Save</button>
</form>
```

- \[ ]

```html
<button (click)="submit(userForm.value)" disable="userForm.invalid">Save</button>
```

- \[x]

```html
<button (click)="submit(userForm.value)" [disabled]="userForm.invalid">Save</button>
```

- \[ ]

```html
<button (click)="submit(userForm.value)" [ngForm.disabled]="userForm.valid">Save</button>
```

- \[ ]

```html
<button (click)="submit(userForm.value)" *ngIf="userForm.valid">Save</button>
```

[Angular.io - Soumettez le formulaire avec ngSubmit](https://angular.io/guide/forms#submit-the-form-with-ngsubmit)

#### Q16. Vous voulez voir quels fichiers seraient générés en créant un nouveau composant de carte de visite. Quelle commande utiliseriez-vous ?

- \[x] ng générer une carte de contact de composant --dry-run
- \[ ] ng générer une carte de contact de composant --no-files
- \[ ] ng générer composant composant --sec
- \[ ] ng générer le composant --exclude

[Angular.io - ng générer des options](https://angular.io/cli/generate#options)

#### Q17. Sur la base du composant suivant, quelle syntaxe de modèle utiliseriez-vous pour lier le champ titleText de TitleCardComponent à la propriété title de l’élément h1 ?

```ts
@Component({
  selector: 'app-title-card',
  template: '<h1 title="User Data"> {{titleText}}</h1>',
})
export class TitleCardComponent {
  titleText = 'User Data';
}
```

- \[ ] `<h1 data-title="titleText">{{ titleText }}</h1>`
- \[ ] `<h1 title="titleText">{{ titleText }}</h1>`
- \[x] `<h1 [title]="titleText">{{ titleText }}</h1>`
- \[ ] `<h1 titleText>{{ titleText }}</h1>`

[Angular.io - Interpolation de chaîne](https://angular.io/guide/interpolation)

#### Q18. Que sont les crochets de cycle de vie Angular ?

- \[ ] enregistreurs pour suivre la santé d’une application Angular
- \[ ] fournisseurs pouvant être utilisés pour suivre les instances des composants
- \[ ] tuyaux intégrés pouvant être utilisés dans les modèles pour les événements DOM
- \[x] méthodes nommées réservées pour les composants et les directives qu’Angular appellera pendant les heures définies de son exécution, et peuvent être utilisées pour exploiter ces moments du cycle de vie

[Angular.io - Crochets de cycle de vie](https://angular.io/guide/lifecycle-hooks)

#### Q19. Choisissez la meilleure description pour ce code de syntaxe de modèle :

```html
<span>Boss: {{job?.bossName}} </span>
```

- \[ ] Le ? est un raccourci pour le tuyau asynchrone. La valeur de la tâche doit être observable.
- \[x] Il utilise l’opérateur de navigation sécurisée (?) sur le champ de travail. Si le champ de tâche n’est pas défini, l’accès au bossName sera ignoré et aucune erreur ne se produira.
- \[ ] Il y a une erreur dans la syntaxe du modèle. Le? n’est pas valide ici.
- \[ ] Il dijoue la valeur de l’emploi s’il en a un; sinon, il affiche le bossName.

[StackOverflow](https://stackoverflow.com/a/60182134)

#### Q20. Comment configurer une définition d’itinéraire pour un UserDetailComponent qui prend en charge le chemin d’URL user/23 (où 23 représente l’ID de l’utilisateur demandé) ?

- \[x] `{ path: 'user/:id', component: UserDetailComponent }`
- \[ ] `{ url: 'user/:id', routedComponent: UserDetailComponent }`
- \[ ] `{ routedPath: 'user/:id', component: UserDetailComponent }`
- \[ ] `{ destination: new UserDetailComponent(), route: 'user/:id' }`

[CodeCraft - Itinéraires paramétrés](https://codecraft.tv/courses/angular/routing/parameterised-routes/#_configuration)

#### Q21. Que font les décorateurs HostListener et le décorateur HostBinding dans cette directive ?

```ts
@Directive({
  selector: '[appCallout]',
})
export class CalloutDirective {
  @HostBinding('style.font-weight') fontWeight = 'normal';

  @HostListener('mouseenter')
  onMouseEnter() {
    this.fontWeight = 'bold';
  }

  @HostListener('mouseleave')
  onMouseLeave() {
    this.fontWeight = 'normal';
  }
}
```

- \[x] Ils définissent le champ CalloutDirective.fontWeight selon que la souris est ou non sur l’élément DOM. HostListener définit ensuite la propriété CSS font-weight sur la valeur fontWeight.
- \[ ] Ils configurent la directive pour vérifier l’élément DOM sur lequel elle se trouve. Si des liaisons d’événements ont été ajoutées pour la souris, entrez et laissez, elle utilisera ce code. Sinon, rien ne se passera.
- \[ ] Il s’agit d’une utilisation incorrecte de HostListener et HostBinding. Les décorateurs HostListener et HostBinding ne font rien sur les directives; ils ne fonctionnent que lorsqu’ils sont utilisés sur des composants.
- \[ ] Si l’élément DOM sur lequel cette directive est placée a la propriété CSS font-weight définie dessus, les événements mouseentent et mouseleave seront déclenchés.

[DigitalOcean](https://www.digitalocean.com/community/tutorials/angular-hostbinding-hostlistener)

#### Q22. Quelle syntaxe de modèle angulaire pouvez-vous utiliser sur ce champ de formulaire piloté par modèle pour accéder à la valeur du champ et vérifier la validation dans le balisage du modèle ?

```html
<input type="text" ngModel name="firstName" required minlength="4" />
<span *ngIf="">Invalid field data</span>
```

- \[x] Vous pouvez utiliser une variable de référence de modèle et la fonctionnalité exportAs de la directive ngModel.
- \[ ] Vous pouvez utiliser la directive ngModel en combinaison avec le nom du champ de saisie.
- \[ ] Vous pouvez utiliser une variable de référence de modèle pour l’élément d’entrée HTML, puis cocher la propriété valide de celui-ci.
- \[ ] Il n’est pas possible d’accéder à la valeur du champ avec des formulaires pilotés par modèle. Vous devez utiliser des formulaires réactifs pour cela.

[Angular.io -Afficher et masquer l’erreur de validation ](https://angular.io/guide/forms#show-and-hide-validation-error-messages)

[Douleur moyenne](https://medium.com/@agoiabeladeyemi/template-driven-forms-in-angular-4a3a5ad960de)

#### Q23. Quel est le type de valeur qui sera stocké dans la variable de référence du modèle headerText dans ce balisage ?

```html
<h1 #headerText>User List</h1>
```

- \[x] un Angular ElementRef, un wrapper autour d’un élément natif
- \[ ] le texte intérieur de l' `<h1>` élément
- \[ ] une classe de composant d’en-tête
- \[ ] le type d’élément DOM natif de HTMLHeadingElement

[Pluralsight - Variable de référence de modèle](https://www.pluralsight.com/guides/how-to-use-template-reference-variables-in-angular)

#### Q24. Quelle est la différence, le cas échéant, entre la logique de code résultante basée sur ces deux configurations de fournisseur ?

```ts
[{ provide: FormattedLogger, useClass: Logger }][{ provide: FormattedLogger, useExisting: Logger }];
```

- \[ ] Ils sont les mêmes. Les deux entraîneront une nouvelle instance de Logger liée au jeton FormattedLogger.
- \[x] La syntaxe useClass indique à l’injecteur de créer une nouvelle instance de Logger et de lier cette instance au jeton FormattedLogger. La syntaxe useExisting fait référence à une instance d’objet déjà existante déclarée comme Logger.
- \[ ] Les deux ont tort. Un type fort ne doit pas être utilisé pour useClass ou useExisting.
- \[ ] Ils sont les mêmes. Les deux entraîneront le jeton FormattedLogger comme alias pour l’instance de Logger.

[Angular.io - Fournisseurs de dépendances](https://angular.io/guide/dependency-injection-providers#defining-providers)

[TektutorialHub](https://www.tektutorialshub.com/angular/angular-providers/)

#### Q25. Quel est le but de la propriété de données (voir dans l’exemple ci-dessous) dans une configuration d’itinéraire ?

```ts
   {
       path: 'customers',
       component: CustomerListComponent,
       data: { accountSection: true }
   }
```

- \[ ] un mappage clé/valeur pour définir des valeurs @Input sur l’instance de composant routé
- \[x] un moyen d’inclure des données statiques en lecture seule associées à l’itinéraire qui peuvent être récupérées à partir de l’ActivatedRoute
- \[ ] une propriété sur l’itinéraire qui peut être utilisée pour charger des données dynamiques pour l’itinéraire
- \[ ] un objet qui sera injecté automatiquement dans le constructeur du composant routé.

[TektutorialsHub](https://www.tektutorialshub.com/angular/angular-pass-data-to-route/#:~:text=Angular%20allows%20us%20to%20pass,of%20the%20history%20state%20object)

[StackOverflow](https://stackoverflow.com/a/36835156)

#### Q26. Comment l’intégré `ngIf` directive structurelle modifier le DOM rendu en fonction de cette syntaxe de modèle?

```ts
@Component({
  selector: 'app-product',
  template: '<div *ngIf="product">{{ product.name }}</div>',
})
export class ProductComponent {
  @Input() product;
}
```

- \[ ] Le `<div>` agit comme un espace réservé. Si le champ de classe de produit est « truthy », le `<div>` sera remplacé par le seul `product.name` valeur; sinon, rien ne sera rendu.
- \[ ] Le `<div>` sera toujours rendu, et si le champ de produit est « véridique », le `<div>` contiendra le `product.name` valeur; sinon, il rendra le `<div>` élément sans valeur.
- \[ ] Cela produit une erreur, puisque ngIf n’est pas une directive structurelle intégrée.
- \[x] Si le champ de classe de produit est « truthy », le DOM rendu inclura le `<div>` avec la valeur de l' `product.name` champ. S’il n’est pas « véridique », le DOM rendu ne contiendra pas le `<div>` élément.

[Référence (angular.io)](https://angular.io/api/common/NgIf)

#### Q27. Qu’est-ce que ce code accomplit ?

```ts
@NgModule({
  declarations: [AppComponent],
  imports: [BrowserModule],
  bootstrap: [AppComponent],
})
export class AppModule {}

platformBrowserDynamic().bootstrapModule(AppModule);
```

- \[ ] Il exécute un test unitaire pour un NgModule.
- \[ ] Il fournit un moyen de coder la structure de document d’une application Angular. Le @NgModule est une forme de commentaire de code en ligne qui est ignoré par le compilateur TypeScript, mais qui apparaîtra avec une mise en forme spéciale dans les applications d’éditeur de code.
- \[ ] Il déclare un module Angular nommé AppModule et le rend disponible pour un chargement paresseux dans toute l’application.
- \[x] Il déclare un module Angular nommé AppModule qui contient un composant amorçage nommé AppComponent. Ensuite, il enregistre ce module avec Angular, afin que l’application puisse démarrer.

[Angular.io - Le NgModule de base](https://angular.io/guide/ngmodules#the-basic-ngmodule)

#### Q28. Quel choix décrit le mieux ce que le _résoudre_ dans cette configuration d’itinéraire ?

```ts
{
   path: ':id',
   component: UserComponent,
   resolve: {
     user: UserResolverService
   }
}
```

- \[x] Avant de charger le _UserComponent_, le routeur s’abonnera au _Observable_ retourné par un _résoudre_ dans le _UserResolverService_. Cette technique peut être utilisée pour obtenir des données préchargées pour un _route_.
- \[ ] Après le _route_ est terminé la résolution, et le composant est chargé et rendu, le _UserResolverService_ aura une méthode nommée _utilisateur_ exécuter qui nettoiera toutes les connexions de données ouvertes.
- \[ ] Il y a une erreur. Le nom de propriété correct est _onResolve_.
- \[ ] Le _UserComponent_ aura un paramètre dans son constructeur pour _utilisateur_, et l' _routeur_ gérera l’injection d’une valeur pour cela d’un appel à un _utilisateur_ dans le _UserResolverService_.

[angular.io](https://angular.io/api/router/Resolve)

#### Q29. Quel est le but du décorateur ContentChildren dans cette classe de composants ?

```ts
@Component({
 . . .
 template: '<ng-content></ng-content›'
})
export class TabsListComponent {
 @ContentChildren(TabComponent) tabs;
}
```

- \[ ] Le cas échéant _OngletsComposant_ des éléments sont ajoutés à la _TabsListComponent_ modèle, ils seront mis dans le <ng-content> au moment de l’exécution.
- \[ ] Il crée _TabComponent_ composants de l' _TabsListComponent_ modèle lorsqu’un _TabsListComponent_ est instancié.
- \[x] Il permet d’accéder à partir de la classe de composants à n’importe quel _TabComponent_ les composants dont le contenu était projeté dans le <ng-content> pour ce composant.
- \[ ] Il restreint les éléments autorisés qui peuvent être placés dans un _TabsListComponent_ élément à autoriser uniquement _TabComponent_ Éléments.

[betterprogramming.pub](https://betterprogramming.pub/understanding-contentchildren-with-an-example-e76ce78968db)

#### Q30. Pour qu’Angular puisse traiter des composants dans une application, où les types de composants doivent-ils être enregistrés ?

- \[ ] dans une balise script dans le fichier index.html
- \[ ] dans une balise de métadonnées de décorateur NgModule nommée _Composants_
- \[ ] Aucune inscription n’est nécessaire, il suffit d’inclure les fichiers de composants dans un répertoire d’application.
- \[x] dans une propriété de métadonnées de décorateur NgModule nommée _Déclarations_

[angular.io](https://angular.io/guide/ngmodule-api#ngmodule-metadata)

#### Q31. Quel est le but de l' `fixture.detectChanges()` appeler ce test unitaire ?

```ts
TestBed.configureTestingModule({
  declarations: [UserCardComponent],
});
let fixture = TestBed.createComponent(UserCardComponent);

fixture.detectChanges();

expect(fixture.nativeElement.querySelector('h1').textContent).toContain(
  fixture.componentInstance.title,
);
```

- \[ ] Il suit toutes les modifications Ul potentielles et échouera au test unitaire si elles sont effectuées.
- \[ ] Il est utilisé pour assurer la stabilité du modèle de composant sur plusieurs tests unitaires dans l’ensemble de la suite de tests.
- \[x] Il force Angular à effectuer une détection des modifications, ce qui rendra le _UserCardComponent_ avant de pouvoir valider son modèle.
- \[ ] Il est utilisé pour consigner les événements de détection des modifications sur la console pendant les exécutions de tests unitaires.

[angular.io](https://angular.io/api/core/testing/ComponentFixture#detectChanges)

#### Q32. À quoi ressemblera le segment d’URL en fonction de l’appel suivant au `Router.navigate` méthode lorsque goToUser reçoit la valeur 15 ?

```ts
export class ToolsComponent {
  constructor(private router: Router) {}
  goToUser(id: number) {
    this.router.navigate(['user', id]);
  }
}
```

- \[x] /utilisateur/15
- \[ ] /utilisateur?id=15
- \[ ] /utilisateur:15
- \[ ] /utilisateur;id=15

[angular.io](https://angular.io/api/router/Router#navigate)

#### Q33. Lorsqu’un service est fourni pour root et est également ajouté à la configuration du fournisseur pour un module chargé paresseusement, quelle instance de ce service l’injecteur fournit-il aux constructeurs dans le module chargé paresseusement ?

- \[x] Une nouvelle instance de ce service est créée lorsque le module est chargé paresseusement.
- \[ ] La fourniture d’un service du même type au niveau d’un module chargé paresseusement n’est pas autorisée.
- \[ ] Si une instance du service n’a pas encore été créée au niveau racine. il en créera un et l’utilisera ensuite.
- \[ ] Une seule instance de ce service est toujours instanciée à la racine et est la seule jamais utilisée, y compris dans les modules paresseux.

#### Q34. Que fait le décorateur HostBinding dans cette directive ?

```ts
@Directive({
  selector: ' [appHighlight] ',
})
export class HighlightDirective {
  @HostBinding('class.highlighted') highlight = true;
}
```

- \[x] Il ajoute la classe CSS nommée en surbrillance à tout élément DOM sur lequel se trouve la directive appHighlight.
- \[ ] HostBinding ne fait rien sur les directives, seulement sur les composants.
- \[ ] Il spécifie si l’élément hôte obtient la classe en surbrillance ajoutée à son attribut class, alors le champ de classe de directive en surbrillance sera défini sur true ; et s’il n’est pas ajouté sur l’hôte, il sera défini sur false.
- \[ ] Il crée un style en ligne sur l’élément hôte avec une propriété CSS nommée highlight définie sur true.

[StackOverflow](https://stackoverflow.com/a/46207423)

#### Q35. Dans les formulaires réactifs, quel type de classe de formulaire Angular est utilisé sur le DOM natif <form> élément pour le câbler?

- \[ ] `FormArray`
- \[ ] `FormControl`
- \[x] `FormGroup`
- \[ ] `all of these answers`

#### Q36. En supposant que le nom d’utilisateur FormControl a été configuré avec un validateur minLength, comment configurer un affichage d’erreur dans le balisage de formulaire réactif suivant pour le champ de nom d’utilisateur ?

```ts
<form [formGroup]="form"›
  <input type="text" formControlName= "username"›
  ...
</form>
```

- \[ ]

```ts
    <span *ngIf="username.minLength.invalid"›
        Username length is not valid
    </span>
```

- \[ ]

```ts
<input type="text" formControlName="username" [showMinLength]="true"›
```

- \[ ]

```ts
    <span *ngIf="form.get('username').getError('minLength') as minLengthError">
      Username must be at least {{ minLengthError.requiredLength }} characters.
    </span>
```

- \[x]

```ts
<input type="text" formControlName="username" #userName="ngModer">
    <span *ngIf="userName.errors.minlength"›
      Username must be at least {{ userName.errors.minlength.requiredLength }} characters.
    </span>
```

[Codecraft](https://codecraft.tv/courses/angular/forms/template-driven/)

#### Q37. Comment le mode d’encapsulation de vue émulée gère-t-il CSS pour un composant ?

- \[ ] Il rend le CSS exactement comme vous l’avez écrit sans aucune modification.
- \[ ] Il utilise le balisage DOM fantôme et CSS.
- \[x] Il crée des attributs uniques pour les éléments DOM et étend les sélecteurs CSS que vous écrivez dans ces ID d’attribut.
- \[ ] Il restitue toutes les règles CSS que vous écrivez en tant que CSS en ligne sur tous les éléments DOM sur lesquels vous les utilisez dans le modèle.

[Angular.io](https://angular.io/guide/view-encapsulation#inspecting-generated-css)

#### Q38. Avec la configuration testbed suivante, que peut-on utiliser pour accéder au DOM rendu pour userCardComponent ?

```ts
TestBed.configureTestingModule({
  declarations: [UserCardComponent],
});
let fixture = TestBed.createComponent(UserCardComponent);
```

- \[ ] `fixture.componentTemplate`
- \[ ] `fixture.getComponentHtml()`
- \[x] `fixture.nativeElement`
- \[ ] `fixture.componentInstance.template `

[StackOverflow](https://stackoverflow.com/a/56504773)

[Angular.io](https://angular.io/guide/testing-components-basics#nativeelement)

#### Q39. Compte tenu de ces deux composants, qu’est-ce qui sera rendu au DOM en fonction de l’utilisation du balisage ?

```ts
@Component({
 selector: 'app-card',
 template: '<h1>Data Card</h1><ng-content></ng-content>'
})
export class CardComponent { }

@Component({
 selector: 'app-bio',
 template: '<ng-content></ng-content>.
})
export class BioComponent { }

// markup usage:
<app-card><app-bio>Been around for four years.</app-bio></app-card>
```

- \[x]

```ts
 <app-card>
  <h1>Data Card</hl>
  <app-bio>
   Been around for four years.
  </app-bio>
 </app-card>
```

- \[ ]

```ts
<h1>Data Card</h1>
 <app-bio>
  Been around for four years.
 </app-bio>
```

- \[ ]

```ts
<app-card>
  <h1>Data Card</hl>
  <ng-content></ng-content>
  <app-bio>
   Been around for four years.
   <ng-content></ng-content>
  </app-bio>
</app-card>
```

- \[ ]

```ts
<app-card>
  <h1>Data Card</hl>
</app-card>
```

#### Q40. Compte tenu du composant app-title-card dans le code ci-dessous, quel DOM le composant app-user-card rendra-t-il ?

```ts
@Component({
   selector: 'app-user-card',
   template: '<app-title-card></app-title-card><p>Jenny Smith</p>'
})

@Component({
   selector: 'app-title-card',
   template: '<h1>User Data</hl>'
})

// usage of user card component in parent component html
<app-user-card></app-user-card>
```

- \[x]

```ts
<app-user-card>
  <app-title-card>
    <h1>User Data</h1>
  </app-title-card>
  <p>Jenny Smith</p>
</app-user-card>
```

- \[ ]

```ts
<h1>User Data</h1>
<p>Jenny Smith<p>
```

- \[ ]

```ts
<app-user-card>
  <app-title-card></app-title-card>
</app-user-card>
```

- \[ ]

```ts
<div app-user-card>
  <h1 app-title-card>User Data</h1>
  <p>Jenny Smith</p>
</div>
```

#### Q41. Choisissez le code correspondant à l’enregistrement personnalisé du fournisseur recherché par le décorateur @Inject () :

```ts
constructor(@Inject('Logger') private logger) { }
```

- \[ ]

```ts
providers: [Logger];
```

- \[x]

```ts
providers: [{ provide: 'Logger', useClass: Logger }];
```

- \[ ]

```ts
@Injectable({
    providedln: 'root'
})
```

- \[ ]

```ts
providers: [{ provide: 'Logger' }];
```

[StackOverflow](https://stackoverflow.com/a/37315355)

[TektutorialHub](https://www.tektutorialshub.com/angular/angular-injector-injectable-inject/)

[Angular.io - L’injection de dépendance en action](https://angular.io/guide/dependency-injection-in-action#supply-a-custom-provider-with-inject)

#### Q42. Quel choix décrit le mieux l’utilisation suivante de la méthode HttpClient.get dans la méthode de classe getsettings ?

```ts
export class SettingsService {
    constructor(private httpClient: HttpClient) { }
    ...

getSettings()
{
    return this.httpClient.get<Settings>(this.settingsUrl)
        .pipe(
            retry(3)
        );
}}
```

- \[ ] La méthode de canal RxJs est un alias pour la méthode subscribe, donc un appel à `getSettings` exécutera la requête get. L’opérateur de nouvelle tentative est utilisé pour indiquer à l’appel de tuyau de réessayer la requête get trois fois.
- \[ ] Il produira une erreur au moment de l’exécution car la méthode pipe n’est pas disponible hors du `Httpclient.get` appeler.
- \[ ] Chaque appel à la méthode getSettings entraînera le Httpclient à effectuer trois demandes get totales à settingsUrl, ce qui n’est pas idéal car il y aura toujours deux appels supplémentaires qui ne sont pas nécessaires. L’opérateur de nouvelle tentative ne doit pas être utilisé de cette manière.
- \[x] Lorsque le résultat de la méthode getSettings est abonné, l’appel HTTP GET est effectué ; s’il échoue, il sera réessayé jusqu’à trois fois avant d’abandonner et de renvoyer une erreur.

[learnrxjs.io](https://www.learnrxjs.io/learn-rxjs/operators/error_handling/retry)

[dev.to](https://dev.to/gparlakov/how-does-rxjs-retry-work-412p)

#### Q43. Lorsqu’un service nécessite une configuration pour initialiser son état par défaut via une méthode, comment pouvez-vous vous assurer que cette méthode est appelée avant que le service ne soit injecté n’importe où ?

- \[ ] Placez plutôt la logique de cette méthode de service dans le constructeur de service.
- \[x] Utilisez un fournisseur d’usine au niveau AppModule racine qui dépend du service pour appeler cette méthode de service.
- \[ ] il n’est pas possible de le faire au début de l’application; vous ne pouvez le faire qu’au niveau d’un composant.
- \[ ] Instanciez une instance du service au niveau global (étendue de la fenêtre), puis appelez cette méthode.

#### Q44. Quelle déclaration décrit le mieux cette utilisation du banc d’essai ?

```ts
const spy = jasmine.createSpyObj('DataService', ['getUsersFromApi']);
TestBed.configureTestingModule({
  providers: [UserService, { provide: DataService, useValue: spy }],
});
const userService = TestBed.get(UserService);
```

- \[ ] Le banc d’essai est requis chaque fois que vous souhaitez utiliser un objet espion dans un test unitaire pour un fournisseur Angular.
- \[ ] Le banc d’essai est utilisé pour tester la vue d’un composant.
- \[x] Le banc d’essai échafaude un NgModule avec deux fournisseurs et gère toute injection de dépendance. Si une classe Angular demande le DataService dans son constructeur, le TestBed injectera spy dans ce constructeur.
- \[ ] Le banc d’essai configure le testeur pour lui dire d’exécuter uniquement des tests pour les deux fournisseurs répertoriés dans son tableau de fournisseurs.
- `All other tests be ignored, including tests that assert results against one of these providers and a non-defined provider.`
  `Although it will work when multiple providers in this configuration are asserted against in a single test.`

#### Q45. Quelle est la principale différence entre un composant et une directive?

- \[ ] Un composant utilise une propriété de métadonnées de sélecteur et une directive n’en utilise pas.
- \[ ] Une directive peut être utilisée pour ajouter des événements personnalisés au DOM et un composant ne le peut pas.
- \[x] Un composant a un modèle et une directive n’en a pas.
- \[ ] Une directive ne peut cibler que des éléments DOM natifs.

[StackOverflow](https://stackoverflow.com/a/34616190)

#### Q46. Que pourriez-vous ajouter à cette classe de directive pour permettre de définir la longueur tronquée lors de l’utilisation de la directive dans le balisage ?

```ts
  @Directive({
      selector: '[appTruncate]'
  })
  export class TruncateDirective {
      . . .
  }

  // example of desired usage:
  <p [appTruncate]="10">Some very long text here</p>
```

- \[x] `@Input() appTruncate: number;`
- \[ ] `@Output() appTruncate;`
- \[ ] `constructor(maxLength: number) { }`
- \[ ] `Nothing. The directive selector cannot be used to pass in values to the directive.`

[Angular.io](https://angular.io/guide/attribute-directives#passing-values-into-an-attribute-directive)

[StackOverflow](https://stackoverflow.com/a/46303049)

#### Q47. Comment pouvez-vous transmettre des paramètres de requête à ceci `HttpClient.get` demander?

```ts
export class OrderService {
  constructor(private httpClient: HttpClient) {}

  getOrdersByYear(year: number): Observable<Order[]> {
    return this.httpClient.get<Order[]>(this.ordersUrl);
  }
}
```

- \[ ] `return this.httpClient.get<Order[]>(this.ordersUrl, {'year': year})`
- \[ ] `return this.httpClient.get<Order[]>(this.ordersUrl, year)`
- \[x]

```ts
const options = { params: new HttpParams().set('year', year) };
return this.httpClient.get<Order[]>(this.ordersUrl, options);
```

- \[ ]

```ts
getOrdersByYear(year: number): Observable<Order[]> {
    return this.httpClient.addParam('year', year).get<Order[]>(this.ordersUrl, year);
}
```

[StackOverflow](https://stackoverflow.com/a/34475594)

[TektutorialHub](https://www.tektutorialshub.com/angular/angular-pass-url-parameters-query-strings/#httpparams)

#### Q48. En supposant que le `DataService` a été enregistré dans les fournisseurs de l’application, quelle réponse décrit le mieux ce qui se passe en fonction du constructeur de ce composant ?

```ts
    @Component({
        ...
    })
    export class OrderHistoryComponent {
        constructor(private dataService: DataService) {}
        ...
    }
```

- \[ ] Il déclare que le `OrderHistoryComponent` aura sa propre version d’un `DataService` et qu’il ne devrait jamais utiliser d’instances existantes. Le `DataService` devrait être instancié dans la classe en tant que champ privé pour que ce code soit complet et fonctionne.
- \[x] Lorsque Angular crée une nouvelle instance du `OrderHistoryComponent`, l’injecteur fournira une instance d’un `DataService` au premier argument du constructeur de composants. Le constructeur `dataService` sera utilisé pour définir un champ d’instance privée portant le même nom sur l’instance.
- \[ ] Il fournit un moyen de faire des tests de composants uniquement; le constructeur n’a aucune utilisation dans l’exécution réelle de l’application Angular.
- \[ ] Il permet à l’élément personnalisé ciblé par le composant d’avoir une propriété personnalisée nommée `dataService` qui peut être utilisé pour lier un existant `DataService` instance à.

[StackOverflow](https://stackoverflow.com/a/49755822)

[Angular.io - Injection de dépendance](https://angular.io/guide/dependency-injection)

#### Q49. Terminez ce balisage à l’aide de l’icône `ngIf` directive pour implémenter un autre cas qui affichera le texte « L’utilisateur n’est pas actif »:

```ts
<div *ngIf="userIsActive; else inactive">
  Currently active!
</div>
```

- \[ ]

```ts
<div #inactive>User is not active.</div>
```

- \[ ]

```ts
<div *ngIf="inactive">
  User is not active.
</div>
```

- \[ ]

```ts
<ng-template #else="inactive">
  <div>User is not active.</div>
</ng-template>
```

- \[x]

```ts
<ng-template #inactive>
  <div>User is not active.</div>
</ng-template>
```

[Angular.io](https://angular.io/api/common/NgIf)

#### Q50. Quelle est la syntaxe correcte pour une définition d’itinéraire pour charger paresseusement un module d’entités ?

- \[ ]

```
  {
      path: 'users',
      lazy: './users/users.module#UsersModule'
  }
```

- \[x]

```
{
    path: 'users',
    loadChildren: () => import('./users/users.module').then(m => m.UserModule)
}
```

- \[ ]

```
{
    path: 'users',
    loadChildren: './users/users.module#UsersModule'
}
```

- \[ ]

```
{
    path: 'users',
    module: UsersModule
}
```

[Angular.io - Modules de chargement paresseux](https://angular.io/guide/lazy-loading-ngmodules)

#### Q51. Décrivez comment la validation est configurée et configurée dans cet exemple de formulaires réactifs :

```ts
export class UserFormControl implements OnInit {
    ...
    ngOnInit() {
        this.form = this.formBuilder.group({
            username: this.formBuilder.control('',
                [Validators.required, Validators.minLength(5), this.unique]),
        )};
    }
    unique(control: FormControl) {
        return control.value !== 'admin' ? null: {notUnique: true};
    }
}
```

- \[ ] Le `FormControl` pour `username` est configuré pour exclure trois validateurs des validateurs qu’il est autorisé à utiliser.
- \[ ] Le `FormControl` pour `username` est en cours de configuration pour permettre l’utilisation de trois validateurs possibles : `required, maxLength`, et un personnalisé nommé `unique`. Pour les activer `validators`, une directive de validateur devrait être placée sur les champs de formulaire dans le balisage.
- \[ ] La validation ne peut pas être configurée de cette manière dans les formulaires réactifs.
- \[x] Le `FormControl` pour `username` est configuré avec trois validateurs : le `required` et `minLength` les validateurs provenant d’Angular et une fonction de validateur personnalisée nommée `unique` qui vérifie la valeur non égale à la chaîne `admin`.

[Angular.io - Validation du formulaire](https://angular.io/guide/form-validation)

[Blog de l’Université Angular](https://blog.angular-university.io/angular-custom-validators/)

#### Q52. Que fait le décorateur injectable sur cette classe de service?

```ts
@Injectable({
    providedIn: 'root'
)}
export class DataService { }
```

- \[ ] Il enregistre un fournisseur pour le service qui n’est disponible qu’au niveau du module racine, pas pour les modules enfants.
- \[x] Il enregistre un fournisseur pour le service dans l’injecteur d’application racine, ce qui rend une seule instance de celui-ci disponible dans toute l’application.
- \[ ] Cela permet de faire en sorte que le service ne puisse être injecté que dans le composant amorçage de l’application.
- \[ ] Il configure une règle de temps de compilation qui vous permet de placer le type de service uniquement dans la propriété de métadonnées providers du NgModule racine.

[Angular.io](https://angular.io/guide/providers#providing-a-service)

#### Q53. Décrire l’utilisation de ce code

```ts
export interface AppSettings {
  title: string;
  version: number;
}
export const APP_SETTINGS = new InjectionToken<AppSettings>('app.settings');
```

- \[ ] L’InjectionToken ajoute une instance des AppSettings au fournisseur racine via l’appel du constructeur InjectionToken, ce qui la rend automatiquement disponible pour tous les NgModules, services et composants de l’application Angular sans qu’il soit nécessaire de l’injecter n’importe où.
- \[x] L’InjectionToken est utilisé pour créer un jeton de fournisseur pour une dépendance non-classe. Un littéral d’objet peut être fournisseur en tant que valeur pour le type de fournisseur de dépendance APP_SETTINGS qui peut ensuite être injecté dans des composants, des services, etc.
- \[ ] L’InjectionToken est utilisé pour créer un décorateur dynamique pour les AppSettings qui peut être utilisé sur les paramètres du constructeur via un décorateur @AppSettings.
- \[ ] Ce code a une erreur car vous ne pouvez pas utiliser une interface TypeScript pour le type générique sur l’InjectionToken

#### Q54. Pour l’exemple de formulaires pilotés par modèle suivant, quel argument peut être transmis à la méthode submit dans l’événement click pour envoyer les données du formulaire ?

```html
<form #form="ngForm">
  <input type="text" ngModel="firstName" />
  <input type="text" ngModel="lastName" />
  <button (click)="submit()">Save</button>
</form>
```

- \[x] submit(form.value)
- \[ ] soumettre($event)
- \[ ] submit(ngForm.value)
- \[ ] submit(Prénom, Nom)

#### Q55. Quel est le but de la configuration de la propriété prelodingStrategy dans ce code de routeur ?

```ts
RouterModule.forRoot(
  ...{
    preloadingStrategy: PreloadAllModules,
  },
);
```

- \[ ] Il permet de marquer des itinéraires individuels pour le préchargement.
- \[ ] Il précharge toutes les dépendances pour les itinéraires, créant des instances de services au démarrage de l’application pour la première fois
- \[ ] Il garantit que tous les modules sont intégrés dans un seul fichier de bundle de modules d’application.
- \[ ] Il configure le routeur pour charger immédiatement tous les itinéraires qui ont une propriété loadChildren (itinéraires qui sont généralement chargés sur demande)

#### Q56. Quelle est une autre façon d’écrire ce balisage pour lier la valeur du champ de classe `userName` à l `h1` propriété de titre d’élément?

```html
<h1 [title]="userName">Current user is {{ userName }}</h1>
```

- \[ ] title="nom_utilisateur »
- \[x] title="{{ nom_utilisateur }} »
- \[ ] title="{{ 'nom_utilisateur' }} »
- \[ ] La seule façon de le faire est d’utiliser les crochets.

#### Q57. Qu’est-ce que le `async` pipe doing dans cet exemple ?

```ts
@Component({
  selector: 'app-users',
  template: '<div *ngFor="let user of users | async">{{ user.name }}</div>',
})
export class UsersComponent implements OnInit {
  users;
  constructor(private httpClient: HttpClient) {}
  ngOnInit(): void {
    this.users = this.httpClient.get<{ name: string }>('users');
  }
}
```

- \[ ] Il ne fait rien, puisque le tuyau asynchrone ne peut pas être utilisé dans un `ngFor` déclaration.
- \[ ] Il configure le `ngFor` itération pour prendre en charge plusieurs listes d’utilisateurs en même temps.
- \[x] Il s’abonne à l’observable renvoyé par le `HttpClient.get` et déballage de la valeur renvoyée afin qu’elle puisse être itérée dans le `ngFor`.
- \[ ] Il autorise tous les utilisateurs du `users` à restituer simultanément au DOM.

#### Q58. Comment utiliser cette directive dans le balisage en fonction de sa valeur de sélecteur

```ts
@Directive({
	selector: '[appTruncate]'
})
export class TruncateDirective{
	. . .
}
```

- \[ ] `html <p data-directive="appTruncate">Some long text </p> `
- \[x] `html <p appTruncate>Some long text</p> `
- \[ ] `html <p app-truncate>Some long text</p> `
- \[ ] `html <app-truncate>Some long text</app-truncate> `

#### Q59. Quel hook de cycle de vie peut être utilisé sur un composant pour surveiller toutes les modifications apportées aux valeurs de @Input sur ce composant ?

- \[ ] ngOnInit
- \[ ] ngChanges
- \[ ] ngAfterInputChange
- \[x] ngOnChanges

[Comment détecter quand une valeur @Input() change dans Angular?](https://stackoverflow.com/a/44686085/1573267)

#### Q60. Quel serait un exemple d’utilisation de la syntaxe de modèle de ce tuyau personnalisé ?

```ts
@Pipe({ name: 'truncate' })
export class TruncatePipe implements PipeTransform {
	transform(value: string, maxLength: number, showEllipsis: boolean){
		const newValue = maxLength ? value.substr(0, maxLength): value;
		return showEllipsis ? '${newValue}...` : newValue;
	}
}
```

- \[x] {( 'un long texte' | tronquer:10 })
- \[ ] {( 'un texte long' | tronquer:10:true })
- \[ ] {( 'un long texte' | tronquer })
- \[ ] toutes ces réponses

\[revérifiez les réponses]

#### Q61. Quelle commande Angular CLI exécuteriez-vous pour générer un UsersComponent et l’ajouter au SharedModule (dans le fichier shared.module.ts de votre application) ?

- \[ ] ng générer le composant --newModule=shared
- \[ ] ng générer des utilisateurs de composants --module=shared
- \[ ] ng générer des utilisateurs de composants --shared
- \[ ] ng générer le composant --add=shared

\[revérifiez les réponses]

#### Q62. Comment réécrire ce balisage pour que le conteneur div ne soit pas nécessaire dans le rendu DOM final

```ts
<div *ngIf="location">
	<h1>{{ location.name }}</h1>
	<p>{{ location.description }}</p>
</div>
```

- \[ ]

```ts
<div *ngIf="location">
	<h1>{{ location.name }}</h1>
	<p>{{ location.description }}</p>
{{ endNgIf }}
```

- \[ ]

```ts
<ng-template *ngIf="location">
	<h1>{{ location.name }}</h1>
	<p>{{ location.description }}</p>
</ng-template>
```

- \[ ]

```ts
<div *ngIf="location" [display]=" ' hidden' ">
	<h1>{{ location.name }}</h1>
	<p>{{ location.description }}</p>
</div>
```

- \[x]

```ts
<ng-container *ngIf="location">
	<h1>{{ location.name }}</h1>
	<p>{{ location.description }}</p>
</ng-container>
```

\[revérifier les réponses]

#### Q63. Décrivez l’utilisation de ce code :

```ts
export interface AppSettings {
  title: string;
  version: number;
}
```

- \[ ] Ce code est une erreur car vous ne pouvez pas utiliser une interface TypeScript pour le type générique sur InjectionToken.
- \[ ] L’InjectionToken est utilisé pour créer un jeton de fournisseur pour une dépendance non-classe. Un lieteral d’objet peut être fourni comme valeur pour le type de fournisseur de dépendance APP_SETTINGS qui peut ensuite être injecté dans des composants, des services, etc.
- \[ ] L’InjectionToken ajoute une instance des AppSettings au fournisseur roote via l’appel du constructeur InjectionToken, ce qui la rend automatiquement disponible pour tous les NgModules, services et composants via l’application Angular sans qu’il soit nécessaire de l’injecter n’importe où.
- \[ ] L’InjectionToken est utilisé pour créer un décorateur dynamique pour les AppSettings qui peut être sed sur les paramètres du constructeur via un décorateur @AppSettings.

\[revérifier les réponses]

#### Q64. Quels utilitaires Angular, le cas échéant, sont nécessaires pour tester un service sans dépendances de constructeur ?

- \[ ] Par.css() la méthode d’assistance est nécessaire
- \[ ] Un élément de texte est nécessaire pour exécuter le service pour le test unitaire.
- \[ ] Aucune. Un service peut être instancié et testé à l’unité par lui-même.
- \[x] La classe TestBed est nécessaire pour instancier le service.

[Tests unitaires angulaires](https://angular.io/guide/testing-services) - revérifier les réponses

#### Q65. Quelle est la différence entre les protecteurs d’itinéraire CanActivate et CanLoad?

- \[ ] CanActivate est utilisé pour vérifier l’accès. CanLoad est utilisé pour précharger les données de l’itinéraire.
- \[x] CanLoad est utilisé au démarrage de l’application pour autoriser ou refuser l’ajout d’itinéraires à la table de routage. CanActivate est utilisé pour gérer l’accès aux itinéraires au moment où ils sont demandés.
- \[ ] CanActivate et CanLoad font exactement la même chose.
- \[ ] CanLoad empêche la livraison et le chargement d’un NgModule entier. CanActivate arrête le routage vers un composant de ce NgModule, mais ce module est toujours chargé.

[CanActivate vs Canload](https://stackoverflow.com/questions/42026045/difference-between-angulars-canload-and-canactivate#:~:text=canActivate%20is%20used%20to%20prevent,not%20authorized%20to%20do%20so.) CanActivate empêche l’accès sur les itinéraires, CanLoad empêche le chargement paresseux.

#### Q66. À quoi sert la propriété outlet dans cet objet de définition de routeur ?

```ts
{
	path: 'document',
	component: DocumentComponent,
	outlet: 'document-box'
}
```

- \[ ] il localisera toutes les instances de <document-box> dans le DOM et y insérer un élément DocumentComponent lors de la navigation d’itinéraire.
- \[ ] Il déclare que le DocumentComponent peut être utilisé comme enfant à un <<document-box> en plus d’être acheminé vers.
- \[x] Nous avions l’habitude de cibler un <router-outlet> avec l’attribut name correspondant à la valeur de chaîne comme emplacement du DocumentComponent à restituer lorsqu’il est routé.
- \[ ] C’est une source d’alimentation pour le routeur. (certainement pas la réponse :P)

[Prise angulaire](https://angular.io/api/router/RouterOutlet) - revérifier la réponse
