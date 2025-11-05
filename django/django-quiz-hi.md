## Django

#### प्र1. Django में एक एप्लिकेशन के लिए अपनी पूरी साइट को कैश करने के लिए, आप इन सेटिंग्स को छोड़कर सभी को जोड़ते हैं?

- [ ] django.middleware.common.CommonMiddleware
- [ ] django.middleware.cache.UpdateCacheMiddleware
- [ ] django.middleware.cache.FetchFromCacheMiddleware
- [x] django.middleware.cache.AcceleratedCacheMiddleware

**संदर्भ:**
Django एक मजबूत कैश सिस्टम के साथ आता है जो आपको गतिशील पृष्ठों को सहेजने देता है, इसलिए उन्हें प्रत्येक अनुरोध के लिए गणना करने की आवश्यकता नहीं होती है। सुविधा के लिए, Django विभिन्न स्तरों पर कैश प्रदान करता है - पूरी वेबसाइट से लेकर पृष्ठों तक पृष्ठों के हिस्सों तक DB क्वेरी परिणामों तक मेमोरी में किसी भी ऑब्जेक्ट तक। कैश मिडलवेयर। यदि सक्षम किया गया है, तो प्रत्येक Django-संचालित पृष्ठ URL के आधार पर कैश किया जाएगा।

#### प्र2. Django किस प्रोग्रामिंग भाषा में लिखा गया है?

- [ ] C++
- [ ] Java
- [x] Python
- [ ] Ruby

#### प्र3. किसी फ़ील्ड के लिए स्वचालित रूप से मान प्रदान करने के लिए, या एक से अधिक फ़ील्ड तक पहुंच की आवश्यकता वाली सत्यापन करने के लिए, आपको `___` वर्ग में `___` विधि को ओवरराइड करना चाहिए।

- [ ] validate(); Model
- [ ] group(); Model
- [ ] validate(); Form
- [x] clean(); Model

#### प्र4. एक ग्राहक चाहता है कि उनकी साइट "Rick & Morty" एपिसोड को संख्या या शीर्षक द्वारा लोड कर सके—उदा., shows/3/3 या shows/picklerick। आप कौन सा URL पैटर्न सुझाते हैं?

- [ ] A

```python
url(r'shows/<int:season>/<int:episode>/', views.episode_number),
url(r'shows/<slug:episode_name>/', views.episode_name)
```

- [x] B

```python
path('shows/<int:season>/<int:episode>/', views.episode_number),
path('shows/<slug:episode_name>/', views.episode_name)
```

- [ ] C

```python
path('shows/<int:season>/<int:episode>', views.episode_number),
path('shows/<slug:episode_name>/', views.episode_number)
```

- [ ] D

```python
url(r'^show/(?P<season>[0-9]+)/(?P<episode>[0-9]+)/$', views.episode_number),
url(r'^show/(?P<episode_name>[\w-]+)/', views.episode_name
```

#### प्र5. स्टार्टअप समय पर आप कैसे निर्धारित करते हैं कि मिडलवेयर के एक टुकड़े का उपयोग किया जाना चाहिए?

