## AWS Lambda

#### Q1. Comment augmenter les ressources CPU pour votre Lambda ?

- \[ ] Increase the configured CPU value
- \[ ] Increase the configured timeout value
- \[x] Increase the configured memory value
- \[ ] Increase the configured concurrency value

#### Q2. Comment fournir du code ou du contenu supplémentaire pour votre Lambda ?

- \[ ] blocks
- \[x] layers
- \[ ] aliases
- \[ ] handlers

#### Q3. Comment Step Functions peut-il appeler des Lambdas ?

- \[ ] in sequence
- \[x] both of these answers
- \[ ] neither of these answers
- \[ ] in parallel

#### Q4. Quelle commande AWS CLI appelle une fonction ?

- \[ ] aws lambda invoke --function ReturnBucketName outputfile.txt
- \[ ] aws lambda execute --function-name ReturnBucketName outputfile.txt
- \[x] aws lambda invoke --function-name ReturnBucketName outputfile.txt
- \[ ] aws lambda execute --function ReturnBucketName outputfile.txt

#### Q5. Qu’est-ce qui ajoute des fonctionnalités de suivi à un Lambda ?

- \[ ] AWS Trace
- \[ ] CloudStack
- \[ ] CloudTrail
- \[x] AWS X-Ray

#### Q6. Vous devez créer un pipeline d’intégration/déploiement continu pour un ensemble de Lambdas. Que devriez-vous faire?

- \[ ] Create configuration files and deploy them using AWS CodePipeline.
- \[ ] Create CloudFormation templates and deploy them using AWS CodeBuild
- \[ ] Create configuration file and deploy using AWS CodeBuild
- \[x] Create CloudFormation templates and deploy them using AWS CodePipeline.

#### Q7. Que pouvez-vous utiliser pour surveiller les appels de fonction ?

- \[ ] API Gateway
- \[ ] S3
- \[ ] SAS
- \[x] CLoudTrail

#### Q8. Il est recommandé à AWS d’activer la journalisation Lambda par laquelle de ces méthodes.

- \[ ] Use S3 metrics and CloudWatch alarms
- \[ ] Create custom metrics within your Lambda code.
- \[ ] Create custom metrics within your CloudWatch code.
- \[x] Use Lambda metrics and CloudWatch alarms.

#### Q9. Que peut-on fournir pour les variables d’environnement?

- \[ ] an SSL certificate
- \[ ] a bitmask
- \[x] an AWS KMS key
- \[ ] an HTTP protocol 

#### Q10. Les lambdas permettent d’exécuter quoi d’autre chose ?

- \[ ] binaries.
- \[x] all of these answers
- \[ ] executables
- \[ ] Shell scripts

#### Q11. Dans quel style devez-vous écrire du code Lambda ?

- \[ ] MVC
- \[ ] virtual
- \[x] stateless
- \[ ] protocol

#### Q12. Comment un développeur peut-il fournir du code Lambda ?

- \[ ] by uploading a .zip file
- \[x] all of these answers
- \[ ] by editing inline
- \[ ] from an S3 bucket

#### Q13. Vous testez les performances de votre Lambda pour vérifier que vous définissez correctement la taille de la mémoire. Où vérifiez-vous la surcharge d’exécution ?

- \[ ] CLoudWatch logs
- \[ ] DynamoDB logs
- \[ ] S3 logs
- \[x] Lambda logs.

#### Q14. Qu’est-ce qui facilite la livraison continue de Lambdas ?

- \[ ] CodeStack
- \[ ] ElasticStack
- \[ ] Mobile Hub
- \[x] CodeDeploy

#### Q15. Comment les ressources informatiques sont-elles allouées aux Lambdas ?

- \[x] proportionally
- \[ ] equally
- \[ ] periodically
- \[ ] daily

#### Q16. Vous pouvez restreindre l’étendue des autorisations d’un utilisateur en spécifiant les deux éléments d’une stratégie IAM ?

- \[ ] resources and users
- \[x] resources and conditions
- \[ ] events and users
- \[ ] events and conditions

#### Q17. Qu’est-ce que la journalisation Lambda inclut ?

- \[x] logging streams
- \[ ] rotating streams
- \[ ] logging events
- \[ ] advancing log groups

#### Q18. Que ne peut PAS faire AWS Amplify pour un Lambda ?

- \[ ] create a Lambda
- \[x] be an event source
- \[ ] assign an IAM role
- \[ ] delete a Lambda

#### Q19. Comment créer un Lambda dans un langage de programmation qu’AWS ne prend pas en charge ?

- \[ ] Create a Lambda function with a custom runtime and reference the function in your Lambda
- \[x] Create a Lambda layer with a custom runtime and reference the layer in your lambda
- \[ ] You cannot use Lambda in this situation
- \[ ] Create a Lambda function with a custom runtime

#### Q20. Sur quoi se basent les ressources en aval répertoriées ?

- \[ ] the execution policy
- \[x] the Lambda configuration
- \[ ] the Lambda nodes
- \[ ] the IAM user

