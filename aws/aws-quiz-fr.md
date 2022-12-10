## Amazon Web Services (AWS)

#### Q1. Vous disposez d’une application utilisant une base de données MySQL de 100 Go que vous migrez vers AWS. Que devez-vous prendre en compte lorsque vous décidez d’héberger la base de données sur RDS pour MySQL ou Aurora ?

- \[ ] coût
- \[ ] facilité de maintenance vs granularité du contrôle
- \[x] toutes ces réponses
- \[ ] le moteur de stockage actuel utilisé par l’application, tel que InnoDB ou MyISAM

#### Q2. Quelle base de données est un type de base de données NoSQL capable de stocker et de récupérer rapidement des paires clé-valeur ?

- \[ ] Aurores boréales
- \[ ] Neptune
- \[ ] RDS pour MySQL
- \[x] DynamoDB

#### Q3. Votre base de données est une instance RDS exécutant SQL Server avec réplication multi-AZ et vous disposez de plusieurs anciens utilitaires de console .NET qui effectuent des opérations de base de données toutes les 15 secondes. Lorsque le cluster doit basculer le serveur de base de données principal vers la zone AZ secondaire, les utilitaires .NET commencent à signaler les échecs de connexion à la base de données, bien que d’autres applications puissent accéder à la base de données. Comment corriger ce problème ?

- \[ ] Utilisez la console RDS pour forcer un redémarrage de l’instance de base de données afin que le serveur principal redevienne le serveur maître.
- \[ ] Le serveur exécutant les utilitaires .NET met en cache la recherche DNS sur l’adresse du cluster de bases de données. Videz le cache DNS du serveur et forcez les utilitaires C# à ouvrir de nouvelles connexions à la base de données.
- \[ ] A.NET application conserve l’adresse IP d’une chaîne de connexion jusqu’à ce que la machine hôte soit redémarrée.
- \[x] Les utilitaires NET doivent modifier le point de terminaison SQL Server dans les chaînes de connexion pour lire à partir du serveur de base de données secondaire à l’aide d’un try/catch.

#### Q4. Quels services AWS peuvent vous aider à automatiser votre pipeline de développement pour une intégration et un déploiement continus ?

- \[ ] CodePipeline
- \[ ] CodeDeploy
- \[x] toutes ces réponses
- \[ ] CodeBuild

#### Q5. Quel service AWS est conforme aux normes décrites dans la norme PCI DSS (Payment Card Industry Data Security Standard) niveau 1 pour le traitement et la transmission des données de carte de crédit ?

- \[ ] Passerelle API
- \[x] toutes ces réponses
- \[ ] Service de file d’attente simple (SQS)
- \[ ] Flux de données Kinesis

#### Q6. Vous disposez d’une grande quantité de fichiers sur votre baie de stockage rattachée au réseau qui doivent être archivés et conservés pendant une période de 10 ans en raison des réglementations du secteur. Ces données seront rarement consultées mais doivent être conservées Quel est le meilleur service AWS pour stocker ces données ?

- \[ ] EFS
- \[ ] Boule de neige
- \[ ] OEBS
- \[x] Glacier S3

#### Q7. Pour votre compte racine AWS, vous avez généré un mot de passe aléatoire de la longueur maximale autorisée et inclus des caractères spéciaux. Quelles mesures supplémentaires devez-vous suivre pour sécuriser votre compte racine AWS ?

- \[ ] Créez un rôle AM pour l’administrateur de compte disposant des privilèges les plus élevés. Ne stockez pas le mot de passe root, mais lorsque le compte root est nécessaire, réinitialisez le mot de passe sur le compte root via une confirmation par e-mail et répétez cette procédure.
- \[ ] Stockez votre mot de passe généré aléatoirement dans votre base de données de secrets d’organisation à l’aide d’un service tel que 1Password ou LastPass, et n’accordez l’accès à ce secret qu’à l’équipe DevOps.
- \[ ] Créez des comptes IAM pour vos administrateurs et attachez la stratégie AdministratorAccess à leurs comptes. Désactivez le compte racine dans les paramètres utilisateur.
- \[x] Créez un rôle IAM pour l’administrateur de compte disposant des privilèges les plus élevés et n’utilisez pas le compte racine dans les opérations quotidiennes. Activer l’authentification à deux facteurs sur le compte racine

#### Q8. Quelle option Elastic Load Balancing prend en charge Lambda en tant que cible ?

- \[ ] Équilibreur de charge réseau
- \[ ] Lambda ne peut pas être appelé directement par les requêtes Web entrantes. Vous devez utiliser API Gateway.
- \[ ] Équilibreur de charge classique
- \[x] Équilibreur de charge d’application

#### Q9. Comment concevoir une solution pour la réplication d’une base de données SQL Server dans les régions AWS dans une architecture active-active ?

- \[ ] Utilisez RDS pour SQL Server et créez la même instance dans deux régions différentes. Utilisez le service de migration de base de données pour synchroniser chaque base de données.
- \[ ] Utilisez un appairage VPN ou VPC pour établir une connexion entre les VPC de chaque région. Installez SQL Server Enterprise Edition sur des instances EC2 dans chaque région et configurez un groupe de disponibilité Always On.
- \[x] Utilisez RDS pour SQL Server 2016 ou 2017 Enterprise Edition. Activez la prise en charge multi-AZ et sélectionnez l’option Mise en miroir/Toujours activé. Sélectionnez une autre région pour l’option de mise en miroir.
- \[ ] Vous ne pouvez pas configurer une architecture active-active pour SQL Server qui s’étend sur des régions géographiques.

[Référence](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html?opt_id=oeu1612780272452r0.9199525073583283)

#### Q10. Combien coûte le lancement d’une instance EC2 à partir d’AWS Marketplace ?

- \[ ] Toutes les images d’AWS Marketplace entraînent des frais horaires supplémentaires en plus des frais de la taille d’instance que vous sélectionnez.
- \[ ] Vous ne pouvez lancer que des images créées par d’autres utilisateurs sur votre compte AWS, vous ne payez donc que pour la taille d’instance que vous sélectionnez et les coûts de stockage S3 pour l’image de base.
- \[x] Chaque image a son propre prix qui peut être gratuit ou inclure des frais pour les coûts de licence logicielle. Vous paierez également pour l’instance sur laquelle l’image s’exécute
- \[ ] Toutes les images d’AWS Marketplace contiennent uniquement des logiciels open source sans frais supplémentaires et sont créées par d’autres utilisateurs AWS. Vous ne paierez que pour la taille d’instance que vous sélectionnez.

#### Q11. Lorsque vous utilisez un cluster ECS avec des instances EC2, quelles tâches de maintenance devez-vous effectuer sur les EC2 ?

- \[ ] Les instances créées par ECS n’ont pas de correctifs qui doivent être appliqués ; toutefois, vous devez vous assurer que vos conteneurs contiennent des mises à jour de sécurité importantes.
- \[x] Actualisez le cluster avec des instances créées à partir de la dernière AMI ECS.
- \[ ] Les clusters ECS n’utilisent pas d’instances EC2.
- \[ ] Vous ne devez pas manipuler directement les instances EC2 créées par ECS. AWS mettra automatiquement à jour ces instances.

#### Q12. Quel serveur de mise en cache en mémoire n’est pas pris en charge par ElastiCache ?

- \[ ] Redis 5
- \[ ] Memcached
- \[x] Elasticsearch
- \[ ] Redis 3

#### Q13. Quel service AWS peut être utilisé pour aider à générer la documentation requise par diverses normes de conformité, telles que la norme de sécurité des données de l’industrie des cartes de paiement (PCI DSS) niveau 1 pour le traitement des données de carte de crédit ?

- \[x] Artéfact
- \[ ] Base de données document
- \[ ] Imprimez le résumé de conformité AWS et conservez-le avec la documentation requise pour un audit.
- \[ ] Gestionnaire de secrets

#### Q14. Lorsque vous utilisez AWS pour la recherche et le développement avant une migration planifiée, comment éviter des augmentations ou des pics inattendus dans la facturation ?