- [x] अपने मिडलवेयर के **init** फ़ंक्शन में MiddlewareNotUsed उठाएं।
- [ ] अपने मिडलवेयर वर्ग में not_used विधि लागू करें।
- [ ] django.middleware.IgnoredMiddleware की प्रविष्टि के नीचे मिडलवेयर को सूचीबद्ध करें।
- [ ] [app]/**init**.py में सेटिंग्स से मिडलवेयर को हटाने के लिए कोड लिखें।

#### प्र6. आप वेब पेज के किसी भाग के लिए Django की स्वचालित HTML एस्केपिंग को कैसे बंद करते हैं?

- [ ] उस अनुभाग को autoescape=off स्विच युक्त पैराग्राफ टैग के बीच रखें।
- [x] उस अनुभाग को { percentage mark autoescape off percentage mark} और {percentage mark endautoescape percentage mark} टैग के बीच लपेटें।
- [ ] उस अनुभाग को {percentage mark autoescapeoff percentage mark} और {percentage mark endautoescapeoff percentage mark} टैग के बीच लपेटें।
- [ ] आपको कुछ भी करने की आवश्यकता नहीं है—autoescaping डिफ़ॉल्ट रूप से बंद है।

#### प्र7. कौन सा चरण आपको "django-admin: command not found" त्रुटि का निवारण करने में मदद नहीं करेगा?

- [ ] जांचें कि आपकी Django निर्देशिका के अंदर bin फ़ोल्डर आपके सिस्टम पथ पर है।
- [ ] सुनिश्चित करें कि आपने Django युक्त वर्चुअल वातावरण को सक्रिय किया है।
- [ ] जांचें कि आपने Django स्थापित किया है।
- [x] सुनिश्चित करें कि आपने Django प्रोजेक्ट बनाया है।

#### प्र8. हर बार जब कोई उपयोगकर्ता सहेजा जाता है, तो उनके quiz_score की पुनर्गणना करने की आवश्यकता होती है। इस तर्क को जोड़ने के लिए एक आदर्श स्थान कहां हो सकता है?

- [ ] template
- [x] model
- [ ] database
- [ ] view

#### प्र9. Python में "Rainbow" नामक एक वर्ग शुरू करने का सही तरीका क्या है?

- [ ] Rainbow {}
- [ ] export Rainbow:
- [x] class Rainbow:
- [ ] def Rainbow:

#### प्र10. आपने एक Django प्रोजेक्ट विरासत में लिया है और इसे स्थानीय रूप से चलाना है। यह अपनी सभी निर्भरताओं वाली requirements.txt फ़ाइल के साथ आता है। आपको कौन सी कमांड का उपयोग करना चाहिए?

- [ ] django-admin startproject requirements.txt
- [ ] python install -r requirements.txt
- [x] pip install -r requirements.txt
- [ ] pip install Django

#### प्र11. कौन सी सर्वोत्तम प्रथा माइग्रेशन के लिए प्रासंगिक नहीं है?

- [x] यह सुनिश्चित करने के लिए कि आपके माइग्रेशन अद्यतित हैं, आपको अपने परीक्षण चलाने से पहले updatemigrations चलाना चाहिए।
- [ ] आपको माइग्रेशन चलाने से पहले अपने उत्पादन डेटाबेस का बैकअप लेना चाहिए।
- [ ] आपके माइग्रेशन कोड को स्रोत नियंत्रण के अधीन होना चाहिए।
- [ ] यदि किसी प्रोजेक्ट में बहुत अधिक डेटा है, तो आपको उत्पादन पर माइग्रेशन चलाने से पहले स्टेजिंग कॉपी के खिलाफ परीक्षण करना चाहिए।

#### प्र12. यह URL पैटर्न क्या मैच करेगा? url(r'^\$', views.hello)

- [ ] अक्षर R से शुरू होने वाली स्ट्रिंग
- [x] सर्वर रूट पर एक खाली स्ट्रिंग
- [ ] ^ और $ युक्त एक स्ट्रिंग
- [ ] URL में कहीं भी एक खाली स्ट्रिंग

#### प्र13. Django में HTTP अनुरोध/प्रतिक्रिया चक्र का विशिष्ट क्रम क्या है?

- [x] URL > view > template
- [ ] form > model > view
- [ ] template > view > model
- [ ] URL > template > view > model

#### प्र14. Django के class-based generic views कौन से वर्ग प्रदान करते हैं जो सामान्य वेब विकास कार्यों को लागू करते हैं?

- [ ] concrete
- [ ] thread-safe
- [x] abstract
- [ ] dynamic

#### प्र15. Django टेम्पलेट्स के एक सेट को बनाए रखने के लिए आपको किन कौशल की आवश्यकता है?

- [ ] template syntax
- [x] HTML और template syntax
- [ ] Python, HTML, और template syntax
- [ ] Python और template syntax

#### प्र16. आप Django मॉडल में एक तारे और एक तारामंडल के बीच संबंध को कैसे परिभाषित करेंगे?

- [x] A

```python
class Star(models.Model):
name = models.CharField(max_length=100)
class Constellation(models.Model):
stars = models.ManyToManyField(Star)
```

- [ ] B

```python
class Star(models.Model):
constellation = models.ForeignKey(Constellation, on_delete=models.CASCADE)
class Constellation(models.Model):
stars = models.ForeignKey(Star, on_delete=models.CASCADE)
```

- [ ] C

```python
class Star(models.Model):
name = models.CharField(max_length=100)
class Constellation(models.Model):
stars = models.OneToManyField(Star)
```

- [ ] D

```python
class Star(models.Model):
constellation = models.ManyToManyField(Constellation)
class Constellation(models.Model):
name = models.CharField(max_length=100)
```

#### प्र17. छवियों या CSS जैसी स्थिर फ़ाइलों को सेवा देने के लिए अपने Django 2.x इंस्टेंस को कॉन्फ़िगर करने में कौन सा मान्य चरण नहीं है?

- [x] अपनी urls फ़ाइल में, एक पैटर्न जोड़ें जिसमें आपकी स्थिर निर्देशिका का नाम शामिल हो।
- [ ] अपनी app निर्देशिका के अंदर static नामक एक निर्देशिका बनाएं।
- [ ] static निर्देशिका के तहत app के नाम की एक निर्देशिका बनाएं, और अंदर स्थिर फ़ाइलें रखें।
- [ ] टेम्पलेट टैग {percentage mark load static percentage mark} का उपयोग करें।

#### प्र18. अपने सभी टेम्पलेट्स के लिए एक चर उपलब्ध कराने का सही तरीका क्या है?

- [ ] एक सत्र चर सेट करें।
- [ ] एक वैश्विक चर का उपयोग करें।
- [x] टेम्पलेट संदर्भ में एक शब्दकोश जोड़ें।
- [ ] RequestContext का उपयोग करें।

#### प्र19. क्या आपको नए प्रोजेक्ट्स के लिए एक कस्टम उपयोगकर्ता मॉडल बनाना चाहिए?

- [ ] नहीं। कस्टम उपयोगकर्ता मॉडल का उपयोग करने से admin इंटरफ़ेस और कुछ third-party apps टूट सकते हैं।
- [x] हां। उत्पादन में जाने के बाद परिवर्तन करना आसान है।
- [ ] नहीं। Django का अंतर्निहित models.User वर्ग परीक्षण किया गया है—पहिया को फिर से आविष्कार करने का कोई मतलब नहीं है।
- [ ] हां, क्योंकि कोई अन्य विकल्प नहीं है।

#### प्र20. आप एक पृष्ठ बनाना चाहते हैं जो foreign key (जैसे, एक प्रश्न और उत्तर जो अलग तालिकाओं में रहते हैं) द्वारा जुड़े दो वर्गों के संपादन की अनुमति देता है। आप कौन सी Django सुविधा का उपयोग कर सकते हैं?

- [ ] actions
- [ ] admin
- [ ] mezcal
- [x] inlines

#### प्र21. QuerySets को "lazy" क्यों माना जाता है?

- [ ] QuerySet के परिणाम क्रमबद्ध नहीं होते हैं।
- [x] QuerySets मूल्यांकन तक कोई डेटाबेस गतिविधि नहीं बनाते हैं।
- [ ] QuerySets आवश्यकता तक वस्तुओं को मेमोरी में लोड नहीं करते हैं।
- [ ] QuerySets का उपयोग करते हुए, आप अधिक जटिल क्वेरी निष्पादित नहीं कर सकते।

#### प्र22. निम्नलिखित कोड के साथ अनुरोध पैरामीटर तक पहुंचने का प्रयास करते समय आपको `MultiValueDictKeyError` प्राप्त होती है: request.GET['search_term']। इस परिदृश्य में कौन सा समाधान आपकी सहायता नहीं करेगा?

- [x] अनुरोध विधि के रूप में GET के बजाय POST का उपयोग करने पर स्विच करें।
- [ ] सुनिश्चित करें कि आपके फ़ॉर्म में इनपुट फ़ील्ड का नाम भी "search_term" है।
- [ ] शब्दकोश को सीधे हिट करने के बजाय MultiValueDict की GET विधि का उपयोग करें जैसे: request.GET.get('search_term', '')।
- [ ] इसे एक्सेस करने का प्रयास करने से पहले जांचें कि अनुरोध में search_term पैरामीटर मौजूद है या नहीं।

#### प्र23. Django के Form वर्ग का कौन सा फ़ंक्शन एक फ़ॉर्म के फ़ील्ड को <p> टैग की श्रृंखला के रूप में प्रस्तुत करेगा?

- [ ] show_fields()
- [x] as_p()
- [ ] as_table()
- [ ] fields()

#### प्र24. आपने Django में एक बग पाया है और आप एक पैच सबमिट करना चाहते हैं। सही प्रक्रिया क्या है?

- [ ] GitHub पर Django रिपॉजिटरी को Fork करें।
- [ ] एक pull request सबमिट करें।
- [x] इन सभी उत्तरों।
- [ ] Django का परीक्षण suite चलाएं।

#### प्र25. Django सेटिंग्स के लिए समझदार डिफ़ॉल्ट मान प्रदान करता है। आप इन सेटिंग्स को किस Python मॉड्यूल में पा सकते हैं?

- [ ] `django.utils.default_settings.py`
- [ ] `django.utils.global_settings.py`
- [ ] `django.conf.default_settings.py`
- [x] `django.conf.global_settings.py`

#### प्र26. PEP 8 दिशानिर्देशों के अनुसार कौन सा चर नाम सबसे अच्छा है?

- [ ] numFingers
- [ ] number-of-Fingers
- [x] number_of_fingers
- [ ] finger_num

#### प्र27. एक प्रोजेक्ट ने 500 माइग्रेशन जमा किए हैं। आप कौन सी कार्रवाई करेंगे?

- [ ] संख्या कम करने के लिए मैन्युअल रूप से अपनी माइग्रेशन फ़ाइलों को मर्ज करें
- [ ] संख्या के बारे में चिंता न करें
- [ ] माइग्रेशन की संख्या को कम करने का प्रयास करें
- [x] संख्या कम करने के लिए squashmigrations का उपयोग करें

#### प्र28. मॉडल के साथ व्यवहार करते समय F() ऑब्जेक्ट आपको क्या करने की अनुमति देता है?

- [x] मॉडल ऑब्जेक्ट प्राप्त किए बिना db संचालन करें
- [ ] db transaction isolation levels परिभाषित करें
- [ ] aggregate functions का अधिक आसानी से उपयोग करें
- [ ] पुन: प्रयोज्य QuerySets बनाएं

#### प्र29. पूर्णांक रखने के लिए कौन सा Django फ़ील्ड प्रकार नहीं है?

- [ ] SmallIntegerField
- [x] NegativeIntegerField
- [ ] BigAutoField
- [ ] PositiveIntegerField

#### प्र30. कौन सा वर्तमान में स्थापित संस्करण दिखाएगा?

- [ ] print (django.version)
- [ ] import django django.getVersion()
- [x] import django django.get_version()
- [ ] python -c django --version

#### प्र31. आपको डेटा पढ़ने के लिए http विधि `___` और डेटा अपडेट या बनाने के लिए `___` का उपयोग करना चाहिए

- [ ] READ; WRITE
- [x] GET; POST
- [ ] POST; GET
- [ ] GET; PATCH

#### प्र32. डेटा सबमिट करने के लिए GET पर POST विधि का उपयोग कब करना चाहिए?

- [ ] जब दक्षता महत्वपूर्ण हो
- [ ] जब आप चाहते हैं कि डेटा कैश किया जाए
- [ ] जब आप डिबगिंग में मदद के लिए अपने ब्राउज़र का उपयोग करना चाहते हैं
- [x] जब फ़ॉर्म में डेटा संवेदनशील हो सकता है

#### प्र33. Django sites framework का उपयोग कब करें?

- [x] यदि आपकी एकल स्थापना एक से अधिक साइट को शक्ति देती है
- [ ] यदि आपको स्थिर के साथ-साथ गतिशील सामग्री सेवा देने की आवश्यकता है
- [ ] यदि आप चाहते हैं कि आपके app का एक पूर्ण योग्य डोमेन नाम हो
- [ ] यदि आप 10,000 से अधिक उपयोगकर्ताओं की अपेक्षा कर रहे हैं

#### प्र34. आपको किस infrastructure की आवश्यकता है:

`title=models.charfield(max_length=100, validators=[validate_spelling])`

- [ ] validators नामक initialized array
- [x] एक validators फ़ाइल जिसमें validate_spelling नामक फ़ंक्शन हो जो मॉडल के शीर्ष पर imported हो
- [ ] एक validators फ़ाइल जिसमें validate नामक फ़ंक्शन हो जो मॉडल के शीर्ष पर imported हो
- [ ] spelling package जो मॉडल के शीर्ष पर imported हो

#### प्र35. केवल get और head विधियों को स्वीकार करने के लिए view की आवश्यकता के लिए कौन सा decorator का उपयोग किया जाता है?

- [x] require_safe()
- [ ] require_put()
- [ ] require_post()
- [ ] require_get()

#### प्र36. आप एक पुस्तक और एक लेखक के बीच संबंध को कैसे परिभाषित करेंगे - पुस्तक का केवल एक लेखक है।

```python
class Author (models.model):
book=models.foreignkey(Book,on_delete=models.cascade)
class Book(models.model):
name=models.charfield(max_length=100)
```

- [x] A

```python
class Author (models.model):
name=models.charfield(max_length=100)
class Book(models.model):
author=models.foreignkey(Author,on_delete=models.cascade)
```

- [ ] B

```python
class Author (models.model):
name=models.charfield(max_length=100)
class Book(models.model):
author=models.foreignkey(Author)
```

- [ ] C

```python
class Author (models.model):
name=models.charfield(max_length=100)
class Book(models.model):
author=models.foreignkey(Author,on_delete=models.cascade)
```

- [ ] D

```python
class Author (models.model):
name=models.charfield(max_length=100)
class Book(models.model):
author=Author.name
```

#### प्र37. वह callable क्या है जो एक मान लेता है और यदि मान विफल रहता है तो त्रुटि उठाता है?

- [x] validator
- [ ] deodorizer
- [ ] mediator
- [ ] regular expression

#### प्र38. एक API endpoint को सुरक्षित करने के लिए, इसे केवल पंजीकृत उपयोगकर्ताओं के लिए सुलभ बनाने के लिए, आप अपनी settings.py के default_permissions अनुभाग में rest_framework.permissions.allowAny मान को प्रतिस्थापित कर सकते हैं

- [ ] rest_framework.permissions.IsAdminUser
- [x] rest_framework.permissions.IsAuthenticated
- [ ] rest_framework.permissions.IsAuthorized
- [ ] rest_framework.permissions.IsRegistered

#### प्र39. माइग्रेशन लागू करने के लिए आप किस कमांड का उपयोग करेंगे?

- [ ] makemigration
- [ ] update_db
- [ ] applymigration
- [x] migrate

#### प्र40. किस प्रकार का वर्ग QuerySets और मॉडल इंस्टेंस को APIs में उपयोग के लिए native Python डेटा प्रकारों में परिवर्तित करने की अनुमति देता है?

- [ ] objectwriters
- [x] serializers
- [ ] picklers
- [ ] viewsets

#### प्र41. कोड कैसे समाप्त होना चाहिए?

```python
{ percentage if spark >= 50 percentage }
Lots of spark
{percentage elif spark == 42 percentage}
```

- [ ] { percentage else percentage}
- [x] {percentage endif percentage}
- [ ] कुछ भी आवश्यक नहीं
- [ ] {percentage end percentage}

#### प्र42. कौन सा कोड ब्लॉक एक serializer बनाएगा?

```python
from rest_framework import serializers
from .models import Planet
```

- [x] A

```python
class PlanetSerializer(serializers.ModelSerializer):
class Meta:
model=Planet
fields=('name','position', 'mass', 'rings')
```

- [ ] B

```python
from rest_framework import serializers
from .models import Planet
class PlanetSerializer():
class Meta:
fields=('name','position', 'mass', 'rings')
model=Planet
```

- [ ] C

```python
from django.db import serializers
from .models import Planet
class PlanetSerializer(serializers.ModelSerializer):
fields=('name','position', 'mass', 'rings')
model=Sandwich
```

- [ ] D

```python
from django.db import serializers
from .models import Planet
class PlanetSerializer(serializers.ModelSerializer):
class Meta:
fields=('name')
model=Planet
```

#### प्र43. कौन सा वर्ग आपको स्वचालित रूप से एक Serializer वर्ग बनाने की अनुमति देता है जिसमें आपके मॉडल के फ़ील्ड के अनुरूप फ़ील्ड और validators होते हैं?

- [x] ModelSerializer
- [ ] Model
- [ ] DataSerializer
- [ ] ModelToSerializer

#### प्र44. पहली बार अंतर्निहित admin tool तक पहुंचने के लिए कौन सी कमांड?

- [ ] django-admin setup
- [ ] django-admin runserver
- [ ] python manage.py createuser
- [x] python manage.py createsuperuser

#### प्र45. Virtual environments निर्भरताओं के प्रबंधन के लिए हैं। कौन सी granularity सबसे अच्छा काम करती है?

- [x] आपको प्रत्येक Django प्रोजेक्ट के लिए एक नया virtualenv सेट अप करना चाहिए
- [ ] उनका उपयोग नहीं किया जाना चाहिए
- [ ] अपने सभी Django कार्यों के लिए एक ही venv का उपयोग करें
- [ ] प्रत्येक Django app के लिए एक नया venv का उपयोग करें

#### प्र46. वेबसर्वर चलाने या app बनाने जैसी विभिन्न Django कमांड क्या निष्पादित करती हैं?

- [ ] migrate.py
- [ ] wsgi.py
- [x] manage.py
- [ ] runserver

#### प्र47. Django सर्वोत्तम प्रथा क्या सुझाव देती है कि "fat" होना चाहिए?

- [x] models
- [ ] controllers
- [ ] programmers
- [ ] clients

#### प्र48. Django की डिज़ाइन फिलॉसफी का हिस्सा कौन सा नहीं है?

- [ ] Loose Coupling
- [ ] Less Code
- [ ] Fast Development
- [x] Implicit over explicit

#### प्र49. इस टेम्पलेट कोड का परिणाम क्या है?

{% raw %}{{"live long and prosper"|truncatewords:3}}{% endraw %}

- [x] live long and ...
- [ ] live long and
- [ ] एक संकलन त्रुटि
- [ ] liv

#### प्र50. यह कोड डेटा को मेमोरी में कब लोड करता है?

```
1 sandwiches = Sandwich.objects.filter(is_vegan=True)
2 for sandwich in sandwiches:
3   print(sandwich.name + " - " + sandwich.spice_level)
```

- [ ] लाइन 1
- [ ] यह इस बात पर निर्भर करता है कि क्वेरी द्वारा कितने परिणाम लौटाए जाते हैं।
- [ ] यह कैश पर निर्भर करता है।
- [x] लाइन 2

#### प्र51. आप React front end और Django back end का उपयोग करके एक वेब एप्लिकेशन बना रहे हैं। आपको किसके लिए प्रावधान करने की आवश्यकता होगी?

- [ ] एक NGINX वेब सर्वर
- [ ] एक NoSQL डेटाबेस
- [ ] एक बड़ी हार्ड ड्राइव
- [x] CORS middleware

#### प्र52. API endpoint के माध्यम से मौजूदा मॉडल को उजागर करने के लिए, आपको क्या लागू करने की आवश्यकता है?

- [ ] एक HTTP अनुरोध
- [ ] एक JSON ऑब्जेक्ट
- [ ] एक क्वेरी
- [x] एक serializer

#### प्र53. आप Django को किसी विशेष मॉडल के लिए माइग्रेशन के माध्यम से डेटाबेस तालिका निर्माण या विलोपन संचालन करने से कैसे रोकेंगे?

- [ ] `--exclude=[model_name]` के साथ `migrate` कमांड चलाएं।
- [ ] मॉडल परिभाषा को `models.py` से अपनी फ़ाइल में स्थानांतरित करें।
- [x] मॉडल के अंदर `managed=False` सेट करें।
- [ ] `migrate` कमांड न चलाएं।

#### प्र54. फ़ॉर्म इंस्टेंस का उपयोग करते समय फ़ॉर्म डेटा बदल गया है या नहीं यह जांचने के लिए आप किस विधि का उपयोग कर सकते हैं?

- [x] has_changed()
- [ ] its_changed()
- [ ] has_updated()
- [ ] इनमें से कोई नहीं

#### प्र55. WSGI क्या है?

- [ ] एक सर्वर
- [x] एक इंटरफ़ेस विनिर्देश
- [ ] एक Python मॉड्यूल
- [ ] एक framework

संदर्भ लिंक:- https://wsgi.tutorial.codepoint.net/intro

#### प्र56. Django Reinhardt के सभी गीतों के शीर्षक प्रदर्शित करने के लिए किस generic view का उपयोग किया जाना चाहिए?

- [ ] DetailView
- [ ] TittleView
- [ ] SongView
- [x] ListView

#### प्र57. कौन सा कथन सबसे सटीक है, अपनी स्थानीय/विकास मशीन पर डिफ़ॉल्ट SQLite डेटाबेस का उपयोग करने के संबंध में लेकिन उत्पादन में Postgres?

- [ ] बग्स पेश करने की कम संभावना है क्योंकि SQLite पहले से ही बॉक्स से बाहर काम करता है
- [ ] यह ठीक है, आपको बस दोनों instances को synchronized रखने की आवश्यकता है
- [x] यह एक बुरा विचार है और आगे समस्याएं हो सकती हैं
- [ ] यह प्रोजेक्ट बनाने का सबसे कुशल तरीका है

#### प्र58. आप कस्टम मॉडल Manager क्यों लिखना चाहेंगे?

- [ ] डेटाबेस क्वेरी करने के लिए
- [ ] परीक्षण के लिए डेटाबेस सेट अप करने के लिए
- [x] Manager द्वारा लौटाए गए प्रारंभिक QuerySet को संशोधित करने के लिए
- [ ] डेटाबेस क्वेरी द्वारा लौटाए गए परिणामों को फ़िल्टर करने के लिए

#### प्र59. Django में, टेम्पलेट्स को भेजे जाने वाले डेटा को customize करने के लिए क्या उपयोग किया जाता है?

- [ ] models
- [x] views
- [ ] forms
- [ ] serializers

#### प्र60. सशर्त को पूरा करने के लिए, इस कोड ब्लॉक को किसके साथ समाप्त होना चाहिए?

```shell
% if sparles >= 50 %
  Lots of sparkles!
% elif sparkles == 42 %
  The answer to life, the universe, and everything!
```

- [x] `% endif %`
- [ ] कुछ और आवश्यक नहीं है।
- [ ] `% end%`
- [ ] `% else %`

#### प्र61. फ़ॉर्म से डेटा सबमिट करने के लिए GET विधि पर POST विधि का उपयोग कब करना चाहिए?

- [x] जब फ़ॉर्म में डेटा संवेदनशील हो सकता है
- [ ] जब आप चाहते हैं कि डेटा कैश किया जाए
- [ ] जब आप डिबगिंग में मदद के लिए अपने ब्राउज़र का उपयोग करना चाहते हैं
- [ ] जब दक्षता महत्वपूर्ण हो

#### प्र62. वह callable क्या है जो एक मान लेता है और यदि मान कुछ मानदंडों को पूरा करने में विफल रहता है तो त्रुटि उठाता है?

- [ ] mediator
- [x] validator
- [ ] regular expression
- [ ] deodorizer

#### प्र63. आप एक फ़ॉर्म से Django में एक फ़ाइल अपलोड कर रहे हैं और आप प्राप्त फ़ाइल को मॉडल ऑब्जेक्ट पर एक फ़ील्ड के रूप में सहेजना चाहते हैं। आप बस फ़ाइल ऑब्जेक्ट को **\_से मॉडल में \_\_** प्रकार की फ़ील्ड में असाइन कर सकते हैं।

- [ ] request.META; FileField
- [ ] request.FILES; BLOBField
- [x] request.FILES; FileField
- [ ] request.META.Files; CLOBField

#### प्र64. Django मॉडल की वर्तमान स्थिति को फ़ाइल में संग्रहीत करने के लिए किस python मॉड्यूल का उपयोग किया जा सकता है?

- [x] pickle
- [ ] struct
- [ ] marshal
- [ ] serialize

#### प्र65. मौजूदा Django प्रोजेक्ट में एक नया app जोड़ने के लिए, आपको **_ फ़ाइल के _** अनुभाग को संपादित करना होगा।

- [ ] ALLOWED_HOSTS; settings.py
- [ ] APPS; manage.py
- [x] INSTALLED_APPS; settings.py
- [ ] TEMPLATES; urls.py

#### प्र66. प्रमाणीकरण के लिए आमतौर पर उपयोग किया जाने वाला कौन सा third-party package नहीं है?

- [ ] django-guardian
- [ ] django-rest-auth
- [ ] authtoken
- [x] django-rest-framework-jwt

#### प्र67. django.urls पैकेज में कौन सा फ़ंक्शन view के नाम को देखते हुए URL उत्पन्न करके URLs को हार्डकोड करने से बचने में आपकी सहायता कर सकता है?

- [ ] get_script_prefix()
- [ ] redirect()
- [x] reverse()
- [ ] resolve()

#### प्र68. कौन सी काल्पनिक HTTP अनुरोध विधि है?

- [ ] POST
- [ ] PUT
- [x] PAUSE
- [ ] PATCH

#### प्र69. django.shortcuts पैकेज के भाग के रूप में कौन सा helper function प्रदान नहीं किया गया है?

- [x] render_to_request()
- [ ] render()
- [ ] redirect()
- [ ] get_object_or_404()

[संदर्भ](https://docs.djangoproject.com/en/4.0/topics/http/shortcuts/#:~:text=The%20package%20django.,controlled%20coupling%20for%20convenience's%20sake)

#### प्र70. टेम्पलेट्स को संग्रहीत करने के लिए कौन सा गैर-मानक स्थान है?

- [x] प्रोजेक्ट के रूट स्तर पर
- [ ] एप्लिकेशन के अंदर
- [ ] डेटाबेस में
- [ ] Github पर

#### प्र71. यदि आपने python manage.py runserver 8080 कमांड से 8080 छोड़ दिया तो Django किस port को डिफ़ॉल्ट के रूप में उपयोग करेगा?

- [ ] 8080
- [ ] 80
- [x] 8000
- [ ] यह प्रारंभ होने में विफल हो जाएगा

#### प्र72. Django apps के बारे में कौन सा कथन गलत है?

- [x] Django app Django द्वारा संचालित वेब एप्लिकेशन के लिए शीर्ष-स्तरीय कंटेनर है।
- [ ] Django apps छोटी लाइब्रेरी हैं जो प्रोजेक्ट के एक पहलू का प्रतिनिधित्व करने के लिए डिज़ाइन की गई हैं।
- [ ] प्रत्येक Django app को एक चीज़ करनी चाहिए, और केवल एक चीज़।
- [ ] एक Django प्रोजेक्ट कई apps से बना होता है।

#### प्र73. टेम्पलेट चर नामों में कौन से अक्षर अवैध हैं?

- [ ] अंडरस्कोर।
- [ ] अपरकेस अक्षर।
- [x] विराम चिह्न।
- [ ] संख्याएं।

[संदर्भ](https://docs.djangoproject.com/en/4.1/ref/templates/language/#:~:text=Variable%20names%20consist%20of%20any,may%20not%20be%20a%20number.)

#### प्र74. कौन सा मान्य closing template tag नहीं है?

- [ ] `% endautoescape %`
- [x] `% endifempty %`
- [ ] `% endcomment %`
- [ ] `% endfilter %`

#### प्र75. आपको reverse के बजाय reverse_lazy utility function का उपयोग कब करने की आवश्यकता होगी?

- [ ] जब आप फ़ंक्शन के signature में पैरामीटर के लिए डिफ़ॉल्ट मान के रूप में reverse URL प्रदान करना चाहते हैं
- [x] इन सभी उत्तरों
- [ ] जब आप class-based generic view के url विशेषता के रूप में reverse URL प्रदान करना चाहते हैं
- [ ] जब आप decorator को URL प्रदान करना चाहते हैं, जैसे permission_required() decorator के लिए login_url argument

#### प्र76. \_\_init\_\_.py फ़ाइल का उद्देश्य क्या है?

- [ ] पैकेज में पाए गए मॉड्यूल के सेट का विस्तार करने के लिए
- [ ] विभिन्न रिलीज़ और Python के विभिन्न संस्करणों से संकलित मॉड्यूल को सह-अस्तित्व में रखने की अनुमति देने के लिए
- [ ] प्रोजेक्ट सेटिंग्स को initialize करने के लिए
- [x] निर्देशिका सामग्री को Python मॉड्यूल के रूप में घोषित करने के लिए

[संदर्भ](<https://docs.djangoproject.com/en/4.1/ref/urlresolvers/#:~:text=reverse_lazy()&text=It%20is%20useful%20for%20when,a%20generic%20class%2Dbased%20view>)

#### प्र77. "1200000" को "1.2 million" जैसी अधिक पठनीय रूप में संख्याओं को संपादित करने के लिए किस python package का उपयोग किया जा सकता है?

- [ ] black
- [ ] puffer
- [ ] pitch
- [x] humanize

#### प्र78. आप settings.py फ़ाइल कहां पाएंगे?

- [x] \[projectname\]/settings.py
- [ ] \[projectname\]/\[projectname\]/settings.py
- [ ] \[PYTHON_ROOT\]/settings.py
- [ ] \[DJANGO_ROOT]/settings.py

#### प्र79. एक पुस्तक और एक लेखक के बीच संबंध को परिभाषित करने के लिए आप क्या लिखेंगे—यह मानते हुए कि पुस्तक का केवल एक लेखक है—Django मॉडल में?

- [x] A

```python
class Author (models.Model):
  name = models. CharField (max_length=100)
class Book(models .Model):
  author = models. ForeignKey (Author, on_delete=models. CASCADE)
```

- [ ] B

```python
class Author (models.Model):
  name = models. CharField(max length=100)
class Book(models .Model):
  author = models. ForeignKey (Author)
```

- [ ] C

```python
class Author (models .Model):
  name = models.CharField (max_length=100)
class Book (models .Author) :
  author = Author. name
```

- [ ] D

```python
class Author (models. Model):
  book = models. ForeignKey (Book, on_delete=models.CASCADE)
class Book(models.Model):
  name = models. CharField (max length=100)
```

#### प्र80. Form instance का उपयोग करते समय फ़ॉर्म डेटा बदल गया है या नहीं यह जांचने के लिए आप किस विधि का उपयोग कर सकते हैं?

- [ ] changed_data()
- [x] has_changed()
- [ ] has_updated()
- [ ] is_modified()

#### प्र81. कौन सा कथन सबसे सटीक है, अपनी स्थानीय/विकास मशीन पर डिफ़ॉल्ट SQLite डेटाबेस का उपयोग करने के संबंध में लेकिन उत्पादन में Postgres?

- [ ] यह प्रोजेक्ट बनाने का सबसे कुशल तरीका है
- [ ] बग्स पेश करने की कम संभावना है क्योंकि SQLite पहले से ही बॉक्स से बाहर काम करता है
- [x] यह एक बुरा विचार है और आगे समस्याएं हो सकती हैं
- [ ] यह ठीक है, आपको बस दोनों instances को synchronized रखने की आवश्यकता है

#### प्र82. Django URL routing को कैसे संभालता है?

- [ ] classes का उपयोग करके
- [ ] functions का उपयोग करके
- [x] regular expressions का उपयोग करके
- [ ] fixed path का उपयोग करके

#### प्र83. Django के middleware का उद्देश्य क्या है?

- [ ] डेटाबेस schema को परिभाषित करने के लिए
- [ ] URL routing का प्रबंधन करने के लिए
- [x] HTTP अनुरोधों और प्रतिक्रियाओं को globally संभालने के लिए
- [ ] user interfaces बनाने के लिए

[संदर्भ](https://medium.com/scalereal/everything-you-need-to-know-about-middleware-in-django-2a3bd3853cd6)

#### प्र84. Django के Object-Relational Mapping (ORM) के बारे में निम्नलिखित में से क्या सच है?

- [ ] यह Django एप्लिकेशन में URL routing परिभाषित करने के लिए उपयोग किया जाता है।
- [x] यह आपको Python कोड का उपयोग करके डेटाबेस को query करने की अनुमति देता है।
- [ ] यह HTML टेम्पलेट्स की संरचना को परिभाषित करने के लिए उपयोग किया जाता है।
- [ ] यह उपयोगकर्ता प्रमाणीकरण के प्रबंधन के लिए जिम्मेदार है।

#### प्र85. मॉडल में Django के "many-to-many" फ़ील्ड के बारे में निम्नलिखित में से क्या सच है?

- [ ] यह दो मॉडलों के बीच one-to-one संबंध को परिभाषित करने के लिए उपयोग किया जाता है।
- [ ] यह दो मॉडलों के बीच foreign key संबंध बनाता है।
- [x] यह एक दूसरे के साथ जुड़े कई ऑब्जेक्ट्स की अनुमति देता है।
- [ ] यह एक फ़ील्ड पर unique constraints लागू करता है।

