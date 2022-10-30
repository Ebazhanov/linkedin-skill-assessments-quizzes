## AWS Lambda

#### D1. Come puoi aumentare le risorse della CPU per il tuo Lambda?

- \[ ] Increase the configured CPU value
- \[ ] Increase the configured timeout value
- \[x] Increase the configured memory value
- \[ ] Increase the configured concurrency value

#### D2. Come è possibile fornire codice o contenuto aggiuntivo per lambda?

- \[ ] blocks
- \[x] layers
- \[ ] aliases
- \[ ] handlers

#### D3. In che modo le funzioni step possono chiamare Lambdas?

- \[ ] in sequence
- \[x] both of these answers
- \[ ] neither of these answers
- \[ ] in parallel

#### D4. Quale comando AWS CLI richiama una funzione?

- \[ ] aws lambda invoke --function ReturnBucketName outputfile.txt
- \[ ] aws lambda execute --function-name ReturnBucketName outputfile.txt
- \[x] aws lambda invoke --function-name ReturnBucketName outputfile.txt
- \[ ] aws lambda execute --function ReturnBucketName outputfile.txt

#### D5. Cosa aggiunge funzionalità di traccia a una Lambda?

- \[ ] AWS Trace
- \[ ] CloudStack
- \[ ] CloudTrail
- \[x] AWS X-Ray

#### D6. È necessario creare una pipeline di integrazione/distribuzione continua per un set di Lambda. Cosa dovresti fare?

- \[ ] Create configuration files and deploy them using AWS CodePipeline.
- \[ ] Create CloudFormation templates and deploy them using AWS CodeBuild
- \[ ] Create configuration file and deploy using AWS CodeBuild
- \[x] Create CloudFormation templates and deploy them using AWS CodePipeline.

#### D7. Cosa è possibile utilizzare per monitorare le invocazioni di funzioni?

- \[ ] API Gateway
- \[ ] S3
- \[ ] SAS
- \[x] CLoudTrail

#### D8. È consigliabile aws abilitare la registrazione Lambda con quale di questi metodi.

- \[ ] Use S3 metrics and CloudWatch alarms
- \[ ] Create custom metrics within your Lambda code.
- \[ ] Create custom metrics within your CloudWatch code.
- \[x] Use Lambda metrics and CloudWatch alarms.

#### D9. Cosa può essere previsto per le variabili di ambiente?

- \[ ] an SSL certificate
- \[ ] a bitmask
- \[x] an AWS KMS key
- \[ ] an HTTP protocol 

#### D10. Le lambda consentono l'esecuzione di quali altre cose?

- \[ ] binaries.
- \[x] all of these answers
- \[ ] executables
- \[ ] Shell scripts

#### D11. In che stile devi scrivere il codice Lambda?

- \[ ] MVC
- \[ ] virtual
- \[x] stateless
- \[ ] protocol

#### D12. In che modo uno sviluppatore può fornire codice Lambda?

- \[ ] by uploading a .zip file
- \[x] all of these answers
- \[ ] by editing inline
- \[ ] from an S3 bucket

#### D13. Si sta testando le prestazioni di Lambda per verificare di aver impostato adeguatamente le dimensioni della memoria. Dove si verifica il sovraccarico di esecuzione?

- \[ ] CLoudWatch logs
- \[ ] DynamoDB logs
- \[ ] S3 logs
- \[x] Lambda logs.

#### D14. Cosa facilita la consegna continua di Lambda?

- \[ ] CodeStack
- \[ ] ElasticStack
- \[ ] Mobile Hub
- \[x] CodeDeploy

#### D15. Come vengono allocate le risorse di elaborazione a Lambdas?

- \[x] proportionally
- \[ ] equally
- \[ ] periodically
- \[ ] daily

#### D16. Puoi limitare l'ambito delle autorizzazioni di un utente specificando quali due elementi in una policy IAM?

- \[ ] resources and users
- \[x] resources and conditions
- \[ ] events and users
- \[ ] events and conditions

#### D17. Cosa include la registrazione Lambda?

- \[x] logging streams
- \[ ] rotating streams
- \[ ] logging events
- \[ ] advancing log groups

#### D18. Cosa può fare AWS Amplify NON per un Lambda?

- \[ ] create a Lambda
- \[x] be an event source
- \[ ] assign an IAM role
- \[ ] delete a Lambda

#### D19. In che modo è possibile creare un Lambda in un linguaggio di programmazione non supportato da AWS?

- \[ ] Create a Lambda function with a custom runtime and reference the function in your Lambda
- \[x] Create a Lambda layer with a custom runtime and reference the layer in your lambda
- \[ ] You cannot use Lambda in this situation
- \[ ] Create a Lambda function with a custom runtime

#### D20. Su cosa si basano le risorse a valle elencate?

