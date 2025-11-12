## Angular

#### प्र1. इस कंपोनेंट क्लास में ViewChild डेकोरेटर का उद्देश्य क्या है?

```ts
@Component({
    ...
    template: '<p #bio></p>'
})
export class UserDetailsComponent {
    @ViewChild('bio') bio;
}
```

- [x] यह कंपोनेंट क्लास के भीतर से `<p>` टैग के लिए ElementRef ऑब्जेक्ट तक पहुंच प्रदान करता है जिसमें कंपोनेंट के टेम्पलेट व्यू में bio टेम्पलेट संदर्भ चर है।
- [ ] यह इंगित करता है कि `<p>` टैग को पैरेंट व्यू के चाइल्ड के रूप में रेंडर किया गया है जो इस कंपोनेंट का उपयोग करता है।
- [ ] यह टेम्पलेट में `<p>` टैग को कंटेंट प्रोजेक्शन का समर्थन करता है।
- [ ] यह अंतिम रेंडर में `<p>` टैग को दृश्यमान बनाता है। यदि #bio का उपयोग टेम्पलेट में किया गया था और @ViewChild का उपयोग क्लास में नहीं किया गया था, तो Angular स्वचालित रूप से `<p>` टैग को छुपा देगा जिस पर #bio है।

#### प्र2. रिएक्टिव फॉर्म्स में FormControl को नेटिव DOM इनपुट एलिमेंट से वायर करने के लिए किस विधि का उपयोग किया जाता है?

- [ ] FormControl को दिए गए स्ट्रिंग नाम को `<form>` एलिमेंट पर controls नामक एट्रिब्यूट में जोड़ें ताकि यह संकेत मिल सके कि इसमें कौन से फ़ील्ड शामिल होने चाहिए।
- [ ] DOM एलिमेंट पर value एट्रिब्यूट के चारों ओर वर्ग कोष्ठक बाइंडिंग सिंटैक्स का उपयोग करें और इसे FormControl के इंस्टेंस के बराबर सेट करें।
- [x] formControlName डायरेक्टिव का उपयोग करें और FormControl को दिए गए स्ट्रिंग नाम के बराबर मान सेट करें।
- [ ] FormControl को दिए गए स्ट्रिंग नाम का उपयोग DOM एलिमेंट id एट्रिब्यूट के मान के रूप में करें।

#### प्र3. `ActivatedRoute` क्लास पर `paramMap` और `queryParamMap` में क्या अंतर है?

- [ ] paramMap एक रूट के URL पथ में पैरामीटर का ऑब्जेक्ट लिटरल है। queryParamMap उन्हीं पैरामीटर का एक Observable है।
- [ ] paramMap एक Observable है जिसमें एक रूट के URL पथ का हिस्सा बनने वाले पैरामीटर मान होते हैं। queryParamMap एक विधि है जो कुंजियों की एक सरणी लेती है और paramMap में विशिष्ट पैरामीटर खोजने के लिए उपयोग की जाती है।
- [ ] paramMap Angular 3 से विरासत का नाम है। नया नाम queryParamMap है।
- [x] दोनों अनुरोधित रूट के URL स्ट्रिंग से मान युक्त Observables हैं। paramMap में URL पथ में पैरामीटर मान होते हैं और queryParamMap में URL क्वेरी पैरामीटर होते हैं।

#### प्र4. async पाइप के निम्नलिखित उपयोग के आधार पर, और मान लें कि users क्लास फ़ील्ड एक Observable है, users Observable में कितनी सदस्यताएं बनाई जा रही हैं?

```html
<h2>नाम</h2>
<div *ngFor="let user of users | async">{{ user.name }}</div>
<h2>उम्र</h2>
<div *ngFor="let user of users | async">{{ user.age }}</div>
<h2>लिंग</h2>
<div *ngFor="let user of users | async">{{ user.gender }}</div>
```

- [ ] कोई नहीं। async पाइप स्वचालित रूप से सदस्यता नहीं लेता है।
- [ ] कोई नहीं। टेम्पलेट सिंटैक्स सही नहीं है।
- [x] तीन। प्रत्येक async पाइप के लिए एक है।
- [ ] एक। async पाइप आंतरिक रूप से प्रकार द्वारा Observables को कैश करता है।

#### प्र5. आप इस OrderService में addOrder फ़ंक्शन के भीतर से एक एंडपॉइंट पर POST अनुरोध भेजने के लिए HttpClient का उपयोग कैसे कर सकते हैं?

```ts
export class OrderService {
  constructor(private httpClient: HttpClient) {}

  addOrder(order: Order) {
    // लापता लाइन
  }
}
```

- [ ] `this.httpClient.url(this.orderUrl).post(order);`
- [ ] `this.httpClient.send(this.orderUrl, order);`
- [ ] `this.httpClient.post<Order>(this.orderUrl, order);`
- [x] `this.httpClient.post<Order>(this.orderUrl, order).subscribe();`

#### प्र6. RouterModule.forRoot विधि का उपयोग किसके लिए किया जाता है?

- [ ] किसी भी प्रोवाइडर को पंजीकृत करना जिसका आप रूटेड कंपोनेंट्स में उपयोग करना चाहते हैं।
- [x] रूट एप्लिकेशन स्तर पर रूट परिभाषाओं को पंजीकृत करना।
- [ ] यह इंगित करना कि Angular को आपके रूट को सफल होने के लिए प्रोत्साहित करना चाहिए।
- [ ] यह घोषणा करना कि आप केवल रूट स्तर पर रूटिंग का उपयोग करना चाहते हैं।

#### प्र7. यह कंपोनेंट मेटाडेटा सिलेक्टर किन DOM एलिमेंट्स से मेल खाएगा?

```ts
@Component({
    selector: 'app-user-card',
    . . .
})
```

- [ ] app-user-card एट्रिब्यूट वाला कोई भी एलिमेंट, जैसे `<div app-user-card></div>`।
- [ ] `<app-user-card></app-user-card>` का पहला इंस्टेंस।
- [x] `<app-user-card></app-user-card>` के सभी इंस्टेंस।
- [ ] `<user-card></user-card>` के सभी इंस्टेंस।

#### प्र8. productNames की सूची को रेंडर करने के लिए बिल्ट-इन ngFor स्ट्रक्चरल डायरेक्टिव का उपयोग करने के लिए सही टेम्पलेट सिंटैक्स क्या है?

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

#### प्र9. कंपोनेंट के लिए CSS स्टाइल सेट करने के लिए उपयोग की जाने वाली दो कंपोनेंट डेकोरेटर मेटाडेटा प्रॉपर्टीज कौन सी हैं?

- [ ] viewEncapsulation और viewEncapsulationFiles।
- [ ] केवल एक है और यह css नामक प्रॉपर्टी है।
- [ ] css और cssUrl।
- [x] styles और styleUrls।

#### प्र10. निम्नलिखित कंपोनेंट क्लास के साथ, टेम्पलेट में title क्लास फ़ील्ड का मान प्रदर्शित करने के लिए आप टेम्पलेट में किस टेम्पलेट सिंटैक्स का उपयोग करेंगे?

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
- [ ] टेम्पलेट सिंटैक्स के माध्यम से क्लास फ़ील्ड को टेम्पलेट में प्रदर्शित नहीं किया जा सकता है।

#### प्र11. FormControl पर valueChanges विधि का उद्देश्य क्या है?

