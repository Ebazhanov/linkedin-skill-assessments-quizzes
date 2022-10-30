## AWS Lambda

#### S1. Lambda'nız için CPU kaynaklarını nasıl artırabilirsiniz??

- [ ] Yapılandırılmış CPU değerini artırın
- [ ] Yapılandırılmış zaman aşımı değerini artırın
- [x] Yapılandırılmış bellek değerini artırın
- [ ] Yapılandırılmış eşzamanlılık değerini artırın

#### S2. Lambda'nız için ek kod veya içerik nasıl sağlanabilir??

- [ ] bloklar
- [x] katmanlar
- [ ] diğer adlar
- [ ] işleyiciler

#### S3. Adım Fonksiyonları Lambda'ları nasıl çağırabilir??

- [ ] sırayla
- [x] bu cevapların ikisi de
- [ ] bu cevapların hiçbiri
- [ ] paralel olarak

#### S4. Hangi AWS terminal komutu bir işlevi çağırır?

- [ ] aws lambda invoke --function ReturnBucketName outputfile.txt
- [ ] aws lambda execute --function-name ReturnBucketName outputfile.txt
- [x] aws lambda invoke --function-name ReturnBucketName outputfile.txt
- [ ] aws lambda execute --function ReturnBucketName outputfile.txt

#### S5. Lambda'ya izleme özellikleri ekleyen şey?

- [ ] AWS Trace
- [ ] CloudStack
- [ ] CloudTrail
- [x] AWS X-Ray

#### S6. Bir dizi Lambda için sürekli bir entegrasyon/dağıtım işlem hattı oluşturmanız gerekiyor. Ne yapmalısınız?

- [ ] AWS CodePipeline kullanarak yapılandırma dosyaları oluşturma ve bunları dağıtma.
- [ ] CloudFormation şablonları oluşturma ve AWS CodeBuild kullanarak bunları dağıtma
- [ ] AWS CodeBuild kullanarak yapılandırma dosyası oluşturma ve dağıtma
- [x] CloudFormation şablonları oluşturma ve AWS CodePipeline kullanarak bunları dağıtma.

#### S7. İşlev çağrılarını izlemek için ne kullanabilirsiniz?

- [ ] API Ağ Geçidi
- [ ] S3
- [ ] SAS
- [x] CLoudTrail

#### S8. Lambda günlüğünü bu yöntemlerden hangisiyle etkinleştirmek AWS'nin en iyi uygulamasıdır.

- [ ] S3 ölçümlerini ve CloudWatch alarmlarını kullanın
- [ ] Lambda kodunuz içinde özel metrikler oluşturun.
- [ ] CloudWatch kodunuz içinde özel metrikler oluşturun.
- [x] Lambda metriklerini ve CloudWatch alarmlarını kullanın.

#### S9. Ortam değişkenleri için neler sağlanabilir?

- [ ] bir SSL sertifikası
- [ ] bir bit maskesi
- [x] bir AWS KMS anahtarı
- [ ] bir HTTP protokolü 

#### S10. Lambdalar başka hangi şeylerin çalıştırılmasına izin verir?

- [ ] ikili dosyalar.
- [x] tüm bu cevaplar
- [ ] yürütülebilir dosyalar
- [ ] Shell dosya komutları

#### S11. Lambda kodunu hangi stilde yazmalısınız?

- [ ] MVC
- [ ] sanal
- [x] durumsuz
- [ ] protokol

#### S12. Bir geliştirici Lambda kodunu nasıl sağlayabilir?

- [ ] bir .zip dosyası yükleyerek
- [x] tüm bu cevaplar
- [ ] satır içi düzenleme yaparak
- [ ] bir S3 kovasından

#### S13. Bellek boyutunu uygun şekilde ayarladığınızı doğrulamak için Lambda'nızı performans testine tabi tutuyorsunuz. Yürütme ek yükünü nerede doğruluyorsunuz?

