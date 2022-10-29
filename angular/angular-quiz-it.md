## Angolare

#### D1. Qual è lo scopo del decoratore ViewChild in questa classe di componenti?

```ts
@Component({
    ...
    template: '<p #bio></p>'
})
export class UserDetailsComponent {
    @ViewChild('bio') bio;
}
```

- \[x] Fornisce l'accesso dall'interno della classe componente all'oggetto ElementRef per il `<p>` con la variabile di riferimento del modello bio nella visualizzazione del modello del componente.
- \[ ] Indica che il `<p>` di cui viene eseguito il rendering come figlio della visualizzazione padre che utilizza questo componente.
- \[ ] Rende il `<p>` nel modello supporta la proiezione del contenuto.
- \[ ] Rende il `<p>` visibile nel rendering finale. Se il #bio è stato utilizzato nel modello e il @ViewChild non è stato utilizzato nella classe, Angular nasconderà automaticamente il valore `<p>` che ha #bio su di esso.

[DigitalOcean - viewchild-access-component](https://www.digitalocean.com/community/tutorials/angular-viewchild-access-component)

#### D2. Quale metodo viene utilizzato per collegare un FormControl a un elemento di input DOM nativo in moduli reattivi?

- \[ ] Aggiungere il nome della stringa assegnato a FormControl a un attributo denominato controlli nella finestra di dialogo <form> per indicare quali campi deve includere.
- \[ ] Utilizzare la sintassi di associazione tra parentesi quadre attorno all'attributo value sull'elemento DOM e impostarlo uguale a un'istanza di FormControl.
- \[x] Utilizzare la direttiva formControlName e impostare il valore uguale al nome della stringa assegnato a FormControl.
- \[ ] Utilizzare il nome della stringa assegnato a FormControl come valore per l'attributo id dell'elemento DOM.

[Angular.io - Gruppi di moduli reattivi](https://angular.io/guide/reactive-forms#creating-nested-form-groups)

#### D3. Qual è la differenza tra il `paramMap` E la `queryParamMap` sul `ActivatedRoute` classe?

- \[ ] ParamMap è un oggetto letterale dei parametri nel percorso URL di una route. QueryParamMap è un Observable di quegli stessi parametri.
- \[ ] ParamMap è un Oggetto osservabile che contiene i valori dei parametri che fanno parte del percorso URL di una route. QueryParamMap è un metodo che accetta una matrice di chiavi e viene utilizzato per trovare parametri specifici in paramMap.
- \[ ] paramMap è il nome legacy di Angular 3. Il nuovo nome è queryParamMap.
- \[x] Entrambi sono Osservabili contenenti valori della stringa URL della route richiesta. ParamMap contiene i valori dei parametri presenti nel percorso URL e queryParamMap contiene i parametri di query URL.

[StackOverflow](https://stackoverflow.com/a/49617621)

#### D4. In base al seguente utilizzo della pipe asincrona e supponendo che il campo della classe users sia un Observable, quante sottoscrizioni agli utenti Observable vengono effettuate?

```html
<h2>Names</h2>
<div *ngFor="let user of users | async">{{ user.name }}</div>
<h2>Ages</h2>
<div *ngFor="let user of users | async">{{ user.age }}</div>
<h2>Genders</h2>
<div *ngFor="let user of users | async">{{ user.gender }}</div>
```

- \[ ] Nessuno. La pipe asincrona non viene sottoscritta automaticamente.
- \[ ] Nessuno. La sintassi del modello non è corretta.
- \[x] Tre. Ce n'è uno per ogni pipe asincrona.
- \[ ] Uno. La pipe asincrona memorizza internamente observables per tipo.

[UltimateCourses](https://ultimatecourses.com/blog/angular-ngfor-async-pipe)

#### D5. Come è possibile utilizzare HttpClient per inviare una richiesta POST a un endpoint da una funzione addOrder in questo OrderService?

```ts
export class OrderService {
  constructor(private httpClient: HttpClient) {}

  addOrder(order: Order) {
    // Missing line
  }
}
```

- \[ ] this.httpClient.url(this.orderUrl).post(order);
- \[ ] this.httpClient.send(this.orderUrl, order);
- \[ ] this.httpClient.post<Order>(this.orderUrl, ordine);
- \[x] this.httpClient.post<Order>(this.orderUrl, order).subscribe();

[Angular.io - Invio di dati al server](https://angular.io/guide/http#sending-data-to-a-server)

#### D6. A cosa serve il metodo RouterModule.forRoot?

- \[ ] Registrazione di tutti i provider che si intende utilizzare nei componenti instradati.
- \[x] Registrazione delle definizioni di route a livello di applicazione radice.
- \[ ] Indicando che Angular dovrebbe fare il tifo per i tuoi percorsi per avere successo.
- \[ ] Dichiarando che si intende utilizzare il routing solo a livello di radice.

[O ' REILLY](https://www.oreilly.com/library/view/switching-to-angular/9781788620703/c9e90774-0e10-410b-bd20-d3e9e0b8d117.xhtml)

#### D7. Su quali elementi DOM corrisponderà questo selettore di metadati dei componenti?

```ts
@Component({
    selector: 'app-user-card',
    . . .
})
```

- \[ ] Qualsiasi elemento con l'attributo app-user-card, ad esempio `<div app-user-card></div>`.
- \[ ] La prima istanza di `<app-user-card></app-user-card>`.
- \[x] Tutte le istanze di `<app-user-card></app-user-card>`.
- \[ ] Tutte le istanze di `<user-card></user-card>`.

[Angular.io - Metadati dei componenti](https://angular.io/guide/architecture-components#component-metadata)

#### D8. Qual è la sintassi del modello corretta per l'utilizzo della direttiva strutturale ngFor incorporata per eseguire il rendering di un elenco di productNames?

- \[ ]

```ts
<ul>
  <li [ngFor]="let productName of productNames">{{ productName }}</li>
</ul>
```

- \[ ]

```ts
<ul>
  <li ngFor="let productName of productNames">{{ productName }}</li>
</ul>
```

- \[x]

```ts
<ul>
  <li *ngFor="let productName of productNames">{{ productName }}</li>
</ul>
```

- \[ ]

```ts
<ul>
  <? for productName in productNames { ?>
  <li>{{ productName }}</li>
  <? } ?>
</ul>
```

[Angular.io - Direttive strutturali](https://angular.io/guide/built-in-directives#listing-items-with-ngfor)

#### D9. Quali sono le proprietà dei metadati del decoratore a due componenti utilizzate per impostare gli stili CSS per un componente?

- \[ ] viewEncapsulation e viewEncapsulationFiles.
- \[ ] Ce n'è solo uno ed è la proprietà denominata css.
- \[ ] css e cssUrl.
- \[x] stili e styleUrls.

[Angular.io - Stili dei componenti](https://angular.io/guide/component-styles)

#### D10. Con la classe di componenti seguente, quale sintassi del modello verrà utilizzata nel modello per visualizzare il valore del campo della classe title?

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
- \[ ] Un campo di classe non può essere visualizzato in un modello tramite la sintassi del modello.

[Angular.io - Interpolazione di stringhe o Interpolazione di testo](https://angular.io/guide/interpolation)

#### D11. Qual è lo scopo del metodo valueChanges in un oggetto FormControl?

- \[ ] Viene utilizzato per configurare i valori consentiti per il controllo.
- \[ ] Viene utilizzato per modificare il valore di un controllo in un nuovo valore. Si chiamerebbe tale metodo e si passerebbe il nuovo valore per il campo modulo. Supporta anche il passaggio di una matrice di valori che possono essere impostati nel tempo.
- \[ ] Restituisce un valore booleano in base a se il valore del controllo è diverso dal valore con cui è stato inizializzato.
- \[x] È un osservabile che emette ogni volta che il valore del controllo cambia, in modo da poter reagire a nuovi valori e prendere decisioni logiche in quel momento.

[Angular.io - Visualizzazione di un valore di controllo from](https://angular.io/guide/reactive-forms#displaying-a-form-control-value)

#### D12. Quale direttiva viene utilizzata per collegare un `<a>` tag al routing?

- \[ ] routeTo
- \[x] routerLink
- \[ ] routePath
- \[ ] appLink

[Angular.io - RouterLink](https://angular.io/api/router/RouterLink#description)

#### D13. A cosa serve il decoratore Output in questa classe di componenti?

```ts
@Component({
    selector: 'app-shopping-cart',
    . . .
})
export class ShoppingCartComponent {
    @Output() itemTotalChanged = new EventEmitter();
}
```

- \[ ] Rende il `itemTotalChanged` campo di classe pubblico.
- \[ ] Fornisce un modo per associare i valori al `itemTotalChanged` campo di classe, in questo modo: `<app-shopping-cart [itemTotalChanged]="newTotal"></app-shopping-cart>`.
- \[x] Fornisce un modo per associare gli eventi al `itemTotalChanged` campo di classe, in questo modo: `<app-shopping-cart (itemTotalChanged)="logNewTotal($event)"></app-shopping-cart>`.
- \[ ] È semplicemente un modo per mettere un commento davanti a un campo di classe per la documentazione.

[Angular.io - Invio di dati al componente padre](https://angular.io/guide/inputs-outputs#sending-data-to-a-parent-component)

#### D14. Qual è la differenza tra questi due esempi di markup per la gestione condizionale della visualizzazione?

```html
<div *ngIf="isVisible">Active</div>
<div [hidden]="!isVisible">Active</div>
```

- \[ ] Il `ngIf` è una scorciatoia per l'altro esempio. Quando Angular elabora tale direttiva, scrive un elemento div nel DOM con la proprietà nascosta.
- \[ ] Sono fondamentalmente gli stessi.
- \[x] Il `ngIf` non esegue il rendering del div nel DOM se l'espressione è false. Le `hidden` l'utilizzo della proprietà nasconde il contenuto div nel riquadro di visualizzazione del browser, ma il div è ancora nel DOM.
- \[ ] Il `ngIf` è valido, ma l'uso del `hidden` è errata e genererà un errore.

[StackOverflow](https://stackoverflow.com/a/39778145)

#### D15. Come è possibile disabilitare il pulsante di invio quando il modulo presenta errori in questo esempio di moduli basati su modelli?

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

[Angular.io - Invia il modulo con ngSubmit](https://angular.io/guide/forms#submit-the-form-with-ngsubmit)

#### D16. Si desidera vedere quali file verrebbero generati creando un nuovo componente della scheda contatto. Quale comando useresti?

- \[x] ng generare la scheda contatto del componente --dry-run
- \[ ] ng generare la scheda contatto del componente --no-files
- \[ ] ng genera componente componente --dry
- \[ ] ng genera componente --exclude

[Angular.io - ng genera opzioni](https://angular.io/cli/generate#options)

#### D17. In base al componente seguente, quale sintassi del modello verrà utilizzata per associare il campo titleText di TitleCardComponent alla proprietà title dell'elemento h1?

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

[Angular.io - Interpolazione delle stringhe](https://angular.io/guide/interpolation)

#### D18. Cosa sono gli hook angolari per il ciclo di vita?

- \[ ] logger per monitorare lo stato di salute di un'app Angular
- \[ ] provider che possono essere utilizzati per tenere traccia delle istanze dei componenti
- \[ ] pipe incorporate che possono essere utilizzate nei modelli per eventi DOM
- \[x] metodi denominati riservati per componenti e direttive che Angular chiamerà durante i tempi impostati nella sua esecuzione e possono essere utilizzati per attingere a quei momenti del ciclo di vita

[Angular.io - Ganci per il ciclo di vita](https://angular.io/guide/lifecycle-hooks)

#### D19. Scegli la descrizione migliore per questo codice di sintassi del modello:

```html
<span>Boss: {{job?.bossName}} </span>
```

- \[ ] Il ? è l'abbreviazione per la pipe asincrona. Il valore del lavoro deve essere un Osservabile.
- \[x] Sta usando l'operatore di navigazione sicura (?) sul campo di lavoro. Se il campo job non è definito, l'accesso a bossName verrà ignorato e non si verificherà alcun errore.
- \[ ] Si è verificato un errore nella sintassi del modello. Le? non è valido qui.
- \[ ] Sta giocando il valore del lavoro se ne ha uno; in caso contrario, viene visualizzato il bossName.

[StackOverflow](https://stackoverflow.com/a/60182134)

#### D20. Come si configura una definizione di route per un oggetto UserDetailComponent che supporta il percorso URL user/23 (dove 23 rappresenta l'ID dell'utente richiesto)?

- \[x] `{ path: 'user/:id', component: UserDetailComponent }`
- \[ ] `{ url: 'user/:id', routedComponent: UserDetailComponent }`
- \[ ] `{ routedPath: 'user/:id', component: UserDetailComponent }`
- \[ ] `{ destination: new UserDetailComponent(), route: 'user/:id' }`

[CodeCraft - Percorsi parametrizzati](https://codecraft.tv/courses/angular/routing/parameterised-routes/#_configuration)

#### D21. Cosa stanno facendo i decoratori HostListener e il decoratore HostBinding in questa direttiva?

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

- \[x] Stanno impostando il campo CalloutDirective.fontWeight in base al fatto che il mouse sia o meno sopra l'elemento DOM. HostListener imposta quindi la proprietà CSS font-weight sul valore fontWeight.
- \[ ] Stanno istituendo la direttiva per verificare l'elemento DOM su cui si trova. Se sono stati aggiunti binding di evento per l'ingresso e l'uscita del mouse, utilizzerà questo codice. Altrimenti non accadrà nulla.
- \[ ] Questo è un uso scorretto di HostListener e HostBinding. I decoratori HostListener e HostBinding non fanno nulla sulle direttive; funzionano solo se utilizzati su componenti.
- \[ ] Se l'elemento DOM su cui è posizionata questa direttiva ha la proprietà CSS font-weight impostata su di esso, gli eventi mouseenter e mouseleave verranno generati.

[DigitalOcean](https://www.digitalocean.com/community/tutorials/angular-hostbinding-hostlistener)

#### D22. Quale sintassi del modello angolare è possibile utilizzare in questo campo modulo basato su modello per accedere al valore del campo e verificare la convalida all'interno del markup del modello?

```html
<input type="text" ngModel name="firstName" required minlength="4" />
<span *ngIf="">Invalid field data</span>
```

- \[x] È possibile utilizzare una variabile di riferimento del modello e la funzionalità exportAs della direttiva ngModel.
- \[ ] È possibile utilizzare la direttiva ngModel in combinazione con il nome del campo di input.
- \[ ] È possibile utilizzare una variabile di riferimento del modello per l'elemento di input HTML e quindi selezionare la proprietà valid da tale.
- \[ ] Non è possibile accedere al valore del campo con i moduli basati su modelli. È necessario utilizzare moduli reattivi per questo.

[Angular.io -Mostra e nascondi errore di convalida ](https://angular.io/guide/forms#show-and-hide-validation-error-messages)

[Medio](https://medium.com/@agoiabeladeyemi/template-driven-forms-in-angular-4a3a5ad960de)

#### D23. Qual è il tipo di valore che verrà archiviato nella variabile di riferimento del modello headerText in questo markup?

```html
<h1 #headerText>User List</h1>
```

- \[x] un Angular ElementRef, un wrapper attorno a un elemento nativo
- \[ ] il testo interno del `<h1>` elemento
- \[ ] una classe di componenti di intestazione
- \[ ] il tipo di elemento DOM nativo htmlHeadingElement

[Pluralsight - Variabile di riferimento del modello](https://www.pluralsight.com/guides/how-to-use-template-reference-variables-in-angular)

#### D24. Qual è la differenza, se presente, della logica di codice risultante basata su queste due configurazioni del provider?

```ts
[{ provide: FormattedLogger, useClass: Logger }][{ provide: FormattedLogger, useExisting: Logger }];
```

- \[ ] Sono gli stessi. Entrambi si tradurranno in una nuova istanza di Logger associata al token FormattedLogger.
- \[x] La sintassi useClass indica all'iniettore di creare una nuova istanza di Logger e di associarla al token FormattedLogger. La sintassi useExisting si riferisce a un'istanza di oggetto già esistente dichiarata come Logger.
- \[ ] Entrambi si sbagliano. Un tipo forte non può essere utilizzato per useClass o useExisting.
- \[ ] Sono gli stessi. Entrambi faranno sì che il token FormattedLogger sia un alias per l'istanza di Logger.

[Angular.io - Provider di dipendenze](https://angular.io/guide/dependency-injection-providers#defining-providers)

[TektutorialHub](https://www.tektutorialshub.com/angular/angular-providers/)

#### D25. Qual è lo scopo della proprietà data (vista nell'esempio seguente) in una configurazione di route?

```ts
  {
      path: 'customers',
      component: CustomerListComponent,
      data: { accountSection: true }
  }
```

- \[ ] un mapping chiave/valore per l'impostazione di valori @Input sull'istanza del componente instradato
- \[x] un modo per includere dati statici di sola lettura associati alla route che possono essere recuperati da ActivatedRoute
- \[ ] una proprietà sulla route che può essere utilizzata per caricare dati dinamici per la route
- \[ ] un oggetto che verrà iniettato automaticamente nel costruttore del componente instradato.

[TektutorialsHub](https://www.tektutorialshub.com/angular/angular-pass-data-to-route/#:~:text=Angular%20allows%20us%20to%20pass,of%20the%20history%20state%20object)

[StackOverflow](https://stackoverflow.com/a/36835156)

#### D26. Come funziona il built-in `ngIf` direttiva strutturale modificare il DOM renderizzato in base a questa sintassi del modello?

```ts
@Component({
  selector: 'app-product',
  template: '<div *ngIf="product">{{ product.name }}</div>',
})
export class ProductComponent {
  @Input() product;
}
```

- \[ ] Il `<div>` funge da segnaposto. Se il campo della classe di prodotto è "truthy", l'opzione `<div>` verrà sostituito solo dal `product.name` valore; in caso contrario, non verrà eseguito il rendering di nulla.
- \[ ] Il `<div>` verrà sempre renderizzato e, se il campo di prodotto è "veritiero", il `<div>` conterrà l'elemento `product.name` valore; In caso contrario, verrà eseguito il rendering del comando `<div>` elemento senza valore.
- \[ ] Produce un errore, dal momento che ngIf non è una direttiva strutturale incorporata.
- \[x] Se il campo della classe di prodotto è "truthy", il DOM renderizzato includerà il `<div>` con il valore del `product.name` campo. Se non è "veritiero", il DOM renderizzato non conterrà il `<div>` elemento.

[Riferimento (angular.io)](https://angular.io/api/common/NgIf)

#### D27. Che cosa fa questo codice?

```ts
@NgModule({
  declarations: [AppComponent],
  imports: [BrowserModule],
  bootstrap: [AppComponent],
})
export class AppModule {}

platformBrowserDynamic().bootstrapModule(AppModule);
```

- \[ ] Esegue uno unit test per un NgModule.
- \[ ] Fornisce un modo per codificare la struttura del documento di un'applicazione Angular. Il @NgModule è una forma di commento del codice inline che viene ignorato dal compilatore TypeScript ma viene visualizzato con una formattazione speciale nelle applicazioni dell'editor di codice.
- \[ ] Dichiara un modulo Angular denominato AppModule e lo rende disponibile per il lazy loading in tutta l'applicazione.
- \[x] Dichiara un modulo Angular denominato AppModule che contiene un componente bootstrap denominato AppComponent. Quindi registra quel modulo con Angular, in modo che l'app possa avviarsi.

[Angular.io - Il NgModule di base](https://angular.io/guide/ngmodules#the-basic-ngmodule)

#### D28. Quale scelta descrive meglio ciò che il _risolvere_ in questa configurazione di route?

```ts
{
   path: ':id',
   component: UserComponent,
   resolve: {
     user: UserResolverService
   }
}
```

- \[x] Prima di caricare il _Componente utente_, il router si iscriverà al _Osservabile_ restituito da un _risolvere_ nella finestra di dialogo _Metodo UserResolverService_. Questa tecnica può essere utilizzata per ottenere dati precaricati per un _rotta_.
- \[ ] Dopo il _rotta_ viene eseguita la risoluzione e il componente viene caricato e sottoposto a rendering, il parametro _Metodo UserResolverService_ avrà un metodo denominato _utente_ esecuzione che ripulirà tutte le connessioni dati aperte.
- \[ ] Si è verificato un errore. Il nome della proprietà corretto è _onResolve_.
- \[ ] Il _Componente utente_ avrà un parametro nel suo costruttore per *utente*E la _router_ gestirà l'iniezione di un valore per questo da una chiamata a un _utente_ nella finestra di dialogo _Metodo UserResolverService_.

[angular.io](https://angular.io/api/router/Resolve)

#### D29. Qual è lo scopo del decoratore ContentChildren in questa classe di componenti?

```ts
@Component({
 . . .
 template: '<ng-content></ng-content›'
})
export class TabsListComponent {
 @ContentChildren(TabComponent) tabs;
}
```

- \[ ] Se presente _TabsComponente_ Gli elementi vengono aggiunti alla finestra di dialogo _TabsListaComponente_ modello, verranno inseriti nel modello <ng-content> in fase di esecuzione.
- \[ ] Crea _TabComponente_ componenti nella finestra di dialogo _TabsListaComponente_ modello quando un modello _TabsListaComponente_ viene creata un'istanza.
- \[x] Fornisce l'accesso dall'interno della classe componente a qualsiasi _TabComponente_ Componenti che sono stati proiettati nel contenuto nella finestra di dialogo <ng-content> per questo componente.
- \[ ] Limita gli elementi consentiti che possono essere inseriti in un _TabsListaComponente_ per consentire solo _TabComponente_ elementi.

[betterprogramming.pub](https://betterprogramming.pub/understanding-contentchildren-with-an-example-e76ce78968db)

#### D30. Affinché Angular possa elaborare i componenti in un'applicazione, dove devono essere registrati i tipi di componenti?

- \[ ] all'interno di un tag di script nel file index.html
- \[ ] in un tag di metadati del decoratore NgModule denominato _Componenti_
- \[ ] Non è necessaria alcuna registrazione, è sufficiente includere i file dei componenti in una directory dell'app.
- \[x] in una proprietà di metadati del decoratore NgModule denominata _Dichiarazioni_

[angular.io](https://angular.io/guide/ngmodule-api#ngmodule-metadata)

#### D31. Qual è lo scopo del `fixture.detectChanges()` chiamare in questo unit test?

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

- \[ ] Tiene traccia di eventuali modifiche Ul e fallirà lo unit test se ne vengono effettuate.
- \[ ] Viene utilizzato per garantire la stabilità del modello di componente tra più unit test nell'intero gruppo di test.
- \[x] Forza Angular a eseguire il rilevamento delle modifiche, che eseguirà il rendering del _UserCardComponent_ prima di poter convalidare il relativo modello.
- \[ ] Viene utilizzato per registrare gli eventi di rilevamento delle modifiche nella console durante le esecuzioni degli unit test.

[angular.io](https://angular.io/api/core/testing/ComponentFixture#detectChanges)

#### D32. Che aspetto avrà il segmento url in base alla seguente chiamata al `Router.navigate` quando goToUser viene passato il valore 15?

```ts
export class ToolsComponent {
  constructor(private router: Router) {}
  goToUser(id: number) {
    this.router.navigate(['user', id]);
  }
}
```

- \[x] /utente/15
- \[ ] /utente?id=15
- \[ ] /utente:15
- \[ ] /utente;id=15

[angular.io](https://angular.io/api/router/Router#navigate)

#### D33. Quando un servizio viene fornito per root e viene anche aggiunto alla configurazione del provider per un modulo lazy-loaded, quale istanza di tale servizio fornisce l'iniettore ai costruttori nel modulo lazy-loaded?

- \[x] Una nuova istanza di tale servizio viene creata quando il modulo è pigro caricato.
- \[ ] Non è consentito fornire un servizio dello stesso tipo a livello di modulo lazy-loaded.
- \[ ] Se un'istanza del servizio non è stata ancora creata a livello radice. ne creerà uno lì e poi lo userà.
- \[ ] Una singola istanza di quel servizio viene sempre istanziata alla radice ed è l'unica mai utilizzata, anche all'interno di moduli pigri.

#### D34. Cosa sta facendo il decoratore HostBinding in questa direttiva?

```ts
@Directive({
  selector: ' [appHighlight] ',
})
export class HighlightDirective {
  @HostBinding('class.highlighted') highlight = true;
}
```

- \[x] Sta aggiungendo la classe CSS denominata evidenziata a qualsiasi elemento DOM che ha la direttiva appHighlight su di esso.
- \[ ] HostBinding non fa nulla sulle direttive, solo sui componenti.
- \[ ] Sta specificando se l'elemento host ottiene la classe evidenziata aggiunta al suo attributo class, quindi l'evidenziazione del campo della classe di direttiva verrà impostata su true; e se non viene aggiunto sull'host verrà impostato su false.
- \[ ] Sta creando uno stile in linea sull'elemento host con una proprietà CSS denominata highlight impostata su true.

[StackOverflow](https://stackoverflow.com/a/46207423)

#### D35. Nei moduli reattivi, quale tipo di classe di modulo Angular viene utilizzato sul DOM nativo <form> elemento per cablarlo?

- \[ ] `FormArray`
- \[ ] `FormControl`
- \[x] `FormGroup`
- \[ ] `all of these answers`

#### D36. Supponendo che il nome utente FormControl sia stato configurato con un validatore minLength, come è possibile impostare una visualizzazione degli errori nel seguente markup dei moduli reattivi per il campo nome utente?

```html
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

[Codice](https://codecraft.tv/courses/angular/forms/template-driven/)

#### D37. In che modo la modalità di incapsulamento della vista emulata gestisce i CSS per un componente?

- \[ ] Rende il CSS esattamente come l'hai scritto senza alcuna modifica.
- \[ ] Fa uso di markup DOM ombra e CSS.
- \[x] Crea attributi univoci per gli elementi DOM e definisce gli ambiti dei selettori CSS scritti in tali ID attributo.
- \[ ] Esegue il rendering di tutte le regole CSS che scrivi come CSS in linea su tutti gli elementi DOM su cui le usi nel modello.

[Angular.io](https://angular.io/guide/view-encapsulation#inspecting-generated-css)

#### D38. Con la seguente configurazione di TestBed, cosa è possibile utilizzare per accedere al DOM renderizzato per UserCardComponent?

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

#### D39. Dati questi due componenti, cosa verrà renderizzato al DOM in base all'utilizzo del markup?

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

#### D40. Dato il componente app-title-card nel codice seguente, quale DOM eseguirà il rendering del componente app-user-card?

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

#### D41. Scegli il codice corrispondente per la registrazione del provider personalizzato che il decoratore @Inject () sta cercando:

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

[Angular.io - Dependency Injection In Azione](https://angular.io/guide/dependency-injection-in-action#supply-a-custom-provider-with-inject)

#### D42. Quale scelta descrive meglio il seguente utilizzo del metodo HttpClient.get nel metodo della classe getsettings?

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

- \[ ] Il metodo pipe RxJs è un alias per il metodo subscribe, quindi una chiamata a `getSettings` eseguirà la query get. L'operatore di ripetizione dei tentativi viene utilizzato per indicare alla chiamata di pipe di riprovare la query get tre volte.
- \[ ] Produrrà un errore in fase di esecuzione perché il metodo pipe non è disponibile al di fuori del `Httpclient.get` chiamare.
- \[ ] Ogni singola chiamata al metodo getSettings comporterà che Httpclient effettui tre richieste get totali a settingsUrl, il che non è l'ideale perché ci saranno sempre due chiamate extra che non sono necessarie. L'operatore di ripetizione tentativi non deve essere utilizzato in questo modo.
- \[x] Quando viene sottoscritto il risultato del metodo getSettings, verrà effettuata la chiamata HTTP GET; se fallisce, verrà ritentato fino a tre volte prima che si arrenda e restituisca un errore.

[learnrxjs.io](https://www.learnrxjs.io/learn-rxjs/operators/error_handling/retry)

[dev.to](https://dev.to/gparlakov/how-does-rxjs-retry-work-412p)

#### D43. Quando un servizio richiede un'installazione per inizializzare lo stato predefinito tramite un metodo, come è possibile assicurarsi che tale metodo venga richiamato prima che il servizio venga iniettato ovunque?

- \[ ] Inserire invece la logica di quel metodo di servizio nel costruttore del servizio.
- \[x] Utilizzare un provider di fabbrica a livello di AppModule radice che dipende dal servizio per chiamare tale metodo di servizio.
- \[ ] non è possibile farlo all'avvio dell'applicazione; puoi farlo solo a livello di componente.
- \[ ] Creare un'istanza di un'istanza del servizio a livello globale (ambito finestra) e quindi chiamare tale metodo.

#### D44. Quale affermazione descrive meglio questo utilizzo del TestBed?

```ts
const spy = jasmine.createSpyObj('DataService', ['getUsersFromApi']);
TestBed.configureTestingModule({
  providers: [UserService, { provide: DataService, useValue: spy }],
});
const userService = TestBed.get(UserService);
```

- \[ ] Il TestBed è richiesto ogni volta che si desidera utilizzare un oggetto spia in uno unit test per un provider Angular.
- \[ ] Il TestBed viene utilizzato per testare la vista di un componente.
- \[x] Il TestBed impalca un NgModule con due provider e gestisce qualsiasi iniezione di dipendenza. Se una classe Angular richiede DataService nel relativo costruttore, TestBed inietterà spy in tale costruttore.
- \[ ] Il TestBed sta configurando il test runner per dirgli di eseguire solo test per i due provider elencati nel suo array di provider.
- `All other tests be ignored, including tests that assert results against one of these providers and a non-defined provider.`
  `Although it will work when multiple providers in this configuration are asserted against in a single test.`

#### D45. Qual è la differenza principale tra un componente e una direttiva?

- \[ ] Un componente utilizza una proprietà di metadati del selettore e una direttiva no.
- \[ ] Una direttiva può essere utilizzata per aggiungere eventi personalizzati al DOM e un componente non può.
- \[x] Un componente ha un modello e una direttiva no.
- \[ ] Una direttiva può essere destinata solo agli elementi DOM nativi.

[StackOverflow](https://stackoverflow.com/a/34616190)

#### D46. Cosa si potrebbe aggiungere a questa classe di direttiva per consentire di impostare la lunghezza del troncato durante l'utilizzo della direttiva nel markup?

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

#### D47. Come è possibile passare i parametri di query a questo `HttpClient.get` richiesta?

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

#### D48. Supponendo il `DataService` è stato registrato nei provider per l'applicazione, quale risposta descrive meglio cosa succede in base al costruttore di questo componente?

```ts
    @Component({
        ...
    })
    export class OrderHistoryComponent {
        constructor(private dataService: DataService) {}
        ...
    }
```

- \[ ] Dichiara che il `OrderHistoryComponent` avrà la propria versione di un `DataService` e che non dovrebbe mai utilizzare istanze esistenti. Le `DataService` dovrebbe essere istanziato all'interno della classe come campo privato affinché questo codice sia completo e funzionante.
- \[x] Quando Angular crea una nuova istanza del `OrderHistoryComponent`, l'iniettore fornirà un'istanza di un `DataService` al primo argomento del costruttore del componente. Il costruttore `dataService` verrà utilizzato per impostare un campo di istanza privata con lo stesso nome sull'istanza.
- \[ ] Fornisce un modo per eseguire solo test dei componenti; il costruttore non viene utilizzato nell'esecuzione effettiva dell'applicazione Angular.
- \[ ] Consente all'elemento personalizzato a cui è destinato il componente di avere una proprietà personalizzata denominata `dataService` che può essere utilizzato per associare un `DataService` istanza a.

[StackOverflow](https://stackoverflow.com/a/49755822)

[Angular.io - Iniezione di dipendenze](https://angular.io/guide/dependency-injection)

#### D49. Completare questo markup utilizzando il comando `ngIf` direttiva per implementare un altro caso che visualizzerà il testo "L'utente non è attivo":

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

#### D50. Qual è la sintassi corretta per una definizione di route per caricare pigramente un modulo di feature?

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

[Angular.io - Moduli di caricamento pigro](https://angular.io/guide/lazy-loading-ngmodules)

#### D51. Descrivere come viene impostata e configurata la convalida in questo esempio di moduli reattivi:

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

- \[ ] Il `FormControl` per `username` viene configurato per escludere tre validatori dai validatori che è consentito utilizzare.
- \[ ] Il `FormControl` per `username` si sta configurando per consentire l'utilizzo di tre possibili validatori: `required, maxLength`e uno personalizzato denominato `unique`. Per abilitarli `validators`, una direttiva di convalida dovrebbe essere inserita nei campi modulo nel markup.
- \[ ] La convalida non può essere impostata in questo modo in forme reattive.
- \[x] Il `FormControl` per `username` si sta configurando con tre validatori: il `required` e `minLength` validatori che provengono da Angular e una funzione di convalida personalizzata denominata `unique` che verifica la presenza del valore non uguale alla stringa `admin`.

[Angular.io - Convalida del modulo](https://angular.io/guide/form-validation)

[Angular University Blog](https://blog.angular-university.io/angular-custom-validators/)

#### D52. Cosa fa il decoratore iniettabile in questa classe di servizio?

```ts
@Injectable({
    providedIn: 'root'
)}
export class DataService { }
```

- \[ ] Registra un provider per il servizio che è disponibile solo a livello di modulo root, non per eventuali moduli figlio.
- \[x] Registra un provider per il servizio nell'iniettore dell'applicazione radice, rendendo disponibile una singola istanza di esso in tutta l'applicazione.
- \[ ] Fa in modo che il servizio possa essere iniettato solo nel componente bootstrapped per l'applicazione.
- \[ ] Imposta una regola di tempo di compilazione che consente di inserire il tipo di servizio solo nella proprietà dei metadati dei provider della radice NgModule.

[Angular.io](https://angular.io/guide/providers#providing-a-service)

#### D53. Descrivi l'utilizzo di questo codice

```ts
export interface AppSettings {
  title: string;
  version: number;
}
export const APP_SETTINGS = new InjectionToken<AppSettings>('app.settings');
```

- \[ ] InjectionToken aggiunge un'istanza di AppSettings al provider root tramite la chiamata del costruttore InjectionToken, rendendola automaticamente disponibile a tutti i NgModules, servizi e componenti in tutta l'applicazione Angular senza la necessità di iniettarla da nessuna parte.
- \[x] InjectionToken viene utilizzato per creare un token provider per una dipendenza non di classe. Un valore letterale Object può essere provider come valore per il tipo di provider di dipendenza APP_SETTINGS che può quindi essere iniettato in componenti, servizi, ecc..
- \[ ] InjectionToken viene utilizzato per creare un decoratore dinamico per AppSettings che può essere utilizzato sui parametri del costruttore tramite un decoratore @AppSettings.
- \[ ] Questo codice presenta un errore poiché non è possibile utilizzare un'interfaccia TypeScript per il tipo generico su InjectionToken

#### D54. Per l'esempio di moduli basati su modello seguente, quale argomento può essere passato al metodo di invio nell'evento click per inviare i dati per il modulo?

```html
<form #form="ngForm">
  <input type="text" ngModel="firstName" />
  <input type="text" ngModel="lastName" />
  <button (click)="submit()">Save</button>
</form>
```

- \[x] submit(form.value)
- \[ ] invia($event)
- \[ ] submit(ngForm.value)
- \[ ] submit(Nome, cognome)

#### D55. Qual è lo scopo della configurazione della proprietà prelodingStrategy in questo codice router?

```ts
RouterModule.forRoot(
  ...{
    preloadingStrategy: PreloadAllModules,
  },
);
```

- \[ ] Abilita la possibilità di contrassegnare i singoli percorsi per il precaricamento.
- \[ ] Precarica tutte le dipendenze per le route, creando istanze di servizi al primo avvio dell'app
- \[ ] Assicura che tutti i moduli vengano integrati in un singolo file bundle del modulo app.
- \[ ] Configura il router per caricare immediatamente tutte le route che hanno una proprietà loadChildren (route che vengono in genere caricate quando richiesto)

#### D56. Qual è un modo alternativo per scrivere questo markup per associare il valore del campo della classe `userName` al `h1` proprietà element title?

```html
<h1 [title]="userName">Current user is {{ userName }}</h1>
```

- \[ ] title="userName"
- \[x] title="{{ userName }}"
- \[ ] title="{{ 'userName' }}"
- \[ ] L'unico modo per farlo è usare le parentesi quadre.

#### D57. Cos'è il `async` pipe facendo in questo esempio?

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

- \[ ] Non sta facendo nulla, poiché la pipe asincrona non può essere utilizzata in un `ngFor` affermazione.
- \[ ] Sta configurando il `ngFor` per supportare più elenchi di utenti contemporaneamente.
- \[x] Si sta abbonando all'osservabile restituito dal `HttpClient.get` e il wrapping del valore restituito in modo che possa essere ripetuto nella finestra di dialogo `ngFor`.
- \[ ] Consente a tutti gli utenti di partecipare al `users` da eseguire il rendering contemporaneamente al DOM.

#### D58. Come utilizzeresti questa direttiva nel markup in base al suo valore di selezione

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

#### D59. Quale hook del ciclo di vita può essere utilizzato su un componente per monitorare tutte le modifiche ai valori @Input su quel componente?

- \[ ] ngOnInit
- \[ ] ngChanges
- \[ ] ngAfterInputChange
- \[x] ngOnChanges

[Come rilevare quando un valore @Input() cambia in Angular?](https://stackoverflow.com/a/44686085/1573267)

#### D60. Quale sarebbe un esempio di utilizzo della sintassi del modello di questa pipe personalizzata?

```ts
@Pipe({ name: 'truncate' })
export class TruncatePipe implements PipeTransform {
	transform(value: string, maxLength: number, showEllipsis: boolean){
		const newValue = maxLength ? value.substr(0, maxLength): value;
		return showEllipsis ? '${newValue}...` : newValue;
	}
}
```

- \[x] {( 'del testo lungo' | troncare:10 })
- \[ ] {( 'some long text' | truncate:10:true })
- \[ ] {( 'un po' di testo lungo' | troncare })
- \[ ] tutte queste risposte

\[ricontrolla le risposte]

#### D61. Quale comando Angular CLI verrà eseguito per generare un oggetto UsersComponent e aggiungerlo a SharedModule (nel file shared.module.ts nell'applicazione)?

- \[ ] ng genera componente --newModule=shared
- \[ ] ng genera utenti componenti --module=shared
- \[ ] ng genera utenti componenti --shared
- \[ ] ng genera componente --add=shared

\[ricontrolla le risposte]

#### D62. Come è possibile riscrivere questo markup in modo che il contenitore div non sia necessario nel rendering DOM finale

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

\[ricontrolla le risposte]

#### D63. Descrivi l'utilizzo di questo codice:

```ts
export interface AppSettings {
  title: string;
  version: number;
}
```

- \[ ] Questo codice è un errore poiché non è possibile utilizzare un'interfaccia TypeScript per il tipo generico su InjectionToken.
- \[ ] InjectionToken viene utilizzato per creare un token provider per una dipendenza non di classe. Un oggetto lieteral può essere fornito come valore per il tipo di provider di dipendenza APP_SETTINGS che può quindi essere iniettato in componenti, servizi e così via.
- \[ ] InjectionToken aggiunge un'istanza di AppSettings al provider roote tramite la chiamata del costruttore InjectionToken, rendendola automaticamente disponibile a tutti i NgModules, servizi e componenti attraverso l'applicazione Angular senza la necessità di iniettarla da nessuna parte.
- \[ ] InjectionToken viene utilizzato per creare un decoratore dinamico per AppSettings che può essere utilizzato sui parametri del costruttore tramite un decoratore @AppSettings.

\[ricontrolla le risposte]

#### D64. Quali utilità Angular, se presenti, sono necessarie per eseguire lo unit test di un servizio senza dipendenze del costruttore?

- \[ ] È necessario il metodo helper By.css()
- \[ ] Per eseguire il servizio per lo unit test è necessario uno staffaggio di testo.
- \[ ] Nessuno. È possibile creare un'istanza di un servizio e testare l'unità da solo.
- \[x] La classe TestBed è necessaria per creare un'istanza del servizio.

[Unit test angolari](https://angular.io/guide/testing-services) - ricontrollare le risposte

#### D65. Qual è la differenza tra canActivate e le protezioni del percorso CanLoad?

- \[ ] CanActivate viene utilizzato per controllare l'accesso. CanLoad viene utilizzato per precaricare i dati per il percorso.
- \[x] CanLoad viene usato all'avvio dell'app per consentire o negare l'aggiunta di route alla tabella di route. CanActivate viene utilizzato per gestire l'accesso ai percorsi nel momento in cui vengono richiesti.
- \[ ] CanActivate e CanLoad fanno esattamente la stessa cosa.
- \[ ] CanLoad impedisce la consegna e il caricamento di un intero NgModule. CanActivate interrompe il routing a un componente in tale NgModule, ma tale modulo è ancora caricato.

[CanActivate vs Canload](https://stackoverflow.com/questions/42026045/difference-between-angulars-canload-and-canactivate#:~:text=canActivate%20is%20used%20to%20prevent,not%20authorized%20to%20do%20so.) CanActivate impedisce l'accesso sui percorsi, CanLoad impedisce il caricamento lento.

#### D66. A cosa serve la proprietà outlet in questo oggetto definizione router?

```ts
{
	path: 'document',
	component: DocumentComponent,
	outlet: 'document-box'
}
```

- \[ ] individuerà tutte le istanze di <document-box> nel DOM e inserire un elemento DocumentComponent al loro interno durante la navigazione del percorso.
- \[ ] Dichiara che il DocumentComponent può essere utilizzato come figlio per un <<document-box> oltre ad essere instradato a.
- \[x] Eravamo soliti prendere di mira un <router-outlet> con l'attributo name che corrisponde al valore stringa come percorso per il documentComponent di cui eseguire il rendering quando viene instradato.
- \[ ] È una fonte di energia per il router. (sicuramente non la risposta :P)

[Uscita angolare](https://angular.io/api/router/RouterOutlet) - ricontrolla la risposta
