#### Q1. Que fera la commande de dépendance mvn:tree?

- [ ] Vérifier les dépendances définies dans le fichier POM.
- [x] Imprimer un rapport des dépendances de votre projet sous forme d'arborescence.
- [ ] Télécharger toutes les dépendances transitives.
- [ ] Élaguer les dépendances inutilisées de votre arborescence de dépendances.

#### Q2. Comment exécuter un test unitaire unique dans Maven?

- [ ] Maven exécute automatiquement un seul test unitaire.
- [x] Utilisez le drapeau -Dtest= et passez le nom du test.
- [ ] Utilisez un plugin qui peut spécifier le test que vous souhaitez exécuter.
- [ ] Il n'est pas possible de le faire.

#### Q3. Comment les profils Maven peuvent-ils être déclenchés?

- [ ] en appelant explicitement les profils à l'aide du drapeau -P
- [ ] en fonction des variables d'environnement
- [x] toutes les réponses ci-dessus
- [ ] via les paramètres Maven

#### Q4. Pourquoi une commande mvn install ne déploiera-t-elle pas d'artefacts dans un dépôt distant?

- [ ] Le nom de l'artefact doit également être spécifié dans la commande.
- [ ] Le nom du dépôt distant doit également être spécifié dans la commande.
- [ ] Le déploiement des artefacts dans un dépôt distant doit être effectué manuellement.
- [x] La phase de déploiement (deploy) du cycle de vie Maven par défaut intervient après la phase d'installation (install).

#### Q5. Supposons que vous souhaitiez inclure un fichier de propriétés dans le JAR généré par votre construction Maven. Dans quel répertoire devez-vous le placer?

- [x] `${basedir}/src/main/resources`
- [ ] `${basedir}/src/main/java/resources`
- [ ] `${basedir}/resources`
- [ ] `${basedir}/src/main/properties`

#### Q6. Quelle structure dans un fichier settings.xml permet de flexibiliser les propriétés en fonction de certaines valeurs pour l'exécution de Maven?

- [ ] Environnement
- [ ] Propriétés
- [ ] Commutateur
- [x] Profils

#### Q7. Que signifie le fait que la portée (scope) d'une dépendance est "runtime"?

- [x] La dépendance n'est pas nécessaire pour compiler le projet, mais elle est nécessaire à l'exécution.
- [ ] La dépendance est nécessaire à la fois à la compilation et à l'exécution, et doit être empaquetée pour la distribution.
- [ ] La dépendance est nécessaire à la fois à la compilation et à l'exécution, mais n'a pas besoin d'être empaquetée pour la distribution.
- [ ] La dépendance est requise pour la compilation.

#### Q8. Si vous souhaitez utiliser un fichier JAR développé localement dans un autre projet et que ce fichier JAR n'a pas été déployé dans le référentiel central Maven ou dans votre propre référentiel local, quel objectif Maven devez-vous exécuter sur le projet du fichier JAR développé localement?

- [ ] package
- [x] install
- [ ] compile
- [ ] test

#### Q9. Quel est le type d'emballage par défaut pour un artefact de construction de projet Maven?

- [ ] WAR
- [x] JAR
- [ ] EAR
- [ ] POM

#### Q10. Que fait la commande suivante?

> mvn archetype:generate \
> -DgroupID=sample-maven-project \
> -DartifactID=com.palmer.bethan.sample \
> -Dversion=1.0.0 \
> -DinteractiveMode=false

- [ ] Elle ne fait rien car aucun archetype n'a été spécifié.
- [ ] Elle génère un nouvel archetype Maven.
- [x] Elle génère un nouveau projet Maven en utilisant l'archétype Maven par défaut.
- [ ] Elle nettoie et installe le projet sample-maven-project.