- [ ] इसका उपयोग यह कॉन्फ़िगर करने के लिए किया जाता है कि नियंत्रण के लिए कौन से मान की अनुमति है।
- [ ] इसका उपयोग नियंत्रण के मान को नए मान में बदलने के लिए किया जाता है। आप उस विधि को कॉल करेंगे और फ़ॉर्म फ़ील्ड के लिए नया मान पास करेंगे। यह समय के साथ सेट किए जा सकने वाले मानों की सरणी को पास करने का भी समर्थन करता है।
- [ ] यह इस बात के आधार पर एक Boolean लौटाता है कि नियंत्रण का मान उस मान से अलग है या नहीं जिसके साथ इसे आरंभ किया गया था।
- [x] यह एक observable है जो हर बार नियंत्रण का मान बदलता है, तो उत्सर्जित होता है, ताकि आप नए मानों पर प्रतिक्रिया कर सकें और उस समय तर्क निर्णय ले सकें।

#### प्र12. रूटिंग के लिए `<a>` टैग को लिंक करने के लिए किस डायरेक्टिव का उपयोग किया जाता है?

- [ ] routeTo
- [x] routerLink
- [ ] routePath
- [ ] appLink

#### प्र13. इस कंपोनेंट क्लास में Output डेकोरेटर का उपयोग किसके लिए किया जाता है?

```ts
@Component({
    selector: 'app-shopping-cart',
    . . .
})
export class ShoppingCartComponent {
    @Output() itemTotalChanged = new EventEmitter();
}
```

- [ ] यह `itemTotalChanged` क्लास फ़ील्ड को सार्वजनिक बनाता है।
- [ ] यह `itemTotalChanged` क्लास फ़ील्ड में मानों को बाइंड करने का एक तरीका प्रदान करता है, जैसे: `<app-shopping-cart [itemTotalChanged]="newTotal"></app-shopping-cart>`।
- [x] यह `itemTotalChanged` क्लास फ़ील्ड में इवेंट्स को बाइंड करने का एक तरीका प्रदान करता है, जैसे: `<app-shopping-cart (itemTotalChanged)="logNewTotal($event)"></app-shopping-cart>`।
- [ ] यह बस दस्तावेज़ीकरण के लिए क्लास फ़ील्ड के सामने टिप्पणी डालने का एक तरीका है।

#### प्र14. सशर्त रूप से प्रदर्शन को संभालने के लिए इन दो मार्कअप उदाहरणों के बीच क्या अंतर है?

```html
<div *ngIf="isVisible">Active</div>
<div [hidden]="!isVisible">Active</div>
```

- [ ] `ngIf` दूसरे उदाहरण के लिए शॉर्टहैंड है। जब Angular उस डायरेक्टिव को प्रोसेस करता है, तो यह hidden प्रॉपर्टी के साथ DOM में एक div एलिमेंट लिखता है।
- [ ] वे मूल रूप से समान हैं।
- [x] `ngIf` डायरेक्टिव DOM में div को रेंडर नहीं करता है यदि एक्सप्रेशन false है। `hidden` प्रॉपर्टी उपयोग ब्राउज़र व्यूपोर्ट में div सामग्री को छुपाता है, लेकिन div अभी भी DOM में है।
- [ ] `ngIf` मान्य है, लेकिन `hidden` प्रॉपर्टी का उपयोग गलत है और एक त्रुटि फेंक देगा।

#### प्र15. इस टेम्पलेट-संचालित फ़ॉर्म उदाहरण में फ़ॉर्म में त्रुटियां होने पर आप सबमिट बटन को कैसे अक्षम कर सकते हैं?

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

#### प्र16. यह देखने के लिए कि एक नया contact-card कंपोनेंट बनाने से कौन सी फ़ाइलें जेनरेट होंगी, आप किस Angular CLI कमांड का उपयोग करेंगे?

- [x] ng generate component contact-card --dry-run
- [ ] ng generate component contact-card --no-files
- [ ] ng generate component component --dry
- [ ] ng generate component --exclude

#### प्र17. निम्नलिखित कंपोनेंट के आधार पर, TitleCardComponent के titleText फ़ील्ड को h1 एलिमेंट title प्रॉपर्टी से बाइंड करने के लिए आप किस टेम्पलेट सिंटैक्स का उपयोग करेंगे?

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

#### प्र18. Angular लाइफसाइकिल हुक्स क्या हैं?

- [ ] Angular ऐप के स्वास्थ्य को ट्रैक करने के लिए लॉगर
- [ ] प्रोवाइडर जिनका उपयोग कंपोनेंट्स के इंस्टेंस को ट्रैक करने के लिए किया जा सकता है
- [ ] बिल्ट-इन पाइप जिनका उपयोग DOM इवेंट्स के लिए टेम्पलेट में किया जा सकता है
- [x] कंपोनेंट्स और डायरेक्टिव्स के लिए आरक्षित नामित विधियां जिन्हें Angular अपने निष्पादन में सेट समय के दौरान कॉल करेगा, और उन लाइफसाइकिल क्षणों में टैप करने के लिए उपयोग किया जा सकता है

#### प्र19. इस टेम्पलेट सिंटैक्स कोड के लिए सर्वोत्तम विवरण चुनें:

```html
<span>Boss: {{job?.bossName}} </span>
```

- [ ] ? async पाइप के लिए शॉर्टहैंड है। job मान एक Observable होना चाहिए।
- [x] यह job फ़ील्ड पर सुरक्षित नेविगेशन ऑपरेटर (?) का उपयोग कर रहा है। यदि job फ़ील्ड अपरिभाषित है, तो bossName तक पहुंच को अनदेखा किया जाएगा और कोई त्रुटि नहीं होगी।
- [ ] टेम्पलेट सिंटैक्स में एक त्रुटि है। ? यहाँ मान्य नहीं है।
- [ ] यह job मान प्रदर्शित कर रहा है यदि इसमें एक है; अन्यथा यह bossName प्रदर्शित कर रहा है।

#### प्र20. आप UserDetailComponent के लिए रूट परिभाषा को कैसे कॉन्फ़िगर करेंगे जो URL पथ user/23 का समर्थन करता है (जहां 23 अनुरोधित उपयोगकर्ता की id का प्रतिनिधित्व करता है)?

- [x] `{ path: 'user/:id', component: UserDetailComponent }`
- [ ] `{ url: 'user/:id', routedComponent: UserDetailComponent }`
- [ ] `{ routedPath: 'user/:id', component: UserDetailComponent }`
- [ ] `{ destination: new UserDetailComponent(), route: 'user/:id' }`

#### प्र21. इस डायरेक्टिव में HostListener डेकोरेटर और HostBinding डेकोरेटर क्या कर रहे हैं?

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

- [x] वे CalloutDirective.fontWeight फ़ील्ड को इस आधार पर सेट कर रहे हैं कि माउस DOM एलिमेंट पर है या नहीं। HostListener फिर font-weight CSS प्रॉपर्टी को fontWeight मान पर सेट करता है।
- [ ] वे डायरेक्टिव को DOM एलिमेंट की जांच करने के लिए सेट कर रहे हैं जिस पर यह है। यदि इसमें माउस enter और leave के लिए इवेंट बाइंडिंग जोड़ी गई है तो यह इस कोड का उपयोग करेगा। अन्यथा, कुछ नहीं होगा।
- [ ] यह HostListener और HostBinding का गलत उपयोग है। HostListener और HostBinding डेकोरेटर डायरेक्टिव्स पर कुछ नहीं करते हैं; वे केवल कंपोनेंट्स पर उपयोग किए जाने पर काम करते हैं।
- [ ] यदि इस डायरेक्टिव को जिस DOM एलिमेंट पर रखा गया है, उस पर CSS प्रॉपर्टी font-weight सेट है, तो mouseenter और mouseleave इवेंट उठाए जाएंगे।

