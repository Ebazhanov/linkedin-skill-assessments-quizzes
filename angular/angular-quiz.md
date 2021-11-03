## Angular

#### Q1. What is the purpose of the ViewChild decorator in this component class?

```javascript
@Component({
    ...
    template: '<p #bio></p>'
})
export class UserDetailsComponent {
    @ViewChild('bio') bio;
}
```

- [x] It provides access from within the component class to the ElementRef object for the `<p>` tag that has the bio template reference variable in the component's template view.
- [ ] It indicates that the `<p>` tag be rendered as a child of the parent view that uses this component.
- [ ] It makes the `<p>` tag in the template support content projection.
- [ ] It makes the `<p>` tag visible in the final render. If the #bio was used in the template and the @ViewChild was not used in the class, then Angular would automatically hide the `<p>` tag that has #bio on it.

[Reference (DigitalOcean - viewchild-access-component)](https://www.digitalocean.com/community/tutorials/angular-viewchild-access-component)

#### Q2. What method is used to wire up a FormControl to a native DOM input element in reactive forms?

- [ ] Add the string name given to the FormControl to an attribute named controls on the <form> element to indicate what fields it should include.
- [ ] Use the square bracket binding syntax around the value attribute on the DOM element and set that equal to an instance of the FormControl.
- [x] Use the formControlName directive and set the value equal to the string name given to the FormControl.
- [ ] Use the string name given to the FormControl as the value for the DOM element id attribute.

[Reference (Angular.io - Reactive Form Groups)](https://angular.io/guide/reactive-forms#creating-nested-form-groups)

#### Q3. What is the difference between the `paramMap` and the `queryParamMap` on the `ActivatedRoute` class?

- [ ] The paramMap is an object literal of the parameters in a route's URL path. The queryParamMap is an Observable of those same parameters.
- [ ] The paramMap is an Observable that contains the parameter values that are part of a route's URL path. The queryParamMap is a method that takes in an array of keys and is used to find specific parameters in the paramMap.
- [ ] paramMap is the legacy name from Angular 3. The new name is queryParamMap.
- [x] Both are Observables containing values from the requested route's URL string. The paramMap contains the parameter values that are in the URL path and the queryParamMap contains the URL query parameters.

[Reference (StackOverflow)](https://stackoverflow.com/a/49617621)

#### Q4. Based on the following usage of the async pipe, and assuming the users class field is an Observable, how many subscriptions to the users Observable are being made?

```html
<h2>Names</h2>
<div *ngFor="let user of users | async">{{ user.name }}</div>
<h2>Ages</h2>
<div *ngFor="let user of users | async">{{ user.age }}</div>
<h2>Genders</h2>
<div *ngFor="let user of users | async">{{ user.gender }}</div>
```

- [ ] None. The async pipe does not subscribe automatically.
- [ ] None. The template syntax is not correct.
- [x] Three. There is one for each async pipe.
- [ ] One. The async pipe caches Observables by type internally.

[References (UltimateCourses)](https://ultimatecourses.com/blog/angular-ngfor-async-pipe)

#### Q5. How can you use the HttpClient to send a POST request to an endpoint from within an addOrder function in this OrderService?

```javascript
export class OrderService {
    constructor(private httpClient: HttpClient) { }

    addOrder(order: Order) {
      // Missing line
    }
}
```

- [ ] this.httpClient.url(this.orderUrl).post(order);
- [ ] this.httpClient.send(this.orderUrl, order);
- [ ] this.httpClient.post<Order>(this.orderUrl, order);
- [x] this.httpClient.post<Order>(this.orderUrl, order).subscribe();

[Reference (Angular.io - Sending data to server)](https://angular.io/guide/http#sending-data-to-a-server)

#### Q6. What is the RouterModule.forRoot method used for?

- [ ] Registering any providers that you intend to use in routed components.
- [x] Registering route definitions at the root application level.
- [ ] Indicating that Angular should cheer on your routes to be successful.
- [ ] Declaring that you intend to use routing only at the root level.

[Reference (O'REILLY)](https://www.oreilly.com/library/view/switching-to-angular/9781788620703/c9e90774-0e10-410b-bd20-d3e9e0b8d117.xhtml)

#### Q7. Which DOM elements will this component metadata selector match on?

```javascript
@Component({
    selector: 'app-user-card',
    . . .
})
```

- [ ] Any element with the attribute app-user-card, such as `<div app-user-card></div>`.
- [ ] The first instance of `<app-user-card></app-user-card>`.
- [x] All instances of `<app-user-card></app-user-card>`.
- [ ] All instances of `<user-card></user-card>`.

[Reference (Angular.io - Component Metadata)](https://angular.io/guide/architecture-components#component-metadata)

#### Q8. What is the correct template syntax for using the built-in ngFor structural directive to render out a list of productNames?

- [ ]

```html
<ul>
  <li [ngFor]="let productName of productNames">{{ productName }}</li>
</ul>
```

- [ ]

```html
<ul>
  <li ngFor="let productName of productNames">{{ productName }}</li>
</ul>
```

- [x]

```html
<ul>
  <li *ngFor="let productName of productNames">{{ productName }}</li>
</ul>
```

- [ ]

```html
<ul>
  <? for productName in productNames { ?>
  <li>{{ productName }}</li>
  <? } ?>
</ul>
```

[Reference (Angular.io- Structural Directives)](https://angular.io/guide/built-in-directives#listing-items-with-ngfor)

#### Q9. What are the two component decorator metadata properties used to set up CSS styles for a component?

- [ ] viewEncapsulation and viewEncapsulationFiles.
- [ ] There is only one and it is the property named css.
- [ ] css and cssUrl.
- [x] styles and styleUrls.

[Reference (Angular.io - Component Styles)](https://angular.io/guide/component-styles)

#### Q10. With the following component class, what template syntax would you use in the template to display the value of the title class field?

```javascript
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
- [ ] A class field cannot be displayed in a template via the template syntax.

[Reference (Angular.io - String Interpolation or Text Interpolation)](https://angular.io/guide/interpolation)

#### Q11. What is the purpose of the valueChanges method on a FormControl?

- [ ] It is used to configure what values are allowed for the control.
- [ ] It is used to change the value of a control to a new value. You would call that method and pass in the new value for the form field. It even supports passing in an array of values that can be set over time.
- [ ] It returns a Boolean based on if the value of the control is different from the value with which it was initialized.
- [x] It is an observable that emits every time the value of the control changes, so you can react to new values and make logic decisions at that time.

[Reference (Angular.io - Displaying a from control value)](https://angular.io/guide/reactive-forms#displaying-a-form-control-value)

#### Q12. What directive is used to link an `<a>` tag to routing?

- [ ] routeTo
- [x] routerLink
- [ ] routePath
- [ ] appLink

[Reference (Angular.io - RouterLink)](https://angular.io/api/router/RouterLink#description)

#### Q13. What is the Output decorator used for in this component class?

```javascript
@Component({
    selector: 'app-shopping-cart',
    . . .
})
export class ShoppingCartComponent {
    @Output() itemTotalChanged = new EventEmitter();
}
```

- [ ] It makes the `itemTotalChanged` class field public.
- [ ] It provides a way to bind values to the `itemTotalChanged` class field, like so: `<app-shopping-cart [itemTotalChanged]="newTotal"></app-shopping-cart>`.
- [x] It provides a way to bind events to the `itemTotalChanged` class field, like so: `<app-shopping-cart (itemTotalChanged)="logNewTotal($event)"></app-shopping-cart>`.
- [ ] It is simply a way to put a comment in front of a class field for documentation.

[Reference (Angular.io - Sending data to parent component)](https://angular.io/guide/inputs-outputs#sending-data-to-a-parent-component)

#### Q14. What is the difference between these two markup examples for conditionally handling display?

```html
<div *ngIf="isVisible">Active</div>
<div [hidden]="!isVisible">Active</div>
```

- [ ] The `ngIf` is shorthand for the other example. When Angular processes that directive, it writes a div element to the DOM with the hidden property.
- [ ] They are fundamentally the same.
- [x] The `ngIf` directive does not render the div in the DOM if the expression is false. The `hidden` property usage hides the div content in the browser viewport, but the div is still in the DOM.
- [ ] The `ngIf` is valid, but the use of the `hidden` property is wrong and will throw an error.

[Reference (StackOverflow)](https://stackoverflow.com/a/39778145)

#### Q15. How can you disable the submit button when the form has errors in this template-driven forms example?

```html
<form #userForm="ngForm">
  <input type="text" ngModel name="firstName" required />
  <input type="text" ngModel name="lastName" required />
  <button (click)="submit(userForm.value)">Save</button>
</form>
```

- [ ]

```html
<button (click)="submit(userForm.value)" disable="userForm.invalid">Save</button>
```

- [x]

```html
<button (click)="submit(userForm.value)" [disabled]="userForm.invalid">Save</button>
```

- [ ]

```html
<button (click)="submit(userForm.value)" [ngForm.disabled]="userForm.valid">Save</button>
```

- [ ]

```html
<button (click)="submit(userForm.value)" *ngIf="userForm.valid">Save</button>
```

[Reference (Angular.io - Submit the form with ngSubmit)](https://angular.io/guide/forms#submit-the-form-with-ngsubmit)

#### Q16. You want to see what files would be generated by creating a new contact-card component. Which command would you use?

- [x] ng generate component contact-card --dry-run
- [ ] ng generate component contact-card --no-files
- [ ] ng generate component component --dry
- [ ] ng generate component --exclude

[Reference (Angular.io - ng generate options)](https://angular.io/cli/generate#options)

#### Q17. Based on the following component, what template syntax would you use to bind the TitleCardComponent's titleText field to the h1 element title property?

```javascript
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

[Reference (Angular.io - String Interpolation)](https://angular.io/guide/interpolation)

#### Q18. What are Angular lifecycle hooks?

- [ ] loggers for tracking the health of an Angular app
- [ ] providers that can be used to track the instances of components
- [ ] built-in pipes that can be used in templates for DOM events
- [x] reserved named methods for components and directives that Angular will call during set times in its execution, and can be used to tap into those lifecycle moments

[Reference (Angular.io - Lifecycle hooks)](https://angular.io/guide/lifecycle-hooks)

#### Q19. Pick the best description for this template syntax code:

```html
<span>Boss: {{job?.bossName}} </span>
```

- [ ] The ? is shorthand for the async pipe. The job value must be an Observable.
- [x] It is using the safe navigation operator (?) on the job field. If the job field is undefined, the access to the bossName will be ignored and no error will occur.
- [ ] There is an error in the template syntax. The ? is not valid here.
- [ ] It is diplaying the job value if it has one; otherwise it is displaying the bossName.

[Reference (StackOverflow)](https://stackoverflow.com/a/60182134)

#### Q20. How would you configure a route definition for a UserDetailComponent that supports the URL path user/23 (where 23 represents the id of the requested user)?

- [x] `{ path: 'user/:id', component: UserDetailComponent }`
- [ ] `{ url: 'user/:id', routedComponent: UserDetailComponent }`
- [ ] `{ routedPath: 'user/:id', component: UserDetailComponent }`
- [ ] `{ destination: new UserDetailComponent(), route: 'user/:id' }`

[Reference (CodeCraft - Parameterised Routes)](https://codecraft.tv/courses/angular/routing/parameterised-routes/#_configuration)

#### Q21. What are the HostListener decorators and the HostBinding decorator doing in this directive?

```javascript
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

- [x] They are setting the CalloutDirective.fontWeight field based on whether or not the mouse is over the DOM element. The HostListener then sets the font-weight CSS property to the fontWeight value.
- [ ] They are setting up the directive to check the DOM element that it is on. If it has event bindings added for mouse enter and leave it will use this code. Otherwise nothing will happen.
- [ ] This is an incorrect use of HostListener and HostBinding. The HostListener and HostBinding decorators do not do anything on directives; they work only when used on components.
- [ ] If the DOM element that this directive is placed on has the CSS property font-weight set on it, the mouseenter and mouseleave events will get raised.

[Reference (DigitalOcean)](https://www.digitalocean.com/community/tutorials/angular-hostbinding-hostlistener)

#### Q22. What Angular template syntax can you use on this template-driven form field to access the field value and check for validation within the template markup?

```html
<input type="text" ngModel name="firstName" required minlength="4" />
<span *ngIf="">Invalid field data</span>
```

- [x] You can make use of a template reference variable and the exportAs feature that the ngModel directive has.
- [ ] You can use the ngModel directive in combination with the input field name.
- [ ] You can use a template reference variable for the HTML input element and then check the valid property off of that.
- [ ] It is not possible to get access to the field value with template-driven forms. You must use reactive forms for that.

[Reference (Angular.io -Show and hide validation error )](https://angular.io/guide/forms#show-and-hide-validation-error-messages) | [Medium](https://medium.com/@agoiabeladeyemi/template-driven-forms-in-angular-4a3a5ad960de)

#### Q23. What is the value type that will be stored in the headerText template reference variable in this markup?

```html
<h1 #headerText>User List</h1>
```

- [x] an Angular ElementRef, a wrapper around a native element
- [ ] the inner text of the `<h1>` element
- [ ] a header component class
- [ ] the native DOM element type of HTMLHeadingElement

[Reference (Pluralsight - Template reference variable)](https://www.pluralsight.com/guides/how-to-use-template-reference-variables-in-angular)

#### Q24. What is the difference, if any, of the resulting code logic based on these two provider configurations?

```javascript
[{ provide: FormattedLogger, useClass: Logger }][{ provide: FormattedLogger, useExisting: Logger }];
```

- [ ] They are the same. Both will result in a new instance of Logger that is bound to the FormattedLogger token.
- [x] The useClass syntax tells the injector to make a new instance of Logger and bind that instance to the FormattedLogger token. The useExisting syntax refers to an already existing object instance declared as Logger.
- [ ] Both of them are wrong. A strong type connot be used for useClass or useExisting.
- [ ] They are the same. Both will result in the FormattedLogger token being an alias for the instance of Logger.

Reference [(Angular.io - Dependency Providers)](https://angular.io/guide/dependency-injection-providers#defining-providers) | [ (TektutorialHub)](https://www.tektutorialshub.com/angular/angular-providers/)

#### Q25. What is the purpose of the data property (seen in the example below) in a route configuration?

```javascript
   {
       path: 'customers',
       component: CustomerListComponent,
       data: { accountSection: true }
   }
```

- [ ] a key/value mapping for setting @Input values on the routed component instance
- [x] a way to include static, read-only data associated with the route that can be retrieved from the ActivatedRoute
- [ ] a property on the route that can be used to load dynamic data for the route
- [ ] an object that will get auto-injected into the routed component's constructor.

Reference [TektutorialsHub](https://www.tektutorialshub.com/angular/angular-pass-data-to-route/#:~:text=Angular%20allows%20us%20to%20pass,of%20the%20history%20state%20object.) | [StackOverflow](https://stackoverflow.com/a/36835156)

#### Q26. How does the built-in `ngIf` structural directive change the rendered DOM based on this template syntax?

```javascript
@Component({
  selector: 'app-product',
  template: '<div *ngIf="product">{{ product.name }}</div>',
})
export class ProductComponent {
  @Input() product;
}
```

- [ ] The `<div>` acts as a placeholder. If the product class field is "truthy," the `<div>` will get replaced by just the `product.name` value; if not, then nothing will get rendered.
- [ ] The `<div>` will always be rendered, and if the product field is "truthy," the `<div>` element will contain the `product.name` value; otherwise it will render the `<div>` element with no value in it.
- [ ] It produces an error, since ngIf is not a built-in structural directive.
- [x] If the product class field is "truthy," then the rendered DOM will include the `<div>` with the value of the `product.name` field. If it is not "truthy,' the rendered DOM will not contain the `<div>` element.

[Reference (angular.io)](https://angular.io/api/common/NgIf)

#### Q27. What does this code accomplish?

```javascript
@NgModule({
  declarations: [AppComponent],
  imports: [BrowserModule],
  bootstrap: [AppComponent],
})
export class AppModule {}

platformBrowserDynamic().bootstrapModule(AppModule);
```

- [ ] It executes a unit test for an NgModule.
- [ ] It provides a way to code the document structure of an Angular application. The @NgModule is a form of inline code commenting that gets ignored by the TypeScript compiler but will show up with special formatting in code editor applications.
- [ ] It declares an Angular module named AppModule and makes it available for lazy loading throughout the application.
- [x] It declares an Angular module named AppModule that contains a bootstrapped component named AppComponent. Then it registers that module with Angular, so the app can start up.

[Reference (Angular.io - The basic NgModule)](https://angular.io/guide/ngmodules#the-basic-ngmodule)

#### Q28. Which choice best describes what the _resolve_ property does in this route configuration?

```javascript
{
   path: ':id',
   component: UserComponent,
   resolve: {
     user: UserResolverService
   }
}
```

- [x] Prior to loading the _UserComponent_, the router will subscribe to the _Observable_ returned by a _resolve_ method in the _UserResolverService_. This technique can be used to get preloaded data for a _route_.
- [ ] After the _route_ is done resolving, and the component is loaded and rendered, the _UserResolverService_ will have a method named _user_ run that will clean up any open data connections.
- [ ] There is an error. The correct property name is _onResolve_.
- [ ] The _UserComponent_ will have a parameter in its constructor for _user_, and the _router_ will handle injecting in a value for that from a call to a _user_ method in the _UserResolverService_.

[Reference (angular.io)](https://angular.io/api/router/Resolve)

#### Q29. What is the purpose of the ContentChildren decorator in this component class?

```javascript
@Component({
 . . .
 template: '<ng-content></ng-content›'
})
export class TabsListComponent {
 @ContentChildren(TabComponent) tabs;
}
```

- [ ] If any _TabsComponent_ elements are added to the _TabsListComponent_ template, they will get put into the <ng-content> element at runtime.
- [ ] It creates _TabComponent_ components in the _TabsListComponent_ template when a _TabsListComponent_ is instantiated.
- [x] It provides access from within the component class to any _TabComponent_ components that were content projected into the <ng-content> for this component.
- [ ] It restricts the allowed elements that can be put into a _TabsListComponent_ element to allow only _TabComponent_ elements.

[Reference (betterprogramming.pub)](https://betterprogramming.pub/understanding-contentchildren-with-an-example-e76ce78968db)

#### Q30. In order for Angular to process components in an application, where do the component types need to be registered?

- [ ] within a script tag in the index.html file
- [ ] in an NgModule decorator metadata tag named _components_
- [ ] No registration is needed simply include the component files in an app directory.
- [x] in an NgModule decorator metadata property named _declarations_

[Reference (angular.io)](https://angular.io/guide/ngmodule-api#ngmodule-metadata)

#### Q31. What is the purpose of the `fixture.detectChanges()` call in this unit test?

```javascript
TestBed.configureTestingModule({
  declarations: [UserCardComponent],
});
let fixture = TestBed.createComponent(UserCardComponent);

fixture.detectChanges();

expect(fixture.nativeElement.querySelector('h1').textContent).toContain(
  fixture.componentInstance.title,
);
```

- [ ] It tracks any potential Ul changes and will fail the unit test if any are made.
- [ ] It is used to ensure component template stability across multiple unit tests in the entire test suite.
- [x] It forces Angular to perform change detection, which will render the _UserCardComponent_ before you can validate its template.
- [ ] It is used to log change-detection events to the console during unit test runs.

[Reference (angular.io)](https://angular.io/api/core/testing/ComponentFixture#detectChanges)

#### Q32. What will the URL segment look like based on the following call to the `Router.navigate` method when goToUser is passed the value 15?

```javascript
export class ToolsComponent {
 constructor (private router: Router) { }
 goToUser (id: number) {
   this.router.navigate(['user', id]);
 }
}
```

- [x] /user/15
- [ ] /user?id=15
- [ ] /user:15
- [ ] /user;id=15

[Reference (angular.io)](https://angular.io/api/router/Router#navigate)

#### Q33. When a service is provided for root and is also added to the provider's configuration for a lazy-loaded module, what instance of that service does the injector provide to constructors in the lazy-loaded module?

- [x] A new instance of that service is created when the module is lazy loaded.
- [ ] Providing a service of the same type at a lazy-loaded module level is not allowed.
- [ ] If an instance of the service has not been created at the root level yet. it will create one there and then use it.
- [ ] A single instance of that service is always instantiated at root and is the only one ever used, including within lazy modules.

#### Q34. What is the HostBinding decorator doing in this directive?

```javascript
@Directive({
  selector: ' [appHighlight] ',
})
export class HighlightDirective {
  @HostBinding('class.highlighted') highlight = true;
}
```

- [x] It is adding the CSS class named highlighted to any DOM element that has the appHighlight directive on it.
- [ ] HostBinding does not do anything on directives, only on components.
- [ ] It is specifying if the host element gets the highlighted class added to its class attribute, then the directive class field highlight will get set to
      true; and if it is not added on the host it will get set to false.
- [ ] It is creating an inline style on the host element with a CSS property named highlight set to true.

[Reference (StackOverflow)](https://stackoverflow.com/a/46207423)

#### Q35. In reactive forms, what Angular form class type is used on the native DOM <form> element to wire it up?

- [ ] `FormArray`
- [ ] `FormControl`
- [x] `FormGroup`
- [ ] `all of these answers`

#### Q36. Assuming the username FormControl has been configured with a minLength validator, how can you set up an error display in the following reactive

forms markup for the username field?

```html
<form [formGroup]="form"›
  <input type="text" formControlName= "username"›
  ...
</form>
```

- [ ]

```javascript
    <span *ngIf="username.minLength.invalid"›
        Username length is not valid
    </span>
```

- [ ]

```javascript
<input type="text" formControlName="username" [showMinLength]="true"›
```

- [ ]

```javascript
    <span *ngIf="form.get('username').getError('minLength') as minLengthError">
      Username must be at least {{ minLengthError.requiredLength }} characters.
    </span>
```

- [x]

```javascript
<input type="text" formControlName="username" #userName="ngModer">
    <span *ngIf="userName.errors.minlength"›
      Username must be at least {{ userName.errors.minlength.requiredLength }} characters.
    </span>
```

[Refrence (Codecraft)](https://codecraft.tv/courses/angular/forms/template-driven/)

#### Q37. How does the emulated view encapsulation mode handle CSS for a component?

- [ ] It renders the CSS exactly how you wrote it without any changes.
- [ ] It makes use of shadow DOM markup and CSS.
- [x] It creates unique attributes for DOM elements and scopes the CSS selectors you write to those attribute ids.
- [ ] It renders all of the CSS rules you write as inline CSS on all of the DOM elements you use them on in the template.

[Reference (Angular.io)](https://angular.io/guide/view-encapsulation#inspecting-generated-css)

#### Q38. With the following TestBed setup, what can be used to access the rendered DOM for the UserCardComponent?

```javascript
TestBed.configureTestingModule({
  declarations: [UserCardComponent],
});
let fixture = TestBed.createComponent(UserCardComponent);
```

- [ ] `fixture.componentTemplate`
- [ ] `fixture.getComponentHtml()`
- [x] `fixture.nativeElement`
- [ ] `fixture.componentInstance.template `

[Reference (StackOverflow)](https://stackoverflow.com/a/56504773)

[Reference (Angular.io)](https://angular.io/guide/testing-components-basics#nativeelement)

#### Q39. Given these two components, what will get rendered to the DOM based on the markup usage?

```javascript
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

- [x]

```javascript
 <app-card>
  <h1>Data Card</hl>
  <app-bio>
   Been around for four years.
  </app-bio>
 </app-card>
```

- [ ]

```javascript
<h1>Data Card</h1>
 <app-bio>
  Been around for four years.
 </app-bio>
```

- [ ]

```javascript
<app-card>
  <h1>Data Card</hl>
  <ng-content></ng-content>
  <app-bio>
   Been around for four years.
   <ng-content></ng-content>
  </app-bio>
</app-card>
```

- [ ]

```javascript
<app-card>
  <h1>Data Card</hl>
</app-card>
```

#### Q40. Given the app-title-card component in the code below, what DOM will the app-user-card component render?

```javascript
@Component({
   selector: 'app-user-card',
   template: '<app-title-card></app-title-card><p>3enny Smith</p>'
})

@Component({
   selector: 'app-title-card',
   template: '<h1>User Data</hl>'
})

// usage of user card component in parent component html
<app-user-card></app-user-card>
```

- [x]

```javascript
<app-user-card>
  <app-title-card>
    <h1>User Data</h1>
  </app-title-card>
  <p>genny Smith</p>
</app-user-card>
```

- [ ]

```javascript
<h1>User Data</h1>
<p>Jenny Smith<p>
```

- [ ]

```javascript
<app-user-card>
  <app-title-card></app-title-card>
</app-user-card>
```

- [ ]

```javascript
<div app-user-card>
  <h1 app-title-card>User Data</h1>
  <p>Jenny Smith</p>
</div>
```

#### Q41. Pick the matching code for the custom provider registration that the @Inject () decorator is looking for:

```javascript
constructor(@Inject('Logger') private logger) { }
```

- [ ]

```javascript
providers: [Logger];
```

- [x]

```javascript
providers: [{ provide: 'Logger', useClass: Logger }];
```

- [ ]

```javascript
@Injectable({
    providedln: 'root'
})
```

- [ ]

```javascript
providers: [{ provide: 'Logger' }];
```

References [StackOverflow](https://stackoverflow.com/a/37315355) | [TektutorialHub](https://www.tektutorialshub.com/angular/angular-injector-injectable-inject/) | [Angular.io - Dependency Injection In Action](https://angular.io/guide/dependency-injection-in-action#supply-a-custom-provider-with-inject)

#### Q42. Which choice best describes the following usage of the HttpClient . get method in the getsettings class method?

```javascript
export class SettingsService {
    constructor(private httpClient: HttpClient) { }
    ...

getSettings()
{
    return this.httpClient.get < Settings > (this.settingsUrl)
        .pipe(
            retry(3)
        );
}}
```

- [ ] The RxJs pipe method is an alias for the subscribe method, so a call to `getSettings` will execute the get query. The retry operator is used to tell the pipe call to retry the get query three times.
- [ ] It will produce an error at runtime because the pipe method is not available off of the `Httpclient.get` call.
- [ ] Every single call to the getSettings method will result in the Httpclient making three total get requests to the settingsUrl, which is not ideal because there will always be two extra calls that are not needed. The retry operator should not be used in this manner.
- [x] When the result of the getSettings method is subscribed to, the HTTP GET call will be made; if it fails, it will be retried up to three times before it gives up and returns an error.

Reference [learnrxjs.io](https://www.learnrxjs.io/learn-rxjs/operators/error_handling/retry) | [dev.to](https://dev.to/gparlakov/how-does-rxjs-retry-work-412p)

#### Q43. When a service requires some setup to initialize its default state through a method, how can you make sure that said method is invoked before the service gets injected anywhere?

- [ ] Put the logic of that service method into the service constructor instead.
- [x] Use a factory provider at the root AppModule level that depends on the service to call that service method.
- [ ] it is not possible to do it at application start; you can do it only at a component level.
- [ ] Instantiate an instance of the service at the global level (window scope) and then call that method.

#### Q44. What statement best describes this usage of the TestBed?

```javascript
const spy = jasmine.createSpyObj('DataService', ['getUsersFromApi']);
TestBed.configureTestingModule({
  providers: [UserService, { provide: DataService, useValue: spy }],
});
const userService = TestBed.get(UserService);
```

- [ ] The TestBed is required anytime you want to make use of a spy object in a unit test for an Angular provider.
- [ ] The TestBed is being used to test a component's view.
- [x] The TestBed scaffolds an NgModule with two providers and handles any dependeny injection. If any Angular class requests the DataService in its constructor, the TestBed will inject spy in that constructor.
- [ ] The TestBed is configuring the test runner to tell it to only execute tests for the two providers listed in its providers array.
- `All other tests be ignored, including tests that assert results against one of these providers and a non-defined provider.`
  `Although it will work when multiple providers in this configuration are asserted against in a single test.`

#### Q45. What is the primary difference between a component and a directive?

- [ ] A component uses a selector metadata property and a directive does not.
- [ ] A directive can be used for adding custom events to the DOM and a component cannot.
- [x] A component has a template and a directive does not.
- [ ] A directive can target only native DOM elements.

[Reference (StackOverflow)](https://stackoverflow.com/a/34616190)

#### Q46. What could you add to this directive class to allow the truncate length to be set during directive usage in markup?

```
@Directive({
    selector: '[appTruncate]'
})
export class TruncateDirective {
    . . .
}

// example of desired usage:
<p [appTruncate]="10">Some very long text here</p>
```

- [x] `@Input() appTruncate: number;`
- [ ] `@Output() appTruncate;`
- [ ] `constructor(maxLength: number) { }`
- [ ] `Nothing. The directive selector cannot be used to pass in values to the directive.`

Reference [Angular.io](https://angular.io/guide/attribute-directives#passing-values-into-an-attribute-directive) | [StackOverflow](https://stackoverflow.com/a/46303049)

#### Q47. How can you pass query parameters to this `HttpClient.get` request?

```
export class OrderService {
    constructor(private httpClient: HttpClient) { }

    getOrdersByYear(year: number): Observable<Order[]> {
      return this.httpClient.get<Order[]>(this.ordersUrl);
    }
}
```

- [ ] `return this.httpClient.get<Order[]>(this.ordersUrl, {'year': year})`
- [ ] `return this.httpClient.get<Order[]>(this.ordersUrl, year)`
- [x]

```
const options = {params: new HttpParams().set('year', year) };
return this.httpClient.get<Order[]>(this.ordersUrl, options);
```

- [ ]

```angularjs
getOrdersByYear(year: number): Observable<Order[]> {
    return this.httpClient.addParam('year', year).get<Order[]>(this.ordersUrl, year);
}
```

Reference [StackOverflow](https://stackoverflow.com/a/34475594) | [TektutorialHub](https://www.tektutorialshub.com/angular/angular-pass-url-parameters-query-strings/#httpparams)

#### Q48. Assuming the `DataService` has been registered in the providers for the application, which answer best describes what happens based on this component's constructor?

```
@Component({
    ...
})
export class OrderHistoryComponent {
    constructor(private dataService: DataService) {}
    ...
}
```

- [ ] It is declaring that the `OrderHistoryComponent` will have its own version of a `DataService` and that it should never use any existing instances. The `DataService` would need to be instantiated within the class as a private field for this code to be complete and working.
- [x] When Angular creates a new instance of the `OrderHistoryComponent`, the injector will provide an instance of a `DataService` class to the component constructor's first argument. The constructor's `dataService` parameter will be used to set a private instance field with the same name on the instance.
- [ ] It provides a way to do component testing only; the constructor has no usage in the actual run of the Angular application.
- [ ] It enables the custom element that the component targets to have a custom property named `dataService` that can be used to bind an existing `DataService` instance to.

Reference [StackOverflow](https://stackoverflow.com/a/49755822) | [Angular.io - Dependency Injection](https://angular.io/guide/dependency-injection)

#### Q49. Finish this markup using the `ngIf` directive to implement an else case that will display the text "User is not active":

```angular2html
<div *ngIf="userIsActive; else inactive">
  Currently active!
</div>
```

- [ ]

```angular2html
<div #inactive>
  User is not active.
</div>
```

- [ ]

```angular2html
<div *ngIf="inactive">
  User is not active.
</div>
```

- [ ]

```angular2html
<ng-template #else="inactive">
  <div>User is not active.</div>
</ng-template>
```

- [x]

```angular2html
<ng-template #inactive>
  <div>User is not active.</div>
</ng-template>
```

[Reference (Angular.io)](https://angular.io/api/common/NgIf)

#### Q50. What is the correct syntax for a route definition to lazy load a feature module?

- [ ]

```
{
    path: 'users',
    lazy: './users/users.module#UsersModule'
}
```

- [x]

```
{
    path: 'users',
    loadChildren: () => import('./users/users.module').then(m => m.UserModule)
}
```

- [ ]

```
{
    path: 'users',
    loadChildren: './users/users.module#UsersModule'
}
```

- [ ]

```
{
    path: 'users',
    module: UsersModule
}
```

[Reference (Angular.io - Lazy Loading Modules)](https://angular.io/guide/lazy-loading-ngmodules)

#### Q51. Describe how the validation is set up and configured in this reactive forms example:

```
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

- [ ] The `FormControl` for `username` is getting configured to exclude three validators from the validators that it is allowed to use.
- [ ] The `FormControl` for `username` is getting configured to allow three possible validators to be used: `required, maxLength`, and a custom one named `unique`. To enable these `validators`, a validator directive would need to be put on the form fields in the markup.
- [ ] Validation cannot be set up this way in reactive forms.
- [x] The `FormControl` for `username` is getting configured with three validators: the `required` and `minLength` validators that come from Angular, and a custom validator function named `unique` that checks for the value not equal to the string `admin`.

Reference [Angular.io - Form Validation](https://angular.io/guide/form-validation) | [Angular University Blog](https://blog.angular-university.io/angular-custom-validators/)

#### Q52. What does the Injectable decorator do on this service class?

```
@Injectable({
    providedIn: 'root'
)}
export class DataService { }
```

- [ ] It registers a provider for the service that is available only at the root module level, not to any children modules.
- [x] It registers a provider for the service in the root application injector, making a single instance of it available throughout the application.
- [ ] It makes it so the service can be injected only in the bootstrapped component for the application.
- [ ] It sets up a compile time rule that allows you to put the service type only in the providers metadata property of the root NgModule.

[Reference (Angular.io)](https://angular.io/guide/providers#providing-a-service)

#### Q53. Describe the usage of this code

```
export interface AppSettings {
	title: string;
	version: number;
}
export const APP_SETTINGS = new Injection<AppSettings>('app.settings');
```

- [ ] The InjectionToken is adding an instance of the AppSettings to the root provider via the InjectionToken constructor call, making it automatically available to all NgModules, services and components throughout the Angular application without the need to inject it anywhere.
- [ ] The InjectionToken is used to create a provider token for a non-class dependency. An Object literal can be provider as a value for the APP_SETTINGS dependency provider type that can then be injected into components, services, etc ..
- [ ] The InjectionToken is used to create a dynamic decorator for the AppSettings that can be used on constructor parameters via an @AppSettings decorator.
- [ ] This code has an error since you cannot use a TypeScript interface for the generic type on the InjectionToken

#### Q54. For the following template-driven forms example, what argument can be passed to the submit method in the click event to submit the data for the form?

```
<form #form="ngForm">
	<input type="text" ngModel="firstName">
	<input type="text" ngModel="lastName">
	<button (click)="submit()">Save</button>
</form>
```

- [ ] submit(form.value)
- [ ] submit($event)
- [ ] submit(ngForm.value)
- [ ] submit(FirstName, lastName)

#### Q54. What is the purpose of the prelodingStrategy property configuration in this router code?

```
RouterModule.forRoot (
	...
	{
	preloadingStrategy: PreloadAllModules
	}
)
```

- [ ] It enables the option to flag individual routes for preloading.
- [ ] It preloads all dependencies for routes, creating instances of services when the app first starts up
- [ ] It ensures all modules get built into a single app module bundle file.
- [ ] It configures the router to immediately load all routes that have a loadChildren property(routes that are typically loaded when requested)

#### Q55. What is an alternative way to write this markup to bind the value of the class field `userName` to the `h1` element title property?

```html
<h1 [title]="userName">Current user is {{ userName }}</h1>
```

- [ ] title="userName"
- [ ] title="{{ userName }}"
- [ ] title="{{ 'userName' }}"
- [ ] The only way to do it is by using the square brackets.

#### Q56. What is the `async` pipe doing in this example?

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

- [ ] It is doing nothing, since the async pipe cannot be used in an `ngFor` statement.
- [ ] It is configuring the `ngFor` iteration to support multiple lists of users at the same time.
- [ ] It is subscribing to the observable returned from the `HttpClient.get` method and unwrapping the returned value so it can be iterated over in the `ngFor`.
- [ ] It is allowing all of the users in the `users` field to be rendered concurrently to the DOM.