- [ ] CLoudWatch günlükleri
- [ ] DynamoDB günlükleri
- [ ] S3 günlükleri
- [x] Lambda günlükleri.

#### S14. Lambda'ların sürekli teslimatını ne kolaylaştırır?

- [ ] CodeStack
- [ ] ElasticStack
- [ ] Mobil Merkez
- [x] CodeDeploy

#### S15. Bilgi işlem kaynakları Lambda'lara nasıl tahsis edilir?

- [x] orantılı olarak
- [ ] eşit olarak
- [ ] periyodik olarak
- [ ] günlük olarak

#### S16. Bir IAM ilkesinde hangi iki öğeyi belirterek bir kullanıcının izinlerinin kapsamını kısıtlayabilirsiniz?

- [ ] kaynaklar ve kullanıcılar
- [x] kaynaklar ve koşullar
- [ ] olaylar ve kullanıcılar
- [ ] olaylar ve koşullar

#### S17. Lambda günlük kaydı neleri içerir?

- [x] günlük akışları
- [ ] dönen akışlar
- [ ] olayları günlüğe kaydetme
- [ ] ilerleyen günlük grupları

#### S18. AWS Amplify bir Lambda için ne YAPAMAZ?

- [ ] bir Lambda oluşturmak
- [x] bir olay kaynağı olmak
- [ ] bir IAM rolü atamak
- [ ] bir Lambda silmek

#### S19. AWS'nin desteklemediği bir programlama dilinde bir Lambda'yı nasıl yazarsınız?

- [ ] Özel bir çalışma zamanına sahip bir Lambda işlevi oluşturun ve Lambda'nızda bu işleve referans verin
- [x] Özel bir çalışma zamanına sahip bir Lambda katmanı oluşturun ve lambda'nızda bu katmana referans verin
- [ ] Bu durumda Lambda kullanamazsınız
- [ ] Özel çalışma zamanına sahip bir Lambda işlevi oluşturma

#### S20. Listelenen aşağı akış kaynakları neye dayanmaktadır?

- [ ] yürütme politikası
- [x] Lambda yapılandırması
- [ ] Lambda düğümleri
- [ ] IAM kullanıcısı

#### S21. Hangisi bir Lambda çifti için eşdeğer ve geçerli bir etikettir?

- [ ] department:Sales,department:Sales
- [x] department:Sales,department:sales
- [ ] aws:demo;aws:demo
- [ ] aws:demo;aws:DEMO

#### S22. Lambda'lardan giden bağlantılar şu şekilde olmalıdır `_`.

- [ ] bu cevapların hiçbiri
- [ ] UDP/IP
- [ ] TCP/IP
- [x] bu cevapların ikisi de

#### S23. CloudWatch eylemleri nasıl yapılandırılır?

- [ ] otomatik olarak
- [ ] bu cevapların hiçbiri
- [x] manual olarak
- [ ] ad hoc

#### S24. Akış tabanlı uygulamanızı ve ilgili Lambda'yı test ediyorsunuz. AWS'nin en iyi uygulamaları neyi değiştirerek test etmenizi önerir?

- [ ] stream and record sizes
- [ ] stream ve shard boyutları
- [x] yığın ve kayıt boyutları
- [ ] batch ve shard boyutları

#### S25. Lambda'nızı birden fazla VPC'deki hizmetler için kullanılabilir hale getirmeniz gerekir. Ne yapmalısınız?

- [ ] Her alt ağı bir VPC'ye yerleştirin. Tüm alt ağları Lambda'nızla ilişkilendirin.
- [ ] Tüm alt ağları bir VPC'ye yerleştirin. Tüm alt ağları Lambda'nızla ilişkilendirin.
- [ ] Lambda'nızı birden fazla VPC'de kullanılabilir olacak şekilde yapılandırın.
- [x] Tüm uygulama VPC'lerini gözetlenecek şekilde yapılandırın.

#### S26. Lambda fonksiyonu ile ilişkili maliyet nasıl hesaplanır?

