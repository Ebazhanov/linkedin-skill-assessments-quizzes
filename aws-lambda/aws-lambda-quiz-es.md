## AWS Lambda

#### P1. ¿Cómo puede aumentar los recursos de CPU para Lambda?

- \[ ] Increase the configured CPU value
- \[ ] Increase the configured timeout value
- \[x] Increase the configured memory value
- \[ ] Increase the configured concurrency value

#### P2. ¿Cómo se puede proporcionar código o contenido adicional para Lambda?

- \[ ] blocks
- \[x] layers
- \[ ] aliases
- \[ ] handlers

#### P3. ¿Cómo puede Step Functions llamar a Lambdas?

- \[ ] in sequence
- \[x] both of these answers
- \[ ] neither of these answers
- \[ ] in parallel

#### P4. ¿Qué comando de la AWS CLI invoca una función?

- \[ ] aws lambda invoke --function ReturnBucketName outputfile.txt
- \[ ] aws lambda execute --function-name ReturnBucketName outputfile.txt
- \[x] aws lambda invoke --function-name ReturnBucketName outputfile.txt
- \[ ] aws lambda execute --function ReturnBucketName outputfile.txt

#### P5. ¿Qué añade capacidades de rastreo a un Lambda?

- \[ ] AWS Trace
- \[ ] CloudStack
- \[ ] CloudTrail
- \[x] AWS X-Ray

#### P6. Debe crear una canalización de integración/implementación continua para un conjunto de Lambdas. ¿Qué debes hacer?

- \[ ] Create configuration files and deploy them using AWS CodePipeline.
- \[ ] Create CloudFormation templates and deploy them using AWS CodeBuild
- \[ ] Create configuration file and deploy using AWS CodeBuild
- \[x] Create CloudFormation templates and deploy them using AWS CodePipeline.

#### P7. ¿Qué se puede utilizar para supervisar las invocaciones de funciones?

- \[ ] API Gateway
- \[ ] S3
- \[ ] SAS
- \[x] CLoudTrail

#### P8. Es una práctica recomendada de AWS habilitar el registro de Lambda mediante cuál de estos métodos.

- \[ ] Use S3 metrics and CloudWatch alarms
- \[ ] Create custom metrics within your Lambda code.
- \[ ] Create custom metrics within your CloudWatch code.
- \[x] Use Lambda metrics and CloudWatch alarms.

#### P9. ¿Qué se puede proporcionar para las variables de entorno?

- \[ ] an SSL certificate
- \[ ] a bitmask
- \[x] an AWS KMS key
- \[ ] an HTTP protocol 

#### P10. ¿Las lambdas permiten ejecutar qué otras cosas?

- \[ ] binaries.
- \[x] all of these answers
- \[ ] executables
- \[ ] Shell scripts

#### P11. ¿En qué estilo debe escribir código Lambda?

- \[ ] MVC
- \[ ] virtual
- \[x] stateless
- \[ ] protocol

#### P12. ¿Cómo puede un desarrollador proporcionar código Lambda?

- \[ ] by uploading a .zip file
- \[x] all of these answers
- \[ ] by editing inline
- \[ ] from an S3 bucket

#### P13. Está probando el rendimiento de Lambda para comprobar que ha establecido el tamaño de memoria correctamente. ¿Dónde se verifica la sobrecarga de ejecución?

- \[ ] CLoudWatch logs
- \[ ] DynamoDB logs
- \[ ] S3 logs
- \[x] Lambda logs.

#### P14. ¿Qué facilita la entrega continua de Lambdas?

- \[ ] CodeStack
- \[ ] ElasticStack
- \[ ] Mobile Hub
- \[x] CodeDeploy

#### P15. ¿Cómo se asignan los recursos informáticos a Lambdas?

- \[x] proportionally
- \[ ] equally
- \[ ] periodically
- \[ ] daily

#### P16. ¿Puede restringir el ámbito de los permisos de un usuario especificando qué dos elementos de una política de IAM?

- \[ ] resources and users
- \[x] resources and conditions
- \[ ] events and users
- \[ ] events and conditions

#### P17. ¿Qué incluye el registro de Lambda?

- \[x] logging streams
- \[ ] rotating streams
- \[ ] logging events
- \[ ] advancing log groups

#### P18. ¿Qué puede no hacer AWS Amplify por un Lambda?

- \[ ] create a Lambda
- \[x] be an event source
- \[ ] assign an IAM role
- \[ ] delete a Lambda

#### P19. ¿Cómo se crea un Lambda en un lenguaje de programación que AWS no admite?

- \[ ] Create a Lambda function with a custom runtime and reference the function in your Lambda
- \[x] Create a Lambda layer with a custom runtime and reference the layer in your lambda
- \[ ] You cannot use Lambda in this situation
- \[ ] Create a Lambda function with a custom runtime