#### प्र22. टेम्पलेट मार्कअप के भीतर फ़ील्ड मान तक पहुंचने और सत्यापन की जांच करने के लिए इस टेम्पलेट-संचालित फ़ॉर्म फ़ील्ड पर आप किस Angular टेम्पलेट सिंटैक्स का उपयोग कर सकते हैं?

```html
<input type="text" ngModel name="firstName" required minlength="4" />
<span *ngIf="">Invalid field data</span>
```

- [x] आप टेम्पलेट संदर्भ चर और exportAs सुविधा का उपयोग कर सकते हैं जो ngModel डायरेक्टिव में है।
- [ ] आप इनपुट फ़ील्ड नाम के संयोजन में ngModel डायरेक्टिव का उपयोग कर सकते हैं।
- [ ] आप HTML इनपुट एलिमेंट के लिए टेम्पलेट संदर्भ चर का उपयोग कर सकते हैं और फिर उसकी valid प्रॉपर्टी की जांच कर सकते हैं।
- [ ] टेम्पलेट-संचालित फ़ॉर्म के साथ फ़ील्ड मान तक पहुंच प्राप्त करना संभव नहीं है। इसके लिए आपको रिएक्टिव फ़ॉर्म का उपयोग करना होगा।

#### प्र23. इस मार्कअप में headerText टेम्पलेट संदर्भ चर में संग्रहीत होने वाला मान प्रकार क्या है?

```html
<h1 #headerText>User List</h1>
```

- [x] एक Angular ElementRef, एक नेटिव एलिमेंट के चारों ओर एक रैपर
- [ ] `<h1>` एलिमेंट का आंतरिक टेक्स्ट
- [ ] एक हेडर कंपोनेंट क्लास
- [ ] HTMLHeadingElement का नेटिव DOM एलिमेंट प्रकार

#### प्र24. इन दो प्रोवाइडर कॉन्फ़िगरेशन के आधार पर परिणामी कोड लॉजिक में क्या अंतर है, यदि कोई है?

```ts
[{ provide: FormattedLogger, useClass: Logger }][{ provide: FormattedLogger, useExisting: Logger }];
```

- [ ] वे समान हैं। दोनों Logger के एक नए इंस्टेंस का परिणाम होंगे जो FormattedLogger टोकन से बाउंड है।
- [x] useClass सिंटैक्स इंजेक्टर को Logger का एक नया इंस्टेंस बनाने और उस इंस्टेंस को FormattedLogger टोकन से बाइंड करने के लिए कहता है। useExisting सिंटैक्स Logger के रूप में घोषित पहले से मौजूद ऑब्जेक्ट इंस्टेंस को संदर्भित करता है।
- [ ] दोनों गलत हैं। useClass या useExisting के लिए एक strong type का उपयोग नहीं किया जा सकता है।
- [ ] वे समान हैं। दोनों FormattedLogger टोकन को Logger के इंस्टेंस के लिए एक उपनाम होने का परिणाम होंगे।

#### प्र25. रूट कॉन्फ़िगरेशन में data प्रॉपर्टी (नीचे दिए गए उदाहरण में देखी गई) का उद्देश्य क्या है?

```ts
   {
       path: 'customers',
       component: CustomerListComponent,
       data: { accountSection: true }
   }
```

- [ ] रूटेड कंपोनेंट इंस्टेंस पर @Input मानों को सेट करने के लिए एक key/value मैपिंग
- [x] रूट से जुड़े स्थिर, केवल-पढ़ने योग्य डेटा को शामिल करने का एक तरीका जिसे ActivatedRoute से पुनर्प्राप्त किया जा सकता है
- [ ] रूट के लिए गतिशील डेटा लोड करने के लिए उपयोग की जा सकने वाली प्रॉपर्टी
- [ ] एक ऑब्जेक्ट जो रूटेड कंपोनेंट के constructor में स्वतः इंजेक्ट हो जाएगा।

#### प्र26. बिल्ट-इन `ngIf` स्ट्रक्चरल डायरेक्टिव इस टेम्पलेट सिंटैक्स के आधार पर रेंडर किए गए DOM को कैसे बदलता है?

```ts
@Component({
  selector: 'app-product',
  template: '<div *ngIf="product">{{ product.name }}</div>',
})
export class ProductComponent {
  @Input() product;
}
```

- [ ] `<div>` एक प्लेसहोल्डर के रूप में कार्य करता है। यदि product क्लास फ़ील्ड "truthy" है, तो `<div>` को केवल `product.name` मान से बदल दिया जाएगा; यदि नहीं, तो कुछ भी रेंडर नहीं होगा।
- [ ] `<div>` हमेशा रेंडर होगा, और यदि product फ़ील्ड "truthy" है, तो `<div>` एलिमेंट में `product.name` मान होगा; अन्यथा, यह बिना किसी मान के `<div>` एलिमेंट को रेंडर करेगा।
- [ ] यह एक त्रुटि उत्पन्न करता है क्योंकि ngIf एक बिल्ट-इन स्ट्रक्चरल डायरेक्टिव नहीं है।
- [x] यदि product क्लास फ़ील्ड "truthy" है, तो रेंडर किए गए DOM में `product.name` फ़ील्ड के मान के साथ `<div>` शामिल होगा। यदि यह "truthy" नहीं है, तो रेंडर किए गए DOM में `<div>` एलिमेंट नहीं होगा।

#### प्र27. यह कोड क्या पूरा करता है?

```ts
@NgModule({
  declarations: [AppComponent],
  imports: [BrowserModule],
  bootstrap: [AppComponent],
})
export class AppModule {}

platformBrowserDynamic().bootstrapModule(AppModule);
```

- [ ] यह एक NgModule के लिए यूनिट टेस्ट निष्पादित करता है।
- [ ] यह एक Angular एप्लिकेशन की दस्तावेज़ संरचना को कोड करने का एक तरीका प्रदान करता है। @NgModule इनलाइन कोड टिप्पणी का एक रूप है जो TypeScript कंपाइलर द्वारा अनदेखा किया जाता है लेकिन कोड एडिटर एप्लिकेशन में विशेष फ़ॉर्मेटिंग के साथ दिखाई देगा।
- [ ] यह AppModule नामक एक Angular मॉड्यूल घोषित करता है और इसे पूरे एप्लिकेशन में lazy loading के लिए उपलब्ध कराता है।
- [x] यह AppModule नामक एक Angular मॉड्यूल घोषित करता है जिसमें AppComponent नामक एक bootstrapped कंपोनेंट होता है। फिर यह उस मॉड्यूल को Angular के साथ पंजीकृत करता है, ताकि ऐप शुरू हो सके।

#### प्र28. इस रूट कॉन्फ़िगरेशन में _resolve_ प्रॉपर्टी का सबसे अच्छा विवरण कौन सा है?

```ts
{
   path: ':id',
   component: UserComponent,
   resolve: {
     user: UserResolverService
   }
}
```