- \[ ] Utilisez le tableau de bord de facturation pour créer un budget de coûts. Entrez le montant maximum que vous souhaitez facturer chaque mois. Tout frais dépassant ce montant entraînera la suspension automatique de ces ressources par AWS.
- \[ ] À l’aide du compte AWS racine, activez l’accès IAM aux informations de facturation du compte. Assurez-vous que vos utilisateurs IAM disposent de la stratégie Billing FullAccessGroup. Ensuite, à partir du tableau de bord de facturation, vérifiez les frais accumulés une fois par jour.
- \[ ] Si vous utilisez l’offre gratuite AWS, vous devrez confirmer l’utilisation de tout service qui dépasse les limites de l’offre gratuite AWS.
- \[x] L’utilisation du compte AWS racine active les alertes de facturation dans les préférences de l’utilisateur. Utilisez ensuite CloudWatch pour créer une alarme de facturation et définir un seuil à un montant spécifique en dollars pour vos frais mensuels estimés.

#### Q15. Vous créez une table DynamoDB pour stocker tous les films sortis depuis 1938. Votre application permettra aux utilisateurs de rechercher par titre de film et de voir les détails de ce film. Compte tenu de l’exemple ci-dessous montrant les données vidéo que vous allez importer, quel est le meilleur ensemble de clés à appliquer à cette table ?

```json
{
  "title": "The Avengers",
  "year": 2012,
  "cast": ["Mark Ruffalo", "Robert Downey, Jr."],
  "genres": ["Action"]
}
```

- \[ ] La clé primaire doit être une clé de partition du champ de titre.
- \[ ] La clé primaire doit être le champ de titre et la clé de partition doit être le champ genres.
- \[ ] La clé primaire doit être une clé composite composée d’une clé de partition dans le champ de titre et d’une clé de tri dans le champ d’année.
- \[x] La clé primaire doit être créée comme une valeur complètement unique, telle qu’une liste numérique séquentielle d’ID de film. La clé de partition doit être un champ de titre pour une recherche rapide.

#### Q16. Quel magasin de données offre un moyen simple et rapide de stocker les attributs utilisateur de base dans un format basé sur un objet ?

- \[ ] ORDS pour Oracle
- \[ ] Décalage vers le rouge
- \[ ] Neptune
- \[x] DynamoDB

#### Q17. Vous avez besoin d’une base de données sans schéma. Quel service de base de données Amazon fournit cette solution ?

- \[ ] ORDS
- \[ ] Aurores boréales
- \[ ] Décalage vers le rouge
- \[x] DynamoDB

#### Q18. Quel canal de communication SNS ne prend-il pas en charge en mode natif ?

- \[ ] Message texte OSMS
- \[ ] notification push
- \[ ] courriel
- \[x] appel téléphonique automatisé

#### Q19. Lors de la conception d’une application Web sans serveur à l’aide de Lambda, quel concept clé devez-vous prendre en compte dans votre conception ?

- \[ ] Les applications Web sans serveur s’exécutent dans le navigateur Web de l’utilisateur, vous devrez donc stocker toutes les données que l’utilisateur modifie directement dans une base de données.
- \[ ] Lambda vous permet uniquement d’écrire des fonctions en JavaScript.
- \[ ] Lambda n’utilise pas de serveurs, il ne peut donc renvoyer que la même requête à chaque utilisateur.
- \[x] Lambda est sans état, il ne se souviendra donc pas qui est un utilisateur entre les demandes.

#### Q20. Un principe de DevOps est de considérer l’infrastructure comme du code. Quel service AWS vous permet de scripter votre infrastructure AWS ?

- \[ ] CloudTrail
- \[x] CloudFormation
- \[ ] AWS Config
- \[ ] Catalogue de services AWS

#### Q21. Vous avez créé une instance Windows EC2 avec une adresse IP publique et installé SQL Server. Lorsque vous tentez de vous connecter à SQL Server à partir de SQL Server Enterprise Manager sur votre ordinateur local, l’instance Windows EC2 ne parvient pas à établir une connexion au serveur. Quelle est la première chose que vous devriez vérifier?

- \[ ] Vérifiez les tables de routage pour le VPC.
- \[x] Vérifiez que les groupes de sécurité affectés autorisent le trafic du port TCP 1433 à partir de votre adresse IP actuelle.
- \[ ] Vérifiez les stratégies dans le Pare-feu Windows.
- \[ ] Vérifiez que vous vous connectez à l’instance à l’aide d’un utilisateur qui n’est pas sa.

#### Q22. Vous hébergez une application configurée pour diffuser du contenu multimédia vers ses clients sur les ports TCP 3380-3384, 3386-3388 et 3390. L’onglet Entrant ci-dessous affiche trois stratégies de groupe de sécurité entrantes attachées à cette instance. Quelle politique devriez-vous utiliser?

![image](images/001.png?raw=png)

- \[x] La règle qui expose les ports TCP 3380-3390 exposerait également publiquement le port 3389 (RDP) à l’ensemble d’Internet. Écrivez des règles distinctes pour n’exposer que les ports nécessaires.
- \[ ] La première règle de groupe de sécurité autorise tout le trafic dans cette instance. Exposer l’ensemble de votre instance à l’ensemble d’Internet laisse le serveur ouvert à diverses attaques des autres services s’exécutant sur différents numéros de port.
- \[ ] Vérifiez que les propriétaires de compte AWS contrôlent réellement l’intégralité du bloc CIDR C pour 12.228.11.0-255 et qu’il s’agit d’adresses IP sécurisées pour l’accès RDP à cette instance.
- \[ ] Il n’y a pas de recommandations à faire.

#### Q23. Vous disposez de quatre serveurs Web frontaux derrière un équilibreur de charge, qui utilisent NFS pour accéder à une autre instance EC2 qui redimensionne et stocke des images pour l’application frontale. Quelles stratégies de groupe de sécurité doivent être affectées à ces serveurs ?

- \[ ] Attribuez des adresses IP Elastic à toutes les instances et créez un groupe qui permet à tout le trafic de passer entre chacune des cinq instances
  Adresses IP Élastiques et autorisent tout le trafic HTTPS entrant.
- \[x] Les serveurs Web frontaux doivent autoriser HTTPS. Affectez un autre groupe à toutes les instances qui permettent à tout le trafic de passer entre les instances utilisant ce groupe.
- \[ ] Créez un groupe de sécurité qui autorise le trafic NFS, HTTP et HTTPS entrant à partir de toutes les adresses IP. Appliquez ce groupe à tous les serveurs.
- \[ ] Créez un groupe de sécurité qui autorise le trafic HTTP et HTTPS entrant à partir de toutes les adresses IP et appliquez-le aux serveurs Web. Créez un deuxième groupe de sécurité pour le magasin de fichiers NFS qui autorise le trafic NFS sortant vers la plage d’adresses IP privée des serveurs Web frontaux.

#### Q24. Vous avez un serveur Web Linux EC2 qui expire soudainement sur toutes les requêtes HTTP et vos tentatives de connexion SSH expirent. Vous remarquez qu’il échoue la vérification de l’état du système dans la console EC2. Quelles mesures devriez-vous prendre?

- \[x] Restaurez l’instance à partir de la dernière image AMI. Les vérifications de l’état du système indiquent que le système de fichiers de l’instance est endommagé.
- \[ ] Arrêtez et démarrez l’instance. Cela déplacera l’instance vers un autre hôte.
- \[ ] Contactez le support AWS. L’échec d’une vérification de l’état du système indique une défaillance du matériel sous-jacent et doit être résolu par un représentant AWS.
- \[ ] Redémarrez l’instance. Cela arrêtera et démarrera l’instance et la déplacera vers un autre hôte.

#### Q25. Vous disposez de plusieurs serveurs sur site et souhaitez stocker vos sauvegardes hors site sur AWS. Quel service de sauvegarde entièrement géré pouvez-vous utiliser pour expédier vos sauvegardes à AWS ?

