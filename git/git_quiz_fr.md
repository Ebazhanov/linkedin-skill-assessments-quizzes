## Git

#### Q1. Comment pouvez-vous vérifier votre version actuelle de Git ?

- [ ] git --v
- [x] git --version
- [ ] git --option
- [ ] git --current

[Référence](https://www.howtogeek.com/759319/how-to-check-and-update-your-git-version/)

#### Q2. Quelle commande vous permet de créer une connexion entre un dépôt local et distant ?

- [ ] git remote add new
- [x] git remote add origin
- [ ] git remote new origin
- [ ] git remote origin

[Référence](https://stackoverflow.com/questions/20291731/how-to-connect-to-a-remote-git-repository)

#### Q3. Décrivez ce que font ces commandes Git dans l'historique des commits :

```bash
git reset --hard HEAD~5
git merge --squash HEAD@{1}
```

- [ ] Elles réinitialisent HEAD au cinquième commit dans le dépôt, puis fusionnent avec la branche principale.
- [x] HEAD de la branche actuelle est réinitialisé en arrière de cinq commits, puis les commits précédents sont écrasés en un seul commit.
- [ ] Elles suppriment les cinq derniers commits.
- [ ] Elles fusionnent les cinq derniers commits dans une nouvelle branche.

**Explication :**

- `git reset --hard HEAD~5` réinitialise la branche actuelle au commit juste avant les 5 derniers (voir `man gitrevisions` pour plus de détails sur cette notation et d'autres alternatives intéressantes comme `HEAD@{2 days ago}`). Comme il s'agit d'une réinitialisation dure, elle écrasera également tous les changements dans l'arborescence de travail. Voir `man git-reset`.
- `git merge --squash HEAD@{1}` HEAD@{1} est là où la branche était juste avant la commande précédente (encore une fois, voir `man gitrevisions`). Cette commande configure l'état de l'index comme il le serait juste après une fusion à partir de ce commit. Toute cette opération pourrait être une manière de prendre 5 commits d'une branche dans laquelle vous avez commencé une nouvelle fonctionnalité et de les écraser en un seul commit, un commit significatif.

[Référence](https://stackoverflow.com/questions/70962338/documentation-of-default-target-of-git-merge-squash)

#### Q4. Votre projet actuel comporte plusieurs branches : master, beta et push-notifications. Vous venez de terminer la fonctionnalité de notification dans la branche push-notifications et vous souhaitez la valider dans la branche beta. Comment pouvez-vous y parvenir ?

- [ ] Basculez sur la branche push-notifications et exécutez git merge beta.
- [ ] Basculez sur la branche master et exécutez git merge beta -> push-notifications.
- [ ] Supprimez la branche push-notifications et elle sera automatiquement validée dans la branche master.
- [x] Basculez sur la branche beta et exécutez git merge push-notifications.

[Référence](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)

#### Q5. Quelle est la signification de la commande suivante ?

`git add -A`

- [x] Tous les fichiers nouveaux et mis à jour sont ajoutés à la zone de transit.
- [ ] Les fichiers sont ajoutés à la zone de transit dans l'ordre alphabétique.
- [ ] Tous les fichiers nouveaux sont ajoutés à la zone de transit.
- [ ] Seuls les fichiers mis à jour sont ajoutés à la zone de transit.

[Référence](https://git-scm.com/docs/git-add)
[Référence](https://www.geeksforgeeks.org/difference-between-git-add-a-and-git-add/)

#### Q6. Que va afficher la commande suivante dans le Terminal ?

`git remote -v`

- [x] Une liste des dépôts distants et de leurs URL.
- [ ] La version actuelle de Git que vous exécutez.
- [ ] Un éditeur en ligne pour modifier les dépôts distants.
- [ ] Les cinq dernières versions de Git que vous avez installées.

[Référence](https://git-scm.com/docs/git-remote)
[Référence](https://www.javatpoint.com/git-remote)

#### Q7. En regardant les commandes suivantes, décrivez ce qui se passe.

```bash
git checkout feature-user-location
git cherry-pick kj2342134sdf090093f0sdgasdf99sdfo992mmmf9921231
```

- [ ] Le commit est marqué pour une publication sur la branche feature-user-location.
- [x] Un commit est copié de sa branche d'origine vers la branche feature-user-location.
- [ ] Le commit est sélectionné comme nouvelle tête de l'historique des commits.
- [ ] Un commit est copié de la branche feature-user-location vers la branche master.
- [ ] La branche est basculée sur la branche feature-user-location, et le commit spécifié est appliqué à la branche.

Explication :

'git checkout feature-user-location' bascule sur la branche 'feature-user-location'.
'git cherry-pick kj2342134sdf090093f0sdgasdf99sdfo992mmmf9921231' applique les modifications du commit spécifié ('kj2342134sdf090093f0sdgasdf99sdfo992mmmf9921231') à la branche actuelle (feature-user-location). Cela revient en fait à copier le commit de sa branche d'origine dans la branche feature-user-location.
Ainsi, cette séquence de commandes permet de cherry-pick un commit spécifique sur la branche feature-user-location.

#### Q8. Que fait la commande suivante dans le référentiel Git ?

`git reset --soft HEAD^`

- [ ] Elle supprime tous les commits précédents et réinitialise l'historique du référentiel à son état initial.
- [ ] Elle réinitialise la branche de travail au premier commit.
- [ ] Elle maintient HEAD au commit actuel mais efface tous les commits précédents.
- [x] Elle positionne HEAD sur le commit précédent et laisse les modifications du commit annulé dans la zone de transit.

[Référence](https://git-scm.com/docs/git-reset)
[Référence](https://stackoverflow.com/questions/24568936/what-is-the-difference-between-git-reset-hard-head1-and-git-reset-soft-head)

#### Q9. Vous trouvez un bogue dans votre projet, mais vous ne pouvez pas localiser où il a été introduit dans l'historique des commits. Comment diagnostiqueriez-vous ce

problème ?

- [ ] Revenez manuellement en arrière dans votre historique des commits.
- [ ] Utilisez git search -diff pour comparer tous les commits de l'historique de votre référentiel.
- [ ] Exécutez un rebasage Git pour trouver le commit problématique.
- [x] Utilisez git bisect pour comparer le commit problématique à un commit antérieur qui fonctionne comme prévu.

[Référence](https://git-scm.com/docs/git-bisect)
[Référence](https://stackoverflow.com/questions/69552866/how-to-diagnose-a-problem-in-git-commit-history)

#### Q10. Pourquoi utiliseriez-vous la commande suivante ?

`git rebase -i HEAD~10`

- [ ] Pour effectuer une recherche comparative des 10 derniers commits pour trouver les différences.
- [x] Pour répertorier les 10 derniers commits et les modifier avec les commandes squash ou fixup.
- [ ] Pour supprimer les 10 derniers commits et réinitialiser HEAD.
- [ ] Pour mettre en cache localement les 10 derniers commits.

[Référence](https://git-scm.com/docs/git-rebase#_interactive_mode)
[Référence](https://stackoverflow.com/questions/363908/how-do-i-use-git-rebase-i-to-rebase-all-changes-in-a-branch)

#### Q11. Pourquoi utiliseriez-vous un crochet pre-receive dans votre référentiel distant ?

- [ ] Vous ne le feriez pas, vous l'utiliseriez dans le référentiel local.
- [x] Pour exécuter un script lorsque un dépôt distant reçoit une poussée qui est déclenchée avant que les références ne soient mises à jour.
- [ ] Pour exécuter un script après les mises à jour effectuées dans le référentiel distant.
- [ ] Pour déboguer toutes les balises de commit et les versions de publication.

[Référence](https://git-scm.com/docs/githooks)
[Référence](https://docs.github.com/en/enterprise-server@3.10/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/working-with-pre-receive-hooks)

#### Q12. Quelle option pouvez-vous utiliser pour appliquer des configurations Git dans tout votre environnement Git ?

- [ ] `--all`
- [ ] `--master`
- [x] `--global`
- [ ] `--update`

[Référence](https://git-scm.com/docs/git-config)
[Référence](https://www.git-scm.com/book/en/v2/Customizing-Git-Git-Configuration)

#### Q13. Comment pourriez-vous fusionner plusieurs commits en un seul sans utiliser git merge --squash ?

- [ ] Mise en cache
- [ ] Vous ne le pouvez pas. git merge --squash est la seule commande Git pour cette opération.
- [x] Rebaser
- [ ] Reflog

[Référence](https://git-scm.com/docs/git-rebase#_interactive_mode)
[Référence](https://stackoverflow.com/questions/31409736/squash-commits-directly-on-feature-without-rebase-or-merge)

#### Q14. Si vous avez cloné un référentiel Git existant, qu'arriverait-il ?

- [ ] Une nouvelle copie écraserait le référentiel central.
- [x] Une copie du référentiel serait créée sur votre machine locale.
- [ ] Rien, le clonage n'est pas une fonction Git prise en charge.
- [ ] Une copie du référentiel serait créée sur la plateforme d'hébergement.

[Référence](https://git-scm.com/docs/git-clone)
[Référence](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

#### Q15. Comment pouvez-vous afficher une liste des fichiers ajoutés ou modifiés dans un commit spécifique ?

- [ ] Trouvez le commit dans le référentiel distant, car c'est le seul endroit où ce type d'information est stocké.
- [x] Utilisez la commande `diff-tree` avec le hachage du commit.
- [ ] Exécutez `git commit --info` avec le hachage du commit.
- [ ] Accédez aux données du stash du commit avec `git stash`.

[Référence](https://git-scm.com/docs/git-diff-tree)
[Référence](https://stackoverflow.com/questions/424071/how-do-i-list-all-the-files-in-a-commit#:~:text=If%20you%20want%20to%20get%20the%20list%20of,you%20can%20use%20git%20ls-tree%20--name-only%20-r%20%3Ccommit-ish%3E)
