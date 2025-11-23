## Angular

#### F1. Was ist der Zweck des ViewChild-Dekorators in dieser Komponentenklasse?

```ts
@Component({
    ...
    template: '<p #bio></p>'
})
export class UserDetailsComponent {
    @ViewChild('bio') bio;
}
```

- [x] Er bietet Zugriff von innerhalb der Komponentenklasse auf das ElementRef-Objekt für das `<p>`-Tag, das die bio-Template-Referenzvariable in der Template-Ansicht der Komponente hat.
- [ ] Er zeigt an, dass das `<p>`-Tag als Kind der übergeordneten Ansicht gerendert wird, die diese Komponente verwendet.
- [ ] Er ermöglicht es dem `<p>`-Tag im Template, Content Projection zu unterstützen.
- [ ] Er macht das `<p>`-Tag im finalen Rendering sichtbar. Wenn #bio im Template verwendet wurde und @ViewChild nicht in der Klasse verwendet wurde, würde Angular das `<p>`-Tag mit #bio automatisch verbergen.

[DigitalOcean - viewchild-access-component](https://www.digitalocean.com/community/tutorials/angular-viewchild-access-component)

#### F2. Welche Methode wird verwendet, um ein FormControl in reaktiven Formularen mit einem nativen DOM-Eingabeelement zu verbinden?

- [ ] Fügen Sie den String-Namen, der dem FormControl gegeben wurde, einem Attribut namens controls auf dem `<form>`-Element hinzu, um anzugeben, welche Felder es enthalten soll.
- [ ] Verwenden Sie die eckige Klammer-Binding-Syntax um das value-Attribut auf dem DOM-Element und setzen Sie dies gleich einer Instanz des FormControl.
- [x] Verwenden Sie die formControlName-Direktive und setzen Sie den Wert gleich dem String-Namen, der dem FormControl gegeben wurde.
- [ ] Verwenden Sie den String-Namen, der dem FormControl gegeben wurde, als Wert für das id-Attribut des DOM-Elements.

[Angular.io - Reactive Form Groups](https://angular.io/guide/reactive-forms#creating-nested-form-groups)

#### F3. Was ist der Unterschied zwischen `paramMap` und `queryParamMap` in der `ActivatedRoute`-Klasse?

- [ ] Die paramMap ist ein Objekt-Literal der Parameter im URL-Pfad einer Route. Die queryParamMap ist ein Observable dieser gleichen Parameter.
- [ ] Die paramMap ist ein Observable, das die Parameterwerte enthält, die Teil des URL-Pfads einer Route sind. Die queryParamMap ist eine Methode, die ein Array von Schlüsseln entgegennimmt und verwendet wird, um bestimmte Parameter in der paramMap zu finden.
- [ ] paramMap ist der Legacy-Name aus Angular 3. Der neue Name ist queryParamMap.
- [x] Beide sind Observables, die Werte aus dem angeforderten URL-String der Route enthalten. Die paramMap enthält die Parameterwerte, die im URL-Pfad sind, und die queryParamMap enthält die URL-Query-Parameter.

[StackOverflow](https://stackoverflow.com/a/49617621)

#### F4. Basierend auf der folgenden Verwendung der async-Pipe und unter der Annahme, dass das Klassenfeld users ein Observable ist, wie viele Subscriptions zum users-Observable werden erstellt?

```html
<h2>Namen</h2>
<div *ngFor="let user of users | async">{{ user.name }}</div>
<h2>Alter</h2>
<div *ngFor="let user of users | async">{{ user.age }}</div>
<h2>Geschlechter</h2>
<div *ngFor="let user of users | async">{{ user.gender }}</div>
```

- [ ] Keine. Die async-Pipe abonniert nicht automatisch.
- [ ] Keine. Die Template-Syntax ist nicht korrekt.
- [x] Drei. Es gibt eine für jede async-Pipe.
- [ ] Eine. Die async-Pipe cached Observables nach Typ intern.

[UltimateCourses](https://ultimatecourses.com/blog/angular-ngfor-async-pipe)

#### F5. Wie können Sie den HttpClient verwenden, um eine POST-Anfrage an einen Endpunkt aus einer addOrder-Funktion in diesem OrderService zu senden?

```ts
export class OrderService {
  constructor(private httpClient: HttpClient) {}

  addOrder(order: Order) {
    // Fehlende Zeile
  }
}
```

- [ ] `this.httpClient.url(this.orderUrl).post(order);`
- [ ] `this.httpClient.send(this.orderUrl, order);`
- [ ] `this.httpClient.post<Order>(this.orderUrl, order);`
- [x] `this.httpClient.post<Order>(this.orderUrl, order).subscribe();`

[Angular.io - Daten an Server senden](https://angular.io/guide/http#sending-data-to-a-server)

#### F6. Wofür wird die RouterModule.forRoot-Methode verwendet?

- [ ] Zum Registrieren von Providern, die Sie in gerouteten Komponenten verwenden möchten.
- [x] Zum Registrieren von Route-Definitionen auf der Root-Anwendungsebene.
- [ ] Um anzuzeigen, dass Angular Ihre Routes zum Erfolg anfeuern soll.
- [ ] Um zu deklarieren, dass Sie Routing nur auf der Root-Ebene verwenden möchten.

[O'REILLY](https://www.oreilly.com/library/view/switching-to-angular/9781788620703/c9e90774-0e10-410b-bd20-d3e9e0b8d117.xhtml)

#### F7. Welche DOM-Elemente werden mit diesem Komponenten-Metadaten-Selektor übereinstimmen?

```ts
@Component({
    selector: 'app-user-card',
    . . .
})
```

- [ ] Jedes Element mit dem Attribut app-user-card, wie z.B. `<div app-user-card></div>`.
- [ ] Die erste Instanz von `<app-user-card></app-user-card>`.
- [x] Alle Instanzen von `<app-user-card></app-user-card>`.
- [ ] Alle Instanzen von `<user-card></user-card>`.

[Angular.io - Component Metadata](https://angular.io/guide/architecture-components#component-metadata)

#### F8. Was ist die korrekte Template-Syntax für die Verwendung der eingebauten strukturellen ngFor-Direktive, um eine Liste von productNames zu rendern?

- [ ] A

  ```html
  <ul>
    <li [ngFor]="let productName of productNames">{{ productName }}</li>
  </ul>
  ```

- [ ] B

  ```html
  <ul>
    <li ngFor="let productName of productNames">{{ productName }}</li>
  </ul>
  ```

- [x] C

  ```html
  <ul>
    <li *ngFor="let productName of productNames">{{ productName }}</li>
  </ul>
  ```

- [ ] D

  ```html
  <ul>
    <? for productName in productNames { ?>
    <li>{{ productName }}</li>
    <? } ?>
  </ul>
  ```

[Angular.io - Strukturelle Direktiven](https://angular.io/guide/built-in-directives#listing-items-with-ngfor)

#### F9. Was sind die beiden Komponenten-Dekorator-Metadaten-Eigenschaften, die verwendet werden, um CSS-Stile für eine Komponente einzurichten?

- [ ] viewEncapsulation und viewEncapsulationFiles.
- [ ] Es gibt nur eine und das ist die Eigenschaft namens css.
- [ ] css und cssUrl.
- [x] styles und styleUrls.

[Angular.io - Component Styles](https://angular.io/guide/component-styles)

#### F10. Mit der folgenden Komponentenklasse, welche Template-Syntax würden Sie im Template verwenden, um den Wert des title-Klassenfelds anzuzeigen?

```ts
@Component({
  selector: 'app-title-card',
  template: '',
})
class TitleCardComponent {
  title = 'User Data';
}
```

- [ ] `{{ 'title' }}`
- [x] `{{ title }}`
- [ ] `[title]`
- [ ] Ein Klassenfeld kann nicht über die Template-Syntax in einem Template angezeigt werden.

[Angular.io - String Interpolation oder Text Interpolation](https://angular.io/guide/interpolation)

#### F11. Was ist der Zweck der valueChanges-Methode auf einem FormControl?

- [ ] Sie wird verwendet, um zu konfigurieren, welche Werte für das Control erlaubt sind.
- [ ] Sie wird verwendet, um den Wert eines Controls auf einen neuen Wert zu ändern. Sie würden diese Methode aufrufen und den neuen Wert für das Formularfeld übergeben. Sie unterstützt sogar das Übergeben eines Arrays von Werten, die im Laufe der Zeit gesetzt werden können.
- [ ] Sie gibt einen Boolean zurück, basierend darauf, ob der Wert des Controls sich von dem Wert unterscheidet, mit dem es initialisiert wurde.
- [x] Es ist ein Observable, das jedes Mal emittiert, wenn sich der Wert des Controls ändert, sodass Sie auf neue Werte reagieren und zu diesem Zeitpunkt logische Entscheidungen treffen können.

[Angular.io - Anzeigen eines Formular-Control-Werts](https://angular.io/guide/reactive-forms#displaying-a-form-control-value)

#### F12. Welche Direktive wird verwendet, um ein `<a>`-Tag mit Routing zu verknüpfen?

- [ ] routeTo
- [x] routerLink
- [ ] routePath
- [ ] appLink

[Angular.io - RouterLink](https://angular.io/api/router/RouterLink#description)

#### F13. Wofür wird der Output-Dekorator in dieser Komponentenklasse verwendet?

```ts
@Component({
    selector: 'app-shopping-cart',
    . . .
})
export class ShoppingCartComponent {
    @Output() itemTotalChanged = new EventEmitter();
}
```

- [ ] Es macht das `itemTotalChanged`-Klassenfeld öffentlich.
- [ ] Es bietet eine Möglichkeit, Werte an das `itemTotalChanged`-Klassenfeld zu binden, so: `<app-shopping-cart [itemTotalChanged]="newTotal"></app-shopping-cart>`.
- [x] Es bietet eine Möglichkeit, Ereignisse an das `itemTotalChanged`-Klassenfeld zu binden, so: `<app-shopping-cart (itemTotalChanged)="logNewTotal($event)"></app-shopping-cart>`.
- [ ] Es ist einfach eine Möglichkeit, einen Kommentar vor ein Klassenfeld zur Dokumentation zu setzen.

[Angular.io - Daten an übergeordnete Komponente senden](https://angular.io/guide/inputs-outputs#sending-data-to-a-parent-component)

#### F14. Was ist der Unterschied zwischen diesen beiden Markup-Beispielen für die bedingte Handhabung der Anzeige?

```html
<div *ngIf="isVisible">Aktiv</div>
<div [hidden]="!isVisible">Aktiv</div>
```

- [ ] Das `ngIf` ist eine Kurzform für das andere Beispiel. Wenn Angular diese Direktive verarbeitet, schreibt es ein div-Element in das DOM mit der hidden-Eigenschaft.
- [ ] Sie sind grundsätzlich gleich.
- [x] Die `ngIf`-Direktive rendert das div nicht im DOM, wenn der Ausdruck false ist. Die Verwendung der `hidden`-Eigenschaft verbirgt den div-Inhalt im Browser-Viewport, aber das div ist immer noch im DOM.
- [ ] Das `ngIf` ist gültig, aber die Verwendung der `hidden`-Eigenschaft ist falsch und wird einen Fehler werfen.

[StackOverflow](https://stackoverflow.com/a/39778145)

#### F15. Wie können Sie den Submit-Button deaktivieren, wenn das Formular in diesem Template-getriebenen Formular-Beispiel Fehler hat?

```html
<form #userForm="ngForm">
  <input type="text" ngModel name="firstName" required />
  <input type="text" ngModel name="lastName" required />
  <button (click)="submit(userForm.value)">Speichern</button>
</form>
```

- [ ] A

  ```html
  <button (click)="submit(userForm.value)" disable="userForm.invalid">Speichern</button>
  ```

- [x] B

  ```html
  <button (click)="submit(userForm.value)" [disabled]="userForm.invalid">Speichern</button>
  ```

- [ ] C

  ```html
  <button (click)="submit(userForm.value)" [ngForm.disabled]="userForm.valid">Speichern</button>
  ```

- [ ] D

  ```html
  <button (click)="submit(userForm.value)" *ngIf="userForm.valid">Speichern</button>
  ```

[Angular.io - Formular mit ngSubmit absenden](https://angular.io/guide/forms#submit-the-form-with-ngsubmit)

#### F16. Welchen Angular CLI-Befehl würden Sie verwenden, um zu sehen, welche Dateien durch das Erstellen einer neuen contact-card-Komponente generiert würden?

- [x] ng generate component contact-card --dry-run
- [ ] ng generate component contact-card --no-files
- [ ] ng generate component component --dry
- [ ] ng generate component --exclude

[Angular.io - ng generate Optionen](https://angular.io/cli/generate#options)

#### F17. Basierend auf der folgenden Komponente, welche Template-Syntax würden Sie verwenden, um das titleText-Feld der TitleCardComponent an die title-Eigenschaft des h1-Elements zu binden?

```ts
@Component({
  selector: 'app-title-card',
  template: '<h1 title="User Data"> {{titleText}}</h1>',
})
export class TitleCardComponent {
  titleText = 'User Data';
}
```

- [ ] `<h1 data-title="titleText">{{ titleText }}</h1>`
- [ ] `<h1 title="titleText">{{ titleText }}</h1>`
- [x] `<h1 [title]="titleText">{{ titleText }}</h1>`
- [ ] `<h1 titleText>{{ titleText }}</h1>`

[Angular.io - String Interpolation](https://angular.io/guide/interpolation)

#### F18. Was sind Angular-Lifecycle-Hooks?

- [ ] Logger zur Verfolgung der Gesundheit einer Angular-App
- [ ] Provider, die verwendet werden können, um die Instanzen von Komponenten zu verfolgen
- [ ] Eingebaute Pipes, die in Templates für DOM-Events verwendet werden können
- [x] Reservierte benannte Methoden für Komponenten und Direktiven, die Angular während bestimmter Zeiten in seiner Ausführung aufruft und die verwendet werden können, um in diese Lifecycle-Momente einzutauchen

[Angular.io - Lifecycle Hooks](https://angular.io/guide/lifecycle-hooks)

#### F19. Wählen Sie die beste Beschreibung für diese Template-Syntax aus:

```html
<span>Chef: {{job?.bossName}} </span>
```

- [ ] Das ? ist eine Kurzform für die async-Pipe. Der job-Wert muss ein Observable sein.
- [x] Es verwendet den Safe-Navigation-Operator (?) auf dem job-Feld. Wenn das job-Feld undefined ist, wird der Zugriff auf bossName ignoriert und es tritt kein Fehler auf.
- [ ] Es gibt einen Fehler in der Template-Syntax. Das ? ist hier nicht gültig.
- [ ] Es zeigt den job-Wert an, wenn er einen hat; andernfalls zeigt es den bossName an.

[StackOverflow](https://stackoverflow.com/a/60182134)

#### F20. Wie würden Sie eine Route-Definition für eine UserDetailComponent konfigurieren, die den URL-Pfad user/23 unterstützt (wobei 23 die ID des angeforderten Benutzers darstellt)?

- [x] `{ path: 'user/:id', component: UserDetailComponent }`
- [ ] `{ url: 'user/:id', routedComponent: UserDetailComponent }`
- [ ] `{ routedPath: 'user/:id', component: UserDetailComponent }`
- [ ] `{ destination: new UserDetailComponent(), route: 'user/:id' }`

[CodeCraft - Parametrisierte Routes](https://codecraft.tv/courses/angular/routing/parameterised-routes/#_configuration)

#### F21. Was machen die HostListener-Dekoratoren und der HostBinding-Dekorator in dieser Direktive?

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

- [x] Sie setzen das CalloutDirective.fontWeight-Feld basierend darauf, ob die Maus über dem DOM-Element ist oder nicht. Der HostListener setzt dann die CSS-Eigenschaft font-weight auf den fontWeight-Wert.
- [ ] Sie richten die Direktive ein, um das DOM-Element zu überprüfen, auf dem sie sich befindet. Wenn es Event-Bindings für Maus-Enter und -Leave hinzugefügt hat, wird dieser Code verwendet. Andernfalls passiert nichts.
- [ ] Dies ist eine falsche Verwendung von HostListener und HostBinding. Die HostListener- und HostBinding-Dekoratoren machen nichts bei Direktiven; sie funktionieren nur, wenn sie bei Komponenten verwendet werden.
- [ ] Wenn das DOM-Element, auf dem diese Direktive platziert ist, die CSS-Eigenschaft font-weight gesetzt hat, werden die mouseenter- und mouseleave-Events ausgelöst.

[DigitalOcean](https://www.digitalocean.com/community/tutorials/angular-hostbinding-hostlistener)

#### F22. Welche Angular-Template-Syntax können Sie auf diesem Template-getriebenen Formularfeld verwenden, um auf den Feldwert zuzugreifen und die Validierung innerhalb des Template-Markups zu überprüfen?

```html
<input type="text" ngModel name="firstName" required minlength="4" />
<span *ngIf="">Ungültige Felddaten</span>
```

- [x] Sie können eine Template-Referenzvariable und die exportAs-Funktion verwenden, die die ngModel-Direktive hat.
- [ ] Sie können die ngModel-Direktive in Kombination mit dem Eingabefeldnamen verwenden.
- [ ] Sie können eine Template-Referenzvariable für das HTML-Eingabeelement verwenden und dann die valid-Eigenschaft davon überprüfen.
- [ ] Es ist nicht möglich, Zugriff auf den Feldwert mit Template-getriebenen Formularen zu erhalten. Sie müssen dafür reaktive Formulare verwenden.

1. [Angular.io - Validierungsfehlermeldungen anzeigen und verbergen](https://angular.io/guide/forms#show-and-hide-validation-error-messages)
2. [Medium](https://medium.com/@agoiabeladeyemi/template-driven-forms-in-angular-4a3a5ad960de)

#### F23. Welcher Werttyp wird in der headerText-Template-Referenzvariablen in diesem Markup gespeichert?

```html
<h1 #headerText>Benutzerliste</h1>
```

- [x] Eine Angular ElementRef, ein Wrapper um ein natives Element
- [ ] Der innere Text des `<h1>`-Elements
- [ ] Eine Header-Komponentenklasse
- [ ] Der native DOM-Elementtyp HTMLHeadingElement

[Pluralsight - Template-Referenzvariable](https://www.pluralsight.com/guides/how-to-use-template-reference-variables-in-angular)

#### F24. Was ist der Unterschied, falls vorhanden, der resultierenden Code-Logik basierend auf diesen beiden Provider-Konfigurationen?

```ts
[{ provide: FormattedLogger, useClass: Logger }][{ provide: FormattedLogger, useExisting: Logger }];
```

- [ ] Sie sind gleich. Beide werden zu einer neuen Instanz von Logger führen, die an das FormattedLogger-Token gebunden ist.
- [x] Die useClass-Syntax weist den Injector an, eine neue Instanz von Logger zu erstellen und diese Instanz an das FormattedLogger-Token zu binden. Die useExisting-Syntax bezieht sich auf eine bereits existierende Objektinstanz, die als Logger deklariert ist.
- [ ] Beide sind falsch. Ein starker Typ kann nicht für useClass oder useExisting verwendet werden.
- [ ] Sie sind gleich. Beide werden dazu führen, dass das FormattedLogger-Token ein Alias für die Instanz von Logger ist.

1. [Angular.io - Dependency Providers](https://angular.io/guide/dependency-injection-providers#defining-providers)
2. [TektutorialHub](https://www.tektutorialshub.com/angular/angular-providers/)

#### F25. Was ist der Zweck der data-Eigenschaft (im folgenden Beispiel zu sehen) in einer Route-Konfiguration?

```ts
   {
       path: 'customers',
       component: CustomerListComponent,
       data: { accountSection: true }
   }
```

- [ ] Ein Key/Value-Mapping zum Setzen von @Input-Werten auf der gerouteten Komponenteninstanz
- [x] Eine Möglichkeit, statische, schreibgeschützte Daten einzuschließen, die mit der Route verknüpft sind und die von der ActivatedRoute abgerufen werden können
- [ ] Eine Eigenschaft auf der Route, die verwendet werden kann, um dynamische Daten für die Route zu laden
- [ ] Ein Objekt, das automatisch in den Konstruktor der gerouteten Komponente injiziert wird.

1. [TektutorialsHub](https://www.tektutorialshub.com/angular/angular-pass-data-to-route/#:~:text=Angular%20allows%20us%20to%20pass,of%20the%20history%20state%20object)
2. [StackOverflow](https://stackoverflow.com/a/36835156)

#### F26. Wie ändert die eingebaute strukturelle `ngIf`-Direktive das gerenderte DOM basierend auf dieser Template-Syntax?

```ts
@Component({
  selector: 'app-product',
  template: '<div *ngIf="product">{{ product.name }}</div>',
})
export class ProductComponent {
  @Input() product;
}
```

- [ ] Das `<div>` fungiert als Platzhalter. Wenn das product-Klassenfeld "truthy" ist, wird das `<div>` durch nur den `product.name`-Wert ersetzt; wenn nicht, wird nichts gerendert.
- [ ] Das `<div>` wird immer gerendert, und wenn das product-Feld "truthy" ist, enthält das `<div>`-Element den `product.name`-Wert; andernfalls rendert es das `<div>`-Element ohne Wert darin.
- [ ] Es erzeugt einen Fehler, da ngIf keine eingebaute strukturelle Direktive ist.
- [x] Wenn das product-Klassenfeld "truthy" ist, dann enthält das gerenderte DOM das `<div>` mit dem Wert des `product.name`-Felds. Wenn es nicht "truthy" ist, enthält das gerenderte DOM nicht das `<div>`-Element.

[Referenz (angular.io)](https://angular.io/api/common/NgIf)

#### F27. Was bewirkt dieser Code?

```ts
@NgModule({
  declarations: [AppComponent],
  imports: [BrowserModule],
  bootstrap: [AppComponent],
})
export class AppModule {}

platformBrowserDynamic().bootstrapModule(AppModule);
```

- [ ] Es führt einen Unit-Test für ein NgModule aus.
- [ ] Es bietet eine Möglichkeit, die Dokumentstruktur einer Angular-Anwendung zu codieren. Das @NgModule ist eine Form von Inline-Code-Kommentierung, die vom TypeScript-Compiler ignoriert wird, aber mit spezieller Formatierung in Code-Editor-Anwendungen angezeigt wird.
- [ ] Es deklariert ein Angular-Modul namens AppModule und macht es für Lazy Loading in der gesamten Anwendung verfügbar.
- [x] Es deklariert ein Angular-Modul namens AppModule, das eine Bootstrap-Komponente namens AppComponent enthält. Dann registriert es dieses Modul bei Angular, damit die App starten kann.

[Angular.io - Das grundlegende NgModule](https://angular.io/guide/ngmodules#the-basic-ngmodule)

#### F28. Welche Wahl beschreibt am besten, was die _resolve_-Eigenschaft in dieser Route-Konfiguration macht?

```ts
{
   path: ':id',
   component: UserComponent,
   resolve: {
     user: UserResolverService
   }
}
```

- [x] Vor dem Laden der _UserComponent_ wird der Router das _Observable_ abonnieren, das von einer _resolve_-Methode im _UserResolverService_ zurückgegeben wird. Diese Technik kann verwendet werden, um vorgeladene Daten für eine _Route_ zu erhalten.
- [ ] Nachdem die _Route_ aufgelöst wurde und die Komponente geladen und gerendert ist, wird der _UserResolverService_ eine Methode namens _user_ ausführen, die alle offenen Datenverbindungen bereinigt.
- [ ] Es gibt einen Fehler. Der korrekte Eigenschaftsname ist _onResolve_.
- [ ] Die _UserComponent_ wird einen Parameter in ihrem Konstruktor für _user_ haben, und der _Router_ wird das Injizieren eines Werts dafür von einem Aufruf einer _user_-Methode im _UserResolverService_ handhaben.

[angular.io](https://angular.io/api/router/Resolve)

#### F29. Was ist der Zweck des ContentChildren-Dekorators in dieser Komponentenklasse?

```ts
@Component({
 . . .
 template: '<ng-content></ng-content>'
})
export class TabsListComponent {
 @ContentChildren(TabComponent) tabs;
}
```

- [ ] Wenn _TabsComponent_-Elemente zum _TabsListComponent_-Template hinzugefügt werden, werden sie zur Laufzeit in das `<ng-content>`-Element eingefügt.
- [ ] Es erstellt _TabComponent_-Komponenten im _TabsListComponent_-Template, wenn eine _TabsListComponent_ instanziiert wird.
- [x] Es bietet Zugriff von innerhalb der Komponentenklasse auf alle _TabComponent_-Komponenten, die in das `<ng-content>` für diese Komponente projiziert wurden.
- [ ] Es beschränkt die erlaubten Elemente, die in ein _TabsListComponent_-Element eingefügt werden können, um nur _TabComponent_-Elemente zuzulassen.

[betterprogramming.pub](https://betterprogramming.pub/understanding-contentchildren-with-an-example-e76ce78968db)

#### F30. Damit Angular Komponenten in einer Anwendung verarbeiten kann, wo müssen die Komponententypen registriert werden?

- [ ] Innerhalb eines script-Tags in der index.html-Datei
- [ ] In einem NgModule-Dekorator-Metadaten-Tag namens _components_
- [ ] Keine Registrierung ist erforderlich, fügen Sie einfach die Komponentendateien in ein App-Verzeichnis ein.
- [x] In einer NgModule-Dekorator-Metadaten-Eigenschaft namens _declarations_

[angular.io](https://angular.io/guide/ngmodule-api#ngmodule-metadata)

#### F31. Was ist der Zweck des `fixture.detectChanges()`-Aufrufs in diesem Unit-Test?

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

- [ ] Es verfolgt alle potenziellen UI-Änderungen und lässt den Unit-Test fehlschlagen, wenn welche vorgenommen werden.
- [ ] Es wird verwendet, um die Stabilität des Komponenten-Templates über mehrere Unit-Tests in der gesamten Test-Suite hinweg zu gewährleisten.
- [x] Es zwingt Angular, Change Detection durchzuführen, was die _UserCardComponent_ rendert, bevor Sie ihr Template validieren können.
- [ ] Es wird verwendet, um Change-Detection-Events während Unit-Test-Läufen in der Konsole zu protokollieren.

[angular.io](https://angular.io/api/core/testing/ComponentFixture#detectChanges)

#### F32. Wie wird das URL-Segment aussehen, basierend auf dem folgenden Aufruf der `Router.navigate`-Methode, wenn goToUser mit dem Wert 15 übergeben wird?

```ts
export class ToolsComponent {
  constructor(private router: Router) {}
  goToUser(id: number) {
    this.router.navigate(['user', id]);
  }
}
```

- [x] /user/15
- [ ] /user?id=15
- [ ] /user:15
- [ ] /user;id=15

[angular.io](https://angular.io/api/router/Router#navigate)

#### F33. Wenn ein Service für root bereitgestellt wird und auch zur Provider-Konfiguration für ein Lazy-Loaded-Modul hinzugefügt wird, welche Instanz dieses Services stellt der Injector Konstruktoren im Lazy-Loaded-Modul bereit?

- [x] Eine neue Instanz dieses Services wird erstellt, wenn das Modul lazy geladen wird.
- [ ] Das Bereitstellen eines Services desselben Typs auf der Ebene eines Lazy-Loaded-Moduls ist nicht erlaubt.
- [ ] Wenn eine Instanz des Services noch nicht auf der Root-Ebene erstellt wurde, wird eine dort erstellt und dann verwendet.
- [ ] Eine einzelne Instanz dieses Services wird immer auf der Root-Ebene instanziiert und ist die einzige, die jemals verwendet wird, einschließlich innerhalb von Lazy-Modulen.

#### F34. Was macht der HostBinding-Dekorator in dieser Direktive?

```ts
@Directive({
  selector: ' [appHighlight] ',
})
export class HighlightDirective {
  @HostBinding('class.highlighted') highlight = true;
}
```

- [x] Er fügt die CSS-Klasse namens highlighted zu jedem DOM-Element hinzu, das die appHighlight-Direktive darauf hat.
- [ ] HostBinding macht nichts bei Direktiven, nur bei Komponenten.
- [ ] Er spezifiziert, dass wenn das Host-Element die highlighted-Klasse zu seinem class-Attribut hinzugefügt bekommt, dann das Direktiven-Klassenfeld highlight auf true gesetzt wird; und wenn es nicht auf dem Host hinzugefügt wird, wird es auf false gesetzt.
- [ ] Er erstellt einen Inline-Stil auf dem Host-Element mit einer CSS-Eigenschaft namens highlight, die auf true gesetzt ist.

[StackOverflow](https://stackoverflow.com/a/46207423)

#### F35. In reaktiven Formularen, welcher Angular-Formularklassentyp wird auf dem nativen DOM-`<form>`-Element verwendet, um es zu verdrahten?

- [ ] `FormArray`
- [ ] `FormControl`
- [x] `FormGroup`
- [ ] `alle diese Antworten`

#### F36. Angenommen, das username-FormControl wurde mit einem minLength-Validator konfiguriert, wie können Sie eine Fehleranzeige im folgenden reaktiven Formular-Markup für das username-Feld einrichten?

```html
<form [formGroup]="form">
  <input type="text" formControlName="username" />
  ...
</form>
```

- [ ] A

  ```html
  <span *ngIf="username.minLength.invalid"> Benutzername-Länge ist nicht gültig </span>
  ```

- [ ] B

  ```html
  <input type="text" formControlName="username" [showMinLength]="true" />
  ```

- [ ] C

  ```html
  <span *ngIf="form.get('username').getError('minLength') as minLengthError">
    Benutzername muss mindestens {{ minLengthError.requiredLength }} Zeichen lang sein.
  </span>
  ```

- [x] D

  ```html
  <input type="text" formControlName="username" #userName="ngModel" />
  <span *ngIf="userName.errors.minlength">
    Benutzername muss mindestens {{ userName.errors.minlength.requiredLength }} Zeichen lang sein.
  </span>
  ```

[Codecraft](https://codecraft.tv/courses/angular/forms/template-driven/)

#### F37. Wie handhabt der emulierte View-Encapsulation-Modus CSS für eine Komponente?

- [ ] Er rendert das CSS genau so, wie Sie es geschrieben haben, ohne Änderungen.
- [ ] Er macht Gebrauch von Shadow-DOM-Markup und CSS.
- [x] Er erstellt eindeutige Attribute für DOM-Elemente und beschränkt die CSS-Selektoren, die Sie schreiben, auf diese Attribut-IDs.
- [ ] Er rendert alle CSS-Regeln, die Sie schreiben, als Inline-CSS auf allen DOM-Elementen, die Sie im Template verwenden.

[Angular.io](https://angular.io/guide/view-encapsulation#inspecting-generated-css)

#### F38. Mit dem folgenden TestBed-Setup, was kann verwendet werden, um auf das gerenderte DOM für die UserCardComponent zuzugreifen?

```ts
TestBed.configureTestingModule({
  declarations: [UserCardComponent],
});
let fixture = TestBed.createComponent(UserCardComponent);
```

- [ ] `fixture.componentTemplate`
- [ ] `fixture.getComponentHtml()`
- [x] `fixture.nativeElement`
- [ ] `fixture.componentInstance.template`

1. [StackOverflow](https://stackoverflow.com/a/56504773)
2. [Angular.io](https://angular.io/guide/testing-components-basics#nativeelement)

#### F39. Gegeben diese beiden Komponenten, was wird basierend auf der Markup-Verwendung in das DOM gerendert?

```ts
@Component({
 selector: 'app-card',
 template: '<h1>Datenkarte</h1><ng-content></ng-content>'
})
export class CardComponent { }

@Component({
 selector: 'app-bio',
 template: '<ng-content></ng-content>.
})
export class BioComponent { }

// Markup-Verwendung:
<app-card><app-bio>Seit vier Jahren dabei.</app-bio></app-card>
```

- [x] A

  ```html
  <app-card>
    <h1>Datenkarte</h1>
    <app-bio> Seit vier Jahren dabei. </app-bio>
  </app-card>
  ```

- [ ] B

  ```html
  <h1>Datenkarte</h1>
  <app-bio>Seit vier Jahren dabei.</app-bio>
  ```

- [ ] C

  ```html
  <app-card>
    <h1>Datenkarte</h1>
    <ng-content></ng-content>
    <app-bio> Seit vier Jahren dabei. <ng-content></ng-content> </app-bio>
  </app-card>
  ```

- [ ] D

  ```html
  <app-card>
    <h1>Datenkarte</h1>
  </app-card>
  ```

#### F40. Gegeben die app-title-card-Komponente im folgenden Code, welches DOM wird die app-user-card-Komponente rendern?

```ts
@Component({
   selector: 'app-user-card',
   template: '<app-title-card></app-title-card><p>Jenny Smith</p>'
})

@Component({
   selector: 'app-title-card',
   template: '<h1>Benutzerdaten</h1>'
})

// Verwendung der User-Card-Komponente im HTML der übergeordneten Komponente
<app-user-card></app-user-card>
```

- [x] A

  ```html
  <app-user-card>
    <app-title-card>
      <h1>Benutzerdaten</h1>
    </app-title-card>
    <p>Jenny Smith</p>
  </app-user-card>
  ```

- [ ] B

  ```html
  <h1>Benutzerdaten</h1>
  <p>Jenny Smith</p>
  <p></p>
  ```

- [ ] C

  ```html
  <app-user-card>
    <app-title-card></app-title-card>
  </app-user-card>
  ```

- [ ] D

  ```html
  <div app-user-card>
    <h1 app-title-card>Benutzerdaten</h1>
    <p>Jenny Smith</p>
  </div>
  ```

#### F41. Wählen Sie den passenden Code für die benutzerdefinierte Provider-Registrierung aus, nach der der @Inject()-Dekorator sucht:

```ts
constructor(@Inject('Logger') private logger) { }
```

- [ ] A

  ```ts
  providers: [Logger];
  ```

- [x] B

  ```ts
  providers: [{ provide: 'Logger', useClass: Logger }];
  ```

- [ ] C

  ```ts
  @Injectable({
      providedln: 'root'
  })
  ```

- [ ] D

  ```ts
  providers: [{ provide: 'Logger' }];
  ```

1. [StackOverflow](https://stackoverflow.com/a/37315355)
2. [TektutorialHub](https://www.tektutorialshub.com/angular/angular-injector-injectable-inject/)
3. [Angular.io - Dependency Injection In Action](https://angular.io/guide/dependency-injection-in-action#supply-a-custom-provider-with-inject)

#### F42. Welche Wahl beschreibt am besten die folgende Verwendung der HttpClient.get-Methode in der getsettings-Klassenmethode?

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

- [ ] Die RxJs-pipe-Methode ist ein Alias für die subscribe-Methode, sodass ein Aufruf von `getSettings` die get-Abfrage ausführt. Der retry-Operator wird verwendet, um dem pipe-Aufruf mitzuteilen, die get-Abfrage dreimal zu wiederholen.
- [ ] Es wird zur Laufzeit einen Fehler erzeugen, da die pipe-Methode nicht vom `Httpclient.get`-Aufruf verfügbar ist.
- [ ] Jeder einzelne Aufruf der getSettings-Methode wird dazu führen, dass der Httpclient insgesamt drei get-Anfragen an die settingsUrl macht, was nicht ideal ist, da es immer zwei zusätzliche Aufrufe geben wird, die nicht benötigt werden. Der retry-Operator sollte nicht auf diese Weise verwendet werden.
- [x] Wenn das Ergebnis der getSettings-Methode abonniert wird, wird der HTTP GET-Aufruf gemacht; wenn er fehlschlägt, wird er bis zu dreimal wiederholt, bevor er aufgibt und einen Fehler zurückgibt.

1. [learnrxjs.io](https://www.learnrxjs.io/learn-rxjs/operators/error_handling/retry)
2. [dev.to](https://dev.to/gparlakov/how-does-rxjs-retry-work-412p)

#### F43. Wenn ein Service eine gewisse Einrichtung benötigt, um seinen Standardzustand durch eine Methode zu initialisieren, wie können Sie sicherstellen, dass diese Methode aufgerufen wird, bevor der Service irgendwo injiziert wird?

- [ ] Legen Sie die Logik dieser Service-Methode stattdessen in den Service-Konstruktor.
- [x] Verwenden Sie einen Factory-Provider auf der Root-AppModule-Ebene, der vom Service abhängt, um diese Service-Methode aufzurufen.
- [ ] Es ist nicht möglich, dies beim Anwendungsstart zu tun; Sie können es nur auf Komponentenebene tun.
- [ ] Instanziieren Sie eine Instanz des Services auf globaler Ebene (Window-Scope) und rufen Sie dann diese Methode auf.

1. [Angular.io](https://angular.io/guide/dependency-injection-providers)
2. [Stackoverflow](https://stackoverflow.com/questions/39803876/how-to-use-factory-provider)

#### F44. Was beschreibt diese Verwendung des TestBed am besten?

```ts
const spy = jasmine.createSpyObj('DataService', ['getUsersFromApi']);
TestBed.configureTestingModule({
  providers: [UserService, { provide: DataService, useValue: spy }],
});
const userService = TestBed.get(UserService);
```

- [ ] Das TestBed ist erforderlich, wenn Sie ein Spy-Objekt in einem Unit-Test für einen Angular-Provider verwenden möchten.
- [ ] Das TestBed wird verwendet, um die Ansicht einer Komponente zu testen.
- [x] Das TestBed erstellt ein NgModule mit zwei Providern und behandelt alle Dependency Injection. Wenn eine Angular-Klasse den DataService in ihrem Konstruktor anfordert, wird das TestBed spy in diesem Konstruktor injizieren.
- [ ] Das TestBed konfiguriert den Test-Runner, um ihm mitzuteilen, dass er nur Tests für die beiden Provider ausführt, die in seinem providers-Array aufgelistet sind.

`Alle anderen Tests werden ignoriert, einschließlich Tests, die Ergebnisse gegen einen dieser Provider und einen nicht definierten Provider bestätigen.`
`Obwohl es funktioniert, wenn mehrere Provider in dieser Konfiguration in einem einzigen Test bestätigt werden.`

#### F45. Was ist der Hauptunterschied zwischen einer Komponente und einer Direktive?

- [ ] Eine Komponente verwendet eine selector-Metadaten-Eigenschaft und eine Direktive nicht.
- [ ] Eine Direktive kann verwendet werden, um benutzerdefinierte Events zum DOM hinzuzufügen, und eine Komponente kann das nicht.
- [x] Eine Komponente hat ein Template und eine Direktive nicht.
- [ ] Eine Direktive kann nur native DOM-Elemente ansprechen.

[StackOverflow](https://stackoverflow.com/a/34616190)

#### F46. Was könnten Sie zu dieser Direktivenklasse hinzufügen, um die Truncate-Länge während der Direktiven-Verwendung im Markup festzulegen?

```ts
@Directive({
    selector: '[appTruncate]'
})
export class TruncateDirective {
    . . .
}

// Beispiel der gewünschten Verwendung:
<p [appTruncate]="10">Sehr langer Text hier</p>
```

- [x] `@Input() appTruncate: number;`
- [ ] `@Output() appTruncate;`
- [ ] `constructor(maxLength: number) { }`
- [ ] `Nichts. Der Direktiven-Selektor kann nicht verwendet werden, um Werte an die Direktive zu übergeben.`

1. [Angular.io](https://angular.io/guide/attribute-directives#passing-values-into-an-attribute-directive)
2. [StackOverflow](https://stackoverflow.com/a/46303049)

#### F47. Wie können Sie Query-Parameter an diese `HttpClient.get`-Anfrage übergeben?

```ts
export class OrderService {
  constructor(private httpClient: HttpClient) {}

  getOrdersByYear(year: number): Observable<Order[]> {
    return this.httpClient.get<Order[]>(this.ordersUrl);
  }
}
```

- [ ] A `return this.httpClient.get<Order[]>(this.ordersUrl, {'year': year})`
- [ ] B `return this.httpClient.get<Order[]>(this.ordersUrl, year)`
- [x] C

  ```ts
  const options = { params: new HttpParams().set('year', year) };
  return this.httpClient.get<Order[]>(this.ordersUrl, options);
  ```

- [ ] D

  ```ts
  getOrdersByYear(year: number): Observable<Order[]> {
      return this.httpClient.addParam('year', year).get<Order[]>(this.ordersUrl, year);
  }
  ```

1. [StackOverflow](https://stackoverflow.com/a/34475594)
2. [TektutorialHub](https://www.tektutorialshub.com/angular/angular-pass-url-parameters-query-strings/#httpparams)

#### F48. Angenommen, der `DataService` wurde in den Providern für die Anwendung registriert, welche Antwort beschreibt am besten, was basierend auf dem Konstruktor dieser Komponente passiert?

```ts
@Component({
    ...
})
export class OrderHistoryComponent {
    constructor(private dataService: DataService) {}
    ...
}
```

- [ ] Es deklariert, dass die `OrderHistoryComponent` ihre eigene Version eines `DataService` haben wird und dass sie niemals existierende Instanzen verwenden sollte. Der `DataService` müsste innerhalb der Klasse als privates Feld instanziiert werden, damit dieser Code vollständig und funktionsfähig ist.
- [x] Wenn Angular eine neue Instanz der `OrderHistoryComponent` erstellt, wird der Injector eine Instanz einer `DataService`-Klasse dem ersten Argument des Komponenten-Konstruktors bereitstellen. Der dataService-Parameter des Konstruktors wird verwendet, um ein privates Instanzfeld mit demselben Namen auf der Instanz zu setzen.
- [ ] Es bietet eine Möglichkeit, nur Komponententests durchzuführen; der Konstruktor hat keine Verwendung im tatsächlichen Betrieb der Angular-Anwendung.
- [ ] Es ermöglicht es dem benutzerdefinierten Element, auf das die Komponente abzielt, eine benutzerdefinierte Eigenschaft namens `dataService` zu haben, die verwendet werden kann, um eine existierende `DataService`-Instanz zu binden.

1. [StackOverflow](https://stackoverflow.com/a/49755822)
2. [Angular.io - Dependency Injection](https://angular.io/guide/dependency-injection)

#### F49. Vervollständigen Sie dieses Markup mit der `ngIf`-Direktive, um einen else-Fall zu implementieren, der den Text "Benutzer ist nicht aktiv" anzeigt:

```html
<div *ngIf="userIsActive; else inactive">Derzeit aktiv!</div>
```

- [ ] A

  ```html
  <div #inactive>Benutzer ist nicht aktiv.</div>
  ```

- [ ] B

  ```html
  <div *ngIf="inactive">Benutzer ist nicht aktiv.</div>
  ```

- [ ] C

  ```html
  <ng-template #else="inactive">
    <div>Benutzer ist nicht aktiv.</div>
  </ng-template>
  ```

- [x] D

  ```html
  <ng-template #inactive>
    <div>Benutzer ist nicht aktiv.</div>
  </ng-template>
  ```

[Angular.io](https://angular.io/api/common/NgIf)

#### F50. Was ist die korrekte Syntax für eine Route-Definition zum Lazy Loading eines Feature-Moduls?

- [ ] A

  ```ts
  {
    path: 'users',
    lazy: './users/users.module#UsersModule'
  }
  ```

- [x] B

  ```ts
  {
    path: 'users',
    loadChildren: () => import('./users/users.module').then(m => m.UserModule)
  }
  ```

- [ ] C

  ```ts
  {
    path: 'users',
    loadChildren: './users/users.module#UsersModule'
  }
  ```

- [ ] D

  ```ts
  {
    path: 'users',
    module: UsersModule
  }
  ```

[Angular.io - Lazy Loading Modules](https://angular.io/guide/lazy-loading-ngmodules)

#### F51. Beschreiben Sie, wie die Validierung in diesem reaktiven Formular-Beispiel eingerichtet und konfiguriert ist:

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

- [ ] Das `FormControl` für `username` wird konfiguriert, um drei Validatoren von den Validatoren auszuschließen, die es verwenden darf.
- [ ] Das `FormControl` für `username` wird konfiguriert, um drei mögliche Validatoren zuzulassen: `required, maxLength` und einen benutzerdefinierten namens `unique`. Um diese `Validatoren` zu aktivieren, müsste eine Validator-Direktive auf die Formularfelder im Markup gesetzt werden.
- [ ] Validierung kann auf diese Weise in reaktiven Formularen nicht eingerichtet werden.
- [x] Das `FormControl` für `username` wird mit drei Validatoren konfiguriert: den `required`- und `minLength`-Validatoren, die von Angular kommen, und einer benutzerdefinierten Validator-Funktion namens `unique`, die prüft, ob der Wert nicht gleich dem String `admin` ist.

1. [Angular.io - Formularvalidierung](https://angular.io/guide/form-validation)
2. [Angular University Blog](https://blog.angular-university.io/angular-custom-validators/)

#### F52. Was macht der Injectable-Dekorator auf dieser Service-Klasse?

```ts
@Injectable({
    providedIn: 'root'
)}
export class DataService { }
```

- [ ] Er registriert einen Provider für den Service, der nur auf der Root-Modul-Ebene verfügbar ist, nicht für untergeordnete Module.
- [x] Er registriert einen Provider für den Service im Root-Anwendungs-Injector, wodurch eine einzelne Instanz davon in der gesamten Anwendung verfügbar gemacht wird.
- [ ] Er macht es so, dass der Service nur in der Bootstrap-Komponente für die Anwendung injiziert werden kann.
- [ ] Er richtet eine Kompilierzeit-Regel ein, die es Ihnen erlaubt, den Service-Typ nur in die providers-Metadaten-Eigenschaft des Root-NgModuls zu setzen.

[Angular.io](https://angular.io/guide/providers#providing-a-service)

#### F53. Beschreiben Sie die Verwendung dieses Codes

```ts
export interface AppSettings {
  title: string;
  version: number;
}
export const APP_SETTINGS = new InjectionToken<AppSettings>('app.settings');
```

- [ ] Das InjectionToken fügt eine Instanz der AppSettings zum Root-Provider über den InjectionToken-Konstruktor-Aufruf hinzu und macht es automatisch für alle NgModules, Services und Komponenten in der gesamten Angular-Anwendung verfügbar, ohne dass es irgendwo injiziert werden muss.
- [x] Das InjectionToken wird verwendet, um ein Provider-Token für eine Nicht-Klassen-Abhängigkeit zu erstellen. Ein Objekt-Literal kann als Wert für den APP_SETTINGS-Dependency-Provider-Typ bereitgestellt werden, der dann in Komponenten, Services usw. injiziert werden kann.
- [ ] Das InjectionToken wird verwendet, um einen dynamischen Dekorator für die AppSettings zu erstellen, der auf Konstruktor-Parametern über einen @AppSettings-Dekorator verwendet werden kann.
- [ ] Dieser Code hat einen Fehler, da Sie kein TypeScript-Interface für den generischen Typ auf dem InjectionToken verwenden können

#### F54. Für das folgende Template-getriebene Formular-Beispiel, welches Argument kann an die submit-Methode im click-Event übergeben werden, um die Daten für das Formular zu übermitteln?

```html
<form #form="ngForm">
  <input type="text" ngModel="firstName" /> <input type="text" ngModel="lastName" />
  <button (click)="submit()">Speichern</button>
</form>
```

- [x] submit(form.value)
- [ ] submit($event)
- [ ] submit(ngForm.value)
- [ ] submit(FirstName, lastName)

#### F55. Was ist der Zweck der `prelodingStrategy`-Eigenschaftskonfiguration in diesem Router-Code?

```ts
RouterModule.forRoot(
  ...{
    preloadingStrategy: PreloadAllModules,
  },
);
```

- [ ] Es aktiviert die Option, einzelne Routen für das Vorladen zu markieren.
- [ ] Es lädt alle Abhängigkeiten für Routen vor und erstellt Instanzen von Services, wenn die App zum ersten Mal startet
- [ ] Es stellt sicher, dass alle Module in eine einzelne App-Modul-Bundle-Datei gebaut werden.
- [x] Es konfiguriert den Router, um sofort alle Routen zu laden, die eine loadChildren-Eigenschaft haben (Routen, die normalerweise bei Bedarf geladen werden)

Referenzen:

- [Angular Router, PreloadAllModules](https://angular.io/api/router/PreloadAllModules)
- [Route-Vorladen in Angular](https://web.dev/route-preloading-in-angular/)
- [Vorladen-Strategie](https://www.tektutorialshub.com/angular/angular-preloading-strategy/)
- [Benutzerdefinierte Vorladen-Strategie](https://www.concretepage.com/angular-2/angular-custom-preloading-strategy#Preloading)
- [Vorladen-Strategie, Ladezeit sparen](https://medium.com/geekculture/preloading-strategy-in-angularsave-loading-time-ca791074fe28)

#### F56. Was ist eine alternative Möglichkeit, dieses Markup zu schreiben, um den Wert des Klassenfelds `userName` an die title-Eigenschaft des h1-Elements zu binden?

```html
<h1 [title]="userName">Aktueller Benutzer ist {{ userName }}</h1>
```

- [ ] `title="userName"`
- [x] `title="{{ userName }}"`
- [ ] `title="{{ 'userName' }}"`
- [ ] Der einzige Weg, dies zu tun, ist die Verwendung der eckigen Klammern.

#### F57. Was macht die `async`-Pipe in diesem Beispiel?

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

- [ ] Sie macht nichts, da die async-Pipe nicht in einer `ngFor`-Anweisung verwendet werden kann.
- [ ] Sie konfiguriert die `ngFor`-Iteration, um mehrere Listen von Benutzern gleichzeitig zu unterstützen.
- [x] Sie abonniert das Observable, das von der `HttpClient.get`-Methode zurückgegeben wird, und entpackt den zurückgegebenen Wert, sodass er in der `ngFor` iteriert werden kann.
- [ ] Sie ermöglicht es, dass alle Benutzer im `users`-Feld gleichzeitig zum DOM gerendert werden.

#### F58. Wie würden Sie diese Direktive im Markup basierend auf ihrem Selektor-Wert verwenden?

```ts
@Directive({  selector: '[appTruncate]'
})
export class TruncateDirective{  . . .
}
```

- [ ] `html <p data-directive="appTruncate">Langer Text </p> `
- [x] `html <p appTruncate>Langer Text</p> `
- [ ] `html <p app-truncate>Langer Text</p> `
- [ ] `html <app-truncate>Langer Text</app-truncate> `

#### F59. Welcher Lifecycle-Hook kann auf einer Komponente verwendet werden, um alle Änderungen an @Input-Werten auf dieser Komponente zu überwachen?

- [ ] ngOnInit
- [ ] ngChanges
- [ ] ngAfterInputChange
- [x] ngOnChanges

[Wie erkennt man, wann sich ein @Input()-Wert in Angular ändert?](https://stackoverflow.com/a/44686085/1573267)

#### F60. Was wäre ein Beispiel für die Template-Syntax-Verwendung dieser benutzerdefinierten Pipe?

```ts
@Pipe({ name: 'truncate' })
export class TruncatePipe implements PipeTransform {
  transform(value: string, maxLength: number, showEllipsis: boolean) {
    const newValue = maxLength ? value.substr(0, maxLength) : value;
    return showEllipsis ? '${newValue}...' : newValue;
  }
}
```

- [ ] `{{ 'langer Text' | truncate:10 }}`
- [x] `{{ 'langer Text' | truncate: 10, true }}`
- [ ] `{{ 'langer Text' | truncate }}`
- [ ] alle diese Antworten

[Wie rufe ich eine Angular 2 Pipe mit mehreren Argumenten auf?](https://stackoverflow.com/questions/36816788/how-do-i-call-an-angular-2-pipe-with-multiple-arguments)

#### F61. Welchen Angular CLI-Befehl würden Sie ausführen, um eine UsersComponent zu generieren und sie zum SharedModule hinzuzufügen (in der Datei shared.module.ts in Ihrer Anwendung)?

- [ ] ng generate component --newModule=shared
- [x] ng generate component users --module=shared
- [ ] ng generate component users --shared
- [ ] ng generate component --add=shared

#### F62. Wie können Sie dieses Markup umschreiben, sodass der div-Container im finalen DOM-Rendering nicht benötigt wird?

```html
<div *ngIf="location">
  <h1>{{ location.name }}</h1>
  <p>{{ location.description }}</p>
</div>
```

- [ ] A

  ```html
  <div *ngIf="location">
    <h1>{{ location.name }}</h1>
    <p>{{ location.description }}</p>
    {{ endNgIf }}
  </div>
  ```

- [ ] B

  ```html
  <ng-template *ngIf="location">
    <h1>{{ location.name }}</h1>
    <p>{{ location.description }}</p>
  </ng-template>
  ```

- [ ] C

  ```html
  <div *ngIf="location" [display]=" ' hidden' ">
    <h1>{{ location.name }}</h1>
    <p>{{ location.description }}</p>
  </div>
  ```

- [x] D

  ```html
  <ng-container *ngIf="location">
    <h1>{{ location.name }}</h1>
    <p>{{ location.description }}</p>
  </ng-container>
  ```

#### F63. Wie können Sie die Template-Syntax verwenden, um ein Komponenten-Klassenfeld namens tabWidth an eine Inline-Style-CSS-Eigenschaft width auf diesem Element zu binden?

<div class="tab"></div>

- [ ] <code>{% raw %}{{ width: tabWidth }}{% endraw %}</code>
- [ ] [width]="tabWidth"
- [ ] [inline.width]="tabWidth"
- [x] [style.width.px]="tabWidth"

#### F64. Welche Angular-Utilities, falls vorhanden, sind erforderlich, um einen Service ohne Konstruktor-Abhängigkeiten per Unit-Test zu testen?

- [ ] Die By.css()-Hilfsmethode wird benötigt
- [ ] Eine Text-Fixture ist erforderlich, um den Service für den Unit-Test auszuführen.
- [ ] Keine. Ein Service kann instanziiert und eigenständig per Unit-Test getestet werden.
- [x] Die TestBed-Klasse wird benötigt, um den Service zu instanziieren.

[Angular Unit-Tests](https://angular.io/guide/testing-services) - Antworten erneut prüfen

#### F65. Was ist der Unterschied zwischen den CanActivate- und den CanLoad-Route-Guards?

- [ ] CanActivate wird verwendet, um den Zugriff zu überprüfen. CanLoad wird verwendet, um Daten für die Route vorzuladen.
- [ ] CanLoad wird beim App-Start verwendet, um das Hinzufügen von Routen zur Route-Tabelle zu erlauben oder zu verweigern. CanActivate wird verwendet, um den Zugriff auf Routen zum Zeitpunkt ihrer Anforderung zu verwalten.
- [ ] CanActivate und CanLoad machen genau dasselbe.
- [x] CanLoad verhindert, dass ein gesamtes NgModule ausgeliefert und geladen wird. CanActivate stoppt das Routing zu einer Komponente in diesem NgModule, aber dieses Modul wird trotzdem geladen.

[CanActivate vs Canload](https://stackoverflow.com/questions/42026045/difference-between-angulars-canload-and-canactivate#:~:text=canActivate%20is%20used%20to%20prevent,not%20authorized%20to%20do%20so.) CanActivate verhindert den Zugriff auf Routen, CanLoad verhindert Lazy Loading.

#### F66. Wofür wird die outlet-Eigenschaft in diesem Router-Definitionsobjekt verwendet?

```ts
{  path: 'document',  component: DocumentComponent,  outlet: 'document-box'
}
```

- [ ] Es findet alle Instanzen von `<document-box>` im DOM und fügt bei der Routen-Navigation ein DocumentComponent-Element in sie ein.
- [ ] Es deklariert, dass die DocumentComponent zusätzlich zum Routing als Kind eines `<document-box>`-Elements verwendet werden kann.
- [x] Es wird verwendet, um ein `<router-outlet>`-Element mit dem name-Attribut, das mit dem String-Wert übereinstimmt, als Ort für das Rendern der DocumentComponent beim Routing anzusprechen.
- [ ] Es ist eine Stromquelle für den Router. (definitiv nicht die Antwort :P)

[Angular-outlet](https://angular.io/api/router/RouterOutlet) - Antwort erneut prüfen

#### F67. In dieser Template-Syntax führt die ngFor-Strukturdirektive jedes Mal, wenn die items-Eigenschaft geändert wird (hinzugefügt, entfernt usw.), ihre Logik für alle DOM-Elemente in der Schleife erneut aus. Welche Syntax kann verwendet werden, um dies performanter zu machen?

```html
<div *ngFor="let item of items">{{ item.id }} - {{ item.name }}</div>
```

- [ ] `*ngFor="let item of items; let uniqueItem"`
- [ ] `*ngFor="let item of items.distinct()"`
- [ ] `*ngFor="let item of items: let i = index"`
- [x] `*ngFor="let item of items; trackBy: trackById"`

[StackOverflow - Wie man `trackBy` mit `ngFor` verwendet](https://stackoverflow.com/a/58025894)

#### F68. Was macht dieser Angular CLI-Befehl?

```bash
ng build --configuration=production --progress=false
```

- [ ] Er baut die Angular-Anwendung, setzt die Build-Konfiguration auf das "production"-Ziel, das in der angular.json-Datei angegeben ist, und protokolliert die Fortschrittsausgabe in der Konsole.
- [ ] Er baut die Angular-Anwendung, setzt die Build-Konfiguration auf das "production"-Ziel, das in der angular.json-Datei angegeben ist, und überwacht Dateien auf Änderungen.
- [ ] Er baut die Angular-Anwendung, setzt die Build-Konfiguration auf das "production"-Ziel, das in der angular.json-Datei angegeben ist, und deaktiviert das Überwachen von Dateien auf Änderungen.
- [x] Er baut die Angular-Anwendung, setzt die Build-Konfiguration auf das "production"-Ziel, das in der angular.json-Datei angegeben ist, und verhindert die Fortschrittsausgabe in der Konsole.

[Angular-Dokumentation - `ng build`](https://angular.io/cli/build#:~:text=%2D%2D-,progress,-Log%20progress%20to)

#### F69. Service-Klassen können als Provider über welche Dekoratoren registriert werden?

- [ ] @Injectable, @NgModule, @Component und @Directive.
- [x] Nur @Injectable.
- [ ] Nur @Injectable und @NgModule.
- [ ] Nur @Service und @NgModule.

#### F70. Wofür wird der Input-Dekorator in dieser Komponentenklasse verwendet?

```ts
@Component({  selector:'app-product-name',  ...
})
export class ProductNameComponent {  @Input() productName: string
}
```

- [ ] Er wird einfach verwendet, um einen Kommentar vor ein Klassenfeld zur Dokumentation zu setzen.
- [x] Er bietet eine Möglichkeit, Werte an das productName-Feld zu binden, indem der Komponenten-Selektor verwendet wird.
- [ ] Er generiert automatisch ein `html
<input type='text' id='productName'>` DOM-Element im Komponenten-Template.
- [ ] Er bietet eine Möglichkeit, Werte an das productName-Instanzfeld zu binden, genau wie native DOM-Element-Property-Bindings.
      [Angular-Dokumentation - `Input()`](https://angular.io/guide/inputs-outputs)

#### F71. Welcher Route-Guard kann verwendet werden, um die Navigation zu einer Route zu vermitteln?

- [x] alle diese Antworten.
- [ ] CanDeactivate.
- [ ] CanLoad
- [ ] CanActivate.
      [Angular-Dokumentation - `Input()`](https://angular.io/guide/inputs-outputs)

#### F72. Wie können Sie den Injector konfigurieren, um ein vorhandenes Objekt für ein Token zu verwenden, anstatt eine Klasseninstanz zu instanziieren?

- [x] Verwenden Sie die `useValue`-Provider-Konfiguration und setzen Sie diese gleich einem vorhandenen Objekt oder einem Objekt-Literal.
- [ ] Es ist nicht möglich. Provider können nur mit Klassentypen konfiguriert werden.
- [ ] Fügen Sie einfach die Objektinstanz oder das Literal zum Provider-Array hinzu.
- [ ] Nutzen Sie die `asValue`-Provider-Konfigurationseigenschaft und setzen Sie sie auf true.

[Konfiguration von Dependency-Providern](https://angular.io/guide/dependency-injection-providers)

#### F73. Basierend auf dieser Route-Definition, was kann in den UserDetailComponent-Konstruktor injiziert werden, um den id-Route-Parameter zu erhalten?

```ts
{path: 'user/:id', component: UserDetailComponent }
```

- [x] ActivatedRoute
- [ ] CurrentRoute
- [ ] UrlPath
- [ ] @Inject('id')

[Häufige Routing-Aufgaben](https://angular.io/guide/router#observable-parammap-and-component-reuse)

#### F74. Mit dem folgenden reaktiven Formular-Markup, was würden Sie hinzufügen, um einen Aufruf an eine onSubmit-Klassenmethode zu verdrahten?

```html
<form [formGroup]="form">
  <input type="text" formControlName="username" />
  <button type="submit" [disabled]="form. invalid">Absenden</button>
</form>
```

- [ ] keine dieser Antworten
- [ ] Fügen Sie (click)="onSubmit()" zum `<button>`-Element hinzu.
- [x] Fügen Sie (ngSubmit )="onSubmit ()" zum `<form>`-Element hinzu.
- [ ] beide dieser Antworten

[Angular - Formulare](https://angular.io/guide/forms)

#### F75. Was ist der erwartete DOM-Code für diese Verwendung des ngClass-Attribut-Direktivs, wenn isActive true ist?

```html
<div [ngClass]="{ 'active-item': isActive }">Element Eins</div>
```

- [ ] `<div active-item>Element Eins</div>`
- [x] `<div class="active-item">Element Eins</div>`
- [ ] `<div class="is-active">Element Eins</div>`
- [ ] `<div class="active-item isActive">Element Eins</div>`

[Angular - NgClass](https://angular.io/api/common/NgClass)

#### F76. Welche Antwort erklärt am besten die Verwendung von ngModel in diesem Template-Code?

```html
<input [(ngModel)]="user.name" />
```

- [ ] Es zeigt das Eingabeelement bedingt an, wenn die user.name-Eigenschaft einen Wert hat.
- [x] Es ist die bidirektionale Datenbindungs-Syntax. Die value-Eigenschaft des Eingabeelements wird an die user.name-Eigenschaft gebunden, und das Wertänderungs-Event für das Formularelement aktualisiert den user.name-Eigenschaftswert.
- [ ] Es gibt einen Tippfehler im Code. Es sollte nur die eckigen Klammern haben.
- [ ] Es bindet den Wert der user.name-Eigenschaft an die val-Eigenschaft des Eingabeelements, um seinen Anfangswert zu setzen.

[Angular - NgModel](https://angular.io/api/forms/NgModel)

#### F77. NgModules können innerhalb anderer NgModules enthalten sein. Welches Code-Beispiel sollten Sie verwenden, um TableModule in SharedModule einzuschließen?

- [ ] @NgModule({
      exports: [TableModule]
      })
      export class SharedModule {}

text

- [x] @NgModule({
      imports: [TableModule]
      })
      export class SharedModule {}

text

- [ ] @NgModule({
      declarations: [TableModule]
      })
      export class SharedModule {}

text

- [ ] @NgModule({
      providers: [TableModule]
      })
      export class SharedModule {}

#### F78. Welche andere Template-Syntax (die die ngClass-Direktive ersetzt) kann verwendet werden, um die CSS-Klassennamen in diesem Markup hinzuzufügen oder zu entfernen?

```html
<span [ngClass]="{ 'active': isActive, 'can-toggle': canToggle }"> Beschäftigt </span>
```

- [ ] A

  ```html
  <span class="{{ isActive ? 'is-active' : '' }} {{ canToggle ? 'can-toggle' : '' }}">
    Beschäftigt
  </span>
  ```

- [x] B

  ```html
  <span [class.active]="isActive" [class.can-toggle]="canToggle"> Beschäftigt </span>
  ```

- [ ] C

  ```html
  <span [styles.class.active]="isActive" [styles.class.can-toggle]="canToggle"> Beschäftigt </span>
  ```

- [ ] D

  ```html
  <span [css.class.active]="isActive" [css.class.can-toggle]="canToggle"> Beschäftigt </span>
  ```

#### F79. In diesem Direktiven-Dekorator-Beispiel, was ist der Zweck der multi-Eigenschaft im Provider-Objekt-Literal?

```ts
@Directive({
  selector: '[customValidator]',
  providers: [
    {
      provide: NG_VALIDATORS,
      useExisting: CustomValidatorDirective,
      multi: true,
    },
  ],
})
export class CustomValidatorDirective implements Validator {}
```

- [ ] Es zeigt an, dass die CustomValidatorDirective auf mehreren Formularelement-Typen verwendet werden kann.
- [ ] Es erlaubt die Instanziierung mehrerer Instanzen der CustomValidatorDirective. Ohne multi wäre die CustomValidatorDirective ein Singleton für die gesamte App.
- [x] Es erlaubt die Registrierung verschiedener Provider für das einzelne NG_VALIDATORS-Token. In diesem Fall wird die CustomValidatorDirective zur Liste der verfügbaren Formular-Validatoren hinzugefügt.
- [ ] Es zeigt an, dass es mehrere Klassen geben wird, die die Logik-Implementierung für den benutzerdefinierten Validator handhaben.

[StackOverflow](https://stackoverflow.com/questions/38144641/what-is-multi-provider-in-angular2)

#### F80. Welchen Angular CLI-Befehl würden Sie verwenden, um Ihre Unit-Tests in einem Prozess auszuführen, der Ihre Test-Suite bei Dateiänderungen erneut ausführt?

- [ ] ng test --single-run=false
- [ ] ng test --watch-files
- [ ] ng test --progress
- [x] ng test

#### F81. Was ist die häufigste Verwendung für den ngOnDestory-Lifecycle-Hook?

- [ ] Entfernen von DOM-Elementen aus der Ansicht der Komponente
- [ ] Löschen von injizierten Services
- [x] Abmelden von Observables und Trennen
- [ ] Alle oben genannten

#### F82. Welche NgModule-Dekorator-Metadaten-Eigenschaft wird genutzt, um anderen zu erlauben...?

- [ ] public
- [ ] experts
- [ ] Shared
- [x] declarations

#### F83. Mit der folgenden Komponentenklasse, welche Template-Syntax würden Sie im Template verwenden, um das Ergebnis des Aufrufs der currentYear-Klassenfunktion anzuzeigen?

```ts
@Component({
  selector: 'app-date-card',
  template: '',
})
export class DateCardComponent {
  currentYear() {
    return new Date().getFullYear();
  }
}
```

- [x] `{% raw %}{{ currentYear() }}{% endraw %}`
- [ ] `{% raw %}{{ component.currentYear() }}{% endraw %}`
- [ ] `{% raw %}{{ currentYear }}{% endraw %}`
- [ ] Klassenfunktionen können nicht aus der Template-Syntax aufgerufen werden.