#### Q21. Quelle est une balise équivalente et valide pour une paire de Lambdas ?

- \[ ] department:Sales,department:Sales
- \[x] department:Sales,department:sales
- \[ ] aws:demo;aws:demo
- \[ ] aws:demo;aws:DEMO

#### Q22. Les connexions sortantes à partir de Lambdas doivent être `_`.

- \[ ] neither of these answers
- \[ ] UDP/IP
- \[ ] TCP/IP
- \[x] both of these answers

#### Q23. Comment les actions CloudWatch sont-elles configurées ?

- \[ ] automatically
- \[ ] none of these answers
- \[x] manually
- \[ ] ad hoc

#### Q24. Vous testez votre application basée sur un flux et le Lambda associé. Les bonnes pratiques AWS vous conseillent de tester en variant quoi ?

- \[ ] stream and record sizes
- \[ ] stream and shard sizes
- \[x] batch and record sizes
- \[ ] batch and shard sizes

#### Q25. Vous devez mettre votre Lambda à la disposition des services de plusieurs VPC. Que fais-tu?

- \[ ] Place each subnet in a VPC. Associate all subnets to your Lambda.
- \[ ] Place all subnets in a VPC. Associate all subnets to your Lambda.
- \[ ] Configure your Lambda to be available to multiple VPCs.
- \[x] Configure all application VPCs to be peered.

#### Q26. Comment le coût associé à la fonction Lambda est-il calculé ?

- \[ ] number of function calls
- \[ ] amount of code run
- \[x] compute time
- \[ ] amount of infrastructure used

#### Q27. Quel est le moyen le plus rapide de démarrer avec Lambda ?

- \[ ] Author a Lambda from scratch.
- \[x] Use a blueprint.
- \[ ] Use a .zip deployment package.
- \[ ] Use the serverless app repository.

#### Q28. Où l’espace disque est-il alloué aux fonctions Lambda ?

- \[x] /tmp
- \[ ] /default
- \[ ] /temp
- \[ ] /ds

#### Q29. Comment arrêter un Lambda en cours d’exécution qui est bloqué dans une boucle récursive ?

- \[ ] Delete the function.
- \[x] Set the function concurrent execution limit to 0 while you update the code.
- \[ ] Reset the function.
- \[ ] Set the function concurrent execution limit to 100 while you update the code.

#### Q30. Quelles sont les meilleures pratiques AWS pour la configuration Lambda ?

- \[x] Overprovision memory to run your functions faster and reduce your costs. Do not overprovision your function timeout settings.
- \[ ] Overprovision memory and your function timeout settings to run your functions faster and reduce your costs.
- \[ ] Do not overprovision memory. Overprovision your function timeout settings to run your functions faster and reduce costs.
- \[ ] Do not overprovision memory. Do not overprovision your function timeout settings to run your functions faster and reduce costs.

#### Q31. Les autorisations Lambda de base incluent des autorisations pour quoi ?

- \[ ] removing log groups
- \[ ] none of these answers
- \[ ] creating log groups
- \[x] updating log groups

#### Q32. Comment les variables d’environnement sont-elles stockées ?

- \[ ] DynamoDB tables
- \[x] key-value pairs
- \[ ] S3 buckets
- \[ ] none of these answers

#### Q33. Vous devez utiliser un Lambda pour fournir une logique backend à votre site Web. Quel service utilisez-vous pour mettre votre Lambda à la disposition de votre site Web ?

- \[ ] S3
- \[x] API Gateway
- \[ ] X-Ray
- \[ ] DynamoDB

#### Q34. Vous créez un Lambda à déclencher lors de la modification des fichiers dans un compartiment S3. Où devriez-vous mettre le nom du seau?

- \[ ] in the Lambda function code
- \[x] in a Lambda environment variable
- \[ ] in the Lambda tags
- \[ ] in another S3 bucket

#### Q35. Quelle action est nécessaire avant de pouvoir tester un Lambda ?

- \[ ] Deploy the Lambda
- \[ ] Export the function
- \[ ] none of these answers
- \[x] Configure a test event

#### Q36. Quel type de packages pouvez-vous utiliser avec Node.js for Lambdas ?

- \[ ] Fleece
- \[x] NPM
- \[ ] none of these answers
- \[ ] Pod

#### Q37. Les lambdas sont surveillés par défaut à l’aide de quel service ?

- \[ ] CloudTrail
- \[x] CloudWatch
- \[ ] CloudFormation
- \[ ] LogWatch

#### Q38. Qu’est-ce qui peut déclencher l’exécution d’une fonction Lambda ?

- \[ ] a table definition
- \[ ] queue isolation
- \[ ] STS Write
- \[x] an SNS topic

#### Q39. Vous devez définir un déclencheur d’événement S3 sur votre Lambda pour répondre lorsque des données sont ajoutées à votre compartiment à partir d’un autre compartiment S3. Quel type d’événement configurez-vous ?