- \[ ] the execution policy
- \[x] the Lambda configuration
- \[ ] the Lambda nodes
- \[ ] the IAM user

#### D21. Qual è un tag equivalente e valido per una coppia di Lambda?

- \[ ] department:Sales,department:Sales
- \[x] department:Sales,department:sales
- \[ ] aws:demo;aws:demo
- \[ ] aws:demo;aws:DEMO

#### D22. Le connessioni in uscita da Lambdas devono essere `_`.

- \[ ] neither of these answers
- \[ ] UDP/IP
- \[ ] TCP/IP
- \[x] both of these answers

#### D23. Come vengono configurate le azioni di CloudWatch?

- \[ ] automatically
- \[ ] none of these answers
- \[x] manually
- \[ ] ad hoc

#### D24. Stai testando la tua applicazione basata su flusso e il Lambda associato. Le best practice di AWS consigliano di eseguire i test variando cosa?

- \[ ] stream and record sizes
- \[ ] stream and shard sizes
- \[x] batch and record sizes
- \[ ] batch and shard sizes

#### D25. Devi rendere la tua Lambda disponibile per i servizi in più VPC. Che lavoro fai?

- \[ ] Place each subnet in a VPC. Associate all subnets to your Lambda.
- \[ ] Place all subnets in a VPC. Associate all subnets to your Lambda.
- \[ ] Configure your Lambda to be available to multiple VPCs.
- \[x] Configure all application VPCs to be peered.

#### D26. Come viene calcolato il costo associato alla funzione Lambda?

- \[ ] number of function calls
- \[ ] amount of code run
- \[x] compute time
- \[ ] amount of infrastructure used

#### D27. Qual è il modo più veloce per iniziare a usare Lambda?

- \[ ] Author a Lambda from scratch.
- \[x] Use a blueprint.
- \[ ] Use a .zip deployment package.
- \[ ] Use the serverless app repository.

#### D28. Dove viene allocato lo spazio su disco per le funzioni Lambda?

- \[x] /tmp
- \[ ] /default
- \[ ] /temp
- \[ ] /ds

#### D29. Come si ferma un Lambda in esecuzione che è bloccato in un loop ricorsivo?

- \[ ] Delete the function.
- \[x] Set the function concurrent execution limit to 0 while you update the code.
- \[ ] Reset the function.
- \[ ] Set the function concurrent execution limit to 100 while you update the code.

#### D30. Quali sono le best practice AWS per la configurazione Lambda?

- \[x] Overprovision memory to run your functions faster and reduce your costs. Do not overprovision your function timeout settings.
- \[ ] Overprovision memory and your function timeout settings to run your functions faster and reduce your costs.
- \[ ] Do not overprovision memory. Overprovision your function timeout settings to run your functions faster and reduce costs.
- \[ ] Do not overprovision memory. Do not overprovision your function timeout settings to run your functions faster and reduce costs.

#### D31. Le autorizzazioni Lambda di base includono autorizzazioni per cosa?

- \[ ] removing log groups
- \[ ] none of these answers
- \[ ] creating log groups
- \[x] updating log groups

#### D32. Come vengono archiviate le variabili di ambiente?

- \[ ] DynamoDB tables
- \[x] key-value pairs
- \[ ] S3 buckets
- \[ ] none of these answers

#### D33. Devi utilizzare un Lambda per fornire logica di back-end al tuo sito web. Quale servizio utilizzi per rendere la tua Lambda disponibile per il tuo sito web?

- \[ ] S3
- \[x] API Gateway
- \[ ] X-Ray
- \[ ] DynamoDB

#### D34. Si sta creando un Lambda da attivare in caso di modifica dei file in un bucket S3. Dove dovresti mettere il nome del secchio?

- \[ ] in the Lambda function code
- \[x] in a Lambda environment variable
- \[ ] in the Lambda tags
- \[ ] in another S3 bucket

#### D35. Quale azione è necessaria prima di poter testare una Lambda?

- \[ ] Deploy the Lambda
- \[ ] Export the function
- \[ ] none of these answers
- \[x] Configure a test event

#### D36. Che tipo di pacchetti puoi usare con Node.js for Lambdas?

- \[ ] Fleece
- \[x] NPM
- \[ ] none of these answers
- \[ ] Pod

#### D37. Le lambda sono monitorate per impostazione predefinita utilizzando quale servizio?

- \[ ] CloudTrail
- \[x] CloudWatch
- \[ ] CloudFormation
- \[ ] LogWatch

#### D38. Cosa può attivare l'esecuzione di una funzione Lambda?

- \[ ] a table definition
- \[ ] queue isolation
- \[ ] STS Write
- \[x] an SNS topic

#### D39. È necessario impostare un trigger di evento S3 su Lambda per rispondere quando i dati vengono aggiunti al bucket da un altro bucket S3. Quale tipo di evento si configura?