- [x] _UserComponent_ को लोड करने से पहले, राउटर _UserResolverService_ में एक _resolve_ विधि द्वारा लौटाए गए _Observable_ को सदस्यता लेगा। इस तकनीक का उपयोग एक _route_ के लिए प्रीलोडेड डेटा प्राप्त करने के लिए किया जा सकता है।
- [ ] _route_ को हल करने के बाद, और कंपोनेंट लोड और रेंडर होने के बाद, _UserResolverService_ में _user_ नामक एक विधि चलेगी जो किसी भी खुले डेटा कनेक्शन को साफ करेगी।
- [ ] एक त्रुटि है। सही प्रॉपर्टी नाम _onResolve_ है।
- [ ] _UserComponent_ के constructor में _user_ के लिए एक पैरामीटर होगा, और _router_ _UserResolverService_ में एक _user_ विधि को कॉल करके उसके लिए एक मान इंजेक्ट करने को संभालेगा।

#### प्र29. इस कंपोनेंट क्लास में ContentChildren डेकोरेटर का उद्देश्य क्या है?

```ts
@Component({
 . . .
 template: '<ng-content></ng-content>'
})
export class TabsListComponent {
 @ContentChildren(TabComponent) tabs;
}
```

- [ ] यदि कोई _TabsComponent_ एलिमेंट _TabsListComponent_ टेम्पलेट में जोड़े जाते हैं, तो वे रनटाइम पर `<ng-content>` एलिमेंट में डाल दिए जाएंगे।
- [ ] यह _TabsListComponent_ टेम्पलेट में _TabComponent_ कंपोनेंट्स बनाता है जब एक _TabsListComponent_ को instantiate किया जाता है।
- [x] यह कंपोनेंट क्लास के भीतर से किसी भी _TabComponent_ कंपोनेंट्स तक पहुंच प्रदान करता है जो इस कंपोनेंट के लिए `<ng-content>` में content projected थे।
- [ ] यह _TabsListComponent_ एलिमेंट में डाले जा सकने वाले अनुमत एलिमेंट्स को केवल _TabComponent_ एलिमेंट्स की अनुमति देने के लिए प्रतिबंधित करता है।

#### प्र30. Angular को एप्लिकेशन में कंपोनेंट्स को प्रोसेस करने के लिए, कंपोनेंट प्रकारों को कहाँ पंजीकृत करने की आवश्यकता है?

- [ ] index.html फ़ाइल में script टैग के भीतर
- [ ] NgModule डेकोरेटर मेटाडेटा टैग में जिसका नाम _components_ है
- [ ] कोई पंजीकरण की आवश्यकता नहीं है बस कंपोनेंट फ़ाइलों को ऐप डायरेक्टरी में शामिल करें।
- [x] NgModule डेकोरेटर मेटाडेटा प्रॉपर्टी में जिसका नाम _declarations_ है

#### प्र31. इस यूनिट टेस्ट में `fixture.detectChanges()` कॉल का उद्देश्य क्या है?

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

- [ ] यह किसी भी संभावित UI परिवर्तन को ट्रैक करता है और यदि कोई बनाया गया है तो यूनिट टेस्ट विफल हो जाएगा।
- [ ] इसका उपयोग पूरे टेस्ट सूट में कई यूनिट टेस्ट में कंपोनेंट टेम्पलेट स्थिरता सुनिश्चित करने के लिए किया जाता है।
- [x] यह Angular को परिवर्तन पहचान करने के लिए मजबूर करता है, जो आपके टेम्पलेट को मान्य करने से पहले _UserCardComponent_ को रेंडर करेगा।
- [ ] इसका उपयोग यूनिट टेस्ट रन के दौरान कंसोल में परिवर्तन-पहचान इवेंट्स को लॉग करने के लिए किया जाता है।

#### प्र32. जब goToUser को मान 15 पास किया जाता है, तो `Router.navigate` विधि की निम्नलिखित कॉल के आधार पर URL सेगमेंट कैसा दिखेगा?

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

#### प्र33. जब एक सेवा को रूट के लिए प्रदान किया जाता है और lazy-loaded मॉड्यूल के लिए प्रोवाइडर कॉन्फ़िगरेशन में भी जोड़ा जाता है, तो injector lazy-loaded मॉड्यूल में constructors को उस सेवा का कौन सा इंस्टेंस प्रदान करता है?

- [x] जब मॉड्यूल lazy loaded होता है तो उस सेवा का एक नया इंस्टेंस बनाया जाता है।
- [ ] lazy-loaded मॉड्यूल स्तर पर समान प्रकार की सेवा प्रदान करने की अनुमति नहीं है।
- [ ] यदि रूट स्तर पर अभी तक सेवा का इंस्टेंस नहीं बनाया गया है, तो यह वहां एक बनाएगा और फिर इसका उपयोग करेगा।
- [ ] उस सेवा का एक single इंस्टेंस हमेशा रूट पर instantiated होता है और केवल एक ही उपयोग किया जाता है, जिसमें lazy मॉड्यूल के भीतर भी शामिल है।

#### प्र34. इस डायरेक्टिव में HostBinding डेकोरेटर क्या कर रहा है?

```ts
@Directive({
  selector: ' [appHighlight] ',
})
export class HighlightDirective {
  @HostBinding('class.highlighted') highlight = true;
}
```

- [x] यह किसी भी DOM एलिमेंट में highlighted नामक CSS क्लास जोड़ रहा है जिस पर appHighlight डायरेक्टिव है।
- [ ] HostBinding डायरेक्टिव्स पर कुछ नहीं करता है, केवल कंपोनेंट्स पर।
- [ ] यह निर्दिष्ट करता है कि यदि होस्ट एलिमेंट को इसकी class एट्रिब्यूट में highlighted क्लास जोड़ी जाती है, तो डायरेक्टिव क्लास फ़ील्ड highlight को true पर सेट किया जाएगा; और यदि होस्ट पर नहीं जोड़ा गया है तो इसे false पर सेट किया जाएगा।
- [ ] यह होस्ट एलिमेंट पर एक इनलाइन स्टाइल बना रहा है जिसमें highlight नामक CSS प्रॉपर्टी true पर सेट है।

#### प्र35. रिएक्टिव फॉर्म्स में, नेटिव DOM `<form>` एलिमेंट पर इसे वायर करने के लिए किस Angular फॉर्म क्लास प्रकार का उपयोग किया जाता है?

- [ ] `FormArray`
- [ ] `FormControl`
- [x] `FormGroup`
- [ ] `इन सभी उत्तरों`

#### प्र36. मान लें कि username FormControl को एक minLength validator के साथ कॉन्फ़िगर किया गया है, आप username फ़ील्ड के लिए निम्नलिखित रिएक्टिव फॉर्म मार्कअप में त्रुटि प्रदर्शन कैसे सेट कर सकते हैं?

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

#### प्र37. एम्युलेटेड व्यू एनकैप्सुलेशन मोड एक कंपोनेंट के लिए CSS को कैसे संभालता है?

- [ ] यह CSS को बिल्कुल वैसे ही रेंडर करता है जैसे आपने इसे बिना किसी बदलाव के लिखा है।
- [ ] यह shadow DOM मार्कअप और CSS का उपयोग करता है।
- [x] यह DOM एलिमेंट्स के लिए अद्वितीय एट्रिब्यूट बनाता है और आपके द्वारा लिखे गए CSS सिलेक्टर्स को उन एट्रिब्यूट IDs पर स्कोप करता है।
- [ ] यह आपके द्वारा लिखे गए सभी CSS नियमों को आपके द्वारा टेम्पलेट में उपयोग किए जाने वाले सभी DOM एलिमेंट्स पर इनलाइन CSS के रूप में रेंडर करता है।