- [ ] fonksiyon çağrı sayısı
- [ ] çalıştırılan kod miktarı
- [x] hesaplama süresi
- [ ] kullanılan altyapı miktarı

#### S27. Lambda ile çalışmaya başlamanın en hızlı yolu nedir?

- [ ] Sıfırdan bir Lambda yazın.
- [x] Bir plan kullanın.
- [ ] Bir .zip dağıtım paketi kullanın.
- [ ] Sunucusuz uygulama deposunu kullanın.

#### S28. Lambda işlevleri için disk alanı nerede ayrılır?

- [x] /tmp
- [ ] /default
- [ ] /temp
- [ ] /ds

#### S29. Özyinelemeli bir döngüde takılı kalmış çalışan bir Lambda'yı nasıl durdurursunuz?

- [ ] Fonksiyonu silin.
- [x] Kodu güncellerken işlev eşzamanlı yürütme sınırını 0 olarak ayarlayın.
- [ ] Fonksiyonu sıfırlayın.
- [ ] Kodu güncellerken işlev eşzamanlı yürütme sınırını 100 olarak ayarlayın.

#### S30. Lambda yapılandırması için AWS'nin en iyi uygulaması nedir?

- [x] İşlevlerinizi daha hızlı çalıştırmak ve maliyetlerinizi azaltmak için belleği aşırı sağlayın. İşlev zaman aşımı ayarlarınızı aşırı sağlamayın.
- [ ] İşlevlerinizi daha hızlı çalıştırmak ve maliyetlerinizi azaltmak için belleği ve işlev zaman aşımı ayarlarınızı aşırı sağlayın.
- [ ] Belleğe aşırı kaynak ayırmayın. İşlevlerinizi daha hızlı çalıştırmak ve maliyetleri azaltmak için işlev zaman aşımı ayarlarınızı aşırı sağlayın..
- [ ] Bellek için aşırı kaynak ayırmayın. İşlevlerinizi daha hızlı çalıştırmak ve maliyetleri düşürmek için işlev zaman aşımı ayarlarınızı fazla sağlamayın.

#### Q31. Basic Lambda permissions include permissions for what?

- [ ] removing log groups
- [ ] none of these answers
- [ ] creating log groups
- [x] updating log groups

#### S32. Ortam değişkenleri nasıl saklanır?

- [ ] DynamoDB tabloları
- [x] anahtar-değer çiftleri
- [ ] S3 kovası
- [ ] bu cevapların hiçbiri

#### S33. Web sitenize arka uç mantığı sağlamak için bir Lambda kullanmanız gerekiyor. Lambda'nızı web sitenizde kullanılabilir hale getirmek için hangi hizmeti kullanıyorsunuz?

- [ ] S3
- [x] API Gateway
- [ ] X-Ray
- [ ] DynamoDB

#### S34. Bir S3 kovasındaki dosyalarda yapılan değişiklikleri tetiklemek için bir Lambda oluşturuyorsunuz. Kova adını nereye koymalısınız?

- [ ] Lambda fonksiyon kodunda
- [x] Lambda ortam değişkeninde
- [ ] Lambda etiketlerinde
- [ ] başka bir S3 kovasında

#### S35. Bir Lambda'yı test etmeden önce hangi eylem gereklidir?

- [ ] Lambda'yı dağıtın
- [ ] Fonksiyonu dışa aktarın
- [ ] bu cevapların hiçbiri
- [x] Bir test etkinliği yapılandırma

#### S36. Lambda'lar için Node.js ile ne tür paketler kullanabilirsiniz?

- [ ] Fleece
- [x] NPM
- [ ] bu cevapların hiçbiri
- [ ] Pod

#### S37. Lambda'lar varsayılan olarak hangi servis kullanılarak izlenir?

- [ ] CloudTrail
- [x] CloudWatch
- [ ] CloudFormation
- [ ] LogWatch

#### S38. Bir Lambda fonksiyonunun yürütülmesini ne tetikleyebilir?