- \[ ] POST
- \[ ] "All object create events"
- \[x] PUT
- \[ ] COPY

#### D40. Per rendere Lambdas più testabile, è consigliabile AWS separare quale di questi?

- \[ ] Lambda configuration from logging code
- \[ ] Lambda handler from logging code
- \[x] Lambda handler from core logic
- \[ ] Lambda configuration from core logic

#### D41. Cosa è incluso in un pacchetto di distribuzione Lambda esportato?

- \[ ] YAML definition
- \[ ] CloudFormation stack configuration
- \[ ] SAML deployment stack
- \[x] Zip file of all related files

#### D42. Quando è possibile modificare il ruolo di esecuzione di un Lambda?

- \[ ] only at creation
- \[ ] only before deployment
- \[ ] never
- \[x] anytime via configuration

#### D43. Qual è la relazione tra il modello SAM e i file modello CloudFormation?

- \[x] I modelli SAM sono un superset di modelli CloudFormation. I modelli SAM includono tipi di risorse aggiuntivi.
- \[ ] I modelli SAM hanno una certa sovrapposizione con i modelli CloudFormation. Entrambi i modelli SAM e CloudFormation includono tipi di risorse che non si trovano nell'altro tipo di modello.
- \[ ] I modelli CloudFormation sono un superset di modelli SAM. I modelli cloudFormation includono tipi di risorse aggiuntivi.
- \[ ] I modelli SAM sono un nome diverso per i modelli CloudFormation. Entrambi i tipi di modello includono gli stessi tipi di risorse.

#### D44. Quale servizio distribuisce Lambdas a livello regionale?

- \[ ] EdgeCloud
- \[ ] CloudEdge
- \[x] CloudFront
- \[ ] CloudStack

#### D45. Quale linguaggio di programmazione supporta AWS Lambda?

- \[ ] custom
- \[x] all of these answers
- \[ ] Java
- \[ ] Ruby

#### D46. È necessario impostare un meccanismo per mettere in atto i controlli per avvisare l'utente quando si verifica un picco di concorrenza Lambda. Cosa dovresti fare?

- \[ ] Distribuisci un allarme CloudTrail che ti avvisa quando le metriche delle funzioni superano la soglia. Crea un budget AWS per monitorare i costi.
- \[x] Distribuisci un allarme CloudWatch che ti avvisa quando i parametri delle funzioni superano la soglia. Crea un budget AWS per monitorare i costi.
- \[ ] Distribuisci un allarme CloudWatch che ti avvisa quando i parametri di funzione superano la soglia. Crea un AWS CostMonitor per monitorare i costi.
- \[ ] Distribuisci un allarme CloudTrail che ti avvisa quando le metriche delle funzioni superano la soglia. Crea un AWS CostMonitor per monitorare i costi.

#### D47. Vuoi ridurre al minimo il tempo di avvio a freddo per la tua Lambda. Che lavoro fai?

- \[ ] Aggiungere codice aggiuntivo per verificare se la cache temporanea, o la directory /tmp, contiene i dati memorizzati.
- \[ ] Aggiungi codice aggiuntivo per verificare se la cache permanente, o la directory /cache, contiene i dati memorizzati.
- \[ ] Non fare nulla. AWS riduce al minimo l'ora di inizio dei cols per impostazione predefinita.
- \[ ] Crea una Lambda di riscaldamento che chiami la tua Lambda ogni minuto

[Riferimento] (https://aws.amazon.com/blogs/compute/new-for-aws-lambda-predictable-start-up-times-with-provisioned-concurrency/

#### D48. Quando viene memorizzato il codice Lambda crittografato?

- \[x] a riposo
- \[ ] in fase di esecuzione
- \[ ] alla distribuzione
- \[ ] nessuna di queste risposte

[Riferimento](https://docs.aws.amazon.com/whitepapers/latest/security-overview-aws-lambda/lambda-functions-and-layers.html)

#### D49. Quando si utilizza un criterio basato sulle risorse per concedere a un servizio, una risorsa o un account l'accesso alla funzione, come è possibile applicare l'ambito di tale autorizzazione??

- \[ ] a livello di funzione a livello di funzione
- \[ ] a livello di alias o funzione a livello di alias o funzione
- \[ ] a livello di versione, alias o funzione a livello di versione, alias o funzione
- \[ ] a livello di versione o funzione

#### D50. Lambda è in grado di leggere eventi da quali altri servizi AWS? (ref-https://docs.aws.amazon.com/lambda/latest/dg/lambda-servizi.html)

- \[ ] Kinesis, S3 e SQS
- \[ ] Kinesis, S3 e SNS
- \[ ] Kinesis, DynamoDB e SNS
- \[ ] Kinesis, DynamoDB e SQS