#### प्र38. निम्नलिखित TestBed सेटअप के साथ, UserCardComponent के लिए रेंडर किए गए DOM तक पहुंचने के लिए क्या उपयोग किया जा सकता है?

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

#### प्र39. इन दो कंपोनेंट्स को देखते हुए, मार्कअप उपयोग के आधार पर DOM में क्या रेंडर होगा?

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

// मार्कअप उपयोग:
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

#### प्र40. नीचे दिए गए कोड में app-title-card कंपोनेंट को देखते हुए, app-user-card कंपोनेंट कौन सा DOM रेंडर करेगा?

```ts
@Component({
   selector: 'app-user-card',
   template: '<app-title-card></app-title-card><p>Jenny Smith</p>'
})

@Component({
   selector: 'app-title-card',
   template: '<h1>User Data</hl>'
})

// पैरेंट कंपोनेंट html में user card कंपोनेंट का उपयोग
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

#### प्र41. कस्टम प्रोवाइडर पंजीकरण के लिए मेल खाने वाला कोड चुनें जिसे @Inject () डेकोरेटर खोज रहा है:

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

#### प्र42. getsettings क्लास विधि में HttpClient.get विधि के निम्नलिखित उपयोग का सर्वोत्तम विवरण कौन सा है?

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

- [ ] RxJs pipe विधि subscribe विधि के लिए एक उपनाम है, इसलिए `getSettings` के लिए एक कॉल get क्वेरी को निष्पादित करेगी। retry ऑपरेटर का उपयोग pipe कॉल को get क्वेरी को तीन बार retry करने के लिए किया जाता है।
- [ ] यह रनटाइम पर एक त्रुटि उत्पन्न करेगा क्योंकि pipe विधि `Httpclient.get` कॉल से उपलब्ध नहीं है।
- [ ] getSettings विधि के प्रत्येक single कॉल के परिणामस्वरूप Httpclient settingsUrl के लिए कुल तीन get अनुरोध करेगा, जो आदर्श नहीं है क्योंकि हमेशा दो अतिरिक्त कॉल होंगी जिनकी आवश्यकता नहीं है। retry ऑपरेटर का इस तरह से उपयोग नहीं किया जाना चाहिए।
- [x] जब getSettings विधि के परिणाम की सदस्यता ली जाएगी, तो HTTP GET कॉल की जाएगी; यदि यह विफल होती है, तो यह हार मानने और त्रुटि वापस करने से पहले तीन बार तक retry की जाएगी।

#### प्र43. जब किसी सेवा को एक विधि के माध्यम से अपनी default स्थिति को आरंभ करने के लिए कुछ सेटअप की आवश्यकता होती है, तो आप यह कैसे सुनिश्चित कर सकते हैं कि सेवा को कहीं भी इंजेक्ट करने से पहले उस विधि को invoke किया जाए?

- [ ] उस सेवा विधि के तर्क को सेवा constructor में डालें।
- [x] रूट AppModule स्तर पर एक factory provider का उपयोग करें जो उस सेवा विधि को कॉल करने के लिए सेवा पर निर्भर करता है।
- [ ] एप्लिकेशन शुरुआत में यह करना संभव नहीं है; आप इसे केवल कंपोनेंट स्तर पर कर सकते हैं।
- [ ] वैश्विक स्तर (window scope) पर सेवा का एक इंस्टेंस instantiate करें और फिर उस विधि को कॉल करें।

#### प्र44. TestBed के इस उपयोग का सबसे अच्छा विवरण कौन सा है?

```ts
const spy = jasmine.createSpyObj('DataService', ['getUsersFromApi']);
TestBed.configureTestingModule({
  providers: [UserService, { provide: DataService, useValue: spy }],
});
const userService = TestBed.get(UserService);
```

- [ ] TestBed की आवश्यकता हर बार होती है जब आप Angular provider के लिए यूनिट टेस्ट में spy ऑब्जेक्ट का उपयोग करना चाहते हैं।
- [ ] TestBed का उपयोग कंपोनेंट के view को टेस्ट करने के लिए किया जा रहा है।
- [x] TestBed दो प्रोवाइडर के साथ एक NgModule को scaffold करता है और किसी भी dependency injection को संभालता है। यदि कोई Angular क्लास अपने constructor में DataService का अनुरोध करती है, तो TestBed उस constructor में spy इंजेक्ट करेगा।
- [ ] TestBed टेस्ट रनर को कॉन्फ़िगर कर रहा है ताकि वह इसे केवल अपने providers सरणी में सूचीबद्ध दो प्रोवाइडर के लिए टेस्ट निष्पादित करने के लिए कह सके।

#### प्र45. कंपोनेंट और डायरेक्टिव के बीच प्राथमिक अंतर क्या है?

- [ ] कंपोनेंट एक selector मेटाडेटा प्रॉपर्टी का उपयोग करता है और डायरेक्टिव नहीं करता है।
- [ ] डायरेक्टिव का उपयोग DOM में कस्टम इवेंट जोड़ने के लिए किया जा सकता है और कंपोनेंट नहीं कर सकता है।
- [x] कंपोनेंट का एक टेम्पलेट होता है और डायरेक्टिव का नहीं होता है।
- [ ] डायरेक्टिव केवल नेटिव DOM एलिमेंट्स को लक्षित कर सकता है।

#### प्र46. मार्कअप में डायरेक्टिव उपयोग के दौरान truncate लंबाई को सेट करने की अनुमति देने के लिए आप इस डायरेक्टिव क्लास में क्या जोड़ सकते हैं?

```ts
@Directive({
    selector: '[appTruncate]'
})
export class TruncateDirective {
    . . .
}