- \[ ] Windows Server 2016 prend en charge S3 comme cible lors de l’utilisation de réplicas de stockage.
- \[x] Utilisez Storage Gateway.
- \[ ] Synchronisez les fichiers directement avec S3 avec l’AWS CLI.
- \[ ] Utilisez la console RDS pour forcer un redémarrage de l’instance de base de données afin que le serveur principal redevienne le serveur maître.

#### Q26. Quelle est la meilleure pratique pour créer une base de données PostgreSQL hautement disponible dans RDS qui peut supporter la perte d’une seule région AWS ?

- \[ ] PostgreSQL ne peut pas être répliqué entre les régions. Restaurez les sauvegardes de base de données à partir d’un compartiment S3 et redirigez vos connexions de base de données vers la nouvelle instance.
- \[ ] Créez des réplicas en lecture dans d’autres régions AWS. Vous pouvez désigner une nouvelle base de données master à partir de n’importe quel réplica en lecture jusqu’à ce que l’échec régional soit résolu.
- \[ ] Vérifiez que votre instance est configurée pour la prise en charge multi-AZ. Les modifications apportées à la base de données seront automatiquement synchronisées avec une autre région en cas de défaillance et RDS sélectionnera automatiquement un nouveau maître jusqu’à ce que la défaillance régionale soit résolue.
- \[x] Créez des réplicas en lecture dans d’autres régions AWS. Assurez-vous que les opérations de lecture sur la base de données se produisent sur un réplica en lecture disponible et envoyez des opérations d’écriture à une autre région si vous devez promouvoir un réplica en lecture en une base de données autonome si le maître est en panne.

#### Q27. Vous avez créé une nouvelle instance Linux EC2 et installé PostgreSQL, mais vous ne pouvez pas établir de connexion au serveur à partir de votre ordinateur local. Quelles mesures prenez-vous pour résoudre ce problème ?

- \[ ] Créez une règle de groupe de sécurité qui autorise tout le trafic à partir de 0.0.0.0/0. Cela permettra de vérifier si une autre règle refuse ou non le trafic.
- \[x] Vérifiez que les groupes de sécurité affectés autorisent le trafic de votre adresse IP vers le port 5432. Vérifiez que PostgreSQL est configuré pour écouter le trafic externe et qu’il est lié à l’interface publique.
- \[ ] Assurez-vous que vous utilisez une adresse IP Elastic et qu’elle est incluse dans le `postgresql.conf` fichier de configuration.
- \[ ] Arrêtez et démarrez l’instance. Les nouvelles règles de groupe de sécurité ne prendront effet qu’après un redémarrage.

#### Q28. Que fait le corps d’instruction de cette stratégie de compartiment S3 ?

```json
{
  "Sid": "bucketpolicy1",
  "Effect": "Allow",
  "Principal": "*",
  "Action": "s3:GetObject",
  "Resource": "arn:aws:s3:::userreports/*",
  "Condition": {
    "IpAddress": { "aws:SourceIp": "68.249.108.0/24" },
    "NotIpAddress": { "aws:SourceIp": "68.249.108.128/32" }
  }
}
```

- \[ ] bucketpolicy1 permet à tout utilisateur d’effectuer n’importe quelle action sur les objets du compartiment userreports, mais limite les objets aux autorisations en lecture seule pour toute personne provenant de 68.249.108.0 à 68.249.108.255 - sauf 68.249.108.128.
- \[ ] bucketpolicy1 permet à tout utilisateur provenant de la plage IP 68.249.108.0 d’accéder aux objets du compartiment userreports et refuse l’accès à 68.249.108.128.
- \[ ] bucketpolicy1 permet à tout utilisateur d’effectuer n’importe quelle action sur les objets du compartiment userreports - à l’exception de toute personne provenant de l’adresse IP de 68.249.108.128.
- \[x] bucketpolicy1 permet à tout utilisateur provenant de la plage d’adresses IP de 68.249.108.0 à 68.249.108.255 d’accéder aux objets du compartiment userreports, à l’exception de toute personne provenant de l’adresse IP de 68.249.108.128.

#### Q29. Un nouveau développeur a été ajouté à l’équipe et vous avez été invité à fournir l’accès au compte AWS de l’organisation. Quelle est la meilleure pratique pour accorder l’accès ?

- \[ ] Donnez au nouveau développeur la connexion IAM attribuée à l’équipe de développement. Cet utilisateur IAM doit déjà inclure toutes les stratégies dont un développeur aurait besoin.
- \[ ] Créez un utilisateur IAM pour le nouveau développeur. Affectez manuellement des stratégies au nouveau compte d’utilisateur IAM.
- \[ ] Ne donnez pas au nouveau développeur l’accès à la console AWS. À l’aide de l’utilisateur IAM affecté au groupe de développement, générez un nouvel ensemble de clés d’accès et étiquetez-les avec le nom du développeur.
- \[x] Créez un utilisateur IAM pour le nouveau développeur. Affectez au nouveau développeur le groupe de développeurs que vous avez déjà créé pour les autres développeurs.

#### Q30. Lors du lancement d’une instance EC2 avec un type d’instance prenant en charge le stockage d’instance, quel cas d’utilisation est le meilleur pour le stockage d’instance ?

- \[x] Utilisez le stockage d’instance pour servir des fichiers temporaires nécessitant une faible latence d’E/S.
- \[ ] Utilisez le stockage d’instance pour gérer les fichiers téléchargés par vos utilisateurs. Comme il est plus sécurisé qu’un volume EBS, vous pouvez isoler tous les fichiers malveillants de l’infection de votre serveur.
- \[ ] Le stockage d’instance est plus rapide que les volumes EBS, installez donc la racine du système d’exploitation sur ce volume pour accélérer les performances du serveur.
- \[ ] Le stockage d’instance est une option déconseillée pour le stockage et ne doit pas être utilisé.

#### Q31. Quelle est la meilleure pratique pour la mise à l’échelle horizontale d’une application web ASP.NET héritée qui repose sur Active Directory et qui est actuellement déployée sur une seule instance Windows EC2 ?

- \[x] Utilisez Sysprep pour arrêter l’instance pendant une fenêtre de maintenance. Créez une image AMI et placez les deux serveurs derrière Application Load Balancer avec des sessions collantes.
- \[ ] Lancez un nouvel EC2 avec la dernière version de Windows Server et réinstallez l’application. Utilisez Application Load Balancer et les sessions collantes pour équilibrer les deux serveurs.
- \[ ] Créez un clone du serveur à l’aide d’une image AMI et d’un équilibreur de charge d’application utilisateur pour équilibrer le trafic entre les deux instances à l’aide de sessions collantes.
- \[ ] La mise à l’échelle horizontale n’est pas la meilleure pratique dans cette situation. Augmentez la taille de l’instance EC2 existante et mettez l’application à l’échelle verticalement.

#### Q32. Que fait cette petite section d’un modèle CloudFormation ?

```yaml
FlowLog:
  Type: AWS::EC2::FlowLog
  Properties:
    DeliverLogsPermissionArn: !GetAtt IamRole.Arn
    LogGroupName: FlowLogsGroup
    ResourceId: !Ref LogVpcId
    ResourceType: VPC
    TrafficType: ALL
```

- \[x] Il écrit les journaux de flux réseau VPC dans le groupe de journaux CloudWatch FlowLogsGroup. Vous pouvez l’utiliser pour inspecter les connexions réseau de votre VPC.
- \[ ] Il enregistre tout le trafic réseau au sein d’un VPC, à l’exception des ID d’instance définis par LogVpcID, et le consigne dans le groupe de journaux CloudWatch FlowLogsGroup.
- \[ ] Il enregistre tout le trafic réseau à destination et en provenance d’une seule instance EC2 dans le groupe de journaux CloudWatch FlowLogsGroup. Vous pouvez l’utiliser pour inspecter le trafic réseau suspect entrant dans une instance EC2.
- \[ ] Il enregistre toutes les requêtes DNS effectuées par les ressources au sein d’un VPC et les enregistre dans CloudWatch FlowLogsGroup. Utilisez cette option pour diagnostiquer les erreurs de recherche DNS dans votre environnement.

