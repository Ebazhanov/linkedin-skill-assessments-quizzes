## Angular

#### 问题1. 在这个组件类中，ViewChild 装饰器的作用是什么？

```ts
@Component({
    ...
    template: '<p #bio></p>'
})
export class UserDetailsComponent {
    @ViewChild('bio') bio;
}
```

- [x] 它提供了从组件类内部访问具有 bio 模板引用变量的 `<p>` 标签的 ElementRef 对象的能力。
- [ ] 它表示 `<p>` 标签被渲染为使用此组件的父视图的子元素。
- [ ] 它使模板中的 `<p>` 标签支持内容投影。
- [ ] 它使 `<p>` 标签在最终渲染中可见。如果在模板中使用了 #bio 但在类中没有使用 @ViewChild，那么 Angular 会自动隐藏带有 #bio 的 `<p>` 标签。

[DigitalOcean - viewchild-access-component](https://www.digitalocean.com/community/tutorials/angular-viewchild-access-component)

#### 问题2. 在响应式表单中，使用什么方法将 FormControl 连接到原生 DOM input 元素？

- [ ] 在 `<form>` 元素上添加一个名为 controls 的属性，并将 FormControl 的字符串名称赋给它，以指示应该包含哪些字段。
- [ ] 在 DOM 元素的 value 属性周围使用方括号绑定语法，并将其设置为 FormControl 的实例。
- [x] 使用 formControlName 指令，并将值设置为 FormControl 的字符串名称。
- [ ] 使用 FormControl 的字符串名称作为 DOM 元素 id 属性的值。

[Angular.io - Reactive Form Groups](https://angular.io/guide/reactive-forms#creating-nested-form-groups)

#### 问题3. ActivatedRoute 类上的 `paramMap` 和 `queryParamMap` 有什么区别？

- [ ] paramMap 是路由 URL 路径中参数的对象字面量。queryParamMap 是这些相同参数的 Observable。
- [ ] paramMap 是一个包含路由 URL 路径中参数值的 Observable。queryParamMap 是一个接受键数组的方法，用于在 paramMap 中查找特定参数。
- [ ] paramMap 是 Angular 3 的遗留名称。新名称是 queryParamMap。
- [x] 两者都是包含请求路由 URL 字符串值的 Observable。paramMap 包含 URL 路径中的参数值，queryParamMap 包含 URL 查询参数。

[StackOverflow](https://stackoverflow.com/a/49617621)

#### 问题4. 基于以下 async 管道的使用，假设 users 类字段是一个 Observable，对 users Observable 进行了多少次订阅？

```html
<h2>姓名</h2>
<div *ngFor="let user of users | async">{{ user.name }}</div>
<h2>年龄</h2>
<div *ngFor="let user of users | async">{{ user.age }}</div>
<h2>性别</h2>
<div *ngFor="let user of users | async">{{ user.gender }}</div>
```

- [ ] 没有。async 管道不会自动订阅。
- [ ] 没有。模板语法不正确。
- [x] 三次。每个 async 管道都有一次订阅。
- [ ] 一次。async 管道在内部按类型缓存 Observable。

[UltimateCourses](https://ultimatecourses.com/blog/angular-ngfor-async-pipe)

#### 问题5. 如何在 OrderService 的 addOrder 函数中使用 HttpClient 向端点发送 POST 请求？

```ts
export class OrderService {
  constructor(private httpClient: HttpClient) {}

  addOrder(order: Order) {
    // 缺少的代码行
  }
}
```

- [ ] `this.httpClient.url(this.orderUrl).post(order);`
- [ ] `this.httpClient.send(this.orderUrl, order);`
- [ ] `this.httpClient.post<Order>(this.orderUrl, order);`
- [x] `this.httpClient.post<Order>(this.orderUrl, order).subscribe();`

[Angular.io - Sending data to server](https://angular.io/guide/http#sending-data-to-a-server)

#### 问题6. RouterModule.forRoot 方法用于什么？

- [ ] 注册您打算在路由组件中使用的任何提供者。
- [x] 在根应用程序级别注册路由定义。
- [ ] 指示 Angular 应该为您的路由的成功加油。
- [ ] 声明您打算仅在根级别使用路由。

[O'REILLY](https://www.oreilly.com/library/view/switching-to-angular/9781788620703/c9e90774-0e10-410b-bd20-d3e9e0b8d117.xhtml)

#### 问题7. 此组件元数据选择器将匹配哪些 DOM 元素？

```ts
@Component({
    selector: 'app-user-card',
    . . .
})
```

- [ ] 任何具有 app-user-card 属性的元素，例如 `<div app-user-card></div>`。
- [ ] `<app-user-card></app-user-card>` 的第一个实例。
- [x] `<app-user-card></app-user-card>` 的所有实例。
- [ ] `<user-card></user-card>` 的所有实例。

[Angular.io - Component Metadata](https://angular.io/guide/architecture-components#component-metadata)

#### 问题8. 使用内置的 ngFor 结构指令渲染 productNames 列表的正确模板语法是什么？

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

#### 问题9. 用于为组件设置 CSS 样式的两个组件装饰器元数据属性是什么？

- [ ] viewEncapsulation 和 viewEncapsulationFiles。
- [ ] 只有一个，它是名为 css 的属性。
- [ ] css 和 cssUrl。
- [x] styles 和 styleUrls。

[Angular.io - Component Styles](https://angular.io/guide/component-styles)

#### 问题10. 对于以下组件类，您将在模板中使用什么模板语法来显示 title 类字段的值？

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
- [ ] 类字段无法通过模板语法在模板中显示。

[Angular.io - String Interpolation or Text Interpolation](https://angular.io/guide/interpolation)

#### 问题11. FormControl 上的 valueChanges 方法的目的是什么？

- [ ] 它用于配置控件允许的值。
- [ ] 它用于将控件的值更改为新值。您可以调用该方法并传入表单字段的新值。它甚至支持传入可以随时间设置的值数组。
- [ ] 它根据控件的值是否与初始化时的值不同返回一个布尔值。
- [x] 它是一个 observable，每次控件值更改时都会发出，因此您可以响应新值并在那时做出逻辑决策。

[Angular.io - Displaying a from control value](https://angular.io/guide/reactive-forms#displaying-a-form-control-value)

#### 问题12. 使用什么指令将 `<a>` 标签链接到路由？

- [ ] routeTo
- [x] routerLink
- [ ] routePath
- [ ] appLink

[Angular.io - RouterLink](https://angular.io/api/router/RouterLink#description)

#### 问题13. 在此组件类中，Output 装饰器用于什么？

```ts
@Component({
    selector: 'app-shopping-cart',
    . . .
})
export class ShoppingCartComponent {
    @Output() itemTotalChanged = new EventEmitter();
}
```

- [ ] 它使 `itemTotalChanged` 类字段成为公共的。
- [ ] 它提供了一种将值绑定到 `itemTotalChanged` 类字段的方法，如：`<app-shopping-cart [itemTotalChanged]="newTotal"></app-shopping-cart>`。
- [x] 它提供了一种将事件绑定到 `itemTotalChanged` 类字段的方法，如：`<app-shopping-cart (itemTotalChanged)="logNewTotal($event)"></app-shopping-cart>`。
- [ ] 它只是在类字段前面放置注释以进行文档记录的一种方式。

[Angular.io - Sending data to parent component](https://angular.io/guide/inputs-outputs#sending-data-to-a-parent-component)

#### 问题14. 这两个标记示例在条件处理显示方面有什么区别？

```html
<div *ngIf="isVisible">Active</div>
<div [hidden]="!isVisible">Active</div>
```

- [ ] `ngIf` 是另一个示例的简写。当 Angular 处理该指令时，它会向 DOM 写入一个具有 hidden 属性的 div 元素。
- [ ] 它们基本上是相同的。
- [x] 如果表达式为 false，`ngIf` 指令不会在 DOM 中渲染 div。`hidden` 属性用法在浏览器视口中隐藏 div 内容，但 div 仍然在 DOM 中。
- [ ] `ngIf` 是有效的，但 `hidden` 属性的使用是错误的，会抛出错误。

[StackOverflow](https://stackoverflow.com/a/39778145)

#### 问题15. 在这个模板驱动表单示例中，当表单有错误时，如何禁用提交按钮？

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

#### 问题16. 您想查看创建新的 contact-card 组件会生成哪些文件。您会使用哪个命令？

- [x] ng generate component contact-card --dry-run
- [ ] ng generate component contact-card --no-files
- [ ] ng generate component component --dry
- [ ] ng generate component --exclude

[Angular.io - ng generate options](https://angular.io/cli/generate#options)

#### 问题17. 基于以下组件，您将使用什么模板语法将 TitleCardComponent 的 titleText 字段绑定到 h1 元素的 title 属性？

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

#### 问题18. 什么是 Angular 生命周期钩子？

- [ ] 用于跟踪 Angular 应用程序健康状况的日志记录器
- [ ] 可用于跟踪组件实例的提供者
- [ ] 可在模板中用于 DOM 事件的内置管道
- [x] 为组件和指令保留的命名方法，Angular 会在其执行的设定时间调用这些方法，可用于挖掘这些生命周期时刻

[Angular.io - Lifecycle hooks](https://angular.io/guide/lifecycle-hooks)

#### 问题19. 为此模板语法代码选择最佳描述：

```html
<span>Boss: {{job?.bossName}} </span>
```

- [ ] ? 是 async 管道的简写。job 值必须是 Observable。
- [x] 它在 job 字段上使用安全导航操作符（?）。如果 job 字段未定义，对 bossName 的访问将被忽略，不会发生错误。
- [ ] 模板语法中有错误。? 在这里无效。
- [ ] 如果它有值，它会显示 job 值；否则它会显示 bossName。

[StackOverflow](https://stackoverflow.com/a/60182134)

#### 问题20. 您如何配置支持 URL 路径 user/23（其中 23 表示请求用户的 id）的 UserDetailComponent 的路由定义？

- [x] `{ path: 'user/:id', component: UserDetailComponent }`
- [ ] `{ url: 'user/:id', routedComponent: UserDetailComponent }`
- [ ] `{ routedPath: 'user/:id', component: UserDetailComponent }`
- [ ] `{ destination: new UserDetailComponent(), route: 'user/:id' }`

[CodeCraft - Parameterised Routes](https://codecraft.tv/courses/angular/routing/parameterised-routes/#_configuration)

#### 问题21. 此指令中的 HostListener 装饰器和 HostBinding 装饰器在做什么？

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

- [x] 它们根据鼠标是否悬停在 DOM 元素上来设置 CalloutDirective.fontWeight 字段。然后 HostListener 将 font-weight CSS 属性设置为 fontWeight 值。
- [ ] 它们正在设置指令以检查它所在的 DOM 元素。如果它为鼠标进入和离开添加了事件绑定，它将使用此代码。否则，什么都不会发生。
- [ ] 这是 HostListener 和 HostBinding 的错误用法。HostListener 和 HostBinding 装饰器在指令上不执行任何操作；它们仅在组件上使用时才起作用。
- [ ] 如果此指令所在的 DOM 元素设置了 CSS 属性 font-weight，则会引发 mouseenter 和 mouseleave 事件。

[DigitalOcean](https://www.digitalocean.com/community/tutorials/angular-hostbinding-hostlistener)

#### 问题22. 在此模板驱动表单字段上，您可以使用什么 Angular 模板语法来访问字段值并在模板标记中检查验证？

```html
<input type="text" ngModel name="firstName" required minlength="4" />
<span *ngIf="">Invalid field data</span>
```

- [x] 您可以使用模板引用变量和 ngModel 指令具有的 exportAs 功能。
- [ ] 您可以将 ngModel 指令与输入字段名称结合使用。
- [ ] 您可以为 HTML input 元素使用模板引用变量，然后检查其 valid 属性。
- [ ] 使用模板驱动表单无法访问字段值。您必须为此使用响应式表单。

1. [Angular.io -Show and hide validation error ](https://angular.io/guide/forms#show-and-hide-validation-error-messages)
2. [Medium](https://medium.com/@agoiabeladeyemi/template-driven-forms-in-angular-4a3a5ad960de)

#### 问题23. 在此标记中，headerText 模板引用变量将存储什么值类型？

```html
<h1 #headerText>User List</h1>
```

- [x] Angular ElementRef，原生元素的包装器
- [ ] `<h1>` 元素的内部文本
- [ ] header 组件类
- [ ] 原生 DOM 元素类型 HTMLHeadingElement

[Pluralsight - Template reference variable](https://www.pluralsight.com/guides/how-to-use-template-reference-variables-in-angular)

#### 问题24. 基于这两个提供者配置，结果代码逻辑有什么区别（如果有的话）？

```ts
[{ provide: FormattedLogger, useClass: Logger }][{ provide: FormattedLogger, useExisting: Logger }];
```

- [ ] 它们是相同的。两者都将导致绑定到 FormattedLogger 令牌的 Logger 新实例。
- [x] useClass 语法告诉注入器创建 Logger 的新实例并将该实例绑定到 FormattedLogger 令牌。useExisting 语法引用已声明为 Logger 的现有对象实例。
- [ ] 两者都是错误的。强类型不能用于 useClass 或 useExisting。
- [ ] 它们是相同的。两者都将导致 FormattedLogger 令牌成为 Logger 实例的别名。

1. [Angular.io - Dependency Providers](https://angular.io/guide/dependency-injection-providers#defining-providers)
2. [TektutorialHub](https://www.tektutorialshub.com/angular/angular-providers/)

#### 问题25. 路由配置中的 data 属性（如下例所示）的目的是什么？

```ts
   {
       path: 'customers',
       component: CustomerListComponent,
       data: { accountSection: true }
   }
```

- [ ] 用于在路由组件实例上设置 @Input 值的键/值映射
- [x] 一种包含与路由关联的静态只读数据的方法，可以从 ActivatedRoute 检索
- [ ] 路由上的属性，可用于为路由加载动态数据
- [ ] 一个将自动注入到路由组件构造函数中的对象。

1. [TektutorialsHub](https://www.tektutorialshub.com/angular/angular-pass-data-to-route/#:~:text=Angular%20allows%20us%20to%20pass,of%20the%20history%20state%20object)
2. [StackOverflow](https://stackoverflow.com/a/36835156)

#### 问题26. 基于此模板语法，内置的 `ngIf` 结构指令如何更改渲染的 DOM？

```ts
@Component({
  selector: 'app-product',
  template: '<div *ngIf="product">{{ product.name }}</div>',
})
export class ProductComponent {
  @Input() product;
}
```

- [ ] `<div>` 充当占位符。如果 product 类字段为"真值"，`<div>` 将被仅 `product.name` 值替换；如果不是，则不会渲染任何内容。
- [ ] `<div>` 将始终被渲染，如果 product 字段为"真值"，`<div>` 元素将包含 `product.name` 值；否则，它将渲染没有值的 `<div>` 元素。
- [ ] 它会产生错误，因为 ngIf 不是内置的结构指令。
- [x] 如果 product 类字段为"真值"，则渲染的 DOM 将包含带有 `product.name` 字段值的 `<div>`。如果不是"真值"，渲染的 DOM 将不包含 `<div>` 元素。

[Reference (angular.io)](https://angular.io/api/common/NgIf)

#### 问题27. 这段代码完成了什么？

```ts
@NgModule({
  declarations: [AppComponent],
  imports: [BrowserModule],
  bootstrap: [AppComponent],
})
export class AppModule {}

platformBrowserDynamic().bootstrapModule(AppModule);
```

- [ ] 它为 NgModule 执行单元测试。
- [ ] 它提供了一种编写 Angular 应用程序文档结构的方法。@NgModule 是一种内联代码注释形式，被 TypeScript 编译器忽略，但会在代码编辑器应用程序中以特殊格式显示。
- [ ] 它声明了一个名为 AppModule 的 Angular 模块，并使其在整个应用程序中可用于延迟加载。
- [x] 它声明了一个名为 AppModule 的 Angular 模块，其中包含一个名为 AppComponent 的引导组件。然后它将该模块注册到 Angular，以便应用程序可以启动。

[Angular.io - The basic NgModule](https://angular.io/guide/ngmodules#the-basic-ngmodule)

#### 问题28. 在此路由配置中，_resolve_ 属性的作用是什么？

```ts
{
   path: ':id',
   component: UserComponent,
   resolve: {
     user: UserResolverService
   }
}
```

- [x] 在加载 _UserComponent_ 之前，路由器将订阅 _UserResolverService_ 中 _resolve_ 方法返回的 _Observable_。此技术可用于获取 _route_ 的预加载数据。
- [ ] 在 _route_ 完成解析后，组件被加载并渲染，_UserResolverService_ 将运行一个名为 _user_ 的方法，该方法将清理任何打开的数据连接。
- [ ] 有错误。正确的属性名称是 _onResolve_。
- [ ] _UserComponent_ 的构造函数中将有一个 _user_ 参数，_router_ 将处理从 _UserResolverService_ 中的 _user_ 方法调用注入该值。

[angular.io](https://angular.io/api/router/Resolve)

#### 问题29. 在此组件类中，ContentChildren 装饰器的目的是什么？

```ts
@Component({
 . . .
 template: '<ng-content></ng-content>'
})
export class TabsListComponent {
 @ContentChildren(TabComponent) tabs;
}
```

- [ ] 如果将任何 _TabsComponent_ 元素添加到 _TabsListComponent_ 模板，它们将在运行时被放入 `<ng-content>` 元素中。
- [ ] 当 _TabsListComponent_ 实例化时，它会在 _TabsListComponent_ 模板中创建 _TabComponent_ 组件。
- [x] 它提供了从组件类内部访问已内容投影到此组件的 `<ng-content>` 中的任何 _TabComponent_ 组件的能力。
- [ ] 它限制可以放入 _TabsListComponent_ 元素的允许元素，只允许 _TabComponent_ 元素。

[betterprogramming.pub](https://betterprogramming.pub/understanding-contentchildren-with-an-example-e76ce78968db)

#### 问题30. 为了让 Angular 处理应用程序中的组件，组件类型需要在哪里注册？

- [ ] 在 index.html 文件的 script 标签中
- [ ] 在名为 _components_ 的 NgModule 装饰器元数据标签中
- [ ] 不需要注册，只需将组件文件包含在 app 目录中即可。
- [x] 在名为 _declarations_ 的 NgModule 装饰器元数据属性中

[angular.io](https://angular.io/guide/ngmodule-api#ngmodule-metadata)

#### 问题31. 在此单元测试中，`fixture.detectChanges()` 调用的目的是什么？

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

- [ ] 它跟踪任何潜在的 UI 更改，如果进行了任何更改，将使单元测试失败。
- [ ] 它用于确保整个测试套件中多个单元测试的组件模板稳定性。
- [x] 它强制 Angular 执行变更检测，这将在您验证模板之前渲染 _UserCardComponent_。
- [ ] 它用于在单元测试运行期间将变更检测事件记录到控制台。

[angular.io](https://angular.io/api/core/testing/ComponentFixture#detectChanges)

#### 问题32. 当 goToUser 传递值 15 时，基于以下对 `Router.navigate` 方法的调用，URL 段将是什么样子？

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

#### 问题33. 当为 root 提供服务并且还将其添加到延迟加载模块的提供者配置时，注入器向延迟加载模块中的构造函数提供该服务的什么实例？

- [x] 当模块延迟加载时，将创建该服务的新实例。
- [ ] 不允许在延迟加载的模块级别提供相同类型的服务。
- [ ] 如果尚未在根级别创建服务实例，它将在那里创建一个，然后使用它。
- [ ] 该服务的单个实例始终在根处实例化，并且是唯一使用的实例，包括在延迟模块中。

#### 问题34. 此指令中的 HostBinding 装饰器在做什么？

```ts
@Directive({
  selector: ' [appHighlight] ',
})
export class HighlightDirective {
  @HostBinding('class.highlighted') highlight = true;
}
```

- [x] 它将名为 highlighted 的 CSS 类添加到任何具有 appHighlight 指令的 DOM 元素。
- [ ] HostBinding 在指令上不执行任何操作，仅在组件上执行。
- [ ] 它指定如果宿主元素的 class 属性添加了 highlighted 类，则指令类字段 highlight 将设置为 true；如果未在宿主上添加，它将设置为 false。
- [ ] 它在宿主元素上创建内联样式，CSS 属性名为 highlight，设置为 true。

[StackOverflow](https://stackoverflow.com/a/46207423)

#### 问题35. 在响应式表单中，在原生 DOM `<form>` 元素上使用什么 Angular 表单类类型来连接它？

- [ ] `FormArray`
- [ ] `FormControl`
- [x] `FormGroup`
- [ ] `所有这些答案`

#### 问题36. 假设 username FormControl 已配置了 minLength 验证器，您如何在以下响应式表单标记中为 username 字段设置错误显示？

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

#### 问题37. 仿真视图封装模式如何处理组件的 CSS？

- [ ] 它完全按照您编写的方式渲染 CSS，无需任何更改。
- [ ] 它使用 shadow DOM 标记和 CSS。
- [x] 它为 DOM 元素创建唯一属性，并将您编写的 CSS 选择器范围限定到这些属性 ID。
- [ ] 它将您编写的所有 CSS 规则渲染为在模板中使用的所有 DOM 元素上的内联 CSS。

[Angular.io](https://angular.io/guide/view-encapsulation#inspecting-generated-css)

#### 问题38. 使用以下 TestBed 设置，可以使用什么来访问 UserCardComponent 的渲染 DOM？

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

#### 问题39. 给定这两个组件，基于标记用法，将向 DOM 渲染什么？

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

// 标记用法：
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

#### 问题40. 给定下面代码中的 app-title-card 组件，app-user-card 组件将渲染什么 DOM？

```ts
@Component({
   selector: 'app-user-card',
   template: '<app-title-card></app-title-card><p>Jenny Smith</p>'
})

@Component({
   selector: 'app-title-card',
   template: '<h1>User Data</hl>'
})

// 在父组件 html 中使用 user card 组件
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

#### 问题41. 为 @Inject() 装饰器正在寻找的自定义提供者注册选择匹配的代码：

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

#### 问题42. 在 getsettings 类方法中，以下 HttpClient.get 方法的使用描述最准确的是哪个？

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

- [ ] RxJs pipe 方法是 subscribe 方法的别名，因此对 `getSettings` 的调用将执行 get 查询。retry 操作符用于告诉 pipe 调用重试 get 查询三次。
- [ ] 它将在运行时产生错误，因为 pipe 方法在 `Httpclient.get` 调用之后不可用。
- [ ] 每次调用 getSettings 方法都将导致 Httpclient 向 settingsUrl 发出总共三次 get 请求，这并不理想，因为总会有两次额外的不需要的调用。不应以这种方式使用 retry 操作符。
- [x] 当订阅 getSettings 方法的结果时，将进行 HTTP GET 调用；如果失败，它将在放弃并返回错误之前重试最多三次。

1. [learnrxjs.io](https://www.learnrxjs.io/learn-rxjs/operators/error_handling/retry)
2. [dev.to](https://dev.to/gparlakov/how-does-rxjs-retry-work-412p)

#### 问题43. 当服务需要通过方法进行一些设置以初始化其默认状态时，如何确保在服务被注入到任何地方之前调用该方法？

- [ ] 将该服务方法的逻辑放入服务构造函数中。
- [x] 在根 AppModule 级别使用依赖于服务的工厂提供者来调用该服务方法。
- [ ] 无法在应用程序启动时执行此操作；您只能在组件级别执行此操作。
- [ ] 在全局级别（window 范围）实例化服务实例，然后调用该方法。

1. [Angular.io](https://angular.io/guide/dependency-injection-providers)
2. [Stackoverflow](https://stackoverflow.com/questions/39803876/how-to-use-factory-provider)

#### 问题44. 哪个语句最能描述 TestBed 的这种用法？

```ts
const spy = jasmine.createSpyObj('DataService', ['getUsersFromApi']);
TestBed.configureTestingModule({
  providers: [UserService, { provide: DataService, useValue: spy }],
});
const userService = TestBed.get(UserService);
```

- [ ] 每当您想在 Angular 提供者的单元测试中使用 spy 对象时，都需要 TestBed。
- [ ] TestBed 正在用于测试组件的视图。
- [x] TestBed 使用两个提供者搭建 NgModule 并处理任何依赖注入。如果任何 Angular 类在其构造函数中请求 DataService，TestBed 将在该构造函数中注入 spy。
- [ ] TestBed 正在配置测试运行器，以告诉它仅执行其 providers 数组中列出的两个提供者的测试。

`所有其他测试都将被忽略，包括针对这些提供者之一和未定义提供者进行断言的测试。`
`尽管在单个测试中针对此配置中的多个提供者进行断言时它会起作用。`

#### 问题45. 组件和指令之间的主要区别是什么？

- [ ] 组件使用选择器元数据属性，而指令不使用。
- [ ] 指令可用于向 DOM 添加自定义事件，而组件不能。
- [x] 组件有模板，而指令没有。
- [ ] 指令只能针对原生 DOM 元素。

[StackOverflow](https://stackoverflow.com/a/34616190)

#### 问题46. 您可以向此指令类添加什么以允许在标记中使用指令时设置截断长度？

```ts
@Directive({
    selector: '[appTruncate]'
})
export class TruncateDirective {
    . . .
}

// 期望用法示例：
<p [appTruncate]="10">Some very long text here</p>
```

- [x] `@Input() appTruncate: number;`
- [ ] `@Output() appTruncate;`
- [ ] `constructor(maxLength: number) { }`
- [ ] `无。指令选择器不能用于将值传递给指令。`

1. [Angular.io](https://angular.io/guide/attribute-directives#passing-values-into-an-attribute-directive)
2. [StackOverflow](https://stackoverflow.com/a/46303049)

#### 问题47. 如何将查询参数传递给此 `HttpClient.get` 请求？

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

#### 问题48. 假设 `DataService` 已在应用程序的提供者中注册，基于此组件的构造函数，哪个答案最能描述会发生什么？

```ts
@Component({
    ...
})
export class OrderHistoryComponent {
    constructor(private dataService: DataService) {}
    ...
}
```

- [ ] 它声明 `OrderHistoryComponent` 将拥有自己的 `DataService` 版本，并且永远不应使用任何现有实例。`DataService` 需要在类中实例化为私有字段，此代码才能完整且正常工作。
- [x] 当 Angular 创建 `OrderHistoryComponent` 的新实例时，注入器将向组件构造函数的第一个参数提供 `DataService` 类的实例。构造函数的 `dataService` 参数将用于在实例上设置同名的私有实例字段。
- [ ] 它提供了一种仅进行组件测试的方法；构造函数在 Angular 应用程序的实际运行中没有用途。
- [ ] 它使组件目标的自定义元素具有名为 `dataService` 的自定义属性，可用于绑定现有的 `DataService` 实例。

1. [StackOverflow](https://stackoverflow.com/a/49755822)
2. [Angular.io - Dependency Injection](https://angular.io/guide/dependency-injection)

#### 问题49. 使用 `ngIf` 指令完成此标记以实现 else 情况，该情况将显示文本"User is not active"：

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

#### 问题50. 延迟加载功能模块的路由定义的正确语法是什么？

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

#### 问题51. 描述此响应式表单示例中如何设置和配置验证：

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

- [ ] `username` 的 `FormControl` 正在配置为从允许使用的验证器中排除三个验证器。
- [ ] `username` 的 `FormControl` 正在配置为允许使用三个可能的验证器：`required, maxLength` 和名为 `unique` 的自定义验证器。要启用这些 `validators`，需要在标记的表单字段上放置验证器指令。
- [ ] 无法以这种方式在响应式表单中设置验证。
- [x] `username` 的 `FormControl` 正在配置三个验证器：来自 Angular 的 `required` 和 `minLength` 验证器，以及名为 `unique` 的自定义验证器函数，该函数检查值不等于字符串 `admin`。

1. [Angular.io - Form Validation](https://angular.io/guide/form-validation)
2. [Angular University Blog](https://blog.angular-university.io/angular-custom-validators/)

#### 问题52. Injectable 装饰器在此服务类上做什么？

```ts
@Injectable({
    providedIn: 'root'
)}
export class DataService { }
```

- [ ] 它为服务注册一个提供者，该提供者仅在根模块级别可用，而不适用于任何子模块。
- [x] 它在根应用程序注入器中为服务注册一个提供者，使其单个实例在整个应用程序中可用。
- [ ] 它使服务只能在应用程序的引导组件中注入。
- [ ] 它设置了一个编译时规则，允许您仅将服务类型放在根 NgModule 的 providers 元数据属性中。

[Angular.io](https://angular.io/guide/providers#providing-a-service)

#### 问题53. 描述此代码的用法

```ts
export interface AppSettings {
  title: string;
  version: number;
}
export const APP_SETTINGS = new InjectionToken<AppSettings>('app.settings');
```

- [ ] InjectionToken 通过 InjectionToken 构造函数调用将 AppSettings 的实例添加到根提供者，使其在整个 Angular 应用程序中自动可用于所有 NgModules、服务和组件，而无需在任何地方注入它。
- [x] InjectionToken 用于为非类依赖项创建提供者令牌。对象字面量可以作为 APP_SETTINGS 依赖提供者类型的值提供，然后可以注入到组件、服务等中。
- [ ] InjectionToken 用于为 AppSettings 创建动态装饰器，可以通过 @AppSettings 装饰器在构造函数参数上使用。
- [ ] 此代码有错误，因为您不能在 InjectionToken 上使用 TypeScript 接口作为泛型类型

#### 问题54. 对于以下模板驱动表单示例，可以将什么参数传递给点击事件中的 submit 方法以提交表单数据？

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

#### 问题55. 此路由器代码中 `prelodingStrategy` 属性配置的目的是什么？

```ts
RouterModule.forRoot(
  ...{
    preloadingStrategy: PreloadAllModules,
  },
);
```

- [ ] 它启用了标记单个路由进行预加载的选项。
- [ ] 它预加载路由的所有依赖项，在应用程序首次启动时创建服务实例
- [ ] 它确保所有模块都构建到单个应用程序模块包文件中。
- [x] 它配置路由器立即加载具有 loadChildren 属性的所有路由（通常在请求时加载的路由）

参考：

- [Angular Router, PreloadAllModules](https://angular.io/api/router/PreloadAllModules)
- [Route preloading in Angular](https://web.dev/route-preloading-in-angular/)
- [Preloading strategy](https://www.tektutorialshub.com/angular/angular-preloading-strategy/)
- [Custom preloading strategy](https://www.concretepage.com/angular-2/angular-custom-preloading-strategy#Preloading)
- [Preloading strategy, save loading time](https://medium.com/geekculture/preloading-strategy-in-angularsave-loading-time-ca791074fe28)

#### 问题56. 编写此标记以将类字段 `userName` 的值绑定到 `h1` 元素 title 属性的替代方法是什么？

```html
<h1 [title]="userName">Current user is {{ userName }}</h1>
```

- [ ] `title="userName"`
- [x] `title="{{ userName }}"`
- [ ] `title="{{ 'userName' }}"`
- [ ] 唯一的方法是使用方括号。

#### 问题57. 在此示例中，`async` 管道在做什么？

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

- [ ] 它什么都不做，因为 async 管道不能在 `ngFor` 语句中使用。
- [ ] 它配置 `ngFor` 迭代以同时支持多个用户列表。
- [x] 它订阅从 `HttpClient.get` 方法返回的 observable，并解包返回的值，以便可以在 `ngFor` 中进行迭代。
- [ ] 它允许 `users` 字段中的所有用户同时渲染到 DOM。

#### 问题58. 基于其选择器值，您将如何在标记中使用此指令

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

#### 问题59. 可以在组件上使用什么生命周期钩子来监视该组件上所有 @Input 值的所有更改？

- [ ] ngOnInit
- [ ] ngChanges
- [ ] ngAfterInputChange
- [x] ngOnChanges

[How to detect when an @Input() value changes in Angular?](https://stackoverflow.com/a/44686085/1573267)

#### 问题60. 此自定义管道的模板语法用法示例是什么？

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
- [ ] 所有这些答案

[How do I call an Angular 2 pipe with multiple arguments?] (https://stackoverflow.com/questions/36816788/how-do-i-call-an-angular-2-pipe-with-multiple-arguments)

#### 问题61. 您将运行哪个 Angular CLI 命令来生成 UsersComponent 并将其添加到 SharedModule（在应用程序的 shared.module.ts 文件中）？

- [ ] ng generate component --newModule=shared
- [x] ng generate component users --module=shared
- [ ] ng generate component users --shared
- [ ] ng generate component --add=shared

#### 问题62. 如何重写此标记，以便在最终 DOM 渲染中不需要 div 容器

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

#### 问题63. 如何使用模板语法将名为 tabWidth 的组件类字段绑定到此元素上的内联样式 width CSS 属性？

<div class="tab"></div>

- [ ] <code>{{ width: tabWidth }}</code>
- [ ] [width]="tabWidth"
- [ ] [inline.width]="tabWidth"
- [x] [style.width.px]="tabWidth"

#### 问题64. 对没有构造函数依赖项的服务进行单元测试需要哪些 Angular 实用程序（如果有）？

- [ ] 需要 By.css() 辅助方法
- [ ] 需要文本 fixture 才能为单元测试运行服务。
- [ ] 无。可以自行实例化服务并进行单元测试。
- [x] 需要 TestBed 类来实例化服务。

[Angular unit tests](https://angular.io/guide/testing-services) - 重新检查答案

#### 问题65. CanActivate 和 CanLoad 路由守卫之间有什么区别？

- [ ] CanActivate 用于检查访问权限。CanLoad 用于为路由预加载数据。
- [ ] CanLoad 在应用程序启动时使用，以允许或拒绝将路由添加到路由表。CanActivate 用于在请求路由时管理对路由的访问。
- [ ] CanActivate 和 CanLoad 完全做同样的事情。
- [x] CanLoad 防止整个 NgModule 被交付和加载。CanActivate 停止路由到该 NgModule 中的组件，但该模块仍然被加载。

[CanActivate vs Canload](https://stackoverflow.com/questions/42026045/difference-between-angulars-canload-and-canactivate#:~:text=canActivate%20is%20used%20to%20prevent,not%20authorized%20to%20do%20so.) CanActivate 阻止访问路由，CanLoad 阻止延迟加载。

#### 问题66. 在此路由器定义对象中，outlet 属性用于什么？

```ts
{  path: 'document',  component: DocumentComponent,  outlet: 'document-box'
}
```

- [ ] 它将定位 DOM 中所有 `<document-box>` 的实例，并在路由导航时将 DocumentComponent 元素插入其中。
- [ ] 它声明 DocumentComponent 除了可以路由到之外，还可以用作 `<document-box>` 元素的子元素。
- [x] 它用于以 name 属性与字符串值匹配的 `<router-outlet>` 元素为目标，作为路由到时渲染 DocumentComponent 的位置。
- [ ] 它是路由器的动力源。（绝对不是答案 :P）

[Angular-outlet](https://angular.io/api/router/RouterOutlet) - 重新检查答案

#### 问题67. 在此模板语法中，每次更改 items 属性（添加、删除等）时，ngFor 结构指令都会为循环中的所有 DOM 元素重新运行其逻辑。可以使用什么语法使其更高效？

```html
<div *ngFor="let item of items">{{ item.id }} - {{ item.name }}</div>
```

- [ ] `*ngFor="let item of items; let uniqueItem"`
- [ ] `*ngFor="let item of items.distinct()"`
- [ ] `*ngFor="let item of items: let i = index"`
- [x] `*ngFor="let item of items; trackBy: trackById"`

[StackOverflow - How to use `trackBy` with `ngFor`](https://stackoverflow.com/a/58025894)

#### 问题68. 此 Angular CLI 命令做什么？

```bash
ng build --configuration=production --progress=false
```

- [ ] 它构建 Angular 应用程序，将构建配置设置为 angular.json 文件中指定的"production"目标，并将进度输出记录到控制台。
- [ ] 它构建 Angular 应用程序，将构建配置设置为 angular.json 文件中指定的"production"目标，并监视文件的更改。
- [ ] 它构建 Angular 应用程序，将构建配置设置为 angular.json 文件中指定的"production"目标，并禁用监视文件的更改。
- [x] 它构建 Angular 应用程序，将构建配置设置为 angular.json 文件中指定的"production"目标，并阻止进度输出到控制台。

[Angular documentation - `ng build`](https://angular.io/cli/build#:~:text=%2D%2D-,progress,-Log%20progress%20to)

#### 问题69. 服务类可以通过哪些装饰器注册为提供者？

- [ ] @Injectable, @NgModule, @Component 和 @Directive。
- [x] 仅 @Injectable。
- [ ] 仅 @Injectable 和 @NgModule。
- [ ] 仅 @Service 和 @NgModule。

#### 问题70. 在此组件类中，Input 装饰器用于什么？

```ts
@Component({  selector:'app-product-name',  ...
})
export class ProductNameComponent {  @Input() productName: string
}
```

- [ ] 它只是用于在类字段前面放置注释以进行文档记录。
- [x] 它提供了一种通过使用组件选择器将值绑定到 productName 字段的方法。
- [ ] 它在组件模板中自动生成 `html
<input type='text' id='productName'>` Dom 元素。
- [ ] 它提供了一种将值绑定到 productName 实例字段的方法，就像原生 DOM 元素属性绑定一样。
      [Angular documentation - `Input()`](https://angular.io/guide/inputs-outputs)

#### 问题71. 哪个路由守卫可用于调解导航到路由？

- [x] 所有这些答案。
- [ ] CanDeactivate。
- [ ] CanLoad
- [ ] CanActivate。
      [Angular documentation - `Input()`](https://angular.io/guide/inputs-outputs)

#### 问题72. 如何配置注入器使用现有对象作为令牌，而不是让它实例化类实例？

- [x] 使用 `useValue` 提供者配置，并将其设置为现有对象或对象字面量。
- [ ] 不可能。提供者只能配置类类型。
- [ ] 只需将对象实例或字面量添加到提供者的数组中。
- [ ] 使用 `asValue` 提供者配置属性，将其设置为 true。

[Configuring dependency providers](https://angular.io/guide/dependency-injection-providers)

#### 问题73. 基于此路由定义，可以将什么注入到 UserDetailComponent 构造函数中以获取 id 路由参数？

```ts
{path: 'user/:id', component: UserDetailComponent }
```

- [x] ActivatedRoute
- [ ] CurrentRoute
- [ ] UrlPath
- [ ] @Inject('id')

[Common Routing Tasks](https://angular.io/guide/router#observable-parammap-and-component-reuse)

#### 问题74. 使用以下响应式表单标记，您将添加什么来连接对 onSubmit 类方法的调用？

```html
<form [formGroup]="form">
  <input type="text" formControlName="username" />
  <button type="submit" [disabled]="form. invalid">Submit</button>
</form>
```

- [ ] 这两个答案都不是
- [ ] 将 (click)="onSubmit()" 添加到 `<button>` 元素。
- [x] 将 (ngSubmit )="onSubmit ()" 添加到 `<form>` 元素。
- [ ] 这两个答案都是

[Angular - Forms](https://angular.io/guide/forms)

#### 问题75. 当 isActive 为 true 时，ngClass 属性指令的这种用法的预期 DOM 代码是什么？

```html
<div [ngClass]="{ 'active-item': isActive }">Item One</div>
```

- [ ] `<div active-item>Item One</div>`
- [x] `<div class="active-item">Item One</div>`
- [ ] `<div class="is-active">Item One</div>`
- [ ] `<div class="active-item isActive">Item One</div>`

[Angular - NgClass](https://angular.io/api/common/NgClass)

#### 问题76. 哪个答案最能解释此模板代码中 ngModel 的用法？

```html
<input [(ngModel)]="user.name" />
```

- [ ] 如果 user.name 属性有值，它会有条件地显示 input 元素。
- [x] 它是双向数据绑定语法。input 元素 value 属性将绑定到 user.name 属性，表单元素的 value change 事件将更新 user.name 属性值。
- [ ] 代码中有错字。它应该只有方括号。
- [ ] 它将 user.name 属性的值绑定到 input 元素的 val 属性以设置其初始值。

[Angular - NgModel](https://angular.io/api/forms/NgModel)

#### 问题77. NgModules 可以包含在其他 NgModules 中。您应该使用哪个代码示例在 SharedModule 中包含 TableModule？

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

#### 问题78. 可以使用什么其他模板语法（替换 ngClass 指令）在此标记中添加或删除 CSS 类名？

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

#### 问题79. 在此指令装饰器示例中，提供者对象字面量中的 multi 属性的目的是什么？

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

- [ ] 它表示 CustomValidatorDirective 可用于多种表单元素类型。
- [ ] 它允许实例化 CustomValidatorDirective 的多个实例。如果没有 multi，CustomValidatorDirective 将是整个应用程序的单例。
- [x] 它允许为单个 NG_VALIDATORS 令牌注册不同的提供者。在这种情况下，它将 CustomValidatorDirective 添加到可用的表单验证器列表中。
- [ ] 它表示将有多个类处理自定义验证器的逻辑实现。

[StackOverflow](https://stackoverflow.com/questions/38144641/what-is-multi-provider-in-angular2)

#### 问题80. 您将使用哪个 Angular CLI 命令来运行单元测试，该过程会在文件更改时重新运行测试套件？

- [ ] ng test --single-run=false
- [ ] ng test --watch-files
- [ ] ng test --progress
- [x] ng test

#### 问题81. ngOnDestory 生命周期钩子最常见的用途是什么？

- [ ] 从组件视图中删除 dom 元素
- [ ] 删除任何注入的服务
- [x] 取消订阅 observables 并分离
- [ ] 以上所有

#### 问题82. 利用什么 NgModule 装饰器元数据属性来允许其他....？

- [ ] public
- [ ] experts
- [ ] Shared
- [x] declarations

#### 问题83. 使用以下组件类，您将在模板中使用什么模板语法来显示调用 currentYear 类函数的结果？

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
- [ ] 不能从模板语法调用类函数。