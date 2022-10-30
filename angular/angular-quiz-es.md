## Angular

#### P1. ¿Cuál es el propósito del decorador ViewChild en esta clase de componentes?

```ts
@Component({
    ...
    template: '<p #bio></p>'
})
export class UserDetailsComponent {
    @ViewChild('bio') bio;
}
```

- \[x] Proporciona acceso desde la clase de componente al objeto ElementRef para el `<p>` que tiene la variable de referencia de plantilla bio en la vista de plantilla del componente.
- \[ ] Indica que el `<p>` se representará como un elemento secundario de la vista principal que utiliza este componente.
- \[ ] Hace que el `<p>` en la plantilla admite la proyección de contenido.
- \[ ] Hace que el `<p>` visible en el renderizado final. Si se utilizó el #bio en la plantilla y no se utilizó el @ViewChild en la clase, Angular ocultaría automáticamente el `<p>` etiqueta que tiene #bio en ella.

[DigitalOcean - viewchild-access-component](https://www.digitalocean.com/community/tutorials/angular-viewchild-access-component)

#### P2. ¿Qué método se utiliza para conectar un FormControl a un elemento de entrada DOM nativo en formas reactivas?

- \[ ] Agregue el nombre de cadena dado al FormControl a un atributo denominado controles en el <form> para indicar qué campos debe incluir.
- \[ ] Utilice la sintaxis de enlace entre corchetes alrededor del atributo value en el elemento DOM y establézcalo igual a una instancia de FormControl.
- \[x] Utilice la directiva formControlName y establezca el valor igual al nombre de cadena dado al FormControl.
- \[ ] Utilice el nombre de cadena dado al FormControl como valor para el atributo id del elemento DOM.

[Angular.io - Grupos de formularios reactivos](https://angular.io/guide/reactive-forms#creating-nested-form-groups)

#### P3. ¿Cuál es la diferencia entre el `paramMap` y el `queryParamMap` en el `ActivatedRoute` ¿clase?

- \[ ] El paramMap es un literal de objeto de los parámetros de la ruta URL de una ruta. El queryParamMap es un Observable de esos mismos parámetros.
- \[ ] El paramMap es un Observable que contiene los valores de parámetro que forman parte de la ruta url de una ruta. QueryParamMap es un método que toma una matriz de claves y se utiliza para buscar parámetros específicos en el paramMap.
- \[ ] paramMap es el nombre heredado de Angular 3. El nuevo nombre es queryParamMap.
- \[x] Ambos son observables que contienen valores de la cadena de URL de la ruta solicitada. El paramMap contiene los valores de parámetro que se encuentran en la ruta de acceso de la dirección URL y el queryParamMap contiene los parámetros de consulta de la dirección URL.

[StackOverflow](https://stackoverflow.com/a/49617621)

#### P4. Según el siguiente uso de la canalización asincrónica, y suponiendo que el campo de clase de usuarios es observable, ¿cuántas suscripciones a los usuarios observables se están realizando?

```html
<h2>Names</h2>
<div *ngFor="let user of users | async">{{ user.name }}</div>
<h2>Ages</h2>
<div *ngFor="let user of users | async">{{ user.age }}</div>
<h2>Genders</h2>
<div *ngFor="let user of users | async">{{ user.gender }}</div>
```

- \[ ] Ninguno. La canalización asincrónica no se suscribe automáticamente.
- \[ ] Ninguno. La sintaxis de la plantilla no es correcta.
- \[x] Tres. Hay uno para cada tubería asincrónica.
- \[ ] Uno. La canalización asincrónica almacena en caché Observables por tipo internamente.

[UltimateCourses](https://ultimatecourses.com/blog/angular-ngfor-async-pipe)

#### P5. ¿Cómo puede utilizar HttpClient para enviar una solicitud POST a un extremo desde una función addOrder en este OrderService?

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
- \[ ] this.httpClient.post<Order>(this.orderUrl, orden);
- \[x] this.httpClient.post<Order>(this.orderUrl, order).subscribe();

[Angular.io - Envío de datos al servidor](https://angular.io/guide/http#sending-data-to-a-server)

#### P6. ¿Para qué se utiliza el método RouterModule.forRoot?

- \[ ] Registrar cualquier proveedor que tenga la intención de utilizar en componentes enrutados.
- \[x] Registro de definiciones de ruta en el nivel de aplicación raíz.
- \[ ] Indicando que Angular debe animar en sus rutas para tener éxito.
- \[ ] Declarar que tiene la intención de utilizar el enrutamiento solo en el nivel raíz.

[O ' REILLY](https://www.oreilly.com/library/view/switching-to-angular/9781788620703/c9e90774-0e10-410b-bd20-d3e9e0b8d117.xhtml)

#### P7. ¿En qué elementos DOM coincidirá este selector de metadatos de componentes?

```ts
@Component({
    selector: 'app-user-card',
    . . .
})
```

- \[ ] Cualquier elemento con el atributo app-user-card, como `<div app-user-card></div>`.
- \[ ] La primera instancia de `<app-user-card></app-user-card>`.
- \[x] Todas las instancias de `<app-user-card></app-user-card>`.
- \[ ] Todas las instancias de `<user-card></user-card>`.

[Angular.io - Metadatos de componentes](https://angular.io/guide/architecture-components#component-metadata)

#### P8. ¿Cuál es la sintaxis de plantilla correcta para usar la directiva estructural ngFor integrada para representar una lista de productNames?

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

[Angular.io- Directivas estructurales](https://angular.io/guide/built-in-directives#listing-items-with-ngfor)

#### P9. ¿Cuáles son las dos propiedades de metadatos del decorador de componentes utilizadas para configurar estilos CSS para un componente?

- \[ ] viewEncapsulation y viewEncapsulationFiles.
- \[ ] Sólo hay uno y es la propiedad llamada css.
- \[ ] css y cssUrl.
- \[x] estilos y styleUrls.

[Angular.io - Estilos de componentes](https://angular.io/guide/component-styles)

#### P10. Con la siguiente clase de componente, ¿qué sintaxis de plantilla usaría en la plantilla para mostrar el valor del campo de clase de título?

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
- \[ ] Un campo de clase no se puede mostrar en una plantilla a través de la sintaxis de la plantilla.

[Angular.io - Interpolación de cadenas o Interpolación de texto](https://angular.io/guide/interpolation)

#### P11. ¿Cuál es el propósito del método valueChanges en un FormControl?

- \[ ] Se utiliza para configurar qué valores se permiten para el control.
- \[ ] Se utiliza para cambiar el valor de un control a un nuevo valor. Llamaría a ese método y pasaría el nuevo valor para el campo de formulario. Incluso admite la aprobación de una matriz de valores que se pueden establecer con el tiempo.
- \[ ] Devuelve un valor booleano basado en si el valor del control es diferente del valor con el que se inicializó.
- \[x] Es un observable que emite cada vez que cambia el valor del control, por lo que puede reaccionar a nuevos valores y tomar decisiones lógicas en ese momento.

[Angular.io: visualización de un valor de control de origen](https://angular.io/guide/reactive-forms#displaying-a-form-control-value)

#### P12. ¿Qué directiva se utiliza para vincular un `<a>` etiqueta a enrutamiento?

- \[ ] routeTo
- \[x] routerLink
- \[ ] routePath
- \[ ] appLink

[Angular.io - RouterLink](https://angular.io/api/router/RouterLink#description)

#### P13. ¿Para qué se utiliza el decorador de salida en esta clase de componentes?

```ts
@Component({
    selector: 'app-shopping-cart',
    . . .
})
export class ShoppingCartComponent {
    @Output() itemTotalChanged = new EventEmitter();
}
```

- \[ ] Hace que el `itemTotalChanged` clase de campo público.
- \[ ] Proporciona una forma de enlazar valores a la `itemTotalChanged` campo de clase, así: `<app-shopping-cart [itemTotalChanged]="newTotal"></app-shopping-cart>`.
- \[x] Proporciona una forma de enlazar eventos a la `itemTotalChanged` campo de clase, así: `<app-shopping-cart (itemTotalChanged)="logNewTotal($event)"></app-shopping-cart>`.
- \[ ] Es simplemente una forma de poner un comentario delante de un campo de clase para la documentación.

[Angular.io - Envío de datos al componente primario](https://angular.io/guide/inputs-outputs#sending-data-to-a-parent-component)

#### P14. ¿Cuál es la diferencia entre estos dos ejemplos de marcado para el manejo condicional de la visualización?

```html
<div *ngIf="isVisible">Active</div>
<div [hidden]="!isVisible">Active</div>
```

- \[ ] El `ngIf` es la abreviatura del otro ejemplo. Cuando Angular procesa esa directiva, escribe un elemento div en el DOM con la propiedad oculta.
- \[ ] Son fundamentalmente lo mismo.
- \[x] El `ngIf` no representa el div en el DOM si la expresión es false. El `hidden` El uso de la propiedad oculta el contenido div en la ventana gráfica del explorador, pero el div todavía está en el DOM.
- \[ ] El `ngIf` es válido, pero el uso de la `hidden` la propiedad es incorrecta y generará un error.

[StackOverflow](https://stackoverflow.com/a/39778145)

#### P15. ¿Cómo puede deshabilitar el botón Enviar cuando el formulario tiene errores en este ejemplo de formularios controlados por plantillas?

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

[Angular.io - Envíe el formulario con ngSubmit](https://angular.io/guide/forms#submit-the-form-with-ngsubmit)

#### T1S. Desea ver qué archivos se generarían creando un nuevo componente de tarjeta de contacto. ¿Qué comando usarías?

- \[x] ng generar componente de tarjeta de contacto --dry-run
- \[ ] ng generar componente contact-card --no-files
- \[ ] ng generar componente componente --seco
- \[ ] ng generar componente --excluir

[Angular.io - ng generar opciones](https://angular.io/cli/generate#options)

#### P17. Basado en el siguiente componente, ¿qué sintaxis de plantilla usaría para enlazar el campo titleText de TitleCardComponent a la propiedad title del elemento h1?

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

[Angular.io - Interpolación de cadenas](https://angular.io/guide/interpolation)

#### P18. ¿Qué son los ganchos de ciclo de vida angular?

- \[ ] registradores para rastrear el estado de una aplicación Angular
- \[ ] proveedores que se pueden utilizar para realizar un seguimiento de las instancias de los componentes
- \[ ] canalizaciones integradas que se pueden usar en plantillas para eventos DOM
- \[x] métodos con nombre reservados para componentes y directivas a los que Angular llamará durante los tiempos establecidos en su ejecución, y se pueden usar para aprovechar esos momentos del ciclo de vida

[Angular.io - Ganchos de ciclo de vida](https://angular.io/guide/lifecycle-hooks)

#### P19. Elija la mejor descripción para este código de sintaxis de plantilla:

```html
<span>Boss: {{job?.bossName}} </span>
```

- \[ ] El ? es la abreviatura de la tubería asincrónica. El valor del trabajo debe ser observable.
- \[x] Está utilizando el operador de navegación segura (?) en el campo de trabajo. Si el campo de trabajo no está definido, se omitirá el acceso al bossName y no se producirá ningún error.
- \[ ] Hay un error en la sintaxis de la plantilla. ¿El? no es válido aquí.
- \[ ] Es minimizar el valor del trabajo si tiene uno; de lo contrario, está mostrando el bossName.

[StackOverflow](https://stackoverflow.com/a/60182134)

#### P20. ¿Cómo configuraría una definición de ruta para un UserDetailComponent que admita la ruta de acceso URL user/23 (donde 23 representa el identificador del usuario solicitado)?

- \[x] `{ path: 'user/:id', component: UserDetailComponent }`
- \[ ] `{ url: 'user/:id', routedComponent: UserDetailComponent }`
- \[ ] `{ routedPath: 'user/:id', component: UserDetailComponent }`
- \[ ] `{ destination: new UserDetailComponent(), route: 'user/:id' }`

[CodeCraft - Rutas parametrizadas](https://codecraft.tv/courses/angular/routing/parameterised-routes/#_configuration)

#### P21. ¿Qué hacen los decoradores de HostListener y el decorador de HostBinding en esta directiva?

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

- \[x] Están configurando el campo CalloutDirective.fontWeight en función de si el mouse está o no sobre el elemento DOM. A continuación, HostListener establece la propiedad CSS font-weight en el valor fontWeight.
- \[ ] Están configurando la directiva para comprobar el elemento DOM en el que se encuentra. Si tiene enlaces de eventos agregados para el mouse, ingrese y salga, usará este código. De lo contrario, no pasará nada.
- \[ ] Este es un uso incorrecto de HostListener y HostBinding. Los decoradores hostListener y HostBinding no hacen nada sobre las directivas; sólo funcionan cuando se utilizan en componentes.
- \[ ] Si el elemento DOM en el que se coloca esta directiva tiene la propiedad CSS font-weight establecida en él, los eventos mouseenter y mouseleave se generarán.

[Océano Digital](https://www.digitalocean.com/community/tutorials/angular-hostbinding-hostlistener)

#### P22. ¿Qué sintaxis de plantilla angular puede usar en este campo de formulario controlado por plantilla para acceder al valor del campo y comprobar la validación dentro del marcado de la plantilla?

```html
<input type="text" ngModel name="firstName" required minlength="4" />
<span *ngIf="">Invalid field data</span>
```

- \[x] Puede utilizar una variable de referencia de plantilla y la característica exportAs que tiene la directiva ngModel.
- \[ ] Puede utilizar la directiva ngModel en combinación con el nombre del campo de entrada.
- \[ ] Puede usar una variable de referencia de plantilla para el elemento de entrada HTML y, a continuación, comprobar la propiedad válida fuera de eso.
- \[ ] No es posible obtener acceso al valor del campo con formularios basados en plantillas. Debe usar formas reactivas para eso.

[Angular.io -Mostrar y ocultar error de validación ](https://angular.io/guide/forms#show-and-hide-validation-error-messages)

[Medio](https://medium.com/@agoiabeladeyemi/template-driven-forms-in-angular-4a3a5ad960de)

#### P23. ¿Cuál es el tipo de valor que se almacenará en la variable de referencia de la plantilla headerText en este marcado?

```html
<h1 #headerText>User List</h1>
```

- \[x] un Angular ElementRef, un contenedor alrededor de un elemento nativo
- \[ ] el texto interno de la `<h1>` elemento
- \[ ] una clase de componente de encabezado
- \[ ] el tipo de elemento DOM nativo de HTMLHeadingElement

[Pluralsight - Variable de referencia de plantilla](https://www.pluralsight.com/guides/how-to-use-template-reference-variables-in-angular)

#### P24. ¿Cuál es la diferencia, si la hay, de la lógica de código resultante basada en estas dos configuraciones de proveedor?

```ts
[{ provide: FormattedLogger, useClass: Logger }][{ provide: FormattedLogger, useExisting: Logger }];
```

- \[ ] Son lo mismo. Ambos darán como resultado una nueva instancia de Logger que está enlazada al token FormattedLogger.
- \[x] La sintaxis useClass indica al inyector que cree una nueva instancia de Logger y la enlace al token FormattedLogger. La sintaxis useExisting hace referencia a una instancia de objeto ya existente declarada como Logger.
- \[ ] Ambos están equivocados. Un tipo fuerte connot se puede utilizar para useClass o useExisting.
- \[ ] Son lo mismo. Ambos darán como resultado que el token FormattedLogger sea un alias para la instancia de Logger.

[Angular.io - Proveedores de dependencia](https://angular.io/guide/dependency-injection-providers#defining-providers)

[TektutorialHub](https://www.tektutorialshub.com/angular/angular-providers/)

#### P25. ¿Cuál es el propósito de la propiedad de datos (que se ve en el ejemplo siguiente) en una configuración de ruta?

```ts
   {
       path: 'customers',
       component: CustomerListComponent,
       data: { accountSection: true }
   }
```

- \[ ] una asignación clave/valor para establecer valores de @Input en la instancia del componente enrutado
- \[x] una forma de incluir datos estáticos de solo lectura asociados con la ruta que se pueden recuperar de ActivatedRoute
- \[ ] una propiedad de la ruta que se puede utilizar para cargar datos dinámicos para la ruta
- \[ ] un objeto que se inyectará automáticamente en el constructor del componente enrutado.

[TektutorialsHub](https://www.tektutorialshub.com/angular/angular-pass-data-to-route/#:~:text=Angular%20allows%20us%20to%20pass,of%20the%20history%20state%20object)

[StackOverflow](https://stackoverflow.com/a/36835156)

#### P26. ¿Cómo funciona el incorporado? `ngIf` La directiva estructural cambia el DOM representado en función de esta sintaxis de plantilla?

```ts
@Component({
  selector: 'app-product',
  template: '<div *ngIf="product">{{ product.name }}</div>',
})
export class ProductComponent {
  @Input() product;
}
```

- \[ ] El `<div>` actúa como marcador de posición. Si el campo de clase de producto es "veraz", el `<div>` será reemplazado por solo el `product.name` valor; si no, entonces nada se renderizará.
- \[ ] El `<div>` siempre se representará, y si el campo de producto es "verdadero", el `<div>` contendrá el elemento `product.name` valor; De lo contrario, representará el `<div>` elemento sin valor en él.
- \[ ] Produce un error, ya que ngIf no es una directiva estructural incorporada.
- \[x] Si el campo de clase de producto es "verdadero", entonces el DOM renderizado incluirá el `<div>` con el valor de la `product.name` campo. Si no es "veraz", el DOM renderizado no contendrá el `<div>` elemento.

[Referencia (angular.io)](https://angular.io/api/common/NgIf)

#### P27. ¿Qué logra este código?

```ts
@NgModule({
  declarations: [AppComponent],
  imports: [BrowserModule],
  bootstrap: [AppComponent],
})
export class AppModule {}

platformBrowserDynamic().bootstrapModule(AppModule);
```

- \[ ] Ejecuta una prueba unitaria para un NgModule.
- \[ ] Proporciona una forma de codificar la estructura del documento de una aplicación Angular. El @NgModule es una forma de comentario de código en línea que el compilador de TypeScript ignora, pero que aparecerá con un formato especial en las aplicaciones de edición de código.
- \[ ] Declara un módulo angular llamado AppModule y lo pone a disposición para la carga diferida en toda la aplicación.
- \[x] Declara un módulo angular denominado AppModule que contiene un componente de arranque denominado AppComponent. Luego registra ese módulo con Angular, para que la aplicación pueda iniciarse.

[Angular.io - El NgModule básico](https://angular.io/guide/ngmodules#the-basic-ngmodule)

#### P28. Qué opción describe mejor lo que el _resolver_ propiedad hace en esta configuración de ruta?

```ts
{
   path: ':id',
   component: UserComponent,
   resolve: {
     user: UserResolverService
   }
}
```

- \[x] Antes de cargar el _UserComponent_, el enrutador se suscribirá a la _Observable_ devuelto por un _resolver_ método en el _UserResolverService_. Esta técnica se puede utilizar para obtener datos precargados para un _ruta_.
- \[ ] Después de la _ruta_ se termina de resolver, y el componente se carga y se procesa, el _UserResolverService_ tendrá un método denominado _usuario_ ejecutar que limpiará cualquier conexión de datos abiertos.
- \[ ] Hay un error. El nombre correcto de la propiedad es _onResolver_.
- \[ ] El _UserComponent_ tendrá un parámetro en su constructor para _usuario_, y el _enrutador_ manejará la inyección de un valor para eso de una llamada a un _usuario_ método en el _UserResolverService_.

[angular.io](https://angular.io/api/router/Resolve)

#### P29. ¿Cuál es el propósito del decorador ContentChildren en esta clase de componentes?

```ts
@Component({
 . . .
 template: '<ng-content></ng-content›'
})
export class TabsListComponent {
 @ContentChildren(TabComponent) tabs;
}
```

- \[ ] Si la hubiera _TabsComponent_ se añaden elementos a la _TabsListComponent_ plantilla, se pondrán en el <ng-content> en tiempo de ejecución.
- \[ ] Crea _TabComponent_ componentes en el _TabsListComponent_ plantilla cuando un _TabsListComponent_ se crea una instancia.
- \[x] Proporciona acceso desde dentro de la clase de componente a cualquier _TabComponent_ componentes que se proyectaron en el contenido <ng-content> para este componente.
- \[ ] Restringe los elementos permitidos que se pueden poner en un _TabsListComponent_ elemento para permitir sólo _TabComponent_ Elementos.

[betterprogramming.pub](https://betterprogramming.pub/understanding-contentchildren-with-an-example-e76ce78968db)

#### P30. Para que Angular procese componentes en una aplicación, ¿dónde deben registrarse los tipos de componentes?

- \[ ] dentro de una etiqueta de script en el archivo index.html
- \[ ] en una etiqueta de metadatos del decorador NgModule denominada _Componentes_
- \[ ] No es necesario registrarse, simplemente incluya los archivos de componentes en un directorio de aplicaciones.
- \[x] en una propiedad de metadatos del decorador NgModule denominada _declaraciones_

[angular.io](https://angular.io/guide/ngmodule-api#ngmodule-metadata)

#### P31. ¿Cuál es el propósito de la `fixture.detectChanges()` llamar en esta prueba unitaria?

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

- \[ ] Realiza un seguimiento de cualquier posible cambio de Ul y fallará la prueba unitaria si se realiza alguna.
- \[ ] Se utiliza para garantizar la estabilidad de la plantilla de componentes en múltiples pruebas unitarias en todo el conjunto de pruebas.
- \[x] Obliga a Angular a realizar la detección de cambios, lo que representará el _UserCardComponent_ antes de poder validar su plantilla.
- \[ ] Se utiliza para registrar eventos de detección de cambios en la consola durante las ejecuciones de pruebas unitarias.

[angular.io](https://angular.io/api/core/testing/ComponentFixture#detectChanges)

#### P32. ¿Cómo se verá el segmento de URL en función de la siguiente llamada al `Router.navigate` cuando a goToUser se le pasa el valor 15?

```ts
export class ToolsComponent {
  constructor(private router: Router) {}
  goToUser(id: number) {
    this.router.navigate(['user', id]);
  }
}
```

- \[x] /usuario/15
- \[ ] /usuario?id=15
- \[ ] /usuario:15
- \[ ] /usuario;id=15

[angular.io](https://angular.io/api/router/Router#navigate)

#### P33. Cuando se proporciona un servicio para root y también se agrega a la configuración del proveedor para un módulo de carga diferida, ¿qué instancia de ese servicio proporciona el inyector a los constructores en el módulo de carga diferida?

- \[x] Se crea una nueva instancia de ese servicio cuando el módulo se carga diferidamente.
- \[ ] No se permite proporcionar un servicio del mismo tipo a nivel de módulo cargado perezosamente.
- \[ ] Si aún no se ha creado una instancia del servicio en el nivel raíz. creará uno allí y luego lo usará.
- \[ ] Una sola instancia de ese servicio siempre se crea una instancia en la raíz y es la única que se usa, incluso dentro de los módulos perezosos.

#### P34. ¿Qué está haciendo el decorador de HostBinding en esta directiva?

```ts
@Directive({
  selector: ' [appHighlight] ',
})
export class HighlightDirective {
  @HostBinding('class.highlighted') highlight = true;
}
```

- \[x] Es agregar la clase CSS nombrada resaltada a cualquier elemento DOM que tenga la directiva appHighlight.
- \[ ] HostBinding no hace nada en directivas, solo en componentes.
- \[ ] Especifica si el elemento host obtiene la clase resaltada agregada a su atributo de clase, entonces el resaltado del campo de clase directiva se establecerá en true; y si no se agrega en el host, se establecerá en false.
- \[ ] Es crear un estilo en línea en el elemento host con una propiedad CSS denominada highlight establecida en true.

[StackOverflow](https://stackoverflow.com/a/46207423)

#### P35. En las formas reactivas, qué tipo de clase de forma angular se utiliza en el DOM nativo <form> elemento para conectarlo?

- \[ ] `FormArray`
- \[ ] `FormControl`
- \[x] `FormGroup`
- \[ ] `all of these answers`

#### P36. Suponiendo que el nombre de usuario FormControl se ha configurado con un validador minLength, ¿cómo puede configurar una visualización de error en el siguiente marcado de formularios reactivos para el campo de nombre de usuario?

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

#### P37. ¿Cómo maneja el modo de encapsulación de vista emulada CSS para un componente?

- \[ ] Representa el CSS exactamente como lo escribió sin ningún cambio.
- \[ ] Hace uso del marcado DOM de sombra y CSS.
- \[x] Crea atributos únicos para los elementos DOM y los ámbitos de los selectores CSS que escribe en esos identificadores de atributos.
- \[ ] Representa todas las reglas CSS que escribe como CSS en línea en todos los elementos DOM en los que las usa en la plantilla.

[Angular.io](https://angular.io/guide/view-encapsulation#inspecting-generated-css)

#### P38. Con la siguiente configuración de TestBed, ¿qué se puede usar para acceder al DOM representado para UserCardComponent?

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

#### P39. Dados estos dos componentes, ¿qué se representará en el DOM en función del uso de marcado?

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

#### P40. Dado el componente app-title-card en el código siguiente, ¿qué DOM representará el componente app-user-card?

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

#### P41. Elija el código coincidente para el registro de proveedor personalizado que el decorador de @Inject () está buscando:

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

[Angular.io - Inyección de dependencia en acción](https://angular.io/guide/dependency-injection-in-action#supply-a-custom-provider-with-inject)

#### P42. ¿Qué opción describe mejor el siguiente uso del método HttpClient.get en el método de clase getsettings?

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

- \[ ] El método de canalización RxJs es un alias para el método subscribe, por lo que una llamada a `getSettings` ejecutará la consulta get. El operador de reintento se utiliza para indicar a la llamada de canalización que vuelva a intentar la consulta get tres veces.
- \[ ] Producirá un error en tiempo de ejecución porque el método de canalización no está disponible fuera del `Httpclient.get` llamar.
- \[ ] Cada llamada al método getSettings dará como resultado que el httpclient realice tres solicitudes de obtención totales a settingsUrl, lo cual no es ideal porque siempre habrá dos llamadas adicionales que no son necesarias. El operador de reintento no debe utilizarse de esta manera.
- \[x] Cuando se suscriba el resultado del método getSettings, se realizará la llamada HTTP GET; si falla, se volverá a intentar hasta tres veces antes de que se rinda y devuelva un error.

[learnrxjs.io](https://www.learnrxjs.io/learn-rxjs/operators/error_handling/retry)

[dev.to](https://dev.to/gparlakov/how-does-rxjs-retry-work-412p)

#### P43. Cuando un servicio requiere alguna configuración para inicializar su estado predeterminado a través de un método, ¿cómo puede asegurarse de que dicho método se invoca antes de que el servicio se inyecte en cualquier lugar?

- \[ ] En su lugar, coloque la lógica de ese método de servicio en el constructor de servicio.
- \[x] Utilice un proveedor de fábrica en el nivel raíz de AppModule que dependa del servicio para llamar a ese método de servicio.
- \[ ] no es posible hacerlo al inicio de la aplicación; solo puede hacerlo a nivel de componente.
- \[ ] Cree una instancia del servicio en el nivel global (ámbito de ventana) y, a continuación, llame a ese método.

#### P44. ¿Qué declaración describe mejor este uso del banco de pruebas?

```ts
const spy = jasmine.createSpyObj('DataService', ['getUsersFromApi']);
TestBed.configureTestingModule({
  providers: [UserService, { provide: DataService, useValue: spy }],
});
const userService = TestBed.get(UserService);
```

- \[ ] El banco de pruebas es necesario en cualquier momento que desee hacer uso de un objeto espía en una prueba unitaria para un proveedor angular.
- \[ ] El banco de pruebas se utiliza para probar la vista de un componente.
- \[x] El Banco de Pruebas despliega un NgModule con dos proveedores y maneja cualquier inyección de dependencia. Si alguna clase Angular solicita el DataService en su constructor, el Banco de Pruebas inyectará spy en ese constructor.
- \[ ] El Banco de pruebas está configurando al ejecutor de pruebas para que le indique que solo ejecute pruebas para los dos proveedores enumerados en su matriz de proveedores.
- `All other tests be ignored, including tests that assert results against one of these providers and a non-defined provider.`
  `Although it will work when multiple providers in this configuration are asserted against in a single test.`

#### P45. ¿Cuál es la principal diferencia entre un componente y una directiva?

- \[ ] Un componente utiliza una propiedad de metadatos selector y una directiva no.
- \[ ] Se puede utilizar una directiva para agregar eventos personalizados al DOM y un componente no.
- \[x] Un componente tiene una plantilla y una directiva no.
- \[ ] Una directiva sólo puede dirigirse a elementos DOM nativos.

[StackOverflow](https://stackoverflow.com/a/34616190)

#### P46. ¿Qué podría agregar a esta clase de directiva para permitir que se establezca la longitud truncada durante el uso de directivas en el marcado?

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

#### P47. ¿Cómo puede pasar parámetros de consulta a este `HttpClient.get` ¿pedir?

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

#### P48. Asumiendo el `DataService` se ha registrado en los proveedores de la aplicación, ¿qué respuesta describe mejor lo que sucede en función del constructor de este componente?

```ts
    @Component({
        ...
    })
    export class OrderHistoryComponent {
        constructor(private dataService: DataService) {}
        ...
    }
```

- \[ ] Se declara que el `OrderHistoryComponent` tendrá su propia versión de un `DataService` y que nunca debe utilizar ninguna instancia existente. El `DataService` necesitaría ser instanciado dentro de la clase como un campo privado para que este código esté completo y funcione.
- \[x] Cuando Angular crea una nueva instancia de la `OrderHistoryComponent`, el inyector proporcionará una instancia de un `DataService` al primer argumento del constructor de componentes. El constructor `dataService` se usará para establecer un campo de instancia privada con el mismo nombre en la instancia.
- \[ ] Proporciona una forma de hacer pruebas de componentes solamente; el constructor no tiene ningún uso en la ejecución real de la aplicación Angular.
- \[ ] Permite que el elemento personalizado al que se dirige el componente tenga una propiedad personalizada denominada `dataService` que se puede utilizar para enlazar un `DataService` instancia a.

[StackOverflow](https://stackoverflow.com/a/49755822)

[Angular.io - Inyección de dependencia](https://angular.io/guide/dependency-injection)

#### Pregunta 49. Finalice este marcado con el botón `ngIf` directiva para implementar otro caso que mostrará el texto "El usuario no está activo":

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

#### Pregunta 50. ¿Cuál es la sintaxis correcta para que una definición de ruta cargue diferidamente un módulo de entidad?

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

[Angular.io - Módulos de carga diferida](https://angular.io/guide/lazy-loading-ngmodules)

#### Pregunta 51. Describa cómo se configura y configura la validación en este ejemplo de formularios reactivos:

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

- \[ ] El `FormControl` para `username` se está configurando para excluir tres validadores de los validadores que se le permite usar.
- \[ ] El `FormControl` para `username` se está configurando para permitir el uso de tres posibles validadores: `required, maxLength`, y uno personalizado denominado `unique`. Para habilitar estos `validators`, sería necesario colocar una directiva de validador en los campos de formulario del marcado.
- \[ ] La validación no se puede configurar de esta manera en formas reactivas.
- \[x] El `FormControl` para `username` se está configurando con tres validadores: el `required` y `minLength` validadores que provienen de Angular y una función de validación personalizada denominada `unique` que comprueba si el valor no es igual a la cadena `admin`.

[Angular.io - Validación de formularios](https://angular.io/guide/form-validation)

[Blog de la Universidad Angular](https://blog.angular-university.io/angular-custom-validators/)

#### P52. ¿Qué hace el decorador inyectable en esta clase de servicio?

```ts
@Injectable({
    providedIn: 'root'
)}
export class DataService { }
```

- \[ ] Registra un proveedor para el servicio que está disponible solo en el nivel de módulo raíz, no para ningún módulo secundario.
- \[x] Registra un proveedor para el servicio en el inyector de aplicación raíz, haciendo que una sola instancia del mismo esté disponible en toda la aplicación.
- \[ ] Lo hace para que el servicio se pueda inyectar solo en el componente de arranque para la aplicación.
- \[ ] Establece una regla de tiempo de compilación que le permite colocar el tipo de servicio solo en la propiedad de metadatos de proveedores de la raíz NgModule.

[Angular.io](https://angular.io/guide/providers#providing-a-service)

#### Pregunta 53. Describir el uso de este código

```ts
export interface AppSettings {
  title: string;
  version: number;
}
export const APP_SETTINGS = new InjectionToken<AppSettings>('app.settings');
```

- \[ ] InjectionToken está agregando una instancia de AppSettings al proveedor raíz a través de la llamada al constructor InjectionToken, lo que la hace automáticamente disponible para todos los NgModules, servicios y componentes en toda la aplicación Angular sin la necesidad de inyectarla en ningún lugar.
- \[x] InjectionToken se utiliza para crear un token de proveedor para una dependencia que no es de clase. Un literal Object puede ser proveedor como un valor para el tipo de proveedor de dependencia APP_SETTINGS que luego se puede inyectar en componentes, servicios, etc.
- \[ ] El InjectionToken se utiliza para crear un decorador dinámico para AppSettings que se puede utilizar en los parámetros del constructor a través de un decorador @AppSettings.
- \[ ] Este código tiene un error ya que no puede utilizar una interfaz de TypeScript para el tipo genérico en injectionToken

#### Pregunta 54. Para el siguiente ejemplo de formularios controlados por plantillas, ¿qué argumento se puede pasar al método submit en el evento click para enviar los datos del formulario?

```html
<form #form="ngForm">
  <input type="text" ngModel="firstName" />
  <input type="text" ngModel="lastName" />
  <button (click)="submit()">Save</button>
</form>
```

- \[x] submit(form.value)
- \[ ] enviar($event)
- \[ ] submit(ngForm.value)
- \[ ] submit(FirstName, lastName)

#### Pregunta 55. ¿Cuál es el propósito de la configuración de la propiedad prelodingStrategy en este código de enrutador?

```ts
RouterModule.forRoot(
  ...{
    preloadingStrategy: PreloadAllModules,
  },
);
```

- \[ ] Permite la opción de marcar rutas individuales para la precarga.
- \[ ] Precarga todas las dependencias para las rutas, creando instancias de servicios cuando la aplicación se inicia por primera vez
- \[ ] Garantiza que todos los módulos se integren en un solo archivo de paquete de módulo de aplicación.
- \[ ] Configura el enrutador para cargar inmediatamente todas las rutas que tienen una propiedad loadChildren (rutas que normalmente se cargan cuando se solicita)

#### Pregunta 56. ¿Cuál es una forma alternativa de escribir este marcado para enlazar el valor del campo de clase? `userName` al `h1` propiedad de título de elemento?

```html
<h1 [title]="userName">Current user is {{ userName }}</h1>
```

- \[ ] title="userName"
- \[x] title="{{ userName }}"
- \[ ] title="{{ 'userName' }}"
- \[ ] La única forma de hacerlo es utilizando los corchetes.

#### Pregunta 57. ¿Qué es el `async` ¿Hacer tubería en este ejemplo?

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

- \[ ] No está haciendo nada, ya que la tubería asincrónica no se puede utilizar en un `ngFor` declaración.
- \[ ] Está configurando el `ngFor` iteración para admitir varias listas de usuarios al mismo tiempo.
- \[x] Se está suscribiendo al observable devuelto desde el `HttpClient.get` y desenvolver el valor devuelto para que se pueda iterar en el cuadro `ngFor`.
- \[ ] Está permitiendo a todos los usuarios en el `users` que se representará simultáneamente en el DOM.

#### Pregunta 58. ¿Cómo se utilizaría esta directiva en el marcado en función de su valor de selector?

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

#### Pregunta 59. ¿Qué gancho de ciclo de vida se puede usar en un componente para supervisar todos los cambios en los valores de @Input en ese componente?

- \[ ] ngOnInit
- \[ ] ngCambios
- \[ ] ngAfterInputChange
- \[x] ngOnChanges

[¿Cómo detectar cuando un valor @Input() cambia en Angular?](https://stackoverflow.com/a/44686085/1573267)

#### P60. ¿Cuál sería un ejemplo de uso de sintaxis de plantilla de esta canalización personalizada?

```ts
@Pipe({ name: 'truncate' })
export class TruncatePipe implements PipeTransform {
	transform(value: string, maxLength: number, showEllipsis: boolean){
		const newValue = maxLength ? value.substr(0, maxLength): value;
		return showEllipsis ? '${newValue}...` : newValue;
	}
}
```

- \[x] {( 'algún texto largo' | truncar:10 })
- \[ ] {( 'algún texto largo' | truncar:10:true })
- \[ ] {( 'algún texto largo' | truncar })
- \[ ] todas estas respuestas

\[vuelva a verificar las respuestas]

#### P61. ¿Qué comando de la CLI angular ejecutaría para generar un UsersComponent y agregarlo al SharedModule (en el archivo shared.module.ts de la aplicación)?

- \[ ] ng generar componente --newModule=shared
- \[ ] ng generar usuarios de componentes --module=shared
- \[ ] ng generar usuarios de componentes --compartido
- \[ ] ng generar componente --add=shared

\[vuelva a verificar las respuestas]

#### P62. ¿Cómo puede reescribir este marcado para que el contenedor div no sea necesario en el renderizado DOM final?

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

\[volver a comprobar las respuestas]

#### P63. Describa el uso de este código:

```ts
export interface AppSettings {
  title: string;
  version: number;
}
```

- \[ ] Este código es un error, ya que no puede utilizar una interfaz de TypeScript para el tipo genérico en InjectionToken.
- \[ ] InjectionToken se utiliza para crear un token de proveedor para una dependencia que no es de clase. Se puede proporcionar un objeto lieteral como un valor para el tipo de proveedor de dependencia APP_SETTINGS que luego se puede inyectar en componentes, servicios, etc.
- \[ ] InjectionToken está agregando una instancia de AppSettings al proveedor roote a través de la llamada al constructor InjectionToken, lo que la hace automáticamente disponible para todos los NgModules, servicios y componentes en toda la aplicación Angular sin la necesidad de inyectarla en ningún lugar.
- \[ ] El InjectionToken se utiliza para crear un decorador dinámico para appSettings que se puede sembrar en los parámetros del constructor a través de un decorador @AppSettings.

\[volver a comprobar las respuestas]

#### Pregunta 64. ¿Qué utilidades angulares, si las hay, se requieren para probar unitariamente un servicio sin dependencias de constructor?

- \[ ] Se necesita el método auxiliar By.css()
- \[ ] Se requiere un accesorio de texto para ejecutar el servicio para la prueba unitaria.
- \[ ] Ninguno. Un servicio puede ser instanciado y probado por unidad por sí solo.
- \[x] La clase TestBed es necesaria para crear instancias del servicio.

[Pruebas unitarias angulares](https://angular.io/guide/testing-services) - volver a comprobar las respuestas

#### Pregunta 65. ¿Cuál es la diferencia entre los protectores de ruta CanActivate y CanLoad?

- \[ ] CanActivate se utiliza para comprobar el acceso. CanLoad se utiliza para precargar datos para la ruta.
- \[x] CanLoad se utiliza al inicio de la aplicación para permitir o denegar la adición de rutas a la tabla de rutas. CanActivate se utiliza para gestionar el acceso a las rutas en el momento en que se solicitan.
- \[ ] CanActivate y CanLoad hacen exactamente lo mismo.
- \[ ] CanLoad impide que se entregue y cargue un NgModule completo. CanActivate deja de enrutar a un componente en ese NgModule, pero ese módulo aún está cargado.

[CanActivate vs Canload](https://stackoverflow.com/questions/42026045/difference-between-angulars-canload-and-canactivate#:~:text=canActivate%20is%20used%20to%20prevent,not%20authorized%20to%20do%20so.) CanActivate impide el acceso en las rutas, CanLoad evita la carga diferida.

#### Pregunta 66. ¿Para qué se utiliza la propiedad de salida en este objeto de definición de enrutador?

```ts
{
	path: 'document',
	component: DocumentComponent,
	outlet: 'document-box'
}
```

- \[ ] localizará todas las instancias de <document-box> en el DOM e insertar un elemento DocumentComponent en ellos en la navegación de rutas.
- \[ ] Declara que documentComponent se puede utilizar como un elemento secundario para un <<document-box> además de ser enrutado a.
- \[x] Se utiliza para apuntar a un <router-outlet> con el atributo name que coincide con el valor de cadena como ubicación para el DocumentComponent que se va a representar cuando se enruta.
- \[ ] Es una fuente de energía para el router. (definitivamente no es la respuesta :P)

[Salida angular](https://angular.io/api/router/RouterOutlet) - volver a comprobar la respuesta