- [ ] bir tablo tanımı
- [ ] kuyruk izolasyonu
- [ ] STS Yazma
- [x] bir SNS konusu

#### S39. Başka bir S3 kovasından kovanıza veri eklendiğinde yanıt vermek için Lambda'nızda bir S3 olay tetikleyicisi ayarlamanız gerekir. Hangi olay türünü yapılandırırsınız?

- [ ] POST
- [ ] "Tüm nesne oluşturma olayları"
- [x] PUT
- [ ] COPY

#### S40. Lambda'ları daha test edilebilir hale getirmek için, aşağıdakilerden hangisini ayırmak AWS'nin en iyi uygulamasıdır?

- [ ] Günlük kodundan Lambda yapılandırması
- [ ] Günlük kodundan Lambda işleyicisi
- [x] Çekirdek mantıktan Lambda işleyicisi
- [ ] Çekirdek mantığından Lambda yapılandırması

#### S41. Dışa aktarılan bir Lambda dağıtım paketine neler dahildir?

- [ ] YAML tanımı
- [ ] CloudFormation yığın yapılandırması
- [ ] SAML dağıtım yığını
- [x] İlgili tüm dosyaların zip dosyası

#### S42. Bir Lambda'nın yürütme rolünü ne zaman değiştirebilirsiniz?

- [ ] sadece oluştururken
- [ ] sadece konuşlandırmadan önce
- [ ] asla
- [x] yapılandırma aracılığıyla her zaman

#### S43. SAM şablonu ile CloudFormation şablon dosyaları arasındaki ilişki nedir?

- [ ] SAM şablonları, CloudFormation şablonlarının bir üst kümesidir. SAM şablonları ek kaynak türleri içerir.
- [ ] SAM şablonlarının CloudFormation şablonlarıyla bazı örtüşmeleri vardır. Hem SAM hem de CloudFormation şablonları, diğer şablon türünde olmayan kaynak türlerini içerir.
- [x] CloudFormation şablonları SAM şablonlarının bir üst kümesidir. CloudFormation şablonları ek kaynak türleri içerir.
- [ ] SAM şablonları, CloudFormation şablonları için farklı bir isimdir. Her iki şablon türü de aynı kaynak türlerini içerir.

#### S44. Lambdas'ı bölgesel olarak hangi hizmet dağıtır?

- [ ] EdgeCloud
- [ ] CloudEdge
- [x] CloudFront
- [ ] CloudStack

#### S45. AWS Lambda hangi programlama dilini destekliyor?

- [ ] özel
- [x] bütün cevaplar
- [ ] Java
- [ ] Ruby

#### S46. Lambda eşzamanlılığında bir artış olduğunda sizi bilgilendirecek kontrolleri devreye sokmak için bir mekanizma kurmanız gerekir. Ne yapmalısınız?

- [ ] İşlev ölçümleri eşiğinizi aştığında sizi bilgilendiren bir CloudTrail alarmı dağıtın. Maliyetleri izlemek için bir AWS bütçesi oluşturun.
- [x] İşlev ölçümleri eşiğinizi aştığında sizi bilgilendiren bir CloudWatch alarmı dağıtın. Maliyetleri izlemek için bir AWS bütçesi oluşturun.
- [ ] İşlev ölçümleri eşiğinizi aştığında sizi bilgilendiren bir CloudWatch alarmı dağıtın. Maliyetleri izlemek için bir AWS CostMonitor oluşturun.
- [ ] İşlev ölçümleri eşiğinizi aştığında sizi bilgilendiren bir CloudTrail alarmı dağıtın. Maliyetleri izlemek için bir AWS CostMonitor oluşturun.

#### S47. Lambda'nız için soğuk başlatma süresini en aza indirmek istiyorsunuz. Ne yapacaksınız?

