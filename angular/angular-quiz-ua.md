# Angular

#### П1. Яке призначення декоратора ViewChild в цьому класі компонента?

```ts
@Component({
    ...
    template: '<p #bio></p>'
})
export class UserDetailsComponent {
    @ViewChild('bio') bio;
}
```

- [x] Він надає доступ з класу компонента до об'єкта ElementRef для тегу `<p>`, який має змінну шаблону bio в поданні шаблону компонента.
- [ ] Він вказує, що тег `<p>` рендериться як дочірній елемент батьківського подання, яке використовує цей компонент.
- [ ] Він робить тег `<p>` у шаблоні підтримуючим проекцію вмісту.
- [ ] Він робить тег `<p>` видимим у фінальному рендері. Якщо #bio був використаний у шаблоні, а @ViewChild не був використаний у класі, тоді Angular автоматично приховає тег `<p>`, який має #bio.

[DigitalOcean - viewchild-access-component](https://www.digitalocean.com/community/tutorials/angular-viewchild-access-component)

#### П2. Який метод використовується для підключення FormControl до нативного DOM елемента input у реактивних формах?

- [ ] Додати строкове ім'я, надане FormControl, до атрибута з назвою controls на елементі `<form>`, щоб вказати, які поля він повинен включати.
- [ ] Використовувати синтаксис прив'язки квадратних дужок навколо атрибута value на DOM елементі та встановити його рівним екземпляру FormControl.
- [x] Використовувати директиву formControlName та встановити значення рівним строковому імені, наданому FormControl.
- [ ] Використовувати строкове ім'я, надане FormControl, як значення для атрибута id DOM елемента.

[Angular.io - Reactive Form Groups](https://angular.io/guide/reactive-forms#creating-nested-form-groups)

#### П3. Яка різниця між `paramMap` та `queryParamMap` у класі `ActivatedRoute`?

- [ ] paramMap - це об'єктний літерал параметрів у шляху URL маршруту. queryParamMap - це Observable тих самих параметрів.
- [ ] paramMap - це Observable, який містить значення параметрів, що є частиною шляху URL маршруту. queryParamMap - це метод, який приймає масив ключів і використовується для пошуку конкретних параметрів у paramMap.
- [ ] paramMap - це застаріла назва з Angular 3. Нова назва - queryParamMap.
- [x] Обидва є Observables, що містять значення з рядка URL запитуваного маршруту. paramMap містить значення параметрів, які знаходяться в шляху URL, а queryParamMap містить параметри запиту URL.

[StackOverflow](https://stackoverflow.com/a/49617621)

#### П4. На основі наступного використання async pipe, і припускаючи, що поле класу users є Observable, скільки підписок на Observable users створюється?

```html
<h2>Імена</h2>
<div *ngFor="let user of users | async">{{ user.name }}</div>
<h2>Вік</h2>
<div *ngFor="let user of users | async">{{ user.age }}</div>
<h2>Стать</h2>
<div *ngFor="let user of users | async">{{ user.gender }}</div>
```

- [ ] Жодної. async pipe не підписується автоматично.
- [ ] Жодної. Синтаксис шаблону неправильний.
- [x] Три. По одній для кожного async pipe.
- [ ] Одна. async pipe кешує Observables за типом внутрішньо.

[UltimateCourses](https://ultimatecourses.com/blog/angular-ngfor-async-pipe)

#### П5. Як ви можете використовувати HttpClient для надсилання POST запиту до endpoint з функції addOrder у цьому OrderService?

```ts
export class OrderService {
  constructor(private httpClient: HttpClient) {}

  addOrder(order: Order) {
    // Відсутній рядок
  }
}
```

- [ ] `this.httpClient.url(this.orderUrl).post(order);`
- [ ] `this.httpClient.send(this.orderUrl, order);`
- [ ] `this.httpClient.post<Order>(this.orderUrl, order);`
- [x] `this.httpClient.post<Order>(this.orderUrl, order).subscribe();`

[Angular.io - Sending data to server](https://angular.io/guide/http#sending-data-to-a-server)

#### П6. Для чого використовується метод RouterModule.forRoot?

- [ ] Для реєстрації будь-яких провайдерів, які ви маєте намір використовувати в маршрутизованих компонентах.
- [x] Для реєстрації визначень маршрутів на кореневому рівні додатку.
- [ ] Для вказівки, що Angular повинен підтримувати ваші маршрути для успішності.
- [ ] Для оголошення, що ви маєте намір використовувати маршрутизацію тільки на кореневому рівні.

[O'REILLY](https://www.oreilly.com/library/view/switching-to-angular/9781788620703/c9e90774-0e10-410b-bd20-d3e9e0b8d117.xhtml)

#### П7. Які DOM елементи будуть відповідати цьому селектору метаданих компонента?

```ts
@Component({
    selector: 'app-user-card',
    . . .
})
```

- [ ] Будь-який елемент з атрибутом app-user-card, наприклад `<div app-user-card></div>`.
- [ ] Перший екземпляр `<app-user-card></app-user-card>`.
- [x] Всі екземпляри `<app-user-card></app-user-card>`.
- [ ] Всі екземпляри `<user-card></user-card>`.

[Angular.io - Component Metadata](https://angular.io/guide/architecture-components#component-metadata)

#### П8. Який правильний синтаксис шаблону для використання вбудованої структурної директиви ngFor для рендерингу списку productNames?

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

[Angular.io- Structural Directives](https://angular.io/guide/built-in-directives#listing-items-with-ngfor)

#### П9. Які дві властивості метаданих декоратора компонента використовуються для налаштування CSS стилів для компонента?

- [ ] viewEncapsulation та viewEncapsulationFiles.
- [ ] Є тільки одна, і це властивість з назвою css.
- [ ] css та cssUrl.
- [x] styles та styleUrls.

[Angular.io - Component Styles](https://angular.io/guide/component-styles)

#### П10. З наступним класом компонента, який синтаксис шаблону ви б використали в шаблоні для відображення значення поля класу title?

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
- [ ] Поле класу не може бути відображене в шаблоні через синтаксис шаблону.

[Angular.io - String Interpolation or Text Interpolation](https://angular.io/guide/interpolation)

#### П11. Яке призначення методу valueChanges на FormControl?

- [ ] Він використовується для налаштування того, які значення дозволені для контролю.
- [ ] Він використовується для зміни значення контролю на нове значення. Ви б викликали цей метод і передавали нове значення для поля форми. Він навіть підтримує передачу масиву значень, які можна встановити з часом.
- [ ] Він повертає Boolean на основі того, чи відрізняється значення контролю від значення, з яким він був ініціалізований.
- [x] Це observable, який випромінює кожного разу, коли значення контролю змінюється, тож ви можете реагувати на нові значення та приймати логічні рішення в цей момент.

[Angular.io - Displaying a from control value](https://angular.io/guide/reactive-forms#displaying-a-form-control-value)

#### П12. Яка директива використовується для прив'язки тегу `<a>` до маршрутизації?

- [ ] routeTo
- [x] routerLink
- [ ] routePath
- [ ] appLink

[Angular.io - RouterLink](https://angular.io/api/router/RouterLink#description)

#### П13. Для чого використовується декоратор Output у цьому класі компонента?

```ts
@Component({
    selector: 'app-shopping-cart',
    . . .
})
export class ShoppingCartComponent {
    @Output() itemTotalChanged = new EventEmitter();
}
```

- [ ] Він робить поле класу `itemTotalChanged` публічним.
- [ ] Він надає спосіб прив'язати значення до поля класу `itemTotalChanged`, наприклад: `<app-shopping-cart [itemTotalChanged]="newTotal"></app-shopping-cart>`.
- [x] Він надає спосіб прив'язати події до поля класу `itemTotalChanged`, наприклад: `<app-shopping-cart (itemTotalChanged)="logNewTotal($event)"></app-shopping-cart>`.
- [ ] Це просто спосіб розмістити коментар перед полем класу для документації.

[Angular.io - Sending data to parent component](https://angular.io/guide/inputs-outputs#sending-data-to-a-parent-component)

#### П14. Яка різниця між цими двома прикладами розмітки для умовної обробки відображення?

```html
<div *ngIf="isVisible">Активний</div>
<div [hidden]="!isVisible">Активний</div>
```

- [ ] `ngIf` є скороченням для іншого прикладу. Коли Angular обробляє цю директиву, він записує елемент div у DOM з властивістю hidden.
- [ ] Вони фундаментально однакові.
- [x] Директива `ngIf` не рендерить div у DOM, якщо вираз є false. Використання властивості `hidden` приховує вміст div у вікні браузера, але div все ще залишається в DOM.
- [ ] `ngIf` є правильним, але використання властивості `hidden` є неправильним і викличе помилку.

[StackOverflow](https://stackoverflow.com/a/39778145)

#### П15. Як ви можете вимкнути кнопку submit, коли форма має помилки в цьому прикладі шаблонних форм?

```html
<form #userForm="ngForm">
  <input type="text" ngModel name="firstName" required />
  <input type="text" ngModel name="lastName" required />
  <button (click)="submit(userForm.value)">Зберегти</button>
</form>
```

- [ ] A

  ```html
  <button (click)="submit(userForm.value)" disable="userForm.invalid">Зберегти</button>
  ```

- [x] B

  ```html
  <button (click)="submit(userForm.value)" [disabled]="userForm.invalid">Зберегти</button>
  ```

- [ ] C

  ```html
  <button (click)="submit(userForm.value)" [ngForm.disabled]="userForm.valid">Зберегти</button>
  ```

- [ ] D

  ```html
  <button (click)="submit(userForm.value)" *ngIf="userForm.valid">Зберегти</button>
  ```

[Angular.io - Submit the form with ngSubmit](https://angular.io/guide/forms#submit-the-form-with-ngsubmit)

#### П16. Ви хочете побачити, які файли будуть створені під час створення нового компонента contact-card. Яку команду ви б використали?

- [x] ng generate component contact-card --dry-run
- [ ] ng generate component contact-card --no-files
- [ ] ng generate component component --dry
- [ ] ng generate component --exclude

[Angular.io - ng generate options](https://angular.io/cli/generate#options)

#### П17. На основі наступного компонента, який синтаксис шаблону ви б використали для прив'язки поля titleText компонента TitleCardComponent до властивості title елемента h1?

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

#### П18. Що таке хуки життєвого циклу Angular?

- [ ] логери для відстеження стану додатку Angular
- [ ] провайдери, які можуть використовуватися для відстеження екземплярів компонентів
- [ ] вбудовані pipe, які можна використовувати в шаблонах для подій DOM
- [x] зарезервовані іменовані методи для компонентів і директив, які Angular буде викликати в певний час під час виконання, і які можна використовувати для доступу до цих моментів життєвого циклу

[Angular.io - Lifecycle hooks](https://angular.io/guide/lifecycle-hooks)

#### П19. Виберіть найкращий опис для цього коду синтаксису шаблону:

```html
<span>Керівник: {{job?.bossName}} </span>
```

- [ ] ? є скороченням для async pipe. Значення job має бути Observable.
- [x] Він використовує оператор безпечної навігації (?) для поля job. Якщо поле job є undefined, доступ до bossName буде проігноровано і помилка не виникне.
- [ ] У синтаксисі шаблону є помилка. ? тут недійсний.
- [ ] Він відображає значення job, якщо воно є; в іншому випадку він відображає bossName.

[StackOverflow](https://stackoverflow.com/a/60182134)

#### П20. Як би ви налаштували визначення маршруту для UserDetailComponent, який підтримує шлях URL user/23 (де 23 представляє id запитуваного користувача)?

- [x] `{ path: 'user/:id', component: UserDetailComponent }`
- [ ] `{ url: 'user/:id', routedComponent: UserDetailComponent }`
- [ ] `{ routedPath: 'user/:id', component: UserDetailComponent }`
- [ ] `{ destination: new UserDetailComponent(), route: 'user/:id' }`

[CodeCraft - Parameterised Routes](https://codecraft.tv/courses/angular/routing/parameterised-routes/#_configuration)

#### П21. Що роблять декоратори HostListener і декоратор HostBinding у цій директиві?

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

- [x] Вони встановлюють поле CalloutDirective.fontWeight на основі того, чи знаходиться миша над DOM елементом. HostListener потім встановлює CSS властивість font-weight на значення fontWeight.
- [ ] Вони налаштовують директиву для перевірки DOM елемента, на якому вона знаходиться. Якщо він має прив'язки подій, додані для входу та виходу миші, буде використовуватися цей код. В іншому випадку нічого не відбудеться.
- [ ] Це неправильне використання HostListener та HostBinding. Декоратори HostListener і HostBinding нічого не роблять на директивах; вони працюють лише при використанні на компонентах.
- [ ] Якщо DOM елемент, на якому розміщена ця директива, має встановлену CSS властивість font-weight, події mouseenter та mouseleave будуть генеруватися.

[DigitalOcean](https://www.digitalocean.com/community/tutorials/angular-hostbinding-hostlistener)

#### П22. Який синтаксис шаблону Angular ви можете використовувати в цьому полі шаблонної форми для доступу до значення поля та перевірки валідації в розмітці шаблону?

```html
<input type="text" ngModel name="firstName" required minlength="4" />
<span *ngIf="">Невірні дані поля</span>
```

- [x] Ви можете використовувати змінну посилання на шаблон і функцію exportAs, яку має директива ngModel.
- [ ] Ви можете використовувати директиву ngModel в комбінації з ім'ям поля input.
- [ ] Ви можете використовувати змінну посилання на шаблон для HTML елемента input, а потім перевірити властивість valid з неї.
- [ ] Неможливо отримати доступ до значення поля з шаблонними формами. Для цього ви повинні використовувати реактивні форми.

1. [Angular.io -Show and hide validation error ](https://angular.io/guide/forms#show-and-hide-validation-error-messages)
2. [Medium](https://medium.com/@agoiabeladeyemi/template-driven-forms-in-angular-4a3a5ad960de)

#### П23. Який тип значення буде збережено в змінній посилання на шаблон headerText у цій розмітці?

```html
<h1 #headerText>Список користувачів</h1>
```

- [x] Angular ElementRef, обгортка навколо нативного елемента
- [ ] внутрішній текст елемента `<h1>`
- [ ] клас компонента заголовка
- [ ] нативний тип DOM елемента HTMLHeadingElement

[Pluralsight - Template reference variable](https://www.pluralsight.com/guides/how-to-use-template-reference-variables-in-angular)

#### П24. Яка різниця, якщо вона є, у результуючій логіці коду на основі цих двох конфігурацій провайдера?

```ts
[{ provide: FormattedLogger, useClass: Logger }][{ provide: FormattedLogger, useExisting: Logger }];
```

- [ ] Вони однакові. Обидва призведуть до нового екземпляра Logger, який прив'язаний до токена FormattedLogger.
- [x] Синтаксис useClass вказує інжектору створити новий екземпляр Logger і прив'язати цей екземпляр до токена FormattedLogger. Синтаксис useExisting посилається на вже існуючий екземпляр об'єкта, оголошений як Logger.
- [ ] Обидва неправильні. Строгий тип не може бути використаний для useClass або useExisting.
- [ ] Вони однакові. Обидва призведуть до того, що токен FormattedLogger буде псевдонімом екземпляра Logger.

1. [Angular.io - Dependency Providers](https://angular.io/guide/dependency-injection-providers#defining-providers)
2. [TektutorialHub](https://www.tektutorialshub.com/angular/angular-providers/)

#### П25. Яке призначення властивості data (яка видна в прикладі нижче) в конфігурації маршруту?

```ts
   {
       path: 'customers',
       component: CustomerListComponent,
       data: { accountSection: true }
   }
```

- [ ] відображення ключ/значення для встановлення значень @Input на екземплярі маршрутизованого компонента
- [x] спосіб включити статичні, тільки для читання дані, пов'язані з маршрутом, які можна отримати з ActivatedRoute
- [ ] властивість маршруту, яку можна використовувати для завантаження динамічних даних для маршруту
- [ ] об'єкт, який буде автоматично впроваджено в конструктор маршрутизованого компонента

1. [TektutorialsHub](https://www.tektutorialshub.com/angular/angular-pass-data-to-route/#:~:text=Angular%20allows%20us%20to%20pass,of%20the%20history%20state%20object)
2. [StackOverflow](https://stackoverflow.com/a/36835156)

#### П26. Як вбудована структурна директива `ngIf` змінює відрендерений DOM на основі цього синтаксису шаблону?

```ts
@Component({
  selector: 'app-product',
  template: '<div *ngIf="product">{{ product.name }}</div>',
})
export class ProductComponent {
  @Input() product;
}
```

- [ ] `<div>` діє як заповнювач. Якщо поле класу product є "truthy", `<div>` буде замінено лише значенням `product.name`; якщо ні, то нічого не буде відрендерено.
- [ ] `<div>` завжди буде відрендерено, і якщо поле product є "truthy", елемент `<div>` міститиме значення `product.name`; в іншому випадку він відрендерить елемент `<div>` без значення в ньому.
- [ ] Він створює помилку, оскільки ngIf не є вбудованою структурною директивою.
- [x] Якщо поле класу product є "truthy", то відрендерений DOM включатиме `<div>` зі значенням поля `product.name`. Якщо воно не є "truthy", відрендерений DOM не міститиме елемент `<div>`.

[Reference (angular.io)](https://angular.io/api/common/NgIf)

#### П27. Що робить цей код?

```ts
@NgModule({
  declarations: [AppComponent],
  imports: [BrowserModule],
  bootstrap: [AppComponent],
})
export class AppModule {}

platformBrowserDynamic().bootstrapModule(AppModule);
```

- [ ] Він виконує модульний тест для NgModule.
- [ ] Він надає спосіб кодувати структуру документа додатку Angular. @NgModule - це форма вбудованого коментування коду, яка ігнорується компілятором TypeScript, але відображатиметься зі спеціальним форматуванням у додатках редакторів коду.
- [ ] Він оголошує модуль Angular з назвою AppModule і робить його доступним для ледачого завантаження в усьому додатку.
- [x] Він оголошує модуль Angular з назвою AppModule, який містить завантажувальний компонент з назвою AppComponent. Потім він реєструє цей модуль в Angular, щоб додаток міг запуститися.

[Angular.io - The basic NgModule](https://angular.io/guide/ngmodules#the-basic-ngmodule)

#### П28. Який варіант найкраще описує, що робить властивість _resolve_ в цій конфігурації маршруту?

```ts
{
   path: ':id',
   component: UserComponent,
   resolve: {
     user: UserResolverService
   }
}
```

- [x] Перед завантаженням _UserComponent_, маршрутизатор підпишеться на _Observable_, що повертається методом _resolve_ у _UserResolverService_. Ця техніка може бути використана для отримання попередньо завантажених даних для _маршруту_.
- [ ] Після того, як _маршрут_ завершить розв'язання, і компонент завантажено та відрендерено, _UserResolverService_ матиме метод з назвою _user_, який виконається для очищення будь-яких відкритих з'єднань даних.
- [ ] Є помилка. Правильна назва властивості - _onResolve_.
- [ ] _UserComponent_ матиме параметр у своєму конструкторі для _user_, і _маршрутизатор_ обробить впровадження значення для цього з виклику методу _user_ у _UserResolverService_.

[angular.io](https://angular.io/api/router/Resolve)

#### П29. Яке призначення декоратора ContentChildren у цьому класі компонента?

```ts
@Component({
 . . .
 template: '<ng-content></ng-content>'
})
export class TabsListComponent {
 @ContentChildren(TabComponent) tabs;
}
```

- [ ] Якщо будь-які елементи _TabsComponent_ додано до шаблону _TabsListComponent_, вони будуть поміщені в елемент `<ng-content>` під час виконання.
- [ ] Він створює компоненти _TabComponent_ у шаблоні _TabsListComponent_, коли створюється екземпляр _TabsListComponent_.
- [x] Він надає доступ з класу компонента до будь-яких компонентів _TabComponent_, які були спроектовані вмістом у `<ng-content>` для цього компонента.
- [ ] Він обмежує дозволені елементи, які можна помістити в елемент _TabsListComponent_, дозволяючи лише елементи _TabComponent_.

[betterprogramming.pub](https://betterprogramming.pub/understanding-contentchildren-with-an-example-e76ce78968db)

#### П30. Щоб Angular міг обробляти компоненти в додатку, де потрібно зареєструвати типи компонентів?

- [ ] всередині тегу script в файлі index.html
- [ ] в тегу метаданих декоратора NgModule з назвою _components_
- [ ] Реєстрація не потрібна, просто включіть файли компонентів у каталог додатку.
- [x] у властивості метаданих декоратора NgModule з назвою _declarations_

[angular.io](https://angular.io/guide/ngmodule-api#ngmodule-metadata)

#### П31. Яке призначення виклику `fixture.detectChanges()` у цьому модульному тесті?

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

- [ ] Він відстежує будь-які потенційні зміни UI і провалить модульний тест, якщо вони будуть внесені.
- [ ] Він використовується для забезпечення стабільності шаблону компонента у кількох модульних тестах у всьому тестовому наборі.
- [x] Він змушує Angular виконати виявлення змін, що відрендерить _UserCardComponent_ перед тим, як ви зможете перевірити його шаблон.
- [ ] Він використовується для логування подій виявлення змін у консоль під час виконання модульних тестів.

[angular.io](https://angular.io/api/core/testing/ComponentFixture#detectChanges)

#### П32. Як буде виглядати сегмент URL на основі наступного виклику методу `Router.navigate`, коли goToUser передається значення 15?

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

#### П33. Коли сервіс надається для root і також додається до конфігурації провайдерів для ледачо завантаженого модуля, який екземпляр цього сервісу інжектор надає конструкторам у ледачо завантаженому модулі?

- [x] Створюється новий екземпляр цього сервісу, коли модуль завантажується ледачо.
- [ ] Надання сервісу того самого типу на рівні ледачо завантаженого модуля не дозволено.
- [ ] Якщо екземпляр сервісу ще не був створений на кореневому рівні, він створить його там, а потім використає.
- [ ] Один екземпляр цього сервісу завжди створюється на root і є єдиним, який коли-небудь використовується, включаючи ледачі модулі.

#### П34. Що робить декоратор HostBinding у цій директиві?

```ts
@Directive({
  selector: ' [appHighlight] ',
})
export class HighlightDirective {
  @HostBinding('class.highlighted') highlight = true;
}
```

- [x] Він додає CSS клас з назвою highlighted до будь-якого DOM елемента, який має директиву appHighlight.
- [ ] HostBinding нічого не робить на директивах, лише на компонентах.
- [ ] Він вказує, що якщо хост-елемент отримає клас highlighted, доданий до його атрибута class, тоді поле класу директиви highlight буде встановлено в true; і якщо воно не буде додано на хості, воно буде встановлено в false.
- [ ] Він створює вбудований стиль на хост-елементі з CSS властивістю highlight, встановленою в true.

[StackOverflow](https://stackoverflow.com/a/46207423)

#### П35. У реактивних формах, який тип класу форми Angular використовується на нативному DOM елементі `<form>` для його підключення?

- [ ] `FormArray`
- [ ] `FormControl`
- [x] `FormGroup`
- [ ] `всі ці відповіді`

#### П36. Припускаючи, що FormControl username був налаштований з валідатором minLength, як ви можете налаштувати відображення помилки в наступній розмітці реактивних форм для поля username?

```html
<form [formGroup]="form">
  <input type="text" formControlName="username" />
  ...
</form>
```

- [ ] A

  ```html
  <span *ngIf="username.minLength.invalid"> Довжина імені користувача недійсна </span>
  ```

- [ ] B

  ```html
  <input type="text" formControlName="username" [showMinLength]="true" />
  ```

- [ ] C

  ```html
  <span *ngIf="form.get('username').getError('minLength') as minLengthError">
    Ім'я користувача повинно містити принаймні {{ minLengthError.requiredLength }} символів.
  </span>
  ```

- [x] D

  ```html
  <input type="text" formControlName="username" #userName="ngModel" />
  <span *ngIf="userName.errors.minlength">
    Ім'я користувача повинно містити принаймні {{ userName.errors.minlength.requiredLength }}
    символів.
  </span>
  ```

[Codecraft](https://codecraft.tv/courses/angular/forms/template-driven/)

#### П37. Як емульований режим інкапсуляції view обробляє CSS для компонента?

- [ ] Він рендерить CSS точно так, як ви його написали, без будь-яких змін.
- [ ] Він використовує розмітку та CSS shadow DOM.
- [x] Він створює унікальні атрибути для DOM елементів і обмежує CSS селектори, які ви пишете, до цих ID атрибутів.
- [ ] Він рендерить всі CSS правила, які ви пишете, як вбудований CSS на всіх DOM елементах, які ви використовуєте в шаблоні.

[Angular.io](https://angular.io/guide/view-encapsulation#inspecting-generated-css)

#### П38. З наступним налаштуванням TestBed, що можна використовувати для доступу до відрендереного DOM для UserCardComponent?

```ts
TestBed.configureTestingModule({
  declarations: [UserCardComponent],
});
let fixture = TestBed.createComponent(UserCardComponent);
```

- [ ] `fixture.componentTemplate`
- [ ] `fixture.getComponentHtml()`
- [x] `fixture.nativeElement`
- [ ] `fixture.componentInstance.template `

1. [StackOverflow](https://stackoverflow.com/a/56504773)
2. [Angular.io](https://angular.io/guide/testing-components-basics#nativeelement)

#### П39. Враховуючи ці два компоненти, що буде відрендерено в DOM на основі використання розмітки?

```ts
@Component({
 selector: 'app-card',
 template: '<h1>Карта даних</h1><ng-content></ng-content>'
})
export class CardComponent { }

@Component({
 selector: 'app-bio',
 template: '<ng-content></ng-content>.
})
export class BioComponent { }

// використання розмітки:
<app-card><app-bio>Існує вже чотири роки.</app-bio></app-card>
```

- [x] A

  ```html
  <app-card>
    <h1>Карта даних</h1>
    <app-bio> Існує вже чотири роки. </app-bio>
  </app-card>
  ```

- [ ] B

  ```html
  <h1>Карта даних</h1>
  <app-bio> Існує вже чотири роки. </app-bio>
  ```

- [ ] C

  ```html
  <app-card>
    <h1>Карта даних</h1>
    <ng-content></ng-content>
    <app-bio>
      Існує вже чотири роки.
      <ng-content></ng-content>
    </app-bio>
  </app-card>
  ```

- [ ] D

  ```html
  <app-card>
    <h1>Карта даних</h1>
  </app-card>
  ```

#### П40. Враховуючи компонент app-title-card у коді нижче, який DOM буде рендерити компонент app-user-card?

```ts
@Component({
   selector: 'app-user-card',
   template: '<app-title-card></app-title-card><p>Дженні Сміт</p>'
})

@Component({
   selector: 'app-title-card',
   template: '<h1>Дані користувача</h1>'
})

// використання компонента user card в HTML батьківського компонента
<app-user-card></app-user-card>
```

- [x] A

  ```html
  <app-user-card>
    <app-title-card>
      <h1>Дані користувача</h1>
    </app-title-card>
    <p>Дженні Сміт</p>
  </app-user-card>
  ```

- [ ] B

  ```html
  <h1>Дані користувача</h1>
  <p>Дженні Сміт</p>
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
    <h1 app-title-card>Дані користувача</h1>
    <p>Дженні Сміт</p>
  </div>
  ```

#### П41. Виберіть відповідний код для реєстрації користувацького провайдера, який шукає декоратор @Inject():

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

#### П42. Який варіант найкраще описує наступне використання методу HttpClient.get у методі класу getsettings?

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

- [ ] Метод pipe RxJs є псевдонимом для методу subscribe, тому виклик `getSettings` виконає запит get. Оператор retry використовується, щоб вказати виклику pipe повторити запит get тричі.
- [ ] Він призведе до помилки під час виконання, оскільки метод pipe недоступний після виклику `Httpclient.get`.
- [ ] Кожен окремий виклик методу getSettings призведе до того, що Httpclient зробить три загальні запити get до settingsUrl, що не ідеально, оскільки завжди будуть два додаткові виклики, які не потрібні. Оператор retry не слід використовувати таким чином.
- [x] Коли результат методу getSettings буде підписано, буде зроблено HTTP GET запит; якщо він не вдасться, він буде повторено до трьох разів, перш ніж він здасться і поверне помилку.

1. [learnrxjs.io](https://www.learnrxjs.io/learn-rxjs/operators/error_handling/retry)
2. [dev.to](https://dev.to/gparlakov/how-does-rxjs-retry-work-412p)

#### П43. Коли сервіс вимагає деякого налаштування для ініціалізації його стану за замовчуванням через метод, як ви можете переконатися, що цей метод викликається перед тим, як сервіс впроваджується будь-куди?

- [ ] Помістити логіку цього методу сервісу в конструктор сервісу натомість.
- [x] Використовувати фабричний провайдер на кореневому рівні AppModule, який залежить від сервісу для виклику цього методу сервісу.
- [ ] Неможливо зробити це на старті додатку; ви можете зробити це лише на рівні компонента.
- [ ] Створити екземпляр сервісу на глобальному рівні (область видимості window), а потім викликати цей метод.

1. [Angular.io](https://angular.io/guide/dependency-injection-providers)
2. [Stackoverflow](https://stackoverflow.com/questions/39803876/how-to-use-factory-provider)

#### П44. Яке твердження найкраще описує це використання TestBed?

```ts
const spy = jasmine.createSpyObj('DataService', ['getUsersFromApi']);
TestBed.configureTestingModule({
  providers: [UserService, { provide: DataService, useValue: spy }],
});
const userService = TestBed.get(UserService);
```

- [ ] TestBed потрібен щоразу, коли ви хочете використовувати об'єкт spy у модульному тесті для провайдера Angular.
- [ ] TestBed використовується для тестування подання компонента.
- [x] TestBed створює NgModule з двома провайдерами і обробляє будь-яке впровадження залежностей. Якщо будь-який клас Angular запитує DataService у своєму конструкторі, TestBed впровадить spy у цей конструктор.
- [ ] TestBed налаштовує test runner, щоб вказати йому виконувати тести лише для двох провайдерів, перелічених у його масиві провайдерів.

#### П45. Яка основна різниця між компонентом і директивою?

- [ ] Компонент використовує властивість метаданих selector, а директива ні.
- [ ] Директива може використовуватися для додавання користувацьких подій до DOM, а компонент не може.
- [x] Компонент має шаблон, а директива ні.
- [ ] Директива може націлюватися лише на нативні DOM елементи.

[StackOverflow](https://stackoverflow.com/a/34616190)

#### П46. Що ви можете додати до цього класу директиви, щоб дозволити встановлення довжини обрізання під час використання директиви в розмітці?

```ts
@Directive({
    selector: '[appTruncate]'
})
export class TruncateDirective {
    . . .
}

// приклад бажаного використання:
<p [appTruncate]="10">Якийсь дуже довгий текст тут</p>
```

- [x] `@Input() appTruncate: number;`
- [ ] `@Output() appTruncate;`
- [ ] `constructor(maxLength: number) { }`
- [ ] `Нічого. Селектор директиви не може використовуватися для передачі значень у директиву.`

1. [Angular.io](https://angular.io/guide/attribute-directives#passing-values-into-an-attribute-directive)
2. [StackOverflow](https://stackoverflow.com/a/46303049)

#### П47. Як ви можете передати параметри запиту до цього запиту `HttpClient.get`?

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

#### П48. Припускаючи, що `DataService` був зареєстрований у провайдерах для додатку, яка відповідь найкраще описує, що відбувається на основі конструктора цього компонента?

```ts
@Component({
    ...
})
export class OrderHistoryComponent {
    constructor(private dataService: DataService) {}
    ...
}
```

- [ ] Він оголошує, що `OrderHistoryComponent` матиме свою власну версію `DataService` і що він ніколи не повинен використовувати будь-які існуючі екземпляри. `DataService` потрібно було б створити всередині класу як приватне поле, щоб цей код був повним і працюючим.
- [x] Коли Angular створює новий екземпляр `OrderHistoryComponent`, інжектор надасть екземпляр класу `DataService` першому аргументу конструктора компонента. Параметр `dataService` конструктора буде використано для встановлення приватного поля екземпляра з тією ж назвою на екземплярі.
- [ ] Він надає спосіб виконувати тестування компонента тільки; конструктор не має використання в фактичному запуску додатку Angular.
- [ ] Він дозволяє користувацькому елементу, на який націлюється компонент, мати користувацьку властивість з назвою `dataService`, яку можна використовувати для прив'язки існуючого екземпляра `DataService`.

1. [StackOverflow](https://stackoverflow.com/a/49755822)
2. [Angular.io - Dependency Injection](https://angular.io/guide/dependency-injection)

#### П49. Завершіть цю розмітку, використовуючи директиву `ngIf` для реалізації випадку else, який відобразить текст "Користувач неактивний":

```html
<div *ngIf="userIsActive; else inactive">Наразі активний!</div>
```

- [ ] A

  ```html
  <div #inactive>Користувач неактивний.</div>
  ```

- [ ] B

  ```html
  <div *ngIf="inactive">Користувач неактивний.</div>
  ```

- [ ] C

  ```html
  <ng-template #else="inactive">
    <div>Користувач неактивний.</div>
  </ng-template>
  ```

- [x] D

  ```html
  <ng-template #inactive>
    <div>Користувач неактивний.</div>
  </ng-template>
  ```

[Angular.io](https://angular.io/api/common/NgIf)

#### П50. Який правильний синтаксис для визначення маршруту для ледачого завантаження функціонального модуля?

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

#### П51. Опишіть, як налаштована та конфігурована валідація в цьому прикладі реактивних форм:

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

- [ ] `FormControl` для `username` налаштовується на виключення трьох валідаторів з валідаторів, які йому дозволено використовувати.
- [ ] `FormControl` для `username` налаштовується на дозвіл використання трьох можливих валідаторів: `required, maxLength` та користувацького з назвою `unique`. Щоб увімкнути ці `валідатори`, директиву валідатора потрібно було б помістити на поля форми в розмітці.
- [ ] Валідацію не можна налаштувати таким чином у реактивних формах.
- [x] `FormControl` для `username` налаштовується з трьома валідаторами: валідаторами `required` і `minLength`, які надходять від Angular, та користувацькою функцією валідатора з назвою `unique`, яка перевіряє, що значення не дорівнює рядку `admin`.

1. [Angular.io - Form Validation](https://angular.io/guide/form-validation)
2. [Angular University Blog](https://blog.angular-university.io/angular-custom-validators/)

#### П52. Що робить декоратор Injectable у цьому класі сервісу?

```ts
@Injectable({
    providedIn: 'root'
)}
export class DataService { }
```

- [ ] Він реєструє провайдер для сервісу, який доступний лише на рівні кореневого модуля, а не для будь-яких дочірніх модулів.
- [x] Він реєструє провайдер для сервісу в кореневому інжекторі додатку, роблячи один екземпляр доступним у всьому додатку.
- [ ] Він робить так, що сервіс може бути впроваджений лише в завантажувальному компоненті для додатку.
- [ ] Він налаштовує правило часу компіляції, яке дозволяє вам помістити тип сервісу лише у властивість метаданих провайдерів кореневого NgModule.

[Angular.io](https://angular.io/guide/providers#providing-a-service)

#### П53. Опишіть використання цього коду

```ts
export interface AppSettings {
  title: string;
  version: number;
}
export const APP_SETTINGS = new InjectionToken<AppSettings>('app.settings');
```

- [ ] InjectionToken додає екземпляр AppSettings до кореневого провайдера через виклик конструктора InjectionToken, роблячи його автоматично доступним для всіх NgModules, сервісів та компонентів у всьому додатку Angular без необхідності впроваджувати його будь-куди.
- [x] InjectionToken використовується для створення токена провайдера для залежності, яка не є класом. Об'єктний літерал може бути наданий як значення для типу провайдера залежності APP_SETTINGS, яке потім може бути впроваджено в компоненти, сервіси тощо.
- [ ] InjectionToken використовується для створення динамічного декоратора для AppSettings, який може використовуватися на параметрах конструктора через декоратор @AppSettings.
- [ ] Цей код має помилку, оскільки ви не можете використовувати інтерфейс TypeScript для загального типу на InjectionToken

#### П54. Для наступного прикладу шаблонних форм, який аргумент можна передати методу submit у події click для надсилання даних форми?

```html
<form #form="ngForm">
  <input type="text" ngModel="firstName" /> <input type="text" ngModel="lastName" />
  <button (click)="submit()">Зберегти</button>
</form>
```

- [x] submit(form.value)
- [ ] submit($event)
- [ ] submit(ngForm.value)
- [ ] submit(FirstName, lastName)

#### П55. Яке призначення властивості конфігурації `prelodingStrategy` у цьому коді маршрутизатора?

```ts
RouterModule.forRoot(
  ...{
    preloadingStrategy: PreloadAllModules,
  },
);
```

- [ ] Він дозволяє опцію позначити окремі маршрути для попереднього завантаження.
- [ ] Він попередньо завантажує всі залежності для маршрутів, створюючи екземпляри сервісів під час першого запуску додатку
- [ ] Він гарантує, що всі модулі будуть побудовані в один файл пакету модуля додатку.
- [x] Він налаштовує маршрутизатор на негайне завантаження всіх маршрутів, які мають властивість loadChildren (маршрути, які зазвичай завантажуються при запиті)

Посилання:

- [Angular Router, PreloadAllModules](https://angular.io/api/router/PreloadAllModules)
- [Route preloading in Angular](https://web.dev/route-preloading-in-angular/)
- [Preloading strategy](https://www.tektutorialshub.com/angular/angular-preloading-strategy/)
- [Custom preloading strategy](https://www.concretepage.com/angular-2/angular-custom-preloading-strategy#Preloading)
- [Preloading strategy, save loading time](https://medium.com/geekculture/preloading-strategy-in-angularsave-loading-time-ca791074fe28)

#### П56. Який альтернативний спосіб написати цю розмітку для прив'язки значення поля класу `userName` до властивості title елемента `h1`?

```html
<h1 [title]="userName">Поточний користувач: {{ userName }}</h1>
```

- [ ] `title="userName"`
- [x] `title="{{ userName }}"`
- [ ] `title="{{ 'userName' }}"`
- [ ] Єдиний спосіб зробити це - використовувати квадратні дужки.

#### П57. Що робить `async` pipe у цьому прикладі?

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

- [ ] Він нічого не робить, оскільки async pipe не може використовуватися в операторі `ngFor`.
- [ ] Він налаштовує ітерацію `ngFor` для підтримки кількох списків користувачів одночасно.
- [x] Він підписується на observable, повернутий з методу `HttpClient.get`, і розгортає повернене значення, щоб його можна було ітерувати в `ngFor`.
- [ ] Він дозволяє всім користувачам у полі `users` бути відрендереними одночасно в DOM.

#### П58. Як би ви використали цю директиву в розмітці на основі її значення селектора

```ts
@Directive({  selector: '[appTruncate]'
})
export class TruncateDirective{  . . .
}
```

- [ ] `html <p data-directive="appTruncate">Якийсь довгий текст </p> `
- [x] `html <p appTruncate>Якийсь довгий текст</p> `
- [ ] `html <p app-truncate>Якийсь довгий текст</p> `
- [ ] `html <app-truncate>Якийсь довгий текст</app-truncate> `

#### П59. Який хук життєвого циклу можна використовувати на компоненті для моніторингу всіх змін значень @Input на цьому компоненті?

- [ ] ngOnInit
- [ ] ngChanges
- [ ] ngAfterInputChange
- [x] ngOnChanges

[How to detect when an @Input() value changes in Angular?](https://stackoverflow.com/a/44686085/1573267)

#### П60. Який би був приклад використання синтаксису шаблону цього користувацького pipe?

```ts
@Pipe({ name: 'truncate' })
export class TruncatePipe implements PipeTransform {
  transform(value: string, maxLength: number, showEllipsis: boolean) {
    const newValue = maxLength ? value.substr(0, maxLength) : value;
    return showEllipsis ? '${newValue}...' : newValue;
  }
}
```

- [ ] `{{ 'якийсь довгий текст' | truncate:10 }}`
- [x] `{{ 'якийсь довгий текст' | truncate: 10, true }}`
- [ ] `{{ 'якийсь довгий текст' | truncate }}`
- [ ] всі ці відповіді

[How do I call an Angular 2 pipe with multiple arguments?](https://stackoverflow.com/questions/36816788/how-do-i-call-an-angular-2-pipe-with-multiple-arguments)

#### П61. Яку команду Angular CLI ви б запустили, щоб згенерувати UsersComponent і додати його до SharedModule (у файлі shared.module.ts у вашому додатку)?

- [ ] ng generate component --newModule=shared
- [x] ng generate component users --module=shared
- [ ] ng generate component users --shared
- [ ] ng generate component --add=shared

#### П62. Як ви можете переписати цю розмітку, щоб контейнер div не був потрібен у фінальному рендері DOM

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

#### П63. Як ви можете використовувати синтаксис шаблону для прив'язки поля класу компонента з назвою tabWidth до вбудованого стилю CSS властивості width на цьому елементі?

```html
<div class="tab"></div>
```

- [ ] `{{ width: tabWidth }}`
- [ ] `[width]="tabWidth"`
- [ ] `[inline.width]="tabWidth"`
- [x] `[style.width.px]="tabWidth"`

#### П64. Які утиліти Angular, якщо такі є, потрібні для модульного тестування сервісу без залежностей конструктора?

- [ ] Потрібен допоміжний метод By.css()
- [ ] Для запуску сервісу для модульного тесту потрібна текстова фікстура.
- [ ] Жодної. Сервіс може бути створений і протестований самостійно.
- [x] Клас TestBed потрібен для створення екземпляра сервісу.

[Angular unit tests](https://angular.io/guide/testing-services)

#### П65. Яка різниця між охоронцями маршруту CanActivate і CanLoad?

- [ ] CanActivate використовується для перевірки доступу. CanLoad використовується для попереднього завантаження даних для маршруту.
- [ ] CanLoad використовується на старті додатку, щоб дозволити або заборонити додавання маршрутів до таблиці маршрутів. CanActivate використовується для управління доступом до маршрутів у момент їх запиту.
- [ ] CanActivate і CanLoad роблять абсолютно одне й те саме.
- [x] CanLoad запобігає завантаженню цілого NgModule. CanActivate зупиняє маршрутизацію до компонента в цьому NgModule, але цей модуль все ще завантажується.

[CanActivate vs Canload](https://stackoverflow.com/questions/42026045/difference-between-angulars-canload-and-canactivate)

#### П66. Для чого використовується властивість outlet в цьому об'єкті визначення маршрутизатора?

```ts
{  path: 'document',  component: DocumentComponent,  outlet: 'document-box'
}
```

- [ ] він знайде всі екземпляри `<document-box>` у DOM і вставить елемент DocumentComponent в них при навігації маршруту.
- [ ] Він оголошує, що DocumentComponent може використовуватися як дочірній елемент до `<document-box>` на додаток до маршрутизації.
- [x] Він використовується для націлювання на елемент `<router-outlet>` з атрибутом name, що відповідає строковому значенню, як місце для рендерингу DocumentComponent при маршрутизації.
- [ ] Це джерело живлення для маршрутизатора.

[Angular-outlet](https://angular.io/api/router/RouterOutlet)

#### П67. У цьому синтаксисі шаблону, кожного разу, коли властивість items змінюється (додається, видаляється тощо), структурна директива ngFor повторно запускає свою логіку для всіх DOM елементів у циклі. Який синтаксис можна використовувати, щоб зробити це більш продуктивним?

```html
<div *ngFor="let item of items">{{ item.id }} - {{ item.name }}</div>
```

- [ ] `*ngFor="let item of items; let uniqueItem"`
- [ ] `*ngFor="let item of items.distinct()"`
- [ ] `*ngFor="let item of items: let i = index"`
- [x] `*ngFor="let item of items; trackBy: trackById"`

[StackOverflow - How to use `trackBy` with `ngFor`](https://stackoverflow.com/a/58025894)

#### П68. Що робить ця команда Angular CLI?

```bash
ng build --configuration=production --progress=false
```

- [ ] Вона збирає додаток Angular, встановлюючи конфігурацію збірки на ціль "production", вказану в файлі angular.json, і логує вивід прогресу в консоль.
- [ ] Вона збирає додаток Angular, встановлюючи конфігурацію збірки на ціль "production", вказану в файлі angular.json, і спостерігає за змінами файлів.
- [ ] Вона збирає додаток Angular, встановлюючи конфігурацію збірки на ціль "production", вказану в файлі angular.json, і вимикає спостереження за змінами файлів.
- [x] Вона збирає додаток Angular, встановлюючи конфігурацію збірки на ціль "production", вказану в файлі angular.json, і запобігає виводу прогресу в консоль.

[Angular documentation - `ng build`](https://angular.io/cli/build)

#### П69. Класи сервісів можуть бути зареєстровані як провайдери через які декоратори?

- [ ] @Injectable, @NgModule, @Component, і @Directive.
- [x] Лише @Injectable.
- [ ] Лише @Injectable і @NgModule.
- [ ] Лише @Service і @NgModule.

#### П70. Для чого використовується декоратор Input у цьому класі компонента?

```ts
@Component({  selector:'app-product-name',  ...
})
export class ProductNameComponent {  @Input() productName: string
}
```

- [ ] Він використовується просто для того, щоб помістити коментар перед полем класу для документації.
- [x] Він надає спосіб прив'язати значення до поля productName, використовуючи селектор компонента.
- [ ] Він автоматично генерує DOM елемент `<input type='text' id='productName'>` у шаблоні компонента.
- [ ] Він надає спосіб прив'язати значення до поля екземпляра productName, як і прив'язки властивостей нативних DOM елементів.

[Angular documentation - `Input()`](https://angular.io/guide/inputs-outputs)

#### П71. Який охоронець маршруту можна використовувати для посередництва в навігації до маршруту?

- [x] всі ці відповіді.
- [ ] CanDeactivate.
- [ ] CanLoad
- [ ] CanActivate.

#### П72. Як ви можете налаштувати інжектор для використання існуючого об'єкта для токена замість того, щоб він створював екземпляр класу?

- [x] Використовувати конфігурацію провайдера `useValue` і встановити її рівною існуючому об'єкту або об'єктному літералу.
- [ ] Це неможливо. Провайдери можуть бути налаштовані лише з типами класів.
- [ ] Просто додати екземпляр об'єкта або літерал до масиву провайдера.
- [ ] Використовувати властивість конфігурації провайдера `asValue`, встановивши її в true.

[Configuring dependency providers](https://angular.io/guide/dependency-injection-providers)

#### П73. На основі цього визначення маршруту, що можна впровадити в конструктор UserDetailComponent, щоб отримати параметр маршруту id?

```ts
{path: 'user/:id', component: UserDetailComponent }
```

- [x] ActivatedRoute
- [ ] CurrentRoute
- [ ] UrlPath
- [ ] @Inject('id')

[Common Routing Tasks](https://angular.io/guide/router#observable-parammap-and-component-reuse)

#### П74. З наступною розміткою реактивної форми, що б ви додали, щоб підключити виклик методу класу onSubmit?

```html
<form [formGroup]="form">
  <input type="text" formControlName="username" />
  <button type="submit" [disabled]="form.invalid">Надіслати</button>
</form>
```

- [ ] жодна з цих відповідей
- [ ] Додати (click)="onSubmit()" до елемента `<button>`.
- [x] Додати (ngSubmit)="onSubmit()" до елемента `<form>`.
- [ ] обидві ці відповіді

[Angular - Forms](https://angular.io/guide/forms)

#### П75. Який очікуваний код DOM для цього використання атрибутної директиви ngClass, коли isActive має значення true?

```html
<div [ngClass]="{ 'active-item': isActive }">Елемент один</div>
```

- [ ] `<div active-item>Елемент один</div>`
- [x] `<div class="active-item">Елемент один</div>`
- [ ] `<div class="is-active">Елемент один</div>`
- [ ] `<div class="active-item isActive">Елемент один</div>`

[Angular - NgClass](https://angular.io/api/common/NgClass)

#### П76. Яке найпоширеніше використання для хука життєвого циклу ngOnDestroy?

- [ ] Видалити DOM елементи з подання компонента
- [ ] Видалити будь-які впроваджені сервіси
- [x] Відписатися від observables і від'єднати обробники подій
- [ ] Всі вищезазначені

#### П77. Яка властивість метаданих декоратора NgModule використовується, щоб дозволити іншим модулям використовувати компоненти та директиви?

- [ ] public
- [x] exports
- [ ] shared
- [ ] declarations

#### П78. Яка відповідь найкраще пояснює використання ngModel в цьому коді шаблону?

```html
<input [(ngModel)]="user.name" />
```

- [ ] Він умовно відображає елемент input, якщо властивість user.name має значення.
- [x] Це синтаксис двостороннього зв'язування даних. Властивість value елемента input буде прив'язана до властивості user.name, а подія зміни значення для елемента форми оновить значення властивості user.name.
- [ ] У коді є помилка. Він повинен мати лише квадратні дужки.
- [ ] Він прив'язує значення властивості user.name до властивості val елемента input, щоб встановити його початкове значення.

[Angular - NgModel](https://angular.io/api/forms/NgModel)

#### П79. NgModules можуть бути включені в інші NgModules. Який зразок коду ви повинні використовувати, щоб включити TableModule у SharedModule?

- [ ] A

  ```ts
  @NgModule({
    exports: [TableModule],
  })
  export class SharedModule {}
  ```

- [x] B

  ```ts
  @NgModule({
    imports: [TableModule],
  })
  export class SharedModule {}
  ```

- [ ] C

  ```ts
  @NgModule({
    declarations: [TableModule],
  })
  export class SharedModule {}
  ```

- [ ] D

  ```ts
  @NgModule({
    providers: [TableModule],
  })
  export class SharedModule {}
  ```

#### П80. Яка різниця між охоронцями маршруту CanActivate і CanLoad?

- [ ] CanActivate використовується для перевірки доступу. CanLoad використовується для попереднього завантаження даних для маршруту.
- [ ] CanLoad використовується на старті додатку, щоб дозволити або заборонити додавання маршрутів до таблиці маршрутів. CanActivate використовується для управління доступом до маршрутів у момент їх запиту.
- [ ] CanActivate і CanLoad роблять абсолютно одне й те саме.
- [x] CanLoad запобігає завантаженню цілого NgModule. CanActivate зупиняє маршрутизацію до компонента в цьому NgModule, але цей модуль все ще завантажується.

[CanActivate vs Canload](https://stackoverflow.com/questions/42026045/difference-between-angulars-canload-and-canactivate)

#### П81. Яке призначення властивості outlet в цьому об'єкті визначення маршрутизатора?

```ts
{  path: 'document',  component: DocumentComponent,  outlet: 'document-box'
}
```

- [ ] він знайде всі екземпляри `<document-box>` у DOM і вставить елемент DocumentComponent в них при навігації маршруту.
- [ ] Він оголошує, що DocumentComponent може використовуватися як дочірній елемент до `<document-box>` на додаток до маршрутизації.
- [x] Він використовується для націлювання на елемент `<router-outlet>` з атрибутом name, що відповідає строковому значенню, як місце для рендерингу DocumentComponent при маршрутизації.
- [ ] Це джерело живлення для маршрутизатора.

[Angular-outlet](https://angular.io/api/router/RouterOutlet)

#### П82. Як ви можете налаштувати інжектор для використання існуючого об'єкта для токена замість того, щоб він створював екземпляр класу?

- [x] Використовувати конфігурацію провайдера `useValue` і встановити її рівною існуючому об'єкту або об'єктному літералу.
- [ ] Це неможливо. Провайдери можуть бути налаштовані лише з типами класів.
- [ ] Просто додати екземпляр об'єкта або літерал до масиву провайдера.
- [ ] Використовувати властивість конфігурації провайдера `asValue`, встановивши її в true.

[Configuring dependency providers](https://angular.io/guide/dependency-injection-providers)

#### П83. На основі цього визначення маршруту, що можна впровадити в конструктор UserDetailComponent, щоб отримати параметр маршруту id?

```ts
{path: 'user/:id', component: UserDetailComponent }
```

- [x] ActivatedRoute
- [ ] CurrentRoute
- [ ] UrlPath
- [ ] @Inject('id')

[Common Routing Tasks](https://angular.io/guide/router#observable-parammap-and-component-reuse)

#### П84. З наступною розміткою реактивної форми, як ви можете прив'язати значення поля класу userName до поля вводу, щоб мати можливість редагувати його?

```html
<form [formGroup]="form">
  <input type="text" formControlName="userName" />
</form>
```

- [ ] Додати [(ngModel)]="userName" до поля вводу.
- [x] Нічого. Це вже правильно налаштовано для редагування.
- [ ] Додати (input)="userName = $event.target.value" до поля вводу.
- [ ] Додати [value]="userName" до поля вводу.

#### П85. Яка різниця між параметрами маршруту та параметрами запиту в Angular?

- [ ] Параметри маршруту є обов'язковими, а параметри запиту - ні.
- [ ] Параметри маршруту - це частина URL, яка визначає конкретний ресурс, тоді як параметри запиту - це додаткова інформація, що передається у вигляді пари ключ-значення.
- [x] Параметри маршруту визначаються в конфігурації маршруту, тоді як параметри запиту можуть бути будь-якими даними, які ви хочете передати маршруту.
- [ ] Параметри маршруту завжди є рядковими, тоді як параметри запиту можуть бути будь-якого типу.

[Angular - Routing & Navigation](https://angular.io/guide/router)

#### П86. Як ви можете реалізувати власну стратегію попереднього завантаження для маршрутизатора Angular?

- [ ] Використовувати вбудовану стратегію PreloadAllModules і налаштувати її в RouterModule.
- [x] Створити клас, який реалізує інтерфейс PreloadingStrategy, і зареєструвати його в RouterModule.
- [ ] Додати властивість preloadingStrategy до конфігурації маршруту.
- [ ] Це неможливо. Angular не дозволяє користувацькі стратегії попереднього завантаження.

#### П87. Яка команда Angular CLI створює новий сервіс з ім'ям data і автоматично реєструє його в кореневому модулі?

- [ ] ng generate service data --module=app
- [x] ng generate service data
- [ ] ng g service data --root
- [ ] ng s data --module=app

#### П88. Яка різниця між ViewChild і ContentChild?

- [ ] Немає різниці. Це синоніми.
- [x] ViewChild використовується для отримання доступу до елементів, що належать до шаблону компонента, тоді як ContentChild - для отримання доступу до елементів, що проектуються в компонент через ng-content.
- [ ] ContentChild є застарілим, і всі його функції були інтегровані в ViewChild.
- [ ] ViewChild використовується для отримання доступу до статичних елементів шаблону, а ContentChild - до динамічних.

[Angular - Component Interaction](https://angular.io/guide/component-interaction)

#### П89. Як ви можете заборонити користувачеві залишати сторінку, якщо є незбережені зміни в формі?

```ts
@Component({...})
export class UserProfileComponent implements CanDeactivate<UserProfileComponent> {
  canDeactivate(
    component: UserProfileComponent,
    currentRoute: ActivatedRouteSnapshot,
    currentState: RouterStateSnapshot,
    nextState?: RouterStateSnapshot
  ): Observable<boolean> | Promise<boolean> | boolean {
    // Ваша логіка перевірки
  }
}
```

- [ ] Додати CanDeactivate до маршруту і реалізувати canDeactivate в класі компонента.
- [x] Реалізувати CanDeactivate в класі компонента і додати його до маршруту.
- [ ] Додати CanDeactivate до модуля і реалізувати canDeactivate в сервісі.
- [ ] Це неможливо. Angular не дозволяє перевіряти вихід зі сторінки.

#### П90. Яка команда Angular CLI створює новий компонент з ім'ям hero?

- [ ] ng generate component hero
- [x] ng g c hero
- [ ] ng generate c hero
- [ ] ng c hero

#### П91. Як ви можете реалізувати інтерфейс CanActivate для захисту маршруту?

```ts
@Injectable({
  providedIn: 'root',
})
export class AuthGuard implements CanActivate {
  constructor(private authService: AuthService) {}

  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): boolean {
    return this.authService.isLoggedIn();
  }
}
```

- [ ] Додати AuthGuard до маршруту в конфігурації маршрутизатора.
- [x] Реалізувати canActivate в класі охоронця і додати його до маршруту.
- [ ] Додати AuthGuard до модуля як провайдера.
- [ ] Це неможливо. Angular не дозволяє захищати маршрути.

#### П92. Яка різниця між структурними і атрибутними директивами?

- [ ] Структурні директиви змінюють структуру DOM, а атрибутні - ні.
- [x] Структурні директиви змінюють структуру DOM, додаючи або видаляючи елементи, тоді як атрибутні директиви змінюють вигляд або поведінку існуючих елементів.
- [ ] Атрибутні директиви завжди приймають значення, а структурні - ні.
- [ ] Немає різниці. Це синоніми.

[Angular - Structural and Attribute Directives](https://angular.io/guide/attribute-directives#structural-directives)

#### П93. Як ви можете реалізувати власний pipe в Angular?

```ts
@Pipe({ name: 'exponentialStrength' })
export class ExponentialStrengthPipe implements PipeTransform {
  transform(value: number, exponent: string): number {
    const exp = parseInt(exponent, 10);
    return Math.pow(value, isNaN(exp) ? 1 : exp);
  }
}
```

- [ ] Додати клас з методом transform і зареєструвати його в модулі.
- [x] Створити клас, який реалізує інтерфейс PipeTransform, і зареєструвати його в модулі.
- [ ] Додати декоратор @Pipe і реалізувати метод transform.
- [ ] Це неможливо. Angular не дозволяє користувацькі pipes.

#### П94. Як ви можете використовувати Angular CLI для створення нового модуля?

- [ ] ng generate module my-module
- [x] ng g m my-module
- [ ] ng generate m my-module
- [ ] ng m my-module

#### П95. Як ви можете реалізувати інтерфейс CanDeactivate для перевірки, чи може компонент бути деактивованим?

```ts
export class UserProfileComponent implements CanDeactivate<UserProfileComponent> {
  canDeactivate(component: UserProfileComponent): Observable<boolean> | Promise<boolean> | boolean {
    return component.canLeave ? component.canLeave() : true;
  }
}
```

- [ ] Реалізувати canDeactivate в класі охоронця і додати його до маршруту.
- [x] Реалізувати canDeactivate в класі компонента і додати його до маршруту.
- [ ] Додати CanDeactivate до модуля і реалізувати canDeactivate в сервісі.
- [ ] Це неможливо. Angular не дозволяє деактивацію компонентів.

#### П96. Як ви можете реалізувати власну стратегію завантаження для маршрутизатора Angular?

```ts
@Injectable({ providedIn: 'root' })
export class CustomPreloadingStrategy implements PreloadingStrategy {
  preload(route: Route, load: () => Observable<any>): Observable<any> {
    return route.data && route.data.preload ? load() : of(null);
  }
}
```

- [ ] Додати клас з методом preload і зареєструвати його в модулі.
- [x] Створити клас, який реалізує інтерфейс PreloadingStrategy, і зареєструвати його в модулі.
- [ ] Додати декоратор @Injectable і реалізувати метод preload.
- [ ] Це неможливо. Angular не дозволяє користувацькі стратегії завантаження.

#### П97. Як ви можете використовувати Angular CLI для створення нового сервісу?

- [ ] ng generate service my-service
- [x] ng g s my-service
- [ ] ng generate s my-service
- [ ] ng s my-service

#### П98. Як ви можете реалізувати інтерфейс Resolve для попереднього завантаження даних маршруту?

```ts
@Injectable({ providedIn: 'root' })
export class UserResolver implements Resolve<User> {
  constructor(private userService: UserService) {}

  resolve(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): Observable<User> {
    return this.userService.getUser(route.params['id']);
  }
}
```

- [ ] Додати клас з методом resolve і зареєструвати його в маршруті.
- [x] Створити клас, який реалізує інтерфейс Resolve, і зареєструвати його в маршруті.
- [ ] Додати декоратор @Injectable і реалізувати метод resolve.
- [ ] Це неможливо. Angular не дозволяє попереднє завантаження даних.

#### П99. Як ви можете реалізувати інтерфейс CanLoad для контролю завантаження модуля?

```ts
@Injectable({
  providedIn: 'root',
})
export class AuthGuard implements CanLoad {
  constructor(private authService: AuthService) {}

  canLoad(route: Route, segments: UrlSegment[]): Observable<boolean> | Promise<boolean> | boolean {
    return this.authService.isLoggedIn();
  }
}
```

- [ ] Додати клас з методом canLoad і зареєструвати його в модулі.
- [x] Створити клас, який реалізує інтерфейс CanLoad, і зареєструвати його в маршруті.
- [ ] Додати декоратор @Injectable і реалізувати метод canLoad.
- [ ] Це неможливо. Angular не дозволяє контролювати завантаження модулів.

#### П100. Як ви можете реалізувати інтерфейс CanActivateChild для контролю доступу до дочірніх маршрутів?

```ts
@Injectable({
  providedIn: 'root',
})
export class AuthGuard implements CanActivateChild {
  constructor(private authService: AuthService) {}

  canActivateChild(
    childRoute: ActivatedRouteSnapshot,
    state: RouterStateSnapshot,
  ): Observable<boolean> | Promise<boolean> | boolean {
    return this.authService.isLoggedIn();
  }
}
```

- [ ] Додати клас з методом canActivateChild і зареєструвати його в маршруті.
- [x] Створити клас, який реалізує інтерфейс CanActivateChild, і зареєструвати його в маршруті.
- [ ] Додати декоратор @Injectable і реалізувати метод canActivateChild.
- [ ] Це неможливо. Angular не дозволяє контролювати доступ до дочірніх маршрутів.