#### P20. ¿En qué se enumeran los recursos posteriores?

- \[ ] the execution policy
- \[x] the Lambda configuration
- \[ ] the Lambda nodes
- \[ ] the IAM user

#### P21. ¿Cuál es una etiqueta equivalente y válida para un par de Lambdas?

- \[ ] department:Sales,department:Sales
- \[x] department:Sales,department:sales
- \[ ] aws:demo;aws:demo
- \[ ] aws:demo;aws:DEMO

#### P22. Las conexiones salientes de Lambdas deben ser `_`.

- \[ ] neither of these answers
- \[ ] UDP/IP
- \[ ] TCP/IP
- \[x] both of these answers

#### P23. ¿Cómo se configuran las acciones de CloudWatch?

- \[ ] automatically
- \[ ] none of these answers
- \[x] manually
- \[ ] ad hoc

#### P24. Está probando la aplicación basada en secuencias y el Lambda asociado. La práctica recomendada de AWS le aconseja que pruebe variando qué.

- \[ ] stream and record sizes
- \[ ] stream and shard sizes
- \[x] batch and record sizes
- \[ ] batch and shard sizes

#### P25. Debe hacer que su Lambda esté disponible para los servicios en varias VPC. ¿A qué te dedicas?

- \[ ] Place each subnet in a VPC. Associate all subnets to your Lambda.
- \[ ] Place all subnets in a VPC. Associate all subnets to your Lambda.
- \[ ] Configure your Lambda to be available to multiple VPCs.
- \[x] Configure all application VPCs to be peered.

#### P26. ¿Cómo se calcula el costo asociado con la función Lambda?

- \[ ] number of function calls
- \[ ] amount of code run
- \[x] compute time
- \[ ] amount of infrastructure used

#### P27. ¿Cuál es la forma más rápida de empezar a usar Lambda?

- \[ ] Author a Lambda from scratch.
- \[x] Use a blueprint.
- \[ ] Use a .zip deployment package.
- \[ ] Use the serverless app repository.

#### P28. ¿Dónde se asigna el espacio en disco para las funciones de Lambda?

- \[x] /tmp
- \[ ] /default
- \[ ] /temp
- \[ ] /ds

#### P29. ¿Cómo se detiene un Lambda en ejecución que está atascado en un bucle recursivo?

- \[ ] Delete the function.
- \[x] Set the function concurrent execution limit to 0 while you update the code.
- \[ ] Reset the function.
- \[ ] Set the function concurrent execution limit to 100 while you update the code.

#### P30. ¿Cuáles son las prácticas recomendadas de AWS para la configuración de Lambda?

- \[x] Overprovision memory to run your functions faster and reduce your costs. Do not overprovision your function timeout settings.
- \[ ] Overprovision memory and your function timeout settings to run your functions faster and reduce your costs.
- \[ ] Do not overprovision memory. Overprovision your function timeout settings to run your functions faster and reduce costs.
- \[ ] Do not overprovision memory. Do not overprovision your function timeout settings to run your functions faster and reduce costs.

#### P31. ¿Los permisos básicos de Lambda incluyen permisos para qué?

- \[ ] removing log groups
- \[ ] none of these answers
- \[ ] creating log groups
- \[x] updating log groups

#### P32. ¿Cómo se almacenan las variables de entorno?

- \[ ] DynamoDB tables
- \[x] key-value pairs
- \[ ] S3 buckets
- \[ ] none of these answers

#### P33. Debe utilizar un Lambda para proporcionar lógica de backend a su sitio web. ¿Qué servicio utiliza para que su Lambda esté disponible para su sitio web?

- \[ ] S3
- \[x] API Gateway
- \[ ] X-Ray
- \[ ] DynamoDB

#### P34. Está creando un Lambda para activar el cambio a archivos en un bucket de S3. ¿Dónde debe poner el nombre del bucket?

- \[ ] in the Lambda function code
- \[x] in a Lambda environment variable
- \[ ] in the Lambda tags
- \[ ] in another S3 bucket

#### P35. ¿Qué acción es necesaria para poder probar un Lambda?

- \[ ] Deploy the Lambda
- \[ ] Export the function
- \[ ] none of these answers
- \[x] Configure a test event

#### P36. ¿Qué tipo de paquetes puede utilizar con Node.js para Lambdas?

- \[ ] Fleece
- \[x] NPM
- \[ ] none of these answers
- \[ ] Pod

#### P37. ¿Los lambdas se supervisan de forma predeterminada mediante qué servicio?

- \[ ] CloudTrail
- \[x] CloudWatch
- \[ ] CloudFormation
- \[ ] LogWatch

#### P38. ¿Qué puede desencadenar la ejecución de una función de Lambda?

- \[ ] a table definition
- \[ ] queue isolation
- \[ ] STS Write
- \[x] an SNS topic