// वांछित उपयोग का उदाहरण:
<p [appTruncate]="10">Some very long text here</p>
```

- [x] `@Input() appTruncate: number;`
- [ ] `@Output() appTruncate;`
- [ ] `constructor(maxLength: number) { }`
- [ ] `कुछ नहीं। डायरेक्टिव सिलेक्टर का उपयोग डायरेक्टिव में मान पास करने के लिए नहीं किया जा सकता है।`

#### प्र47. आप इस `HttpClient.get` अनुरोध में क्वेरी पैरामीटर कैसे पास कर सकते हैं?

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

#### प्र48. मान लें कि `DataService` को एप्लिकेशन के लिए प्रोवाइडर में पंजीकृत किया गया है, इस कंपोनेंट के constructor के आधार पर क्या होता है इसका सर्वोत्तम विवरण कौन सा है?

```ts
@Component({
    ...
})
export class OrderHistoryComponent {
    constructor(private dataService: DataService) {}
    ...
}
```

- [ ] यह घोषित करता है कि `OrderHistoryComponent` का `DataService` का अपना संस्करण होगा और इसे कभी भी किसी मौजूदा इंस्टेंस का उपयोग नहीं करना चाहिए। इस कोड को पूर्ण और कार्यशील होने के लिए `DataService` को क्लास के भीतर एक private फ़ील्ड के रूप में instantiate करने की आवश्यकता होगी।
- [x] जब Angular `OrderHistoryComponent` का एक नया इंस्टेंस बनाता है, तो injector कंपोनेंट constructor के पहले तर्क में `DataService` क्लास का एक इंस्टेंस प्रदान करेगा। constructor का `dataService` पैरामीटर इंस्टेंस पर समान नाम के साथ एक private इंस्टेंस फ़ील्ड सेट करने के लिए उपयोग किया जाएगा।
- [ ] यह केवल कंपोनेंट टेस्टिंग करने का एक तरीका प्रदान करता है; Angular एप्लिकेशन के वास्तविक रन में constructor का कोई उपयोग नहीं है।
- [ ] यह कस्टम एलिमेंट जिसे कंपोनेंट लक्षित करता है, को `dataService` नामक एक कस्टम प्रॉपर्टी रखने में सक्षम बनाता है जिसका उपयोग मौजूदा `DataService` इंस्टेंस को बाइंड करने के लिए किया जा सकता है।

#### प्र49. `ngIf` डायरेक्टिव का उपयोग करके इस मार्कअप को पूरा करें ताकि एक else केस लागू किया जा सके जो "User is not active" टेक्स्ट प्रदर्शित करेगा:

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

#### प्र50. फीचर मॉड्यूल को lazy load करने के लिए रूट परिभाषा के लिए सही सिंटैक्स क्या है?

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

#### प्र51. इस रिएक्टिव फॉर्म उदाहरण में validation कैसे सेट अप और कॉन्फ़िगर किया गया है:

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

- [ ] `username` के लिए `FormControl` उन तीन validators को बाहर करने के लिए कॉन्फ़िगर हो रहा है जो इसे उपयोग करने की अनुमति है।
- [ ] `username` के लिए `FormControl` तीन संभावित validators का उपयोग करने की अनुमति देने के लिए कॉन्फ़िगर हो रहा है: `required, maxLength`, और `unique` नामक एक कस्टम। इन `validators` को सक्षम करने के लिए, मार्कअप में फॉर्म फ़ील्ड पर एक validator डायरेक्टिव रखना होगा।
- [ ] रिएक्टिव फॉर्म में validation को इस तरह से सेट अप नहीं किया जा सकता है।
- [x] `username` के लिए `FormControl` तीन validators के साथ कॉन्फ़िगर हो रहा है: Angular से आने वाले `required` और `minLength` validators, और `unique` नामक एक कस्टम validator फ़ंक्शन जो मान की जांच करता है कि यह string `admin` के बराबर नहीं है।

#### प्र52. इस सेवा क्लास पर Injectable डेकोरेटर क्या करता है?

```ts
@Injectable({
    providedIn: 'root'
)}
export class DataService { }
```

- [ ] यह सेवा के लिए एक provider पंजीकृत करता है जो केवल रूट मॉड्यूल स्तर पर उपलब्ध है, किसी भी चाइल्ड मॉड्यूल के लिए नहीं।
- [x] यह रूट एप्लिकेशन injector में सेवा के लिए एक provider पंजीकृत करता है, जो पूरे एप्लिकेशन में इसका एक single इंस्टेंस उपलब्ध कराता है।
- [ ] यह इसे इस तरह बनाता है कि सेवा को केवल एप्लिकेशन के लिए bootstrapped कंपोनेंट में इंजेक्ट किया जा सकता है।
- [ ] यह एक compile time नियम सेट करता है जो आपको रूट NgModule की providers मेटाडेटा प्रॉपर्टी में केवल सेवा प्रकार डालने की अनुमति देता है।

#### प्र53. इस कोड के उपयोग का वर्णन करें

```ts
export interface AppSettings {
  title: string;
  version: number;
}
export const APP_SETTINGS = new InjectionToken<AppSettings>('app.settings');
```

- [ ] InjectionToken, InjectionToken constructor कॉल के माध्यम से रूट provider में AppSettings का एक इंस्टेंस जोड़ता है, जो इसे Angular एप्लिकेशन में सभी NgModules, services और components के लिए स्वचालित रूप से उपलब्ध कराता है बिना इसे कहीं भी इंजेक्ट करने की आवश्यकता के।
- [x] InjectionToken का उपयोग गैर-class dependency के लिए provider token बनाने के लिए किया जाता है। APP_SETTINGS dependency provider प्रकार के लिए एक Object literal को मान के रूप में प्रदान किया जा सकता है जिसे फिर कंपोनेंट्स, services, आदि में इंजेक्ट किया जा सकता है।
- [ ] InjectionToken का उपयोग AppSettings के लिए एक dynamic डेकोरेटर बनाने के लिए किया जाता है जिसका उपयोग @AppSettings डेकोरेटर के माध्यम से constructor पैरामीटर पर किया जा सकता है।
- [ ] इस कोड में एक त्रुटि है क्योंकि आप InjectionToken पर generic प्रकार के लिए TypeScript interface का उपयोग नहीं कर सकते हैं

#### प्र54. निम्नलिखित टेम्पलेट-संचालित फॉर्म उदाहरण के लिए, फॉर्म के डेटा को सबमिट करने के लिए click इवेंट में submit विधि को कौन सा तर्क पास किया जा सकता है?

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

#### प्र55. इस router कोड में `prelodingStrategy` प्रॉपर्टी कॉन्फ़िगरेशन का उद्देश्य क्या है?

```ts
RouterModule.forRoot(
  ...{
    preloadingStrategy: PreloadAllModules,
  },
);
```

- [ ] यह व्यक्तिगत रूट को preloading के लिए flag करने का विकल्प सक्षम करता है।
- [ ] यह रूट के लिए सभी dependencies को preload करता है, जब ऐप पहली बार शुरू होता है तो services के इंस्टेंस बनाता है
- [ ] यह सुनिश्चित करता है कि सभी modules एक single ऐप मॉड्यूल bundle फ़ाइल में built हों।
- [x] यह router को तुरंत सभी रूट को लोड करने के लिए कॉन्फ़िगर करता है जिनमें loadChildren प्रॉपर्टी है (रूट जो आमतौर पर अनुरोध किए जाने पर लोड होते हैं)

#### प्र56. इस मार्कअप को लिखने का एक वैकल्पिक तरीका क्या है ताकि क्लास फ़ील्ड `userName` के मान को `h1` एलिमेंट title प्रॉपर्टी से बाइंड किया जा सके?

```html
<h1 [title]="userName">Current user is {{ userName }}</h1>
```

- [ ] `title="userName"`
- [x] `title="{{ userName }}"`
- [ ] `title="{{ 'userName' }}"`
- [ ] इसे करने का एकमात्र तरीका वर्ग कोष्ठक का उपयोग करना है।

#### प्र57. इस उदाहरण में `async` पाइप क्या कर रहा है?

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

- [ ] यह कुछ नहीं कर रहा है क्योंकि async पाइप का उपयोग `ngFor` statement में नहीं किया जा सकता है।
- [ ] यह `ngFor` iteration को एक साथ कई उपयोगकर्ताओं की सूचियों का समर्थन करने के लिए कॉन्फ़िगर कर रहा है।
- [x] यह `HttpClient.get` विधि से लौटाए गए observable की सदस्यता ले रहा है और लौटाए गए मान को unwrap कर रहा है ताकि इसे `ngFor` में iterate किया जा सके।
- [ ] यह `users` फ़ील्ड में सभी उपयोगकर्ताओं को DOM में एक साथ render होने की अनुमति दे रहा है।

#### प्र58. आप इस डायरेक्टिव को इसके selector मान के आधार पर मार्कअप में कैसे उपयोग करेंगे

```ts
@Directive({  selector: '[appTruncate]'
})
export class TruncateDirective{  . . .
}
```

- [ ] `html <p data-directive="appTruncate">Some long text </p>`
- [x] `html <p appTruncate>Some long text</p>`
- [ ] `html <p app-truncate>Some long text</p>`
- [ ] `html <app-truncate>Some long text</app-truncate>`

#### प्र59. किस lifecycle hook का उपयोग कंपोनेंट पर उस कंपोनेंट पर सभी @Input मानों में परिवर्तनों की निगरानी के लिए किया जा सकता है?

- [ ] ngOnInit
- [ ] ngChanges
- [ ] ngAfterInputChange
- [x] ngOnChanges

#### प्र60. इस कस्टम पाइप के टेम्पलेट सिंटैक्स उपयोग का एक उदाहरण क्या होगा?

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
- [ ] इन सभी उत्तरों

#### प्र61. आप UsersComponent जेनरेट करने और इसे SharedModule (आपके एप्लिकेशन में shared.module.ts फ़ाइल में) में जोड़ने के लिए कौन सा Angular CLI कमांड चलाएंगे?

- [ ] ng generate component --newModule=shared
- [x] ng generate component users --module=shared
- [ ] ng generate component users --shared
- [ ] ng generate component --add=shared

#### प्र62. आप इस मार्कअप को कैसे फिर से लिख सकते हैं ताकि अंतिम DOM render में div container की आवश्यकता न हो

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

#### प्र63. आप इस एलिमेंट पर inline style width CSS प्रॉपर्टी के लिए tabWidth नामक कंपोनेंट क्लास फ़ील्ड को बाइंड करने के लिए टेम्पलेट सिंटैक्स का उपयोग कैसे कर सकते हैं?

```html
<div class="tab"></div>
```

- [ ] `{{ width: tabWidth }}`
- [ ] `[width]="tabWidth"`
- [ ] `[inline.width]="tabWidth"`
- [x] `[style.width.px]="tabWidth"`

#### प्र64. बिना constructor dependencies वाली सेवा को यूनिट टेस्ट करने के लिए कौन सी Angular utilities की आवश्यकता है, यदि कोई है?

- [ ] By.css() helper विधि की आवश्यकता है
- [ ] सेवा को यूनिट टेस्ट के लिए चलाने के लिए एक text fixture की आवश्यकता है।
- [ ] कोई नहीं। एक सेवा को स्वयं instantiated और यूनिट टेस्ट किया जा सकता है।
- [x] सेवा को instantiate करने के लिए TestBed क्लास की आवश्यकता है।

#### प्र65. CanActivate और CanLoad रूट गार्ड्स के बीच क्या अंतर है?

- [ ] CanActivate का उपयोग पहुंच की जांच करने के लिए किया जाता है। CanLoad का उपयोग रूट के लिए डेटा को preload करने के लिए किया जाता है।
- [ ] CanLoad का उपयोग ऐप startup पर रूट को रूट टेबल में जोड़ने की अनुमति देने या अस्वीकार करने के लिए किया जाता है। CanActivate का उपयोग रूट के अनुरोध किए जाने पर उन तक पहुंच का प्रबंधन करने के लिए किया जाता है।
- [ ] CanActivate और CanLoad बिल्कुल समान काम करते हैं।
- [x] CanLoad एक पूरे NgModule को deliver और लोड होने से रोकता है। CanActivate उस NgModule में एक कंपोनेंट तक रूटिंग को रोकता है, लेकिन वह मॉड्यूल अभी भी लोड होता है।

#### प्र66. इस टेम्पलेट सिंटैक्स में, हर बार items प्रॉपर्टी बदलती है (जोड़ी गई, से हटाई गई, आदि), ngFor स्ट्रक्चरल डायरेक्टिव loop में सभी DOM एलिमेंट्स के लिए अपना तर्क फिर से चलाता है। इसे अधिक performant बनाने के लिए किस सिंटैक्स का उपयोग किया जा सकता है?

```html
<div *ngFor="let item of items">{{ item.id }} - {{ item.name }}</div>
```

- [ ] `*ngFor="let item of items; let uniqueItem"`
- [ ] `*ngFor="let item of items.distinct()"`
- [ ] `*ngFor="let item of items: let i = index"`
- [x] `*ngFor="let item of items; trackBy: trackById"`

#### प्र67. यह Angular CLI कमांड क्या करती है?

```bash
ng build --configuration=production --progress=false
```

- [ ] यह Angular एप्लिकेशन को build करती है, build कॉन्फ़िगरेशन को angular.json फ़ाइल में निर्दिष्ट "production" target पर सेट करती है, और progress output को console में log करती है।
- [ ] यह Angular एप्लिकेशन को build करती है, build कॉन्फ़िगरेशन को angular.json फ़ाइल में निर्दिष्ट "production" target पर सेट करती है, और परिवर्तनों के लिए फ़ाइलों को watching करती है।
- [ ] यह Angular एप्लिकेशन को build करती है, build कॉन्फ़िगरेशन को angular.json फ़ाइल में निर्दिष्ट "production" target पर सेट करती है, और परिवर्तनों के लिए फ़ाइलों को watching अक्षम करती है।
- [x] यह Angular एप्लिकेशन को build करती है, build कॉन्फ़िगरेशन को angular.json फ़ाइल में निर्दिष्ट "production" target पर सेट करती है, और progress output को console में रोकती है।

#### प्र68. सेवा क्लासेस को किन डेकोरेटर के माध्यम से providers के रूप में पंजीकृत किया जा सकता है?

- [ ] @Injectable, @NgModule, @Component, और @Directive।
- [x] केवल @Injectable।
- [ ] केवल @Injectable और @NgModule।
- [ ] केवल @Service और @NgModule।

#### प्र69. इस कंपोनेंट क्लास में Input डेकोरेटर का उपयोग किसके लिए किया जाता है?

```ts
@Component({  selector:'app-product-name',  ...
})
export class ProductNameComponent {  @Input() productName: string
}
```

- [ ] इसका उपयोग केवल documentation के लिए क्लास फ़ील्ड के सामने टिप्पणी डालने के लिए किया जाता है।
- [x] यह कंपोनेंट selector का उपयोग करके productName फ़ील्ड में मानों को बाइंड करने का एक तरीका प्रदान करता है।
- [ ] यह कंपोनेंट टेम्पलेट में स्वचालित रूप से एक `<input type='text' id='productName'>` Dom एलिमेंट जेनरेट करता है।
- [ ] यह productName इंस्टेंस फ़ील्ड में मानों को बाइंड करने का एक तरीका प्रदान करता है, बिल्कुल नेटिव DOM एलिमेंट प्रॉपर्टी bindings की तरह।

#### प्र70. किस रूट गार्ड का उपयोग रूट तक navigation को मध्यस्थ करने के लिए किया जा सकता है?

- [x] इन सभी उत्तरों।
- [ ] CanDeactivate।
- [ ] CanLoad
- [ ] CanActivate।

#### प्र71. आप injector को क्लास इंस्टेंस को instantiate करने के बजाय एक token के लिए एक मौजूदा ऑब्जेक्ट का उपयोग करने के लिए कैसे कॉन्फ़िगर कर सकते हैं?

- [x] `useValue` provider कॉन्फ़िगरेशन का उपयोग करें और इसे एक मौजूदा ऑब्जेक्ट या एक ऑब्जेक्ट literal के बराबर सेट करें।
- [ ] यह संभव नहीं है। Providers को केवल class प्रकारों के साथ कॉन्फ़िगर किया जा सकता है।
- [ ] बस ऑब्जेक्ट इंस्टेंस या literal को provider की सरणी में जोड़ें।
- [ ] `asValue` provider कॉन्फ़िगरेशन प्रॉपर्टी का उपयोग करें, इसे true पर सेट करें।

#### प्र72. इस रूट परिभाषा के आधार पर, id रूट पैरामीटर को प्राप्त करने के लिए UserDetailComponent constructor में क्या इंजेक्ट किया जा सकता है?

```ts
{path: 'user/:id', component: UserDetailComponent }
```

- [x] ActivatedRoute
- [ ] CurrentRoute
- [ ] UrlPath
- [ ] @Inject('id')

#### प्र73. निम्नलिखित रिएक्टिव फॉर्म मार्कअप के साथ, आप onSubmit क्लास विधि को कॉल करने के लिए क्या जोड़ेंगे?

```html
<form [formGroup]="form">
  <input type="text" formControlName="username" />
  <button type="submit" [disabled]="form.invalid">Submit</button>
