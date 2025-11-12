## Angular

#### Q1. What is the purpose of the ViewChild decorator in this component class?

```ts
@Component({
    ...
    template: '<p #bio></p>'
})
export class UserDetailsComponent {
    @ViewChild('bio') bio;
}
```

- [x] It provides access from within the component class to the ElementRef object for the `<p>` tag that has the bio template reference variable in the component's template view.
- [ ] It indicates that the `<p>` tag is rendered as a child of the parent view that uses this component.
- [ ] It makes the `<p>` tag in the template support content projection.
- [ ] It makes the `<p>` tag visible in the final render. If the #bio was used in the template and the @ViewChild was not used in the class, then Angular would automatically hide the `<p>` tag that has #bio on it.

[DigitalOcean - viewchild-access-component](https://www.digitalocean.com/community/tutorials/angular-viewchild-access-component)

#### Q2. What method is used to wire up a FormControl to a native DOM input element in reactive forms?

- [ ] Add the string name given to the FormControl to an attribute named controls on the `<form>` element to indicate what fields it should include.
- [ ] Use the square bracket binding syntax around the value attribute on the DOM element and set that equal to an instance of the FormControl.
- [x] Use the formControlName directive and set the value equal to the string name given to the FormControl.
- [ ] Use the string name given to the FormControl as the value for the DOM element id attribute.

[Angular.io - Reactive Form Groups](https://angular.io/guide/reactive-forms#creating-nested-form-groups)

#### Q3. What is the difference between the `paramMap` and the `queryParamMap` on the `ActivatedRoute` class?

- [ ] The paramMap is an object literal of the parameters in a route's URL path. The queryParamMap is an Observable of those same parameters.
- [ ] The paramMap is an Observable that contains the parameter values that are part of a route's URL path. The queryParamMap is a method that takes in an array of keys and is used to find specific parameters in the paramMap.
- [ ] paramMap is the legacy name from Angular 3. The new name is queryParamMap.
- [x] Both are Observables containing values from the requested route's URL string. The paramMap contains the parameter values that are in the URL path and the queryParamMap contains the URL query parameters.

[StackOverflow](https://stackoverflow.com/a/49617621)

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

[UltimateCourses](https://ultimatecourses.com/blog/angular-ngfor-async-pipe)

#### Q5. How can you use the HttpClient to send a POST request to an endpoint from within an addOrder function in this OrderService?

```ts
export class OrderService {
  constructor(private httpClient: HttpClient) {}

  addOrder(order: Order) {
    // Missing line
  }
}
```

- [ ] `this.httpClient.url(this.orderUrl).post(order);`
- [ ] `this.httpClient.send(this.orderUrl, order);`
- [ ] `this.httpClient.post<Order>(this.orderUrl, order);`
- [x] `this.httpClient.post<Order>(this.orderUrl, order).subscribe();`

[Angular.io - Sending data to server](https://angular.io/guide/http#sending-data-to-a-server)

#### Q6. What is the RouterModule.forRoot method used for?

- [ ] Registering any providers that you intend to use in routed components.
- [x] Registering route definitions at the root application level.
- [ ] Indicating that Angular should cheer on your routes to be successful.
- [ ] Declaring that you intend to use routing only at the root level.

[O'REILLY](https://www.oreilly.com/library/view/switching-to-angular/9781788620703/c9e90774-0e10-410b-bd20-d3e9e0b8d117.xhtml)

#### Q7. Which DOM elements will this component metadata selector match on?

```ts
@Component({
    selector: 'app-user-card',
    . . .
})
```

- [ ] Any element with the attribute app-user-card, such as `<div app-user-card></div>`.
- [ ] The first instance of `<app-user-card></app-user-card>`.
- [x] All instances of `<app-user-card></app-user-card>`.
- [ ] All instances of `<user-card></user-card>`.

[Angular.io - Component Metadata](https://angular.io/guide/architecture-components#component-metadata)

#### Q8. What is the correct template syntax for using the built-in ngFor structural directive to render out a list of productNames?

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

#### Q9. What are the two-component decorator metadata properties used to set up CSS styles for a component?

- [ ] viewEncapsulation and viewEncapsulationFiles.
- [ ] There is only one and it is the property named css.
- [ ] css and cssUrl.
- [x] styles and styleUrls.

[Angular.io - Component Styles](https://angular.io/guide/component-styles)

#### Q10. With the following component class, what template syntax would you use in the template to display the value of the title class field?

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
- [ ] A class field cannot be displayed in a template via the template syntax.

[Angular.io - String Interpolation or Text Interpolation](https://angular.io/guide/interpolation)

#### Q11. What is the purpose of the valueChanges method on a FormControl?

- [ ] It is used to configure what values are allowed for the control.
- [ ] It is used to change the value of a control to a new value. You would call that method and pass in the new value for the form field. It even supports passing in an array of values that can be set over time.
- [ ] It returns a Boolean based on if the value of the control is different from the value with which it was initialized.
- [x] It is an observable that emits every time the value of the control changes, so you can react to new values and make logic decisions at that time.

[Angular.io - Displaying a from control value](https://angular.io/guide/reactive-forms#displaying-a-form-control-value)

#### Q12. What directive is used to link an `<a>` tag to routing?

- [ ] routeTo
- [x] routerLink
- [ ] routePath
- [ ] appLink

[Angular.io - RouterLink](https://angular.io/api/router/RouterLink#description)

#### Q13. What is the Output decorator used for in this component class?

```ts
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

[Angular.io - Sending data to parent component](https://angular.io/guide/inputs-outputs#sending-data-to-a-parent-component)

#### Q14. What is the difference between these two markup examples for conditionally handling display?

```html
<div *ngIf="isVisible">Active</div>
<div [hidden]="!isVisible">Active</div>
```

- [ ] The `ngIf` is shorthand for the other example. When Angular processes that directive, it writes a div element to the DOM with the hidden property.
- [ ] They are fundamentally the same.
- [x] The `ngIf` directive does not render the div in the DOM if the expression is false. The `hidden` property usage hides the div content in the browser viewport, but the div is still in the DOM.
- [ ] The `ngIf` is valid, but the use of the `hidden` property is wrong and will throw an error.

[StackOverflow](https://stackoverflow.com/a/39778145)

#### Q15. How can you disable the submit button when the form has errors in this template-driven forms example?

```html
<form #userForm="ngForm">
  <input type="text" ngModel name="firstName" required />
  <input type="text" ngModel name="lastName" required />
  <button (click)="submit(userForm.value)">Save</button>
</form>
```

- [ ] A

  ```html
  <button (click)="submit(userForm.value)" disable="userForm.invalid">Save</button>
  ```

- [x] B

  ```html
  <button (click)="submit(userForm.value)" [disabled]="userForm.invalid">Save</button>
  ```

- [ ] C

  ```html
  <button (click)="submit(userForm.value)" [ngForm.disabled]="userForm.valid">Save</button>
  ```

- [ ] D

  ```html
  <button (click)="submit(userForm.value)" *ngIf="userForm.valid">Save</button>
  ```

[Angular.io - Submit the form with ngSubmit](https://angular.io/guide/forms#submit-the-form-with-ngsubmit)

#### Q16. You want to see what files would be generated by creating a new contact-card component. Which command would you use?

- [x] ng generate component contact-card --dry-run
- [ ] ng generate component contact-card --no-files
- [ ] ng generate component component --dry
- [ ] ng generate component --exclude

[Angular.io - ng generate options](https://angular.io/cli/generate#options)

#### Q17. Based on the following component, what template syntax would you use to bind the TitleCardComponent's titleText field to the h1 element title property?

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

#### Q18. What are Angular lifecycle hooks?

- [ ] loggers for tracking the health of an Angular app
- [ ] providers that can be used to track the instances of components
- [ ] built-in pipes that can be used in templates for DOM events
- [x] reserved named methods for components and directives that Angular will call during set times in its execution, and can be used to tap into those lifecycle moments

[Angular.io - Lifecycle hooks](https://angular.io/guide/lifecycle-hooks)

#### Q19. Pick the best description for this template syntax code:

```html
<span>Boss: {{job?.bossName}} </span>
```

- [ ] The ? is shorthand for the async pipe. The job value must be an Observable.
- [x] It is using the safe navigation operator (?) on the job field. If the job field is undefined, the access to the bossName will be ignored and no error will occur.
- [ ] There is an error in the template syntax. The ? is not valid here.
- [ ] It is diplaying the job value if it has one; otherwise it is displaying the bossName.

[StackOverflow](https://stackoverflow.com/a/60182134)

#### Q20. How would you configure a route definition for a UserDetailComponent that supports the URL path user/23 (where 23 represents the id of the requested user)?

- [x] `{ path: 'user/:id', component: UserDetailComponent }`
- [ ] `{ url: 'user/:id', routedComponent: UserDetailComponent }`
- [ ] `{ routedPath: 'user/:id', component: UserDetailComponent }`
- [ ] `{ destination: new UserDetailComponent(), route: 'user/:id' }`

[CodeCraft - Parameterised Routes](https://codecraft.tv/courses/angular/routing/parameterised-routes/#_configuration)

#### Q21. What are the HostListener decorators and the HostBinding decorator doing in this directive?

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

- [x] They are setting the CalloutDirective.fontWeight field based on whether or not the mouse is over the DOM element. The HostListener then sets the font-weight CSS property to the fontWeight value.
- [ ] They are setting up the directive to check the DOM element that it is on. If it has event bindings added for mouse enter and leave it will use this code. Otherwise, nothing will happen.
- [ ] This is an incorrect use of HostListener and HostBinding. The HostListener and HostBinding decorators do not do anything on directives; they work only when used on components.
- [ ] If the DOM element that this directive is placed on has the CSS property font-weight set on it, the mouseenter and mouseleave events will get raised.

[DigitalOcean](https://www.digitalocean.com/community/tutorials/angular-hostbinding-hostlistener)

#### Q22. What Angular template syntax can you use on this template-driven form field to access the field value and check for validation within the template markup?

```html
<input type="text" ngModel name="firstName" required minlength="4" />
<span *ngIf="">Invalid field data</span>
```

- [x] You can make use of a template reference variable and the exportAs feature that the ngModel directive has.
- [ ] You can use the ngModel directive in combination with the input field name.
- [ ] You can use a template reference variable for the HTML input element and then check the valid property off of that.
- [ ] It is not possible to get access to the field value with template-driven forms. You must use reactive forms for that.

1. [Angular.io -Show and hide validation error ](https://angular.io/guide/forms#show-and-hide-validation-error-messages)
2. [Medium](https://medium.com/@agoiabeladeyemi/template-driven-forms-in-angular-4a3a5ad960de)

#### Q23. What is the value type that will be stored in the headerText template reference variable in this markup?

```html
<h1 #headerText>User List</h1>
```

- [x] an Angular ElementRef, a wrapper around a native element
- [ ] the inner text of the `<h1>` element
- [ ] a header component class
- [ ] the native DOM element type of HTMLHeadingElement

[Pluralsight - Template reference variable](https://www.pluralsight.com/guides/how-to-use-template-reference-variables-in-angular)

#### Q24. What is the difference, if any, of the resulting code logic based on these two provider configurations?

```ts
[{ provide: FormattedLogger, useClass: Logger }][{ provide: FormattedLogger, useExisting: Logger }];
```

- [ ] They are the same. Both will result in a new instance of Logger that is bound to the FormattedLogger token.
- [x] The useClass syntax tells the injector to make a new instance of Logger and bind that instance to the FormattedLogger token. The useExisting syntax refers to an already existing object instance declared as Logger.
- [ ] Both of them are wrong. A strong type cannot be used for useClass or useExisting.
- [ ] They are the same. Both will result in the FormattedLogger token being an alias for the instance of Logger.

1. [Angular.io - Dependency Providers](https://angular.io/guide/dependency-injection-providers#defining-providers)
2. [TektutorialHub](https://www.tektutorialshub.com/angular/angular-providers/)

#### Q25. What is the purpose of the data property (seen in the example below) in a route configuration?

```ts
   {
       path: 'customers',
       component: CustomerListComponent,
       data: { accountSection: true }
   }
```

- [ ] a key/value mapping for setting @Input values on the routed component instance
- [x] a way to include static, read-only data associated with the route that can be retrieved from the ActivatedRoute
- [ ] property on the route that can be used to load dynamic data for the route
- [ ] an object that will get auto-injected into the routed component's constructor.

1. [TektutorialsHub](https://www.tektutorialshub.com/angular/angular-pass-data-to-route/#:~:text=Angular%20allows%20us%20to%20pass,of%20the%20history%20state%20object)
2. [StackOverflow](https://stackoverflow.com/a/36835156)

#### Q26. How does the built-in `ngIf` structural directive change the rendered DOM based on this template syntax?

```ts
@Component({
  selector: 'app-product',
  template: '<div *ngIf="product">{{ product.name }}</div>',
})
export class ProductComponent {
  @Input() product;
}
```

- [ ] The `<div>` acts as a placeholder. If the product class field is "truthy," the `<div>` will get replaced by just the `product.name` value; if not, then nothing will be rendered.
- [ ] The `<div>` will always be rendered, and if the product field is "truthy," the `<div>` element will contain the `product.name` value; otherwise, it will render the `<div>` element with no value in it.
- [ ] It produces an error since ngIf is not a built-in structural directive.
- [x] If the product class field is "truthy," then the rendered DOM will include the `<div>` with the value of the `product.name` field. If it is not "truthy,' the rendered DOM will not contain the `<div>` element.

[Reference (angular.io)](https://angular.io/api/common/NgIf)

#### Q27. What does this code accomplish?

```ts
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

[Angular.io - The basic NgModule](https://angular.io/guide/ngmodules#the-basic-ngmodule)

#### Q28. Which choice best describes what the _resolve_ property does in this route configuration?

```ts
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

[angular.io](https://angular.io/api/router/Resolve)

#### Q29. What is the purpose of the ContentChildren decorator in this component class?

```ts
@Component({
 . . .
 template: '<ng-content></ng-content>'
})
export class TabsListComponent {
 @ContentChildren(TabComponent) tabs;
}
```

- [ ] If any _TabsComponent_ elements are added to the _TabsListComponent_ template, they will get put into the `<ng-content>` element at runtime.
- [ ] It creates _TabComponent_ components in the _TabsListComponent_ template when a _TabsListComponent_ is instantiated.
- [x] It provides access from within the component class to any _TabComponent_ components that were content projected into the `<ng-content>` for this component.
- [ ] It restricts the allowed elements that can be put into a _TabsListComponent_ element to allow only _TabComponent_ elements.

[betterprogramming.pub](https://betterprogramming.pub/understanding-contentchildren-with-an-example-e76ce78968db)

#### Q30. In order for Angular to process components in an application, where do the component types need to be registered?

- [ ] within a script tag in the index.html file
- [ ] in a NgModule decorator metadata tag named _components_
- [ ] No registration is needed simply include the component files in an app directory.
- [x] in a NgModule decorator metadata property named _declarations_

[angular.io](https://angular.io/guide/ngmodule-api#ngmodule-metadata)

#### Q31. What is the purpose of the `fixture.detectChanges()` call in this unit test?

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

- [ ] It tracks any potential Ul changes and will fail the unit test if any are made.
- [ ] It is used to ensure component template stability across multiple unit tests in the entire test suite.
- [x] It forces Angular to perform change detection, which will render the _UserCardComponent_ before you can validate its template.
- [ ] It is used to log change-detection events to the console during unit test runs.

[angular.io](https://angular.io/api/core/testing/ComponentFixture#detectChanges)

#### Q32. What will the URL segment look like based on the following call to the `Router.navigate` method when goToUser is passed the value 15?

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

#### Q33. When a service is provided for root and is also added to the provider's configuration for a lazy-loaded module, what instance of that service does the injector provide to constructors in the lazy-loaded module?

- [x] A new instance of that service is created when the module is lazy loaded.
- [ ] Providing a service of the same type at a lazy-loaded module level is not allowed.
- [ ] If an instance of the service has not been created at the root level yet. it will create one there and then use it.
- [ ] A single instance of that service is always instantiated at the root and is the only one ever used, including within lazy modules.

#### Q34. What is the HostBinding decorator doing in this directive?

```ts
@Directive({
  selector: ' [appHighlight] ',
})
export class HighlightDirective {
  @HostBinding('class.highlighted') highlight = true;
}
```

- [x] It is adding the CSS class named highlighted to any DOM element that has the appHighlight directive on it.
- [ ] HostBinding does not do anything on directives, only on components.
- [ ] It specifies that if the host element gets the highlighted class added to its class attribute, then the directive class field highlight will get set to true; and if it is not added on the host it will get set to false.
- [ ] It is creating an inline style on the host element with a CSS property named highlight set to true.

[StackOverflow](https://stackoverflow.com/a/46207423)

#### Q35. In reactive forms, what Angular form class type is used on the native DOM `<form>` element to wire it up?

- [ ] `FormArray`
- [ ] `FormControl`
- [x] `FormGroup`
- [ ] `all of these answers`

#### Q36. Assuming the username FormControl has been configured with a minLength validator, how can you set up an error display in the following reactive forms markup for the username field?

```html
<form [formGroup]="form">
  <input type="text" formControlName="username" />
  ...
</form>
```

- [ ] A

  ```html
  <span *ngIf="username.minLength.invalid"> Username length is not valid </span>
  ```

- [ ] B

  ```html
  <input type="text" formControlName="username" [showMinLength]="true" />
  ```

- [ ] C

  ```html
  <span *ngIf="form.get('username').getError('minLength') as minLengthError">
    Username must be at least {{ minLengthError.requiredLength }} characters.
  </span>
  ```

- [x] D

  ```html
  <input type="text" formControlName="username" #userName="ngModel" />
  <span *ngIf="userName.errors.minlength">
    Username must be at least {{ userName.errors.minlength.requiredLength }} characters.
  </span>
  ```

[Codecraft](https://codecraft.tv/courses/angular/forms/template-driven/)

#### Q37. How does the emulated view encapsulation mode handle CSS for a component?

- [ ] It renders the CSS exactly how you wrote it without any changes.
- [ ] It makes use of shadow DOM markup and CSS.
- [x] It creates unique attributes for DOM elements and scopes the CSS selectors you write to those attribute IDs.
- [ ] It renders all of the CSS rules you write as inline CSS on all of the DOM elements you use in the template.

[Angular.io](https://angular.io/guide/view-encapsulation#inspecting-generated-css)

#### Q38. With the following TestBed setup, what can be used to access the rendered DOM for the UserCardComponent?

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

#### Q39. Given these two components, what will get rendered to the DOM based on the markup usage?

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

- [x] A

  ```html
  <app-card>
    <h1>Data Card</hl>
    <app-bio>
      Been around for four years.
    </app-bio>
  </app-card>
  ```

- [ ] B

  ```html
  <h1>Data Card</h1>
  <app-bio> Been around for four years. </app-bio>
  ```

- [ ] C

  ```html
  <app-card>
    <h1>Data Card</hl>
    <ng-content></ng-content>
    <app-bio>
      Been around for four years.
      <ng-content></ng-content>
    </app-bio>
  </app-card>
  ```

- [ ] D

  ```html
  <app-card>
    <h1>Data Card</hl>
  </app-card>
  ```

#### Q40. Given the app-title-card component in the code below, what DOM will the app-user-card component render?

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

- [x] A

  ```html
  <app-user-card>
    <app-title-card>
      <h1>User Data</h1>
    </app-title-card>
    <p>Jenny Smith</p>
  </app-user-card>
  ```

- [ ] B

  ```html
  <h1>User Data</h1>
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
    <h1 app-title-card>User Data</h1>
    <p>Jenny Smith</p>
  </div>
  ```

#### Q41. Pick the matching code for the custom provider registration that the @Inject () decorator is looking for:

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

#### Q42. Which choice best describes the following usage of the HttpClient.get method in the getsettings class method?

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

- [ ] The RxJs pipe method is an alias for the subscribe method, so a call to `getSettings` will execute the get query. The retry operator is used to tell the pipe call to retry the get query three times.
- [ ] It will produce an error at runtime because the pipe method is not available off of the `Httpclient.get` call.
- [ ] Every single call to the getSettings method will result in the Httpclient making three total get requests to the settingsUrl, which is not ideal because there will always be two extra calls that are not needed. The retry operator should not be used in this manner.
- [x] When the result of the getSettings method is subscribed to, the HTTP GET call will be made; if it fails, it will be retried up to three times before it gives up and returns an error.

1. [learnrxjs.io](https://www.learnrxjs.io/learn-rxjs/operators/error_handling/retry)
2. [dev.to](https://dev.to/gparlakov/how-does-rxjs-retry-work-412p)

#### Q43. When a service requires some setup to initialize its default state through a method, how can you make sure that said method is invoked before the service gets injected anywhere?

- [ ] Put the logic of that service method into the service constructor instead.
- [x] Use a factory provider at the root AppModule level that depends on the service to call that service method.
- [ ] It is not possible to do it at the application start; you can do it only at a component level.
- [ ] Instantiate an instance of the service at the global level (window scope) and then call that method.

1. [Angular.io](https://angular.io/guide/dependency-injection-providers)
2. [Stackoverflow](https://stackoverflow.com/questions/39803876/how-to-use-factory-provider)

#### Q44. What statement best describes this usage of the TestBed?

```ts
const spy = jasmine.createSpyObj('DataService', ['getUsersFromApi']);
TestBed.configureTestingModule({
  providers: [UserService, { provide: DataService, useValue: spy }],
});
const userService = TestBed.get(UserService);
```

- [ ] The TestBed is required anytime you want to make use of a spy object in a unit test for an Angular provider.
- [ ] The TestBed is being used to test a component's view.
- [x] The TestBed scaffolds an NgModule with two providers and handles any dependency injection. If any Angular class requests the DataService in its constructor, the TestBed will inject spy in that constructor.
- [ ] The TestBed is configuring the test runner to tell it to only execute tests for the two providers listed in its providers array.

`All other tests be ignored, including tests that assert results against one of these providers and a non-defined provider.`
`Although it will work when multiple providers in this configuration are asserted against in a single test.`

#### Q45. What is the primary difference between a component and a directive?

- [ ] A component uses a selector metadata property and a directive does not.
- [ ] A directive can be used for adding custom events to the DOM and a component cannot.
- [x] A component has a template and a directive does not.
- [ ] A directive can target only native DOM elements.

[StackOverflow](https://stackoverflow.com/a/34616190)

#### Q46. What could you add to this directive class to allow the truncate length to be set during directive usage in markup?

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

- [x] `@Input() appTruncate: number;`
- [ ] `@Output() appTruncate;`
- [ ] `constructor(maxLength: number) { }`
- [ ] `Nothing. The directive selector cannot be used to pass in values to the directive.`

1. [Angular.io](https://angular.io/guide/attribute-directives#passing-values-into-an-attribute-directive)
2. [StackOverflow](https://stackoverflow.com/a/46303049)

#### Q47. How can you pass query parameters to this `HttpClient.get` request?

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

#### Q48. Assuming the `DataService` has been registered in the providers for the application, which answer best describes what happens based on this component's constructor?

```ts
@Component({
    ...
})
export class OrderHistoryComponent {
    constructor(private dataService: DataService) {}
    ...
}
```

- [ ] It declares that the `OrderHistoryComponent` will have its own version of a `DataService` and that it should never use any existing instances. The `DataService` would need to be instantiated within the class as a private field for this code to be complete and working.
- [x] When Angular creates a new instance of the `OrderHistoryComponent`, the injector will provide an instance of a `DataService` class to the component constructor's first argument. The constructor's `dataService` parameter will be used to set a private instance field with the same name on the instance.
- [ ] It provides a way to do component testing only; the constructor has no usage in the actual run of the Angular application.
- [ ] It enables the custom element that the component targets to have a custom property named `dataService` that can be used to bind an existing `DataService` instance to.

1. [StackOverflow](https://stackoverflow.com/a/49755822)
2. [Angular.io - Dependency Injection](https://angular.io/guide/dependency-injection)

#### Q49. Finish this markup using the `ngIf` directive to implement an else case that will display the text "User is not active":

```html
<div *ngIf="userIsActive; else inactive">Currently active!</div>
```

- [ ] A

  ```html
  <div #inactive>User is not active.</div>
  ```

- [ ] B

  ```html
  <div *ngIf="inactive">User is not active.</div>
  ```

- [ ] C

  ```html
  <ng-template #else="inactive">
    <div>User is not active.</div>
  </ng-template>
  ```

- [x] D

  ```html
  <ng-template #inactive>
    <div>User is not active.</div>
  </ng-template>
  ```

[Angular.io](https://angular.io/api/common/NgIf)

#### Q50. What is the correct syntax for a route definition to lazy load a feature module?

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

#### Q51. Describe how the validation is set up and configured in this reactive forms example:

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

- [ ] The `FormControl` for `username` is getting configured to exclude three validators from the validators that it is allowed to use.
- [ ] The `FormControl` for `username` is getting configured to allow three possible validators to be used: `required, maxLength`, and a custom one named `unique`. To enable these `validators`, a validator directive would need to be put on the form fields in the markup.
- [ ] Validation cannot be set up this way in reactive forms.
- [x] The `FormControl` for `username` is getting configured with three validators: the `required` and `minLength` validators that come from Angular, and a custom validator function named `unique` that checks for the value not equal to the string `admin`.

1. [Angular.io - Form Validation](https://angular.io/guide/form-validation)
2. [Angular University Blog](https://blog.angular-university.io/angular-custom-validators/)

#### Q52. What does the Injectable decorator do on this service class?

```ts
@Injectable({
    providedIn: 'root'
)}
export class DataService { }
```

- [ ] It registers a provider for the service that is available only at the root module level, not to any children modules.
- [x] It registers a provider for the service in the root application injector, making a single instance of it available throughout the application.
- [ ] It makes it so the service can be injected only in the bootstrapped component for the application.
- [ ] It sets up a compile time rule that allows you to put the service type only in the providers metadata property of the root NgModule.

[Angular.io](https://angular.io/guide/providers#providing-a-service)

#### Q53. Describe the usage of this code

```ts
export interface AppSettings {
  title: string;
  version: number;
}
export const APP_SETTINGS = new InjectionToken<AppSettings>('app.settings');
```

- [ ] The InjectionToken adds an instance of the AppSettings to the root provider via the InjectionToken constructor call, making it automatically available to all NgModules, services and components throughout the Angular application without the need to inject it anywhere.
- [x] The InjectionToken is used to create a provider token for a non-class dependency. An Object literal can be provider as a value for the APP_SETTINGS dependency provider type that can then be injected into components, services, etc ..
- [ ] The InjectionToken is used to create a dynamic decorator for the AppSettings that can be used on constructor parameters via an @AppSettings decorator.
- [ ] This code has an error since you cannot use a TypeScript interface for the generic type on the InjectionToken

#### Q54. For the following template-driven forms example, what argument can be passed to the submit method in the click event to submit the data for the form?

```html
<form #form="ngForm">
  <input type="text" ngModel="firstName" /> <input type="text" ngModel="lastName" />
  <button (click)="submit()">Save</button>
</form>
```

- [x] submit(form.value)
- [ ] submit($event)
- [ ] submit(ngForm.value)
- [ ] submit(FirstName, lastName)

#### Q55. What is the purpose of the `prelodingStrategy` property configuration in this router code?

```ts
RouterModule.forRoot(
  ...{
    preloadingStrategy: PreloadAllModules,
  },
);
```

- [ ] It enables the option to flag individual routes for preloading.
- [ ] It preloads all dependencies for routes, creating instances of services when the app first starts up
- [ ] It ensures all modules get built into a single app module bundle file.
- [x] It configures the router to immediately load all routes that have a loadChildren property(routes that are typically loaded when requested)

References:

- [Angular Router, PreloadAllModules](https://angular.io/api/router/PreloadAllModules)
- [Route preloading in Angular](https://web.dev/route-preloading-in-angular/)
- [Preloading strategy](https://www.tektutorialshub.com/angular/angular-preloading-strategy/)
- [Custom preloading strategy](https://www.concretepage.com/angular-2/angular-custom-preloading-strategy#Preloading)
- [Preloading strategy, save loading time](https://medium.com/geekculture/preloading-strategy-in-angularsave-loading-time-ca791074fe28)

#### Q56. What is an alternative way to write this markup to bind the value of the class field `userName` to the `h1` element title property?

```html
<h1 [title]="userName">Current user is {{ userName }}</h1>
```

- [ ] `title="userName"`
- [x] `title="{{ userName }}"`
- [ ] `title="{{ 'userName' }}"`
- [ ] The only way to do it is by using the square brackets.

#### Q57. What is the `async` pipe doing in this example?

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

- [ ] It is doing nothing since the async pipe cannot be used in an `ngFor` statement.
- [ ] It is configuring the `ngFor` iteration to support multiple lists of users at the same time.
- [x] It is subscribing to the observable returned from the `HttpClient.get` method and unwrapping the returned value so it can be iterated over in the `ngFor`.
- [ ] It is allowing all of the users in the `users` field to be rendered concurrently to the DOM.

#### Q58. How would you make use of this directive in markup based on its selector value

```ts
@Directive({  selector: '[appTruncate]'
})
export class TruncateDirective{  . . .
}
```

- [ ] `html <p data-directive="appTruncate">Some long text </p> `
- [x] `html <p appTruncate>Some long text</p> `
- [ ] `html <p app-truncate>Some long text</p> `
- [ ] `html <app-truncate>Some long text</app-truncate> `

#### Q59. What lifecycle hook can be used on a component to monitor all changes to @Input values on that component?

- [ ] ngOnInit
- [ ] ngChanges
- [ ] ngAfterInputChange
- [x] ngOnChanges

[How to detect when an @Input() value changes in Angular?](https://stackoverflow.com/a/44686085/1573267)

#### Q60. What would be an example template syntax usage of this custom pipe?

```ts
@Pipe({ name: 'truncate' })
export class TruncatePipe implements PipeTransform {
  transform(value: string, maxLength: number, showEllipsis: boolean) {
    const newValue = maxLength ? value.substr(0, maxLength) : value;
    return showEllipsis ? '${newValue}...' : newValue;
  }
}
```

- [ ] `{{ 'some long text' | truncate:10 }}`
- [x] `{{ 'some long text' | truncate: 10, true }}`
- [ ] `{{ 'some long text' | truncate }}`
- [ ] all of these answers

[How do I call an Angular 2 pipe with multiple arguments?] (https://stackoverflow.com/questions/36816788/how-do-i-call-an-angular-2-pipe-with-multiple-arguments)

#### Q61. Which Angular CLI command would you run to generate a UsersComponent and add it to the SharedModule (in file shared.module.ts in your application)?

- [ ] ng generate component --newModule=shared
- [x] ng generate component users --module=shared
- [ ] ng generate component users --shared
- [ ] ng generate component --add=shared

#### Q62. How can you rewrite this markup so the div container is not needed in the final DOM render

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

#### Q63. How can you use the template syntax to bind a component class field named tabWidth to an inline style width CSS property on this element?

<div class="tab"></div>

- [ ] <code>{{ width: tabWidth }}</code>
- [ ] [width]="tabWidth"
- [ ] [inline.width]="tabWidth"
- [x] [style.width.px]="tabWidth"

#### Q64. What Angular utilities, if any, are required to unit test a service with no constructor dependencies?

- [ ] By.css() helper method is needed
- [ ] A text fixture is required to run the service for the unit test.
- [ ] None. A service can be instantiated and unit tested on its own.
- [x] The TestBed class is needed to instantiate the service.

[Angular unit tests](https://angular.io/guide/testing-services) - recheck answers

#### Q65. What is the difference between the CanActivate and the CanLoad route guards?

- [ ] CanActivate is used to check access. CanLoad is used to preload data for the route.
- [ ] CanLoad is used at app startup to allow or deny routes to be added to the route table. CanActivate is used to manage access to routes at the time they are requested.
- [ ] CanActivate and CanLoad do the exact same thing.
- [x] CanLoad prevents an entire NgModule from being delivered and loaded. CanActivate stops routing to a component in that NgModule, but that module is still loaded.

[CanActivate vs Canload](https://stackoverflow.com/questions/42026045/difference-between-angulars-canload-and-canactivate#:~:text=canActivate%20is%20used%20to%20prevent,not%20authorized%20to%20do%20so.) CanActivate prevents access on routes, CanLoad prevents lazy loading.

#### Q66. What is the outlet property used for in this router definition object?

```ts
{  path: 'document',  component: DocumentComponent,  outlet: 'document-box'
}
```

- [ ] it will locate all instances of `<document-box>` in the DOM and insert a DocumentComponent element into them on route navigation.
- [ ] It declares that the DocumentComponent can be used as a child to a `<document-box>` element in addition ot being routed to.
- [x] It us used to target a `<router-outlet>` element with the name attribute matching the string value as the location for the DocumentComponent to be rendered when routed to.
- [ ] It is a source of power for the router. (definitely not the answer :P)

[Angular-outlet](https://angular.io/api/router/RouterOutlet) - recheck answer

#### Q67. In this template syntax, every time the items property is changed (added to, removed from, etc.), the ngFor structural directive re-runs its logic for all DOM elements in the loop. What syntax can be used to make this more performant?

```html
<div *ngFor="let item of items">{{ item.id }} - {{ item.name }}</div>
```

- [ ] `*ngFor="let item of items; let uniqueItem"`
- [ ] `*ngFor="let item of items.distinct()"`
- [ ] `*ngFor="let item of items: let i = index"`
- [x] `*ngFor="let item of items; trackBy: trackById"`

[StackOverflow - How to use `trackBy` with `ngFor`](https://stackoverflow.com/a/58025894)

#### Q68. What does this Angular CLI command do?

```bash
ng build --configuration=production --progress=false
```

- [ ] It builds the Angular application, setting the build configuration to the "production" target specified in the angular.json file, and logs progress output to the console.
- [ ] It builds the Angular application, setting the build configuration to the "production" target specified in the angular.json file, and watching files for changes.
- [ ] It builds the Angular application, setting the build configuration to the "production" target specified in the angular.json file, and disables watching files for changes.
- [x] It builds the Angular application, setting the build configuration to the "production" target specified in the angular.json file, and prevents progress output to the console.

[Angular documentation - `ng build`](https://angular.io/cli/build#:~:text=%2D%2D-,progress,-Log%20progress%20to)

#### Q69. Service classes can be registered as providers via which decorators?

- [ ] @Injectable, @NgModule, @Component, and @Directive.
- [x] @Injectable only.
- [ ] @Injectable and @NgModule only.
- [ ] @Service and @NgModule only.

#### Q70. What is the Input decorator used for in this component class?

```ts
@Component({  selector:'app-product-name',  ...
})
export class ProductNameComponent {  @Input() productName: string
}
```

- [ ] It is used simply to put a comment in front of a class field for documentation.
- [x] It provides a way to bind values to the productName field by using the component selector.
- [ ] It autogenerates an `html
<input type='text' id='productName'>` Dom element in the component template.
- [ ] It provides a way to bind values to the productName instance field,just like native DOM element property bindings.
      [Angular documentation - `Input()`](https://angular.io/guide/inputs-outputs)

#### Q71. Which route guard can be used to mediate navigation to a route?

- [x] all of these answers.
- [ ] CanDeactivate.
- [ ] CanLoad
- [ ] CanActivate.
      [Angular documentation - `Input()`](https://angular.io/guide/inputs-outputs)

#### Q72. How can you configure the injector to use an existing object for a token instead of having it instantiate a class instance?

- [x] Use the `useValue` provider configuration and set that equal to an existing object or an object literal.
- [ ] It is not possible. Providers can be configured only with class types.
- [ ] Simply add the object instance or literal to the provider's array.
- [ ] Make use of the `asValue` provider configuration property, setting it to true.

[Configuring dependency providers](https://angular.io/guide/dependency-injection-providers)

#### Q73. Based on this route definition, what can be injected into UserDetailComponent constructor to get ahold of the id route parameter?

```ts
{path: 'user/:id', component: UserDetailComponent }
```

- [x] ActivatedRoute
- [ ] CurrentRoute
- [ ] UrlPath
- [ ] @Inject('id')

[Common Routing Tasks](https://angular.io/guide/router#observable-parammap-and-component-reuse)

#### Q74. With the following reactive form markup, what would you add to wire up a call to an onSubmit class method?

```html
<form [formGroup]="form">
  <input type="text" formControlName="username" />
  <button type="submit" [disabled]="form. invalid">Submit</button>
</form>
```

- [ ] neither of these answers
- [ ] Add (click)="onSubmit()" to the `<button>` element.
- [x] Add (ngSubmit )="onSubmit ()" to the `<form>` element.
- [ ] both of these answers

[Angular - Forms](https://angular.io/guide/forms)

#### Q75. What is the expected DOM code for this usage of the ngClass attribute directive when isActive is true?

```html
<div [ngClass]="{ ‘active-item': isActive }">Item One</div>
```

- [ ] `<div active-item>Item One</div>`
- [x] `<div class="active-item">Item One</div>`
- [ ] `<div class="is-active">Item One</div>`
- [ ] `<div class="active-item isActive">Item One</div>`

[Angular - NgClass](https://angular.io/api/common/NgClass)

#### Q76. Which answer best explains the usage of ngModel in this template code?

```html
<input [(ngModel)]="user.name" />
```

- [ ] It is conditionally displaying the input element if the user.name property has a value.
- [x] It is the two-way data binding syntax. The input element value property will be bound to the user.name property, and the value change event for the form element will update the user.name property value.
- [ ] There is a typo in the code. It should have only the square brackets.
- [ ] It is binding the value of the user.name property to the input element's val property to set its initial value.

[Angular - NgModel](https://angular.io/api/forms/NgModel)

#### Q77. NgModules can be included within other NgModules. Which code sample should you use to include TableModule in the SharedModule?

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

#### Q78. What other template syntax (replacing the ngClass directive) can be used to add or remove the CSS class names in this markup?

```html
<span [ngClass]="{ 'active': isActive, 'can-toggle': canToggle }"> Employed </span>
```

- [ ] A

  ```html
  <span class="{{ isActive ? 'is-active' : '' }} {{ canToggle ? 'can-toggle' : '' }}">
    Employed
  </span>
  ```

- [x] B

  ```html
  <span [class.active]="isActive" [class.can-toggle]="canToggle"> Employed </span>
  ```

- [ ] C

  ```html
  <span [styles.class.active]="isActive" [styles.class.can-toggle]="canToggle"> Employed </span>
  ```

- [ ] D

  ```html
  <span [css.class.active]="isActive" [css.class.can-toggle]="canToggle"> Employed </span>
  ```

#### Q79. In this directive decorator example, what is the purpose of the multi property in the provider object literal?

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

- [ ] It indicates that the CustomValidatorDirective can be used on multiple form element types.
- [ ] It allows for multiple instances of the CustomValidatorDirective to be instantiated. Without multi, the CustomValidatorDirective would be a singleton for the entire app.
- [x] It allows the registration of different providers for the single NG_VALIDATORS token. In this case, it is adding the CustomValidatorDirective to the list of form validators available.
- [ ] It indicates that there will be multiple classes that handle the logic implementation for the custom validator.

[StackOverflow](https://stackoverflow.com/questions/38144641/what-is-multi-provider-in-angular2)

#### Q80. Which Angular CLI command would you use to run your unit tests in a process that reruns your test suite on file changes?

- [ ] ng test --single-run=false
- [ ] ng test --watch-files
- [ ] ng test --progress
- [x] ng test

#### Q81. What is the most common use for the ngOnDestory lifecle hook?

- [ ] Remove dome elements from the components's view
- [ ] Delete any injected services the
- [x] Unsubscribe from observables and detach
- [ ] All of the above

#### Q82. What NgModule decorator metadata property is leverage to allow other ....?

- [ ] public
- [ ] experts
- [ ] Shared
- [x] declarations

#### Q83. With the following component class, what template syntax would you use in the template to display the result of calling the currentYear class function?

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
- [ ] Class functions cannot be called from template syntax.

#### Q84. What is the purpose of Angular's `@Input()` decorator?

- [ ] To define output events
- [x] To pass data from parent to child component
- [ ] To inject services
- [ ] To define component metadata

**Explanation:**
The `@Input()` decorator marks a class property as an input property, allowing data to flow from a parent component to a child component through property binding.

[Reference](https://angular.io/api/core/Input)

#### Q85. What is the purpose of Angular's `@Output()` decorator?

- [ ] To receive data from parent
- [x] To emit custom events from child to parent component
- [ ] To output data to console
- [ ] To define component outputs

**Explanation:**
The `@Output()` decorator marks a class property as an output property, typically an EventEmitter, allowing a child component to emit custom events to its parent.

[Reference](https://angular.io/api/core/Output)

#### Q86. What is Angular's change detection strategy `OnPush`?

- [ ] Pushes changes to the server
- [x] Only checks component when inputs change or events occur
- [ ] Pushes notifications to users
- [ ] Always checks for changes

**Explanation:**
`OnPush` change detection strategy tells Angular to only check the component when its input properties change or when an event originates from the component, improving performance.

[Reference](https://angular.io/api/core/ChangeDetectionStrategy)

#### Q87. What is the purpose of Angular's `async` pipe?

- [ ] To make HTTP requests
- [x] To automatically subscribe and unsubscribe from Observables in templates
- [ ] To create async functions
- [ ] To handle promises

**Explanation:**
The `async` pipe subscribes to an Observable or Promise and returns the latest value it has emitted. It automatically unsubscribes when the component is destroyed, preventing memory leaks.

[Reference](https://angular.io/api/common/AsyncPipe)

#### Q88. What is Angular's `ViewChild` decorator used for?

- [ ] To create child components
- [x] To access a child component, directive, or DOM element from the parent
- [ ] To view child routes
- [ ] To display child templates

**Explanation:**
`@ViewChild` is a property decorator that configures a view query, allowing you to access a child component, directive, or DOM element from the parent component class.

[Reference](https://angular.io/api/core/ViewChild)

#### Q89. What is the difference between `ViewChild` and `ContentChild`?

- [x] ViewChild queries the view, ContentChild queries projected content
- [ ] ViewChild is faster
- [ ] ContentChild is deprecated
- [ ] There is no difference

**Explanation:**
`@ViewChild` queries elements in the component's own template, while `@ContentChild` queries elements projected into the component via `<ng-content>`.

[Reference](https://angular.io/api/core/ContentChild)

#### Q90. What is Angular's `NgZone` used for?

- [ ] To create zones in the UI
- [x] To execute code inside or outside Angular's change detection zone
- [ ] To manage time zones
- [ ] To create security zones

**Explanation:**
`NgZone` allows you to execute code inside or outside Angular's zone, which controls when change detection runs. Running code outside the zone can improve performance for operations that don't need change detection.

[Reference](https://angular.io/api/core/NgZone)

#### Q91. What is Angular's `Renderer2` used for?

- [ ] To render HTML
- [x] To safely manipulate DOM elements without directly accessing them
- [ ] To render components
- [ ] To create renderers

**Explanation:**
`Renderer2` provides a safe way to manipulate DOM elements, working across different platforms (browser, server, web worker) and maintaining security.

[Reference](https://angular.io/api/core/Renderer2)

#### Q92. What is Angular's `HostListener` decorator?

- [ ] To listen to host events
- [x] To listen to events on the host element of a directive or component
- [ ] To create event listeners
- [ ] To host listeners

**Explanation:**
`@HostListener` decorator allows you to listen to events on the host element (the element the directive is applied to) from within the directive or component class.

[Reference](https://angular.io/api/core/HostListener)

#### Q93. What is Angular's `HostBinding` decorator?

- [ ] To bind hosts
- [x] To bind a host element property to a directive/component property
- [ ] To create bindings
- [ ] To host bindings

**Explanation:**
`@HostBinding` decorator allows you to bind properties of the host element to properties of the directive or component class.

[Reference](https://angular.io/api/core/HostBinding)

#### Q94. What is Angular's `trackBy` function used for in `*ngFor`?

- [ ] To track user behavior
- [x] To improve performance by tracking items by a unique identifier
- [ ] To track changes
- [ ] To create tracking

**Explanation:**
The `trackBy` function helps Angular track which items have changed, been added, or removed in an `*ngFor` loop, significantly improving performance by reducing DOM manipulations.

[Reference](https://angular.io/api/common/NgForOf#properties)

#### Q95. What is Angular's `ng-content` used for?

- [ ] To create content
- [x] To project content from parent into child component template
- [ ] To display content
- [ ] To manage content

**Explanation:**
`<ng-content>` is used for content projection (transclusion), allowing you to insert content from a parent component into a child component's template.

[Reference](https://angular.io/guide/content-projection)

#### Q96. What is Angular's `ng-template` used for?

- [ ] To create templates
- [x] To define template fragments that can be instantiated programmatically
- [ ] To display templates
- [ ] To manage templates

**Explanation:**
`<ng-template>` defines a template that is not rendered by default but can be instantiated programmatically using directives like `*ngIf`, `*ngFor`, or `ViewContainerRef`.

[Reference](https://angular.io/api/core/ng-template)

#### Q97. What is Angular's `ng-container` used for?

- [ ] To contain components
- [x] To group elements without adding extra DOM nodes
- [ ] To create containers
- [ ] To manage containers

**Explanation:**
`<ng-container>` is a logical container that doesn't render as a DOM element, useful for grouping elements or applying structural directives without adding extra markup.

[Reference](https://angular.io/api/core/ng-container)

#### Q98. What is Angular's `TemplateRef` used for?

- [ ] To reference templates
- [x] To represent an embedded template that can be used to instantiate views
- [ ] To create template references
- [ ] To manage templates

**Explanation:**
`TemplateRef` represents an embedded template (like `<ng-template>`) that can be used to create embedded views programmatically.

[Reference](https://angular.io/api/core/TemplateRef)

#### Q99. What is Angular's `ViewContainerRef` used for?

- [ ] To view containers
- [x] To dynamically create and insert components or templates
- [ ] To reference views
- [ ] To manage containers

**Explanation:**
`ViewContainerRef` represents a container where one or more views can be attached, allowing dynamic creation and insertion of components or templates.

[Reference](https://angular.io/api/core/ViewContainerRef)

#### Q100. What is Angular's `ComponentFactoryResolver` used for?

- [ ] To resolve component factories
- [x] To dynamically create component instances (deprecated in Angular 13+)
- [ ] To create factories
- [ ] To manage components

**Explanation:**
`ComponentFactoryResolver` was used to dynamically create component instances. In Angular 13+, it's deprecated in favor of using `ViewContainerRef.createComponent()` directly.

[Reference](https://angular.io/api/core/ComponentFactoryResolver)

#### Q101. What is Angular's standalone components feature?

- [ ] Components that stand alone
- [x] Components that don't need to be declared in NgModules
- [ ] Independent components
- [ ] Isolated components

**Explanation:**
Standalone components (Angular 14+) can be used without being declared in an NgModule, simplifying the component architecture and reducing boilerplate.

[Reference](https://angular.io/guide/standalone-components)

#### Q102. What is Angular's `inject()` function?

- [ ] To inject dependencies
- [x] A function-based dependency injection alternative to constructor injection
- [ ] To create injections
- [ ] To manage injections

**Explanation:**
The `inject()` function (Angular 14+) allows dependency injection in contexts where constructor injection isn't available, like in factory functions or field initializers.

[Reference](https://angular.io/api/core/inject)

#### Q103. What is Angular's `DestroyRef` used for?

- [ ] To destroy references
- [x] To register cleanup callbacks when a component/directive is destroyed
- [ ] To manage destruction
- [ ] To create destroy references

**Explanation:**
`DestroyRef` (Angular 16+) provides a way to register cleanup callbacks that run when a component or directive is destroyed, offering a cleaner alternative to `ngOnDestroy`.

[Reference](https://angular.io/api/core/DestroyRef)

#### Q104. What is Angular's `takeUntilDestroyed` operator?

- [ ] To take until destroyed
- [x] An RxJS operator that automatically unsubscribes when component is destroyed
- [ ] To manage subscriptions
- [ ] To destroy observables

**Explanation:**
`takeUntilDestroyed` (Angular 16+) is an RxJS operator that automatically completes an observable when the component/directive is destroyed, preventing memory leaks.

[Reference](https://angular.io/api/core/rxjs-interop/takeUntilDestroyed)

#### Q105. What is Angular's `Signal` feature?

- [ ] To send signals
- [x] A reactive primitive for managing state with fine-grained reactivity
- [ ] To create signals
- [ ] To manage signals

**Explanation:**
Signals (Angular 16+) are a new reactive primitive that provides fine-grained reactivity, allowing Angular to track dependencies and update only what's necessary.

[Reference](https://angular.io/guide/signals)

#### Q106. What is Angular's `computed()` function?

- [ ] To compute values
- [x] To create derived signals that automatically update when dependencies change
- [ ] To perform computations
- [ ] To calculate values

**Explanation:**
`computed()` creates a read-only signal that derives its value from other signals, automatically recomputing when dependencies change.

[Reference](https://angular.io/guide/signals#computed-signals)

#### Q107. What is Angular's `effect()` function?

- [ ] To create effects
- [x] To run side effects when signals change
- [ ] To manage effects
- [ ] To apply effects

**Explanation:**
`effect()` runs a side effect function whenever any signal it reads changes, useful for operations like logging, analytics, or DOM manipulation.

[Reference](https://angular.io/guide/signals#effects)

#### Q108. What is Angular's `HttpClient` used for?

- [ ] To create HTTP clients
- [x] To make HTTP requests to backend services
- [ ] To manage clients
- [ ] To handle HTTP

**Explanation:**
`HttpClient` is Angular's service for making HTTP requests, providing a simplified API for common HTTP operations with built-in support for observables.

[Reference](https://angular.io/api/common/http/HttpClient)

#### Q109. What is Angular's `HttpInterceptor` used for?

- [ ] To intercept HTTP
- [x] To intercept and modify HTTP requests and responses
- [ ] To create interceptors
- [ ] To manage HTTP

**Explanation:**
`HttpInterceptor` allows you to intercept HTTP requests and responses, useful for adding authentication headers, logging, error handling, or caching.

[Reference](https://angular.io/api/common/http/HttpInterceptor)

#### Q110. What is Angular's `ActivatedRoute` used for?

- [ ] To activate routes
- [x] To access information about the currently active route
- [ ] To create routes
- [ ] To manage routes

**Explanation:**
`ActivatedRoute` provides access to information about the route associated with a component, including route parameters, query parameters, and data.

[Reference](https://angular.io/api/router/ActivatedRoute)

#### Q111. What is Angular's `Router` service used for?

- [ ] To route traffic
- [x] To navigate between views and manage routing
- [ ] To create routers
- [ ] To handle routing

**Explanation:**
The `Router` service provides navigation and URL manipulation capabilities, allowing programmatic navigation and access to routing state.

[Reference](https://angular.io/api/router/Router)

#### Q112. What is Angular's route guards used for?

- [ ] To guard routes
- [x] To control access to routes based on conditions
- [ ] To protect routes
- [ ] To manage guards

**Explanation:**
Route guards (`CanActivate`, `CanDeactivate`, etc.) are interfaces that allow you to control navigation to and from routes based on custom logic like authentication.

[Reference](https://angular.io/guide/router#preventing-unauthorized-access)

#### Q113. What is Angular's `CanActivate` guard?

- [ ] To activate components
- [x] To determine if a route can be activated
- [ ] To enable routes
- [ ] To activate guards

**Explanation:**
`CanActivate` is a route guard that determines whether a route can be activated, commonly used for authentication and authorization checks.

[Reference](https://angular.io/api/router/CanActivate)

#### Q114. What is Angular's lazy loading?

- [ ] Slow loading
- [x] Loading feature modules on demand rather than at startup
- [ ] Delayed loading
- [ ] Lazy initialization

**Explanation:**
Lazy loading allows you to load feature modules only when they're needed, reducing initial bundle size and improving application startup time.

[Reference](https://angular.io/guide/lazy-loading-ngmodules)

#### Q115. What is Angular's `preloadingStrategy`?

- [ ] To preload strategies
- [x] To define how and when to preload lazy-loaded modules
- [ ] To create preloading
- [ ] To manage loading

**Explanation:**
Preloading strategies determine how lazy-loaded modules are preloaded in the background, balancing initial load time with subsequent navigation speed.

[Reference](https://angular.io/api/router/PreloadingStrategy)

#### Q116. What is Angular's `FormControl` used for?

- [ ] To control forms
- [x] To track the value and validation status of an individual form control
- [ ] To create controls
- [ ] To manage forms

**Explanation:**
`FormControl` tracks the value and validation status of an individual form control, providing methods to update, validate, and observe changes.

[Reference](https://angular.io/api/forms/FormControl)

#### Q117. What is Angular's `FormGroup` used for?

- [ ] To group forms
- [x] To track the value and validity of a group of FormControl instances
- [ ] To create groups
- [ ] To manage forms

**Explanation:**
`FormGroup` aggregates the values and validation status of a collection of `FormControl` instances, representing a form or a section of a form.

[Reference](https://angular.io/api/forms/FormGroup)

#### Q118. What is Angular's `FormArray` used for?

- [ ] To create arrays
- [x] To track the value and validity of an array of FormControl instances
- [ ] To manage arrays
- [ ] To group controls

**Explanation:**
`FormArray` tracks the value and validity of an array of `FormControl`, `FormGroup`, or `FormArray` instances, useful for dynamic forms.

[Reference](https://angular.io/api/forms/FormArray)

#### Q119. What is the difference between template-driven and reactive forms?

- [x] Template-driven uses directives, reactive uses explicit form models
- [ ] Template-driven is faster
- [ ] Reactive forms are deprecated
- [ ] There is no difference

**Explanation:**
Template-driven forms rely on directives in the template, while reactive forms use explicit form models created in the component class, offering more control and testability.

[Reference](https://angular.io/guide/forms-overview)

#### Q120. What is Angular's `Validators` class used for?

- [ ] To validate data
- [x] To provide built-in validation functions for forms
- [ ] To create validators
- [ ] To manage validation

**Explanation:**
The `Validators` class provides a set of built-in validators (required, minLength, email, etc.) that can be used with reactive forms.

[Reference](https://angular.io/api/forms/Validators)

#### Q121. What is Angular's custom validator?

- [ ] A validator you customize
- [x] A function that implements the ValidatorFn interface for custom validation logic
- [ ] A built-in validator
- [ ] A validation service

**Explanation:**
Custom validators are functions that implement the `ValidatorFn` interface, allowing you to create custom validation logic for your forms.

[Reference](https://angular.io/guide/form-validation#defining-custom-validators)

#### Q122. What is Angular's `AsyncValidator`?

- [ ] An async validator
- [x] A validator that performs asynchronous validation like server-side checks
- [ ] A fast validator
- [ ] A delayed validator

**Explanation:**
`AsyncValidator` performs asynchronous validation, useful for checks that require server communication like username availability.

[Reference](https://angular.io/api/forms/AsyncValidator)

#### Q123. What is Angular's `@NgModule` decorator?

- [ ] To create modules
- [x] To define an Angular module with its dependencies and components
- [ ] To import modules
- [ ] To manage modules

**Explanation:**
`@NgModule` decorator marks a class as an Angular module and provides metadata about the module's components, directives, pipes, and dependencies.

[Reference](https://angular.io/api/core/NgModule)

#### Q124. What is Angular's `providedIn` property?

- [ ] To provide in modules
- [x] To specify where a service should be provided (root, module, or component)
- [ ] To create providers
- [ ] To manage injection

**Explanation:**
`providedIn` in the `@Injectable` decorator specifies where the service should be provided, with 'root' making it a singleton available throughout the app.

[Reference](https://angular.io/api/core/Injectable#providedIn)

#### Q125. What is Angular's tree-shakeable providers?

- [ ] Providers that shake trees
- [x] Services that can be removed from the bundle if not used
- [ ] Removable providers
- [ ] Shakeable services

**Explanation:**
Tree-shakeable providers (using `providedIn: 'root'`) allow unused services to be removed from the production bundle, reducing bundle size.

[Reference](https://angular.io/guide/providers#tree-shakable-providers)

#### Q126. What is Angular's `InjectionToken`?

- [ ] A token for injection
- [x] A token used to inject non-class dependencies
- [ ] An injection key
- [ ] A dependency token

**Explanation:**
`InjectionToken` creates a token that can be used to inject non-class dependencies like configuration objects or primitive values.

[Reference](https://angular.io/api/core/InjectionToken)

#### Q127. What is Angular's `forRoot()` pattern?

- [ ] For root modules
- [x] A pattern to configure a module and its providers for the root injector
- [ ] To create roots
- [ ] To manage roots

**Explanation:**
The `forRoot()` static method is a convention for configuring a module and its providers to be used in the root module, typically for singleton services.

[Reference](https://angular.io/guide/singleton-services#the-forroot-pattern)

#### Q128. What is Angular's `forChild()` pattern?

- [ ] For child modules
- [x] A pattern to configure a module for lazy-loaded feature modules
- [ ] To create children
- [ ] To manage children

**Explanation:**
The `forChild()` static method configures a module for use in lazy-loaded feature modules, typically providing routing configuration without duplicating services.

[Reference](https://angular.io/guide/singleton-services#prevent-reimport-of-the-greetingmodule)

#### Q129. What is Angular's `APP_INITIALIZER` token?

- [ ] To initialize apps
- [x] To run initialization logic before the app starts
- [ ] To create initializers
- [ ] To manage initialization

**Explanation:**
`APP_INITIALIZER` is a multi-provider token that allows you to run initialization logic (like loading configuration) before the application starts.

[Reference](https://angular.io/api/core/APP_INITIALIZER)

#### Q130. What is Angular's `PLATFORM_ID` token?

- [ ] A platform identifier
- [x] To identify the platform where the app is running (browser, server, etc.)
- [ ] A platform key
- [ ] A platform token

**Explanation:**
`PLATFORM_ID` is an injection token that identifies the platform where the Angular application is running, useful for platform-specific code.

[Reference](https://angular.io/api/core/PLATFORM_ID)

#### Q131. What is Angular's `isPlatformBrowser()` function?

- [ ] To check if it's a browser
- [x] To determine if the app is running in a browser environment
- [ ] To detect browsers
- [ ] To validate platforms

**Explanation:**
`isPlatformBrowser()` checks if the application is running in a browser environment, useful for conditionally executing browser-specific code.

[Reference](https://angular.io/api/common/isPlatformBrowser)

#### Q132. What is Angular Universal?

- [ ] A universal framework
- [x] Server-side rendering (SSR) for Angular applications
- [ ] A universal module
- [ ] A global service

**Explanation:**
Angular Universal enables server-side rendering of Angular applications, improving initial load time and SEO.

[Reference](https://angular.io/guide/universal)

#### Q133. What is Angular's `TransferState` used for?

- [ ] To transfer states
- [x] To transfer state from server to client in SSR applications
- [ ] To manage state
- [ ] To create transfers

**Explanation:**
`TransferState` allows you to transfer state from the server-rendered application to the client application, avoiding duplicate HTTP requests.

[Reference](https://angular.io/api/platform-browser/TransferState)

#### Q134. What is Angular's `Meta` service used for?

- [ ] For metadata
- [x] To add, update, and remove HTML meta tags
- [ ] To create meta tags
- [ ] To manage metadata

**Explanation:**
The `Meta` service allows you to programmatically add, update, and remove HTML meta tags, useful for SEO and social media sharing.

[Reference](https://angular.io/api/platform-browser/Meta)

#### Q135. What is Angular's `Title` service used for?

- [ ] To create titles
- [x] To get and set the document title
- [ ] To manage titles
- [ ] To display titles

**Explanation:**
The `Title` service provides methods to get and set the HTML document title, useful for dynamic page titles.

[Reference](https://angular.io/api/platform-browser/Title)

#### Q136. What is Angular's `@Pipe` decorator?

- [ ] To create pipes
- [x] To define a pipe for transforming data in templates
- [ ] To manage pipes
- [ ] To apply pipes

**Explanation:**
`@Pipe` decorator marks a class as a pipe and provides metadata about the pipe, including its name and whether it's pure or impure.

[Reference](https://angular.io/api/core/Pipe)

#### Q137. What is the difference between pure and impure pipes?

- [x] Pure pipes only execute when input values change, impure pipes execute on every change detection
- [ ] Pure pipes are faster
- [ ] Impure pipes are deprecated
- [ ] There is no difference

**Explanation:**
Pure pipes (default) only execute when input values change, while impure pipes execute on every change detection cycle, which can impact performance.

[Reference](https://angular.io/guide/pipes#pure-and-impure-pipes)

#### Q138. What is Angular's `DatePipe` used for?

- [ ] To create dates
- [x] To format dates according to locale rules
- [ ] To manage dates
- [ ] To parse dates

**Explanation:**
`DatePipe` formats date values according to locale rules, providing various format options for displaying dates.

[Reference](https://angular.io/api/common/DatePipe)

#### Q139. What is Angular's `CurrencyPipe` used for?

- [ ] To create currency
- [x] To format numbers as currency according to locale rules
- [ ] To manage currency
- [ ] To convert currency

**Explanation:**
`CurrencyPipe` formats numbers as currency according to locale rules, including currency symbol and decimal places.

[Reference](https://angular.io/api/common/CurrencyPipe)

#### Q140. What is Angular's `DecimalPipe` used for?

- [ ] To create decimals
- [x] To format numbers with decimal points according to locale rules
- [ ] To manage decimals
- [ ] To round numbers

**Explanation:**
`DecimalPipe` formats numbers with decimal points according to locale rules, allowing specification of minimum and maximum decimal places.

[Reference](https://angular.io/api/common/DecimalPipe)

#### Q141. What is Angular's `PercentPipe` used for?

- [ ] To calculate percentages
- [x] To format numbers as percentages according to locale rules
- [ ] To create percentages
- [ ] To manage percentages

**Explanation:**
`PercentPipe` formats numbers as percentages according to locale rules, multiplying the value by 100 and appending the percent symbol.

[Reference](https://angular.io/api/common/PercentPipe)

#### Q142. What is Angular's `JsonPipe` used for?

- [ ] To parse JSON
- [x] To convert objects to JSON strings for display
- [ ] To create JSON
- [ ] To manage JSON

**Explanation:**
`JsonPipe` converts a value into its JSON-string representation, useful for debugging and displaying object structures.

[Reference](https://angular.io/api/common/JsonPipe)

#### Q143. What is Angular's `SlicePipe` used for?

- [ ] To slice arrays
- [x] To create a subset of an array or string
- [ ] To cut data
- [ ] To manage slices

**Explanation:**
`SlicePipe` creates a new array or string containing a subset of the elements, similar to JavaScript's `Array.prototype.slice()`.

[Reference](https://angular.io/api/common/SlicePipe)