- \[ ] POST
- \[ ] "All object create events"
- \[x] PUT
- \[ ] COPY

#### Q40. Pour rendre les Lambdas plus testables, il est recommandé par AWS de séparer lesquels d’entre eux ?

- \[ ] Lambda configuration from logging code
- \[ ] Lambda handler from logging code
- \[x] Lambda handler from core logic
- \[ ] Lambda configuration from core logic

#### Q41. Qu’est-ce qui est inclus dans un package de déploiement Lambda exporté ?

- \[ ] YAML definition
- \[ ] CloudFormation stack configuration
- \[ ] SAML deployment stack
- \[x] Zip file of all related files

#### Q42. Quand pouvez-vous modifier le rôle d’exécution d’un Lambda ?

- \[ ] only at creation
- \[ ] only before deployment
- \[ ] never
- \[x] anytime via configuration

#### Q43. Quelle est la relation entre le modèle SAM et les fichiers de modèle CloudFormation ?

- \[x] Les modèles SAM sont un sur-ensemble de modèles CloudFormation. Les modèles SAM incluent des types de ressources supplémentaires.
- \[ ] Les modèles SAM ont un certain chevauchement avec les modèles CloudFormation. Les modèles SAM et CloudFormation incluent des types de ressources qui ne figurent pas dans l’autre type de modèle.
- \[ ] Les modèles CloudFormation sont un sur-ensemble de modèles SAM. Les modèles CloudFormation incluent des types de ressources supplémentaires.
- \[ ] Les modèles SAM sont un nom différent pour les modèles CloudFormation. Les deux types de modèles incluent les mêmes types de ressources.

#### Q44. Quel service déploie Lambdas au niveau régional ?

- \[ ] EdgeCloud
- \[ ] CloudEdge
- \[x] CloudFront
- \[ ] CloudStack

#### Q45. Quel langage de programmation AWS Lambda prend-il en charge ?

- \[ ] custom
- \[x] all of these answers
- \[ ] Java
- \[ ] Ruby

#### Q46. Vous devez configurer un mécanisme pour mettre en place des contrôles afin de vous avertir lorsque vous avez un pic dans l’accès concurrentiel Lambda. Que devriez-vous faire?

- \[ ] Déployez une alarme CloudTrail qui vous avertit lorsque les métriques de fonction dépassent votre seuil. Créez un budget AWS pour surveiller les coûts.
- \[x] Déployez une alarme CloudWatch qui vous avertit lorsque les métriques de fonction dépassent votre seuil. Créez un budget AWS pour surveiller les coûts.
- \[ ] Déployez une alarme CloudWatch qui vous avertit lorsque les métriques de fonction dépassent votre seuil. Créez un AWS CostMonitor pour surveiller les coûts.
- \[ ] Déployez une alarme CloudTrail qui vous avertit lorsque les métriques de fonction dépassent votre seuil. Créez un AWS CostMonitor pour surveiller les coûts.

#### Q47. Vous souhaitez minimiser le temps de démarrage à froid de votre Lambda. Que fais-tu?

- \[ ] Ajoutez du code supplémentaire pour vérifier si le cache transitoire, ou le répertoire /tmp, contient les données que vous avez stockées.
- \[ ] Ajoutez du code supplémentaire pour vérifier si le cache permanent, ou le répertoire /cache, contient les données que vous avez stockées.
- \[ ] Ne rien faire. AWS minimise l’heure de début des cols par défaut.
- \[ ] Créez un Lambda d’échauffement qui appelle votre Lambda toutes les minutes

[Référence] (https://aws.amazon.com/blogs/compute/new-for-aws-lambda-predictable-start-up-times-with-provisioned-concurrency/

#### Q48. Quand le code Lambda stocké est-il chiffré ?

- \[x] au repos
- \[ ] au moment de l’exécution
- \[ ] au déploiement
- \[ ] aucune de ces réponses

[Référence](https://docs.aws.amazon.com/whitepapers/latest/security-overview-aws-lambda/lambda-functions-and-layers.html)

#### Q49. Lorsque vous utilisez une stratégie basée sur les ressources pour donner à un service, une ressource ou un compte l’accès à votre fonction, comment pouvez-vous appliquer la portée de cette autorisation ??

- \[ ] au niveau de la fonctionau niveau de la fonction
- \[ ] au niveau de l’alias ou de la fonction au niveau de l’alias ou de la fonction
- \[ ] au niveau de la version, de l’alias ou de la fonction au niveau de la version, de l’alias ou de la fonction
- \[ ] au niveau de la version ou de la fonction

#### Q50. Lambda peut lire les événements à partir de quels autres services AWS ? (réf-https://docs.aws.amazon.com/lambda/latest/dg/lambda-services.html)

- \[ ] Kinesis, S3 et SQS
- \[ ] Kinesis, S3 et SNS
- \[ ] Kinesis, DynamoDB et SNS
- \[ ] Kinesis, DynamoDB et SQS