#### Q33. Vous exécutez des conteneurs Docker sur ECS. Quelle est la mesure la plus importante à surveiller?

- \[ ] Nombre de conteneurs en cours d’exécution pour chaque service à partir de CloudWatch.
- \[ ] L’intégrité de l’instance de chaque instance EC2 de votre cluster à partir de CloudWatch.
- \[ ] Surveillez le tableau de bord du service EC2. Surveillez les pannes affichées sur le service ECS.
- \[x] Consommation de mémoire de chaque instance EC2 de votre cluster à partir de CloudWatch.

#### Q34. Application Load Balancer peut acheminer le trafic vers plusieurs groupes cibles différents en fonction de plusieurs conditions. Lequel de ces cas d’utilisation n’est pas pris en charge par Application Load Balancer ?

- \[ ] Une requête avec un en-tête HTTP de X-Requested-With: staging peut être acheminée vers un groupe cible pour un service ECS dans votre environnement intermédiaire.
- \[ ] Les adresses IP source correspondant à 192.0.2.0/24 sur un port d’écoute de 1433 peuvent être acheminées vers un groupe cible pour un cluster RDS pour SQL Server.
- \[ ] Un chemin d’accès de /signup\* peut être acheminé vers un groupe cible pour une fonction Lambda qui traite les inscriptions de nouveaux utilisateurs.
- \[x] Une chaîne de requête HTTP POST de ? action=createuser peut être acheminé vers un groupe cible pour un service ECS.

#### Q35. Que fait un VPC ?

- \[x] crée un réseau basé sur le cloud pour interconnecter un ensemble de serveurs et d’appliances virtuels
- \[ ] crée un tunnel sécurisé entre deux réseaux
- \[ ] crée un plan de stockage partagé pour les données d’application à partager entre plusieurs instances.
- \[ ] crée un réseau privé complètement isolé de l’Internet public.

#### Q36. Pouvez-vous perdre l’adresse IP publique associée à votre instance EC2 ?

- \[ ] Oui, vous pouvez le perdre si vous redémarrez l’instance.
- \[x] Oui, vous pouvez le perdre si vous arrêtez et démarrez l’instance.
- \[ ] Non, vous ne perdrez jamais l’adresse IP publique de votre instance.
- \[ ] Oui, vous pouvez le perdre lorsque vous modifiez les propriétés de l’instance et libérez l’adresse IP.

#### Q37. Quel est le meilleur emplacement pour stocker les sauvegardes de base de données sur une instance EC2 configurée en tant que serveur de base de données ?

- \[x] un compartiment S3, synchronisé avec les sauvegardes de base de données via un script qui appelle l’AWS CLI
- \[ ] Volume EBS attaché à l’instance
- \[ ] instance attachée à l’instance
- \[ ] stockage d’instance, avec un script qui réplique les sauvegardes de base de données vers une autre instance dans une zone de disponibilité différente.

#### Q38. Laquelle d’entre elles est une restriction valide sur les propriétés d’un VPC ?

- \[ ] Vous ne pouvez avoir que 10 passerelles Internet par région sur un nouveau compte AWS.
- \[ ] Vous ne pouvez avoir que 10 VPC par région sur un nouveau compte AWS
- \[x] Vous ne pouvez pas créer un bloc CIDR avec un masque de réseau supérieur à /16
- \[ ] Vous ne pouvez avoir que 10 sous-réseaux dans un VPC

#### Q39. Vous avez une instance Linux EC2 qui ne répond pas aux demandes et vous ne pouvez pas vous y connecter via SSH. À l’aide de la console EC2, vous avez émis une commande pour arrêter l’instance, mais depuis 10 minutes, l’instance est à l’état « arrêt ». Quelle est la prochaine étape que vous devriez prendre?

- \[x] Émettez une autre action d’arrêt via la console EC2 et choisissez l’option permettant d’arrêter de force l’instance.
- \[ ] Créez une image AMI de l’instance et choisissez l’option permettant de prendre l’image sans redémarrer l’instance.
- \[ ] Modifiez les propriétés de l’instance et augmentez la taille de l’instance.
- \[ ] Contactez le support AWS. Toute autre action pourrait corrompre le système de fichiers.

#### Q40. Vous disposez de 14 serveurs Web sur site, de 4 serveurs de base de données, de 6 serveurs utilisant un logiciel SIG, de 3 serveurs de fichiers et de 4 serveurs de développement. Quelles considérations devez-vous prendre en compte lors de la migration de ces serveurs vers AWS ?

- \[ ] AWS n’a pas de moyen de séparer la facturation des coûts de calcul, vous devrez donc concevoir un moyen de répartir le budget entre les services.
- \[x] Les nouveaux comptes AWS sont limités à 20 instances EC2 à la demande. Envoyez une demande d’augmentation de vos limites de débit avant de commencer une migration.

#### Q41. Au fur et à mesure que votre application Web se développe et que vos besoins de surveillance des applications deviennent plus complexes, quel service supplémentaire de surveillance des journaux ne devriez-vous PAS envisager ?

- \[ ] Pile ELK : Elasticsearch, Loggly et Kibana
- \[x] PRTG
- \[ ] Nouvelle relique
- \[ ] Datadog

#### Q42. Vous disposez d’une instance EC2 T2 essentielle à votre infrastructure. Comment surveilleriez-vous la métrique la plus importante pour cette instance ?

- \[x] Activez CloudWatch Auto Recovery et mettez des moniteurs sur les vérifications de l’état du système et de l’état de l’instance pour que l’instance vous avertisse lorsque l’une ou l’autre est en alarme.
- \[ ] Utilisez CloudWatch pour placer des moniteurs sur les crédits CPU restants. Si vous manquez de crédit CPU, l’instance sera arrêtée.

#### Q43. Quelle fonctionnalité peut être utilisée pour répondre à une augmentation soudaine du trafic Web?

- \[ ] Groupes EC2 Auto Scaling
- \[ ] AWS Shield Avancé
- \[ ] Réplicas en lecture RDS
- \[x] toutes ces réponses

#### Q44. Si un ensemble de serveurs se trouve dans un sous-réseau privé de votre VPC, comment pouvez-vous connecter ces serveurs à des serveurs sur site ?

- \[ ] Établissez une connexion avec AWS Direct Connect.
- \[ ] Utilisez le VPN client AWS.
- \[ ] Installez un serveur OpenVPN sur une instance située dans le sous-réseau avec une adresse IP élastique.
- \[x] Toutes ces options peuvent établir une connexion à un sous-réseau privé.

#### Q45. Vous disposez d’un équilibreur de charge UDP créé par une instance qui exécute un proxy NGINX. Votre solution de gestion des performances des applications (APM) peut détecter les défaillances dans votre instance d’équilibrage de charge et transférer l’adresse IP Elastic vers une instance de secours passive. À l’aide de l’AWS CLI, quel script programmez-vous dans votre APM pour déplacer l’adresse IP Elastic ?

- \[x] A

<!---->

    aws ec2 disassociate-address --association-id eipassoc-2bebb712
    aws ec2 associate-address --instance-id i-8b953 --allocation-id eipalloc-02d021a

- \[ ] B

<!---->

    aws ec2 release-address --association-id eipassoc-2bebb712
    aws ec2 assign-address --instance-id i-8b953 --allocation-id eipalloc-02d021a

- \[ ] C

<!---->

    aws ec2 stop-instances --instance-ids i-8b953
    wait 30
    aws ec2 disassociate-address --association-id eipassoc-2bebb712
    aws ec2 associate-address --instance-id i-8b953 --allocation-id eipalloc-02d021a
    aws ec2 start-instances --instance-ids i-8b953

- \[ ] D

<!---->

    aws ec2 release-address --association-id eipassoc-2bebb712
    aws ec2 associate-address --instance-id i-8b953 --allocation-id eipalloc-02d021a

#### Q46. Quel service peut héberger vos conteneurs Docker ?