</form>
```

- [ ] इनमें से कोई भी उत्तर नहीं
- [ ] `<button>` एलिमेंट में (click)="onSubmit()" जोड़ें।
- [x] `<form>` एलिमेंट में (ngSubmit )="onSubmit()" जोड़ें।
- [ ] इन दोनों उत्तरों

#### प्र74. जब isActive true है तो ngClass एट्रिब्यूट डायरेक्टिव के इस उपयोग के लिए अपेक्षित DOM कोड क्या है?

```html
<div [ngClass]="{ 'active-item': isActive }">Item One</div>
```

- [ ] `<div active-item>Item One</div>`
- [x] `<div class="active-item">Item One</div>`
- [ ] `<div class="is-active">Item One</div>`
- [ ] `<div class="active-item isActive">Item One</div>`

#### प्र75. इस टेम्पलेट कोड में ngModel के उपयोग की सबसे अच्छी व्याख्या कौन सी है?

```html
<input [(ngModel)]="user.name" />
```

- [ ] यह सशर्त रूप से input एलिमेंट को प्रदर्शित कर रहा है यदि user.name प्रॉपर्टी का मान है।
- [x] यह two-way data binding सिंटैक्स है। input एलिमेंट value प्रॉपर्टी user.name प्रॉपर्टी से बाउंड होगी, और फॉर्म एलिमेंट के लिए value change इवेंट user.name प्रॉपर्टी मान को अपडेट करेगा।
- [ ] कोड में एक typo है। इसमें केवल वर्ग कोष्ठक होने चाहिए।
- [ ] यह user.name प्रॉपर्टी के मान को input एलिमेंट की val प्रॉपर्टी से बाइंड कर रहा है ताकि इसका प्रारंभिक मान सेट किया जा सके।

#### प्र76. NgModules को अन्य NgModules के भीतर शामिल किया जा सकता है। SharedModule में TableModule को शामिल करने के लिए आपको किस कोड सैंपल का उपयोग करना चाहिए?

- [ ] @NgModule({
      exports: [TableModule]
      })
      export class SharedModule {}

- [x] @NgModule({
      imports: [TableModule]
      })
      export class SharedModule {}

- [ ] @NgModule({
      declarations: [TableModule]
      })
      export class SharedModule {}

- [ ] @NgModule({
      providers: [TableModule]
      })
      export class SharedModule {}

#### प्र77. इस मार्कअप में सशर्त रूप से CSS क्लास नाम जोड़ने या हटाने के लिए कौन सा अन्य टेम्पलेट सिंटैक्स (ngClass डायरेक्टिव को बदलते हुए) का उपयोग किया जा सकता है?

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

#### प्र78. इस डायरेक्टिव डेकोरेटर उदाहरण में, provider ऑब्जेक्ट literal में multi प्रॉपर्टी का उद्देश्य क्या है?

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

- [ ] यह इंगित करता है कि CustomValidatorDirective का उपयोग कई फॉर्म एलिमेंट प्रकारों पर किया जा सकता है।
- [ ] यह CustomValidatorDirective के कई इंस्टेंस को instantiated होने की अनुमति देता है। multi के बिना, CustomValidatorDirective पूरे ऐप के लिए एक singleton होगा।
- [x] यह single NG_VALIDATORS token के लिए विभिन्न providers के पंजीकरण की अनुमति देता है। इस मामले में, यह CustomValidatorDirective को उपलब्ध फॉर्म validators की सूची में जोड़ रहा है।
- [ ] यह इंगित करता है कि कस्टम validator के लिए तर्क implementation को संभालने वाली कई classes होंगी।

#### प्र79. आप अपने यूनिट टेस्ट को एक ऐसी प्रक्रिया में चलाने के लिए कौन सा Angular CLI कमांड का उपयोग करेंगे जो फ़ाइल परिवर्तनों पर आपके टेस्ट सूट को फिर से चलाता है?

- [ ] ng test --single-run=false
- [ ] ng test --watch-files
- [ ] ng test --progress
- [x] ng test

#### प्र80. ngOnDestory lifecycle hook का सबसे आम उपयोग क्या है?

- [ ] कंपोनेंट के view से dom एलिमेंट्स को हटाना
- [ ] किसी भी इंजेक्टेड services को डिलीट करना
- [x] observables से unsubscribe करना और detach करना
- [ ] उपरोक्त सभी

#### प्र81. किसी रूट कॉन्फ़िगरेशन में data प्रॉपर्टी (नीचे दिए गए उदाहरण में देखी गई) का उपयोग अन्य को अनुमति देने के लिए किस NgModule डेकोरेटर मेटाडेटा प्रॉपर्टी का लाभ उठाया जाता है....?

- [ ] public
- [ ] experts
- [ ] Shared
- [x] declarations

#### प्र82. निम्नलिखित कंपोनेंट क्लास के साथ, टेम्पलेट में currentYear क्लास फ़ंक्शन को कॉल करने के परिणाम को प्रदर्शित करने के लिए आप टेम्पलेट में किस टेम्पलेट सिंटैक्स का उपयोग करेंगे?

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

- [x] `{{ currentYear() }}`
- [ ] `{{ component.currentYear() }}`
- [ ] `{{ currentYear }}`
- [ ] टेम्पलेट सिंटैक्स से क्लास फ़ंक्शन को कॉल नहीं किया जा सकता है।

#### प्र83. कंपोनेंट के लिए ViewChild डेकोरेटर का उद्देश्य क्या है?

```ts
@Component({
    selector: 'app-user-card',
    . . .
})
export class UserCardComponent {
    @ViewChild('bio') bio;
}
```

- [x] यह कंपोनेंट क्लास के भीतर से `<p>` टैग के लिए ElementRef ऑब्जेक्ट तक पहुंच प्रदान करता है जिसमें कंपोनेंट के टेम्पलेट व्यू में bio टेम्पलेट संदर्भ चर है।
- [ ] यह इंगित करता है कि `<p>` टैग को पैरेंट व्यू के चाइल्ड के रूप में रेंडर किया गया है जो इस कंपोनेंट का उपयोग करता है।
- [ ] यह टेम्पलेट में `<p>` टैग को कंटेंट प्रोजेक्शन का समर्थन करता है।
- [ ] यह अंतिम रेंडर में `<p>` टैग को दृश्यमान बनाता है। यदि #bio का उपयोग टेम्पलेट में किया गया था और @ViewChild का उपयोग क्लास में नहीं किया गया था, तो Angular स्वचालित रूप से `<p>` टैग को छुपा देगा जिस पर #bio है।

---

## अनुवाद पूर्ण

यह Angular प्रश्नोत्तरी का हिंदी अनुवाद है। सभी 83 प्रश्न और उनके विकल्प अनुवादित हैं।