- [ ] Geçici önbellekte veya /tmp dizininde depoladığınız verilerin olup olmadığını kontrol etmek için ekstra kod ekleyin.
- [ ] Kalıcı önbellekte veya /cache dizininde depoladığınız verilerin olup olmadığını kontrol etmek için ekstra kod ekleyin.
- [ ] Hiçbir şey yapmayın. AWS varsayılan olarak cols başlangıç zamanını en aza indirir.
- [ ] Lambda'nızı her dakika çağıran bir ısınma Lambda'sı oluşturun

[Reference](https://aws.amazon.com/blogs/compute/new-for-aws-lambda-predictable-start-up-times-with-provisioned-concurrency/

#### S48. Lambda kodu ne zaman şifrelenmiş olarak saklanır?

- [x] dinlenirken
- [ ] çalışma zamanında
- [ ] konuşlandırmada
- [ ] bu cevapların hiçbiri

[Reference](https://docs.aws.amazon.com/whitepapers/latest/security-overview-aws-lambda/lambda-functions-and-layers.html)

#### S49. İşlevinize bir hizmet, kaynak veya hesap erişimi vermek için kaynak tabanlı bir ilke kullandığınızda, bu iznin kapsamını nasıl uygulayabilirsiniz??

- [ ] fonksiyon seviyesinde
- [ ] takma ad veya işlev düzeyinde
- [ ] sürüm, takma ad veya işlev düzeyinde sürüm, takma ad veya işlev düzeyinde
- [ ] sürüm veya işlev düzeyinde

#### S50. Lambda başka hangi AWS hizmetlerinden gelen olayları okuyabilir? (ref-https://docs.aws.amazon.com/lambda/latest/dg/lambda-services.html)

- [ ] Kinesis, S3, and SQS
- [ ] Kinesis, S3, and SNS
- [ ] Kinesis, DynamoDB, and SNS
- [x] Kinesis, DynamoDB, and SQS

**Açıklama** 
- `Lambda soruda belirtilen tüm servisler için kullanılabilir: Kinesis, S3, SNS, SQS, DynamoDB. Ancak referansta görebileceğiniz gibi, Lambda'nın sorumluluğu ve yöntem çağırma Lambda polling ve Event Driven (senkronize çağırma) olarak kategorize edilebilir. Olay güdümlü bir mimari uyguladığınızda, olay üreten hizmete, işlevin kaynak tabanlı ilkesinde işlevinizi çağırma izni verirsiniz. Ardından bu hizmeti, işlevinizi çağıran olaylar oluşturacak şekilde yapılandırırsınız. Bir Lambda yoklama mimarisi uyguladığınızda, Lambda'ya işlevin yürütme rolündeki diğer hizmete erişme izni verirsiniz. Lambda diğer hizmetten verileri okur, bir olay oluşturur ve işlevinizi çağırır. Bu analize göre, Kinesis-DynamoDB-SQS aynı yöntem çağrısını, Lambda polling'i kullanır.`

#### S51. Bir Lambda ne ile adlandırılabilir?

- [x] tüm bu cevaplar
- [ ] bir DynamoDB tetikleyicisi
- [ ] bir API Gateway
- [ ] bir S3 kova olayı

**Açıklama** (kaynak google)

- `DynamoDB Streams ile, bir DynamoDB tablosu her güncellendiğinde ek iş yapmak için bir Lambda işlevini tetikleyebilirsiniz. Lambda, akıştan kayıtları okur ve akış kayıtlarını içeren bir olayla eşzamanlı olarak işlevinizi çağırır.`
- `Bu olaylar senkronize olaylar olarak kabul edilir. Basitçe söylemek gerekirse, birisi bir API Gateway'i çağırdığında Lambda fonksiyonunuzu tetikleyeceği anlamına gelir. Bu eşzamanlı bir olaydır çünkü Lambda işlevinizin çağrının sonunda doğrudan istemciye yanıt vermesi gerekir.`
- `Amazon Simple Storage Service'ten gelen olay bildirimlerini işlemek için Lambda'yı kullanabilirsiniz. Amazon S3, bir nesne oluşturulduğunda veya silindiğinde Lambda işlevine bir olay gönderebilir.`