#### P39. Debe establecer un desencadenador de eventos de S3 en Lambda para que responda cuando se agreguen datos al bucket desde otro bucket de S3. ¿Qué tipo de evento configura?

- \[ ] POST
- \[ ] "All object create events"
- \[x] PUT
- \[ ] COPY

#### P40. Para que Lambdas sea más comprobable, ¿es una práctica recomendada de AWS separar cuál de ellos?

- \[ ] Lambda configuration from logging code
- \[ ] Lambda handler from logging code
- \[x] Lambda handler from core logic
- \[ ] Lambda configuration from core logic

#### P41. ¿Qué se incluye en un paquete de implementación de Lambda exportado?

- \[ ] YAML definition
- \[ ] CloudFormation stack configuration
- \[ ] SAML deployment stack
- \[x] Zip file of all related files

#### P42. ¿Cuándo se puede cambiar el rol de ejecución de un Lambda?

- \[ ] only at creation
- \[ ] only before deployment
- \[ ] never
- \[x] anytime via configuration

#### P43. ¿Cuál es la relación entre la plantilla SAM y los archivos de plantilla de CloudFormation?

- \[x] Las plantillas SAM son un superconjunto de plantillas de CloudFormation. Las plantillas SAM incluyen tipos de recursos adicionales.
- \[ ] Las plantillas SAM tienen cierta superposición con las plantillas de CloudFormation. Las plantillas SAM y CloudFormation incluyen tipos de recursos que no están en el otro tipo de plantilla.
- \[ ] Las plantillas de CloudFormation son un superconjunto de plantillas SAM. Las plantillas de CloudFormation incluyen tipos de recursos adicionales.
- \[ ] Las plantillas SAM son un nombre diferente para las plantillas de CloudFormation. Ambos tipos de plantilla incluyen los mismos tipos de recursos.

#### P44. ¿Qué servicio implementa Lambdas regionalmente?

- \[ ] EdgeCloud
- \[ ] CloudEdge
- \[x] CloudFront
- \[ ] CloudStack

#### P45. ¿Qué lenguaje de programación admite AWS Lambda?

- \[ ] custom
- \[x] all of these answers
- \[ ] Java
- \[ ] Ruby

#### P46. Debe configurar un mecanismo para establecer controles que le notifiquen cuando tenga un pico en la simultaneidad de Lambda. ¿Qué debes hacer?

- \[ ] Implemente una alarma de CloudTrail que le notifique cuando las métricas de función superen su umbral. Cree un presupuesto de AWS para supervisar los costos.
- \[x] Implemente una alarma de CloudWatch que le notifique cuando las métricas de la función superen su umbral. Cree un presupuesto de AWS para supervisar los costos.
- \[ ] Implemente una alarma de CloudWatch que le notifique cuando las métricas de la función superen su umbral. Cree un AWS CostMonitor para supervisar los costos.
- \[ ] Implemente una alarma de CloudTrail que le notifique cuando las métricas de función superen su umbral. Cree un AWS CostMonitor para supervisar los costos.

#### P47. Desea minimizar el tiempo de inicio en frío de Lambda. ¿A qué te dedicas?

- \[ ] Agregue código adicional para comprobar si la caché transitoria, o el directorio /tmp, tiene los datos que almacenó.
- \[ ] Agregue código adicional para verificar si la caché permanente, o el directorio /cache, tiene los datos que almacenó.
- \[ ] No hacer nada. AWS minimiza la hora de inicio de cols de forma predeterminada.
- \[ ] Cree un Lambda de calentamiento que llame a su Lambda cada minuto

[Referencia] (https://aws.amazon.com/blogs/compute/new-for-aws-lambda-predictable-start-up-times-with-provisioned-concurrency/

#### P48. ¿Cuándo se almacena el código Lambda cifrado?

- \[x] en reposo
- \[ ] en tiempo de ejecución
- \[ ] en el despliegue
- \[ ] ninguna de estas respuestas

[Referencia](https://docs.aws.amazon.com/whitepapers/latest/security-overview-aws-lambda/lambda-functions-and-layers.html)

#### Pregunta 49. Cuando se utiliza una directiva basada en recursos para conceder a un servicio, recurso o cuenta acceso a la función, ¿cómo se puede aplicar el ámbito de ese permiso?

- \[ ] en el nivel de función en el nivel de función
- \[ ] en el nivel de alias o función en el nivel de alias o función
- \[ ] en el nivel de versión, alias o función en el nivel de versión, alias o función
- \[ ] a nivel de versión o función

#### Pregunta 50. Lambda puede leer eventos de qué otros servicios de AWS? (ref-https://docs.aws.amazon.com/lambda/latest/dg/lambda-servicios.html)

- \[ ] Kinesis, S3 y SQS
- \[ ] Kinesis, S3 y SNS
- \[ ] Kinesis, DynamoDB y SNS
- \[ ] Kinesis, DynamoDB y SQS