- \[ ] Voile de lumière
- \[ ] Elastic Container Service (ECS)
- \[ ] Elastic Compute Cloud (EC2)
- \[x] Tous ces services peuvent héberger un conteneur Docker.

#### Q47. Dans la console S3, sous la colonne Accès, qu’indique le badge public à côté du nom du compartiment ?

![image](images/002.png?raw=png)

- \[x] Tous les objets de ce compartiment se voient attribuer un accès public et peuvent être lisibles ou accessibles en écriture par n’importe qui sur Internet. Assurez-vous qu’aucune donnée sensible n’est partagée publiquement dans ce compartiment.
- \[ ] Tous les objets de ce compartiment sont accessibles en écriture, ce qui signifie que l’Internet public a la possibilité de télécharger n’importe quel fichier directement dans votre compartiment S3. Votre compartiment S3 pourrait être utilisé pour servir des logiciels malveillants.
- \[ ] Certains objets de ce compartiment se voient attribuer un accès public. Vérifiez que les objets partagés publiquement dans ce compartiment ne contiennent aucune donnée sensible.
- \[ ] Les objets de ce compartiment peuvent être rendus publics si la liste de contrôle d’accès de cet objet est définie pour permettre à tout le monde d’y accéder. Les compartiments privés ne vous permettent pas de définir des autorisations publiques sur un objet.

#### Q48. Quel privilège est spécifique au compte racine AWS et ne peut pas être accordé à un autre utilisateur IAM sur le compte ?

- \[ ] Révoquez le rôle AdministratorAccess ou accordez-le à un autre utilisateur IAM.
- \[ ] Créez une nouvelle zone hébergée dans Route 53.
- \[x] Supprimez le compte AWS.
- \[ ] Modifiez les détails de facturation.

#### Q49. Votre candidature envoie chaque jour 50 000 e-mails via SES. Puisque vous devez maintenir un faible taux de rebond pour éviter d’être mis en probation, quel système simple concevez-vous pour traiter automatiquement les rebonds durs?

- \[x] Configurez SES pour envoyer tous les événements de rebond à une rubrique SNS. Créez une fonction Lambda qui traite chaque événement de rebond dur et signale automatiquement ce compte comme un rebond dans votre application pour empêcher d’autres tentatives d’envoi.
- \[ ] Configurez SES pour qu’il n’envoie plus aux adresses e-mail figurant sur votre liste de rebond.
- \[ ] Configurez SES pour envoyer les journaux de toutes les tentatives de livraison via Kinesis Firehose. Traitez chaque événement et recherchez les types de rebond et supprimez ces e-mails de votre liste.
- \[ ] Envoyez tous les e-mails via SES avec un en-tête de réponse personnalisé. Configurez SES pour écouter les événements sur cette adresse e-mail et marquer toute adresse e-mail qui répond à ce compte en tant que message renvoyé et la supprimer de votre liste de diffusion.

#### Q50. Votre application Web reçoit une quantité suspecte de mauvaises requêtes provenant d’adresses IP étrangères. Votre entreprise n’opère que dans quelques pays et vous souhaitez bloquer tout autre trafic. Quelle est la meilleure pratique pour limiter l’accès à votre application Web par pays ?

- \[x] Utilisez web Application Firewall et créez une condition de correspondance géographique pour supprimer toutes les demandes provenant de pays qui ne figurent pas sur votre liste d’autorisation.
- \[ ] Utilisez Application Load Balancer pour créer une nouvelle règle de routage qui examine l’adresse IP source. Ajoutez un bloc IP pour les pays qui y ont accès.
- \[ ] Hébergez le frontal de votre site Web dans CloudFront et configurez une restriction géographique sur la distribution.
- \[ ] Utilisez CloudTrail pour surveiller les adresses IP des requêtes incorrectes. Utilisez Lambda pour ajouter ces adresses IP à une règle Application Load Balancer qui bloque les adresses IP.

#### Q51. Quelle est la meilleure pratique pour la maintenance des instances Windows EC2 et l’application des mises à jour ?

- \[ ] Activez la mise à jour automatique dans Windows Update sur chaque EC2 lancé, ou créez votre propre AMI avec cette fonctionnalité activée et lancez toutes vos instances EC2 à partir de cette AMI.
- \[ ] Créez un calendrier de maintenance qu’un employé doit remplir chaque semaine pour confirmer qu’une inspection visuelle de chaque instance a été effectuée et que les correctifs ont été appliqués.
- \[x] Utilisez AWS Systems Manager Patch Manager pour rechercher des instances de correctif qui nécessitent des mises à jour au cours d’une fenêtre de maintenance définie.
- \[ ] Installez Windows Server Update Services sur votre contrôleur Active Directory principal.

#### Q52. En plus de CloudFormation, vous pouvez utiliser d’autres outils d’orchestration pour automatiser la formation et la maintenance des serveurs. Quel outil est _non_ un choix efficace pour l’orchestration d’une grande infrastructure ?

- \[ ] Chef cuisinier
- \[ ] Ansible
- \[ ] Marionnette
- \[x] Vagabond

#### Q53. Qu’advient-il d’une instance SQL Server RDS si la taille des bases de données augmente et dépasse l’espace alloué ?

- \[ ] RDS augmentera automatiquement l’espace alloué de 10 % et enverra au compte racine AWS un e-mail avec les étapes de résolution. Allouez plus d’espace pour éviter les frais d’utilisation excédentaire.
- \[x] L’instance de base de données signale un état STORAGE_FULL et devient inaccessible si l’instance ne dispose pas de suffisamment de stockage pour fonctionner. Allouez plus d’espace à l’instance.
- \[ ] SQL Server fermera toutes les connexions existantes aux bases de données et tentera de réduire ses fichiers journaux pour récupérer de l’espace de stockage.
- \[ ] RDS augmentera automatiquement l’espace alloué de 5% et continuera à allouer un nouvel espace jusqu’à 50% de l’espace alloué initial. Lorsque l’espace de stockage a augmenté de 50 %, RDS arrête automatiquement l’instance pour préserver l’intégrité des données.

#### Q54. Vous disposez d’un parc d’appareils IoT qui envoient des données de télémétrie à une application côté serveur fournie par votre fournisseur IoT pour décoder un format de messagerie propriétaire. Les périphériques sont configurés pour envoyer des rapports de télémétrie à votre serveur via UDP sur le port 6339. Quelle est la meilleure façon de faire évoluer ce serveur à mesure que davantage d’appareils Iot sont ajoutés à votre flotte ?

- \[ ] Utilisez un équilibreur de charge réseau pour répartir le trafic sur vos serveurs. Utilisez les vérifications de l’état UDP pour déterminer si le serveur est disponible pour recevoir le trafic.
- \[x] Utilisez Route 53 avec des vérifications de l’état HTTP. Créez une application sur le serveur pour signaler l’état de préparation du logiciel serveur fourni par le fournisseur à Route 53 via HTTP.
- \[ ] Utilisez Route 53 avec des vérifications de l’état UDP. Au fur et à mesure que vous montez en puissance, Route 53 achemine le trafic vers les nouveaux serveurs s’ils réussissent les vérifications d’intégrité.
- \[ ] Utilisez Application Load Balancer pour répartir le trafic sur vos serveurs.

#### Q55. les règles sortantes d’un groupe de sécurité autorisent uniquement le trafic allant à 0.0.0.0/0 sur le port TCP 22 (SSH) et le port TCP 3306 (MySQL). Passez en revue les règles entrantes répertoriées dans l’image ci-dessous. Quel est le problème le plus important à résoudre avec cette configuration de groupe de sécurité, pour une instance Ubuntu EC2 agissant comme un serveur Web?

![image](https://user-images.githubusercontent.com/8637045/112515574-c077e780-8d6c-11eb-96a6-11f27a0547cf.png?raw=png)

- \[ ] Les règles sortantes bloquent le port UDP 53, de sorte que le serveur ne sera pas en mesure de résoudre les recherches DNS.
- \[x] Les règles sortantes n’autorisent pas le trafic HTTP à quitter l’instance, de sorte que les requêtes HTTP entrantes échoueront car les clients n’obtiendront jamais de réponses HTTP.
- \[ ] Le port SSH entrant ne doit pas être ouvert au public. Limitez SSH à une seule adresse IP ou plage d’adresses IP contrôlées, ou utilisez un VPN pour accéder au VPC de ce serveur.
- \[ ] Tous les ports TCP entrants sont exposés, ce qui remplace les règles HTTP et SSH et expose tous les ports TCP à l’Internet public.

#### Q56. Une instance EC2 exécutant un site WordPress continue d’être piratée, même si vous avez restauré le serveur plusieurs fois et que vous avez corrigé WordPress. Quel service AWS peut vous aider à détecter et à prévenir d’autres attaques ?

- \[ ] CloudWatch
- \[x] GuardDuty
- \[ ] Bouclier
- \[ ] Conseiller en sécurité

#### Q57. Un client non technique souhaite migrer un site WordPress vers AWS à partir d’un serveur privé géré par une société d’hébergement tierce. Vers quel service AWS devriez-vous recommander de migrer le site ?

- \[ ] CloudFront
- \[ ] Une instance EC2 lancée à partir de l’AMI WordPress officielle
- \[ ] S3
- \[x] Voile de lumière

#### Q58. Votre entreprise dispose de serveurs sur site avec une solution de sauvegarde sur site existante qui réplique également les sauvegardes sur un autre campus à l’autre bout du pays avec sa propre solution de sauvegarde sur site. Il vous a été demandé de créer un troisième niveau de redondance en stockant également ces sauvegardes dans le cloud. En cas d’échec de sauvegarde primaire et secondaire, votre patron veut savoir que les sauvegardes cloud peuvent être accessibles le plus rapidement possible pour réduire les temps d’arrêt pendant la récupération. Quelle classe de stockage S3 recommandez-vous pour le coût et les performances ?

- \[ ] Norme S3
- \[ ] Hiérarchisation intelligente S3
- \[ ] Glacier S3
- \[x] Accès peu fréquent S3 One Zone

#### Q59. Quel magasin de Big Data vous permettra de stocker de grands flux de données d’activité utilisateur provenant à la fois d’applications Web et mobiles ?

- \[ ] Neptune
- \[ ] Aurores boréales
- \[ ] RDS pour SQL Server
- \[x] Décalage vers le rouge

#### Q60. Quelle est la meilleure option pour Auto Scaling de vos instances EC2 pour des modèles de trafic prévisibles ?

- \[x] échelle basée sur un calendrier
- \[ ] mise à l’échelle manuelle
- \[ ] échelle basée sur la demande
- \[ ] maintenir les niveaux actuels en tout temps

#### Q61. Vous migrez un cluster RabbitMQ sur site vers AWS. Quel chemin de migration devez-vous choisir pour faciliter la maintenance et le déploiement ?

- \[ ] Réécrivez les parties de votre application qui utilisent RabbitMQ pour utiliser SQS.
- \[ ] Lancez un cluster RabbitMQ avec des instances EC2 à l’aide d’une AMI prise en charge.
- \[ ] Réécrivez les parties de votre application qui utilisent RabbitMQ pour utiliser Kinesis.
- \[x] Réécrivez les parties de votre application qui utilisent RabbitMQ pour utiliser Amazon MQ.

#### Q62. Lors de la création d’une nouvelle instance RDS, que fait l’option Multi-AZ ?

- \[ ] réplique les sauvegardes de votre base de données vers S3 et les rend disponibles dans toutes les régions pour éviter toute perte de données
- \[x] crée une deuxième instance de base de données passive dans la même région qui deviendra la base de données principale lors d’un basculement
- \[ ] crée un cluster de bases de données hautement disponible qui hébergera votre cluster de bases de données dans au moins deux régions
- \[ ] crée une autre instance de base de données dans une autre région et maintient une veille à chaud active pour basculer en cas de défaillance régionale

#### Q63. Quelle est la meilleure classe d’instance EC2 pour un serveur qui a continuellement une charge CPU importante ?

- \[x] C5
- \[ ] T2
- \[ ] R5
- \[ ] H1

#### Q64. Votre système de gestion des performances des applications (APM) peut lire l’état de vos moniteurs CloudWatch et effectuer des actions scriptées. Lorsque la métrique CloudWatch StatusCheckFailed entre dans un état d’échec (valeur de 1), vous souhaitez que votre APM répare automatiquement l’instance. Quel script utilisez-vous ?

- \[x] A

<!---->

    aws ec2 stop-instances --instance-ids i-0b263919b6498b123
    aws ec2 start-instances --instance-ids i-0b263919b6498b123

- \[ ] B

<!---->

    aws ec2 reboot-instances --instance-ids i-0b263919b6498b123

- \[ ] C

<!---->

    aws ec2 reboot-instances --instance-ids i-0b263919b6498b123
    wait 30
    aws ec2 start-instance --instance-ids i-0b263919b6498b123

- \[ ] D

<!---->

    aws ec2 reboot-instances --instance-ids i-0b263919b6498b123
    aws ec2 start-instances --instance-ids i-0b263919b6498b123

#### Q65. Qu’est-ce qui ne va pas avec la troisième règle de groupe de sécurité entrante, qui permet à tout le trafic de sg-269afc5e d’aller vers une instance Ubuntu EC2 configurée comme serveur Web?

![065](https://user-images.githubusercontent.com/33999631/179728393-8a2636ea-04e7-4597-b0cc-8150e2bc91de.png?raw=png)

- \[ ] Tout le trafic sur tous les ports est refusé dans cette instance, ce qui remplace la règle HTTP et la rend redondante.
- \[x] L’instance a été lancée avec le groupe de sécurité par défaut, mais il n’existe aucun moyen pour un administrateur de SSH dans l’instance.
  Ajoutez une autre règle qui autorise l’accès SSH à partir d’une source sécurisée, telle qu’une seule adresse IP ou une plage d’adresses IP gérées.
- \[ ] Il n’y a rien de mal à cette règle de groupe de sécurité. En supposant que sg-269afc5e est appliqué à d’autres ressources qui sont correctement
  sécurisé, cette règle permet à tout le trafic de passer qui est également affecté au groupe de sécurité sg-269afc5e.
- \[ ] Tout le trafic sur tous les ports est autorisé dans cette instance. Cela expose l’instance à tout le trafic Internet public et
  remplace la règle HTTP entrante.

#### Q66. Vous avez un VPC qui possède un sous-réseau public et privé. Il existe une passerelle NAT dans le sous-réseau public qui permet aux instances du sous-réseau privé d’accéder à Internet sans avoir d’exposition publique en dehors du VPC. Quelles doivent être les tables de routage pour le sous-réseau privé ?

![image](images/003.png?raw=png)

- \[x] A

<!---->

    Destination 1: 10.0.0.0/16, Target 1: local;
    Destination 2: 0.0.0.0/0, Target 2: nat-09b4832

- \[ ] B

<!---->

    Destination 1: 10.0.0.0/24, Target 1: local;
    Destination 2: 0.0.0.0/0, Target 2: igw-b2ff47d6

- \[ ] C

<!---->

    Destination 1: 10.0.0.0/24, Target 1: subnet-1948ba2;
    Destination 2: 0.0.0.0/0, Target 2: nat-09b4832

- \[ ] D

<!---->

    Destination 1: 10.0.0.0/16, Target 1: vpc-12bd09ac2;
    Destination 2: 0.0.0.0/0, Target 2: igw-b2ff47d6

#### Q67. Pour se conformer aux exigences d’audit de certaines normes de conformité, quel outil AWS peut être activé pour gérer un journal d’audit des accès et des modifications apportées à votre infrastructure AWS ?

- \[x] CloudTrail
- \[ ] CloudWatch
- \[ ] Outil d’audit et de conformité AWS
- \[ ] GardeDuty

#### Q68. Vous disposez d’une application qui génère des rapports de longue durée, les stocke dans un compartiment S3, puis envoie un e-mail à l’utilisateur qui a demandé le rapport avec un lien pour le télécharger. Quelle est la meilleure pratique pour stocker les données de rapport dans S3 ?

- \[ ] Créez un compartiment S3 public. Lorsque votre application crée l’objet de rapport dans S3, générez deux longs générés aléatoirement
  noms de dossier et placez le fichier dans le sous-dossier le plus profond. Définissez la stratégie de rétention sur l’objet sur une heure et envoyez ce lien par e-mail à
  l’utilisateur. Le lien sera actif pendant une heure.
- \[ ] Créez un compartiment S3 public. Utilisez un hachage de l’adresse e-mail de l’utilisateur ainsi que la date et l’heure auxquelles le rapport a été demandé pour générer un
  nom d’objet unique. Envoyez ce lien par e-mail à l’utilisateur et exécutez une tâche planifiée dans votre application pour supprimer les objets plus anciens
  que sept jours.
- \[x] Créez un compartiment S3 privé. Le lien dans l’e-mail doit amener l’utilisateur à votre application, où vous pouvez vérifier l’utilisateur actif
  ou forcer l’utilisateur à se connecter. Après avoir vérifié que l’utilisateur dispose des droits d’accès à ce fichier, demandez à l’application de récupérer l’objet
  à partir de S3 et renvoyez-le dans la réponse HTTP. Supprimez le fichier du compartiment S3 une fois la demande terminée.
- \[ ] Créez un compartiment S3 privé. Le lien dans l’e-mail doit amener l’utilisateur à votre application, où vous pouvez vérifier l’utilisateur actif
  ou forcer l’utilisateur à se connecter. Définissez l’objet de rapport dans S3 sur public. Afficher à l’utilisateur un bouton « Télécharger » dans le navigateur qui relie
  à l’objet public.

#### Q69. Lors de l’envoi d’un grand volume d’e-mails via SES, quel est l’ensemble de mesures le plus important à surveiller ?

- \[x] vos taux de plainte et de rebond
- \[ ] s’ouvre et clique
- \[ ] clics et livraisons
- \[ ] volume d’envoi au cours des 15 dernières minutes et sur une journée pour surveiller les pics de facturation

#### Q70. Vous allez héberger une application qui utilise une base de données MySQL. Quelle base de données devez-vous sélectionner si vous ne souhaitez pas gérer les tâches de mise à l’échelle ou d’administration de base de données ?

- \[ ] Lancez une image AMI à partir du marché contenant un serveur MySQL préconfiguré.
- \[x] Aurore
- \[ ] RDS pour MySQL
- \[ ] Décalage vers le rouge

#### Q71. Un formulaire dans une application Web envoie des données d’inscription à « http://example.com/signup/new?source=web » et ces données doivent être gérées par un service ECS derrière Application Load Balancer (ALB). Quelle règle ALB acheminera cette demande ?

![image](images/004.png?raw=png)

- \[ ] A

<!---->

    IF (all match)
        Path is /signup*
        Query string is signup:new
    Then
        Forward to ecs-cluse-service <there is a typo - yes!

- \[ ] B

<!---->

    IF (all match)
        Path is /sign/new/&
        Query request method is POST
    Then
        Forward to ecs-cluse-service

- \[ ] C ... Un de plus avec POST
- \[x] D ... Un seul avec Get

#### Q72. Quel service AWS peut héberger le serveur d’applications Web pour un site WordPress ?

- \[ ] S3
- \[x] Elastic BeanStalk
- \[ ] ElasticCache
- \[ ] CloudFront

#### Q73. Que fait l’AWS CLI suivante `create-service` commande pour ECS faire?

    aws ecs create-service \
     --cluster production \
     --service-name rest-api \
     --task-definition rest-api:1 \
     --desired-count 2 \
     --launch-type "FARGATE" \
     --network-configuration \
     "awsvpcConfiguration={subnets=[subnet-0b29129ab],securityGroups=[sg-0b29129ab]}"

- \[ ] modifie les groupes de sécurité de l’exécution **rest-api** tâche
- \[ ] crée un cluster appelé **production** et lance deux conteneurs dans Fargate avec le **rest-api** définition de la tâche
- \[x] lance deux conteneurs sur Fargate dans l’existant **production** à l’aide de l' **rest-api** définition de la tâche
- \[ ] crée une définition de service pour le **rest-api** tâche; placer deux conteneurs sur le cluster de production lors du lancement **ecs-cli** commande up

#### Q74. Vous souhaitez rendre votre API publique rapidement accessible depuis toutes les régions. Quelle est la meilleure façon de le faire?

- \[ ] Créez un point de terminaison API Gateway unique dans une région centrale.
- \[ ] Créez un point de terminaison de passerelle API privée pour chaque région.
- \[ ] Créez un point de terminaison de passerelle API régional pour chaque région.
- \[x] Créez des points de terminaison de passerelle API optimisés pour la périphérie et déployez-les sur un réseau CloudFront.

#### Q75. Quel type de solution de données devriez-vous utiliser pour les données provenant de données non relationnelles et relationnelles provenant d’appareils IoT, de sites Web, d’applications mobiles, etc. ?

- \[ ] Amazon DynamoDB
- \[x] Formation du lac AWS
- \[ ] Amazon Redshift
- \[ ] Amazon Aurora

#### Q76. Vous disposez d’une suite d’analyses qui produit des rapports sur les modèles d’utilisation de votre application Web. Après avoir terminé votre migration vers AWS et utilisé Application Load Balancer pour équilibrer la charge sur votre application Web, votre service marketing a remarqué que les rapports basés sur l’emplacement sur le trafic Web n’affichent que le trafic provenant d’un seul emplacement. Quel est le problème?

- \[ ] Utilisez un équilibreur de charge classique, pas un équilibreur de charge d’application.
- \[x] Application Load Balancer ne conserve pas l’adresse IP source d’origine. Le logiciel d’analyse doit être configuré pour examiner l’en-tête de requête HTTP 'X-Forwarded-For' pour l’adresse IP source correcte.
- \[ ] Application Load Balencer doit être configuré pour conserver l’adresse IP source du trafic qu’il transfère. Créez une stratégie qui active la prise en charge de ProxyProtocol et attachez-la à l’ALB à l’aide de l’AWS CLI.
- \[ ] Configurez les instances EC2 du serveur Web pour qu’elles n’aient que des adresses IP privées. Les adresses IP publiques des instances sont enregistrées dans les journaux du serveur Web, seul alb doit avoir une interface publique et il acheminera le trafic vers les instances via l’interface privée.

#### Q77. Quoi `not` un utilisateur par défaut d’une instance Linux commune lancée à partir d’une AMI ?

- \[ ] ubuntu
- \[x] utilisateur système
- \[ ] ec2-utilisateur
- \[ ] administrateur

[Référence](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connection-prereqs.html)

#### Q78. Vous avez répliqué l’infrastructure qui sert l’API backend pour votre application Web dans toutes les régions afin de mieux servir vos clients aux États-Unis et dans l’UE. Quelle est la meilleure façon de diriger votre application Web vers le centre de données le plus proche ?

- \[x] Utilisez la route 53 avec des recherches de géolocalisation pour diriger le trafic entre les deux régions.
- \[ ] Créez une règle de redirection WAF qui redirige le trafic vers le centre de données de l’UE si l’adresse IP source provient de certains pays.
- \[ ] Achetez une extension de domaine de pays et dirigez vos utilisateurs vers le bon site, tel que example.com et example.co
- \[ ] Demandez à votre application frontale de tester la latence entre chaque centre de données et d’utiliser le centre de données qui répond le plus rapidement.

[Référence](https://aws.amazon.com/premiumsupport/knowledge-center/geolocation-routing-policy/)

#### Q79. Vous avez récemment lancé votre nouveau produit Web et attendez 1 000 nouveaux utilisateurs chaque mois. Cependant, vous venez de recevoir la nouvelle du PDG que votre produit sera présenté lors d’une prochaine conférence couverte par plusieurs médias, ce qui pourrait conduire à 20 000 nouveaux utilisateurs au cours de la semaine prochaine. Comment prévoyez-vous une augmentation soudaine du trafic?

- \[ ] Répliquez votre infrastructure dans deux régions. Vous renforcerez l’application à une défaillance régionale et vous doublerez votre capacité.
- \[ ] Prenez une image AMI d’un serveur frontal pour enregistrer votre configuration, puis ajoutez d’autres serveurs à votre cluster pror à la conférence. Supprimez les serveurs du cluster après le pic de la conférence.
- \[ ] Testez pour déterminer votre débit et le nombre d’utilisateurs que vous pouvez prendre en charge. Développez un plan de mise à l’échelle pour votre front-end, vos microservices et votre base de données basé sur des métriques CloudWatch qui s’alignent sur les goulots d’étranglement testés.
- \[x] Utilisez les groupes Auto Scaling pour créer davantage de serveurs frontaux lorsque les métriques CloudWatch pour l’utilisation du processeur sur une seule instance dépassent 80 % pendant cinq minutes.

[Référence](https://aws.amazon.com/ec2/autoscaling/)

#### Q80. Comment se connecter via SSH à une instance Ec2 Linux avec un volume EBS si vous avez perdu votre paire de clés ?

- \[ ] Arrêtez l’instance et créez une image AMI. Lancez l’image à l’aide d’une nouvelle paire de clés.
- \[ ] Contactez le support AWS. Un spécialiste du support peut restaurer à distance l’accès à votre instance et vous envoyer une nouvelle paire de clés.
- \[ ] Vous ne pouvez pas vous connecter à cette instance EC2. La paire de clés n’est affichée qu’une seule fois. Si vous le perdez, vous avez perdu tout accès à cette instance. Connectez le volume EBS à une autre instance pour récupérer vos fichiers.
- \[x] Attachez le volume EBS à une instance temporaire lancée avec une nouvelle paire de clés et remplacez ~/.ssh/authorized_keys à l’aide du même fichier de la nouvelle instance.

[Référence](https://medium.com/the-10x-dev/how-to-recover-access-login-to-your-aws-instance-after-losing-your-pem-keypair-file-e0d31bae2da4)

#### Q81. Votre centre de données sur site (172.16.128.0/24) est déjà connecté à votre AWS VPC (10.0.0.0/16) par une passerelle client. Vous souhaitez connecter un autre centre de données pour une entreprise que vous venez d’acquérir (172.16.130.0/24) à votre VPC comme indiqué dans l’image. Quelle est la meilleure façon de créer ce lien ?

![image](images/Q80.png?raw=png)

- \[ ] Établissez une connexion entre vos deux centres de données et connectez le deuxième centre de données au premier via un tunnel privé. Le trafic s’écoulera du deuxième centre de données, puis des premières données, puis d’AWS.
- \[ ] Créez une deuxième passerelle client et configurez votre client VPN dans votre deuxième centre de données pour qu’il se connecte à la passerelle réseau privé virtuel.
- \[x] Créez une deuxième passerelle réseau privé virtuel (VPG) et attachez-la au VPC. Créez une passerelle client pour la nouvelle passerelle réseau privé virtuel et utilisez votre client VPN dans votre deuxième centre de données pour établir une connexion au VPG.
- \[ ] Vous ne pouvez pas avoir plus d’une passerelle client par VPC, de sorte que la solution proposée ne fonctionnera pas. Créez un deuxième VPC avec une passerelle réseau privé virtuel et une passerelle client. Établissez un pont entre les deux VPC à l’aide de l’appairage de VPC.

#### Q82. Vous migrez une base de données de 200 Go d’un serveur SQL Server sur site vers RDS pour SQL Server. La base de données doit avoir un temps d’arrêt minimal pendant la migration. Quelle est la meilleure pratique pour migrer cette base de données ?

- \[ ] Fermez toutes les connexions existantes à la base de données SQL Server et utilisez le service de migration de base de données pour transférer les données vers RDS.
- \[x] Utilisez le service de migration de base de données pour répliquer la base de données vers RDS et la maintenir synchronisée pendant la migration. Redirigez vos applications pour utiliser le nouveau point de terminaison RDS.
- \[ ] Détachez la base de données SQL Server pendant la migration. Effectuez une sauvegarde de la base de données et utilisez SQ avec transfert accéléré pour télécharger les sauvegardes vers S3. Restaurez les sauvegardes sur l’instance RDS.
- \[ ] Utilisez l’Assistant Importation et exportation dans SQL Server Enterprise Manager pour créer une tâche d’exportation et exporter les tables vers l’instance RDS.

[Référence](https://aws.amazon.com/dms/)

#### Q83. Vous avez activé l’authentification multifacteur (MFA) pour votre compte racine AWS et vous avez perdu votre appareil MFA. Que devez-vous faire pour récupérer l’accès à votre compte?

- \[ ] Vous ne pouvez pas récupérer l’accès à votre compte racine AWS. Contactez le support AWS.
- \[x] Un e-mail sera envoyé à l’adresse e-mail enregistrée pour vérifier la propriété du compte. Vous devrez ensuite fournir le numéro de téléphone sur le compte.
- \[ ] Un e-mail sera envoyé à l’adresse e-mail enregistrée. Après avoir cliqué sur le lien dans votre e-mail, fournissez l’un des codes de récupération MFA qui ont été créés lorsque MFA a été activé.
- \[ ] Utilisez l’AWS CLI avec le jeton d’accès au compte racine pour désactiver l’authentification multifacteur sur le compte racine. Utilisez ensuite l’interface de ligne de commande pour définir un nouveau mot de passe sur le compte racine.

[Référence](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_lost-or-broken.html)

#### Q84. Comment attribuer une adresse IP Elastic à plusieurs instances EC2 ?

- \[ ] Dans le tableau de bord VPC, cliquez sur Elastic IPs. Sélectionnez l’adresse IP Elastic et cliquez sur Associer l’adresse. Sélectionnez chaque instance EC2 à laquelle vous souhaitez attribuer cette adresse.
- \[ ] Dans le tableau de bord EC2, cliquez sur Instance EC2. Sous Actions, sélectionnez Mise en réseau > Gérer les adresses IP. cliquez pour ajouter une nouvelle adresse IP et tapez l’adresse de l’adresse IP Elastic. Répétez le processus pour chaque instance EC2 à laquelle vous souhaitez affecter cette adresse IP Elastic.
- \[ ] Utilisez l’AWS CLI et transmettez plusieurs options '--instance-id' à la commande aws ec2 assosiate-address.
- \[x] Une adresse IP élastique ne peut pas être affectée à plusieurs instances EC2. Il ne peut être affecté qu’à une seule instance EC2.

[Référence](https://stackoverflow.com/questions/54742522/assign-multiple-ec2-instances-to-one-elastic-ip)

#### Q85. Vous avez créé un VPC doté d’un sous-réseau public et d’un sous-réseau privé. Un serveur Web a été placé dans le sous-réseau public et un serveur de base de données a été placé dans le sous-réseau privé. Le serveur Web est capable de se connecter au serveur de base de données; toutefois, le serveur de base de données à 10.0.1.2 ne peut pas obtenir les mises à jour logicielles. Quelle est la cause de ce problème?

- \[x] Il n’y a pas de passerelle NAT pour le sous-réseau privé, de sorte que le serveur de base de données n’a pas de routes qui lui donnent un accès Internet public pour télécharger les mises à jour logicielles.
- \[ ] Une adresse publique du pool doit être attribuée au serveur de base de données ou une adresse IP Elastic similaire à l’instance 10.0.0.2.
- \[ ] Le routeur n’est pas configuré correctement sur le VPC. Ajoutez une table d’itinéraire pour le VPC qui achemine tout le trafic pour 0.0.0.0/0 vers l’ID de la passerelle Internet.
- \[ ] Il n’y a pas de passerelle Internet de sortie uniquement attachée au sous-réseau privé du VPC.

#### Q86. Avantage d’utiliser S3 Glacier ?

- \[ ] temps d’accès
- \[ ] stocker pour une petite durée
- \[x] coût
- \[ ] entre régions
