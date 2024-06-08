## Git

#### Q1. Як перевірити поточну версію git?

- [ ] git --v
- [x] git --version
- [ ] git --option
- [ ] git --current

[Довідка](https://www.howtogeek.com/759319/how-to-check-and-update-your-git-version/)

#### Q2. Яка команда дозволяє створити зв’язок між локальним і віддаленим репозиторіями?

- [ ] git remote add new
- [x] git remote add origin
- [ ] git remote new origin
- [ ] git remote origin

[Довідка](https://stackoverflow.com/questions/20291731/how-to-connect-to-a-remote-git-repository)

#### Q3. Опишіть, що ці команди Git роблять з історією комітів:

```bash
git reset --hard HEAD~5
git merge --squash HEAD@{1}
```

- [ ] Скидають HEAD до п’ятого коміту в репозиторії, а потім зливаються з головною гілкою.
- [x] HEAD поточної гілки скидається назад на п’ять комітів, потім попередні коміти стискаються в один коміт.
- [ ] Видаляють останні п'ять комітів.
- [ ] Об’єднують останні п’ять комітів у нову гілку.

**Пояснення:**

- `git reset --hard HEAD~5` скидає поточну гілку до 5 коміту безпосередньо перед останніми (перегляньте `man gitrevisions`, щоб дізнатися більше про цю нотацію та інші цікаві альтернативи, такі як `HEAD@{2 days ago}`). Оскільки це апаратне скидання, воно також перезаписує всі зміни в робочому дереві. Перегляньте `man git-reset`.
- `git merge --squash HEAD@{1}` HEAD@{1} – це місце, де була гілка перед попередньою командою (ще раз див. `man gitrevisions`). Ця команда встановлює стан індексу таким, яким він був би після злиття з цим комітом. Ця вся операція може бути засобом щоб взяти 5 комітів з гілки, в якій ви запустили нову функцію, і стиснути їх до одного, значущого коміту.

[Довідка](https://stackoverflow.com/questions/70962338/documentation-of-default-target-of-git-merge-squash)

#### Q4. Ваш поточний проект має кілька гілок: main, beta та push-notifications. Ви щойно завершили роботу над функцією у гілці push-notifications і хочете закріпити зміни для beta. Як ви можете цього досягти?

- [ ] Перемкнутися на гілку push-notifications і запустити git merge beta
- [ ] Перемкнутися на main та запустити git merge beta -> push-notifications
- [ ] Видалити гілку push-notifications, і вона буде автоматично зафіксована в main
- [x] Перемкнутися на beta та запустити git merge push-notifications

[Довідка](https://git-scm.com/book/uk/v2/Галуження-в-git-Основи-галуження-та-зливання)

#### Q5. Що з наведеного нижче вірно, коли ви використовуєте наступну команду?

`git add -A`

- [x] Усі нові та оновлені файли staged
- [ ] Файли розташовані в алфавітному порядку.
- [ ] Усі нові файли staged
- [ ] Лише оновлені файли staged

[Довідка](https://git-scm.com/docs/git-add)
[Довідка](https://www.geeksforgeeks.org/difference-between-git-add-a-and-git-add/)

#### Q6. Що надрукує наступна команда в терміналі?

`git remote -v`

- [x] Список віддалених сховищ та їх URL-адреси
- [ ] Поточна версію git, яку ви використовуєте
- [ ] Вбудований редактор для редагування віддалених сховищ
- [ ] Останні 5 версій git, які ви встановили

[Довідка](https://git-scm.com/docs/git-remote)
[Довідка](https://www.javatpoint.com/git-remote)

#### Q7. Переглядаючи наступні команди, опишіть, що відбувається.

```bash
git checkout feature-user-location
git cherry-pick kj2342134sdf090093f0sdgasdf99sdfo992mmmf9921231
```

- [ ] коміт позначається тегом для випуску в гілці feature-user-location
- [ ] Коміт копіюється з оригінальної гілки до гілки feature-user-location
- [ ] Коміт обирається новим HEAD історії комітів
- [ ] Коміт копіюється з гілки feature-user-location до master
- [x] Гілка перемикається на гілку feature-user-location, і вказаний коміт застосовується до гілки.

Пояснення:

'git checkout feature-user-location' перемикає на гілку 'feature-user-location'.
'git cherry-pick kj2342134sdf090093f0sdgasdf99sdfo992mmmf9921231' застосовує зміни з указаного коміту ('kj2342134sdf090093f0sdgasdf99sdfo992mmmf9921231') до поточної гілки (feature-user-location). Це фактично копіює коміт з його вихідної гілки до гілки feature-user-location.
Таким чином, ця послідовність команд є вибором певного коміту для гілки feature-user-location.

#### Q8. Що робить наступна команда зі сховищем git?

`git reset --soft HEAD^`

- [ ] Видаляє всі попередні коміти та скидає історію сховища до початкового стану.
- [ ] Скидає робочу гілку до першого коміту.
- [ ] Зберігає HEAD у поточному коміті, але очищає всі попередні коміти.
- [x] Встановлює HEAD до попереднього коміту та залишає зміни від скасованого коміту в stage/index.

[Довідка](https://git-scm.com/docs/git-reset)
[Довідка](https://stackoverflow.com/questions/24568936/what-is-the-difference-between-git-reset-hard-head1-and-git-reset-soft-head)

#### Q9. Ви знайшли помилку у своєму проекті, але не можете знайти її в історії комітів. Як би ви діагностували цю проблему?

- [ ] Повернутися вручну за допомогою історії комітів.
- [ ] Скористатися git search -diff, щоб порівняти всі коміти в історії вашого сховища.
- [ ] Запустити git rebase, щоб знайти помилковий коміт.
- [x] Скористатися git bisect для порівняння помилкового коміту з раннім комітом, що працює належним чином.

[Довідка](https://git-scm.com/docs/git-bisect)
[Довідка](https://stackoverflow.com/questions/69552866/how-to-diagnose-a-problem-in-git-commit-history)

#### Q10. Для чого слід використовувати наступну команду?

`git rebase -i HEAD~10`

- [ ] Для запуску порівняльного пошуку останніх 10 комітів на наявність відмінностей
- [x] Для перераховування останніх 10 комітів і зміни їх за допомогою команди squash або fixup
- [ ] Для видалення останніх 10 комітів і скидання HEAD
- [ ] Для локального кешування останніх 10 комітів

[Довідка](https://git-scm.com/docs/git-rebase#_interactive_mode)
[Довідка](https://stackoverflow.com/questions/363908/how-do-i-use-git-rebase-i-to-rebase-all-changes-in-a-branch)

#### Q11. Навіщо використовувати pre-receive хук у віддаленому сховищі?

- [ ] Непотрібно, можна скористатися ним в локальному сховищі
- [x] Для виконання скріпта, коли віддалений пристрій отримує push, який запускається до оновлення будь-яких посилань
- [ ] Для запуску скріпта після оновлення віддаленого репозиторію
- [ ] Для налагодження всіх тегів комітів та версій

[Довідка](https://git-scm.com/docs/githooks)
[Довідка](https://docs.github.com/en/enterprise-server@3.10/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/working-with-pre-receive-hooks)

#### Q12. Якою опцією можна скористатися для застосування конфігурацій git до всього середовища git?

- [ ] `--all`
- [ ] `--master`
- [x] `--global`
- [ ] `--update`

[Довідка](https://git-scm.com/docs/git-config)
[Довідка](https://www.git-scm.com/book/uk/v2/Налаштування-Git-Конфігурація-Git)

#### Q13. Як можна стиснути кілька комітів без використання git merge --squash?

- [ ] Кешування
- [ ] Неможливо. git merge --squash — єдина команда git для цієї операції.
- [x] Перебазування
- [ ] Рефлогінг

[Довідка](https://git-scm.com/docs/git-rebase#_interactive_mode)
[Довідка](https://stackoverflow.com/questions/31409736/squash-commits-directly-on-feature-without-rebase-or-merge)

#### Q14. Коли ви клонуєте існуючий репозиторій git, що трапляється?

- [ ] Нова копія перезапише головний репозиторій
- [x] Копію репозиторію буде створено на вашій локальній машині
- [ ] Нічого, клонування не підтримується функцією git
- [ ] Копія репозиторію буде створена на хостингу

[Довідка](https://git-scm.com/docs/git-clone)
[Довідка](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

#### Q15. Як ви можете відобразити список файлів, доданих або змінених у певному коміті?

- [ ] Знайти коміт у віддаленому сховищі, оскільки це єдине місце, де зберігається така інформація.
- [x] Скористатися командою `diff-tree` з хешем коміту.
- [ ] Запустити `git commit --info` з хешем коміту.
- [ ] Отримати доступ до схованих даних комітів за допомогою `git stash`.

[Довідка](https://git-scm.com/docs/git-diff-tree)
[Довідка](https://stackoverflow.com/questions/424071/how-do-i-list-all-the-files-in-a-commit#:~:text=If%20you%20want%20to%20get%20the%20list%20of,you%20can%20use%20git%20ls-tree%20--name-only%20-r%20%3Ccommit-ish%3E)

#### Q16. Які саме файли в такому .gitignore виключатимуться?

```shell
#.swift
build/

*.txt
*.metadata
```

- [ ] Всі файли з .swift, .txt, або metadata розширеннями, а також вся директорія build
- [ ] Тільки директорія build
- [x] Всі файли в директорії build, також файли з розширеннями .txt або .metadata
- [ ] Тільки файли з розширеннями .swift та .txt.

[Довідка](https://git-scm.com/docs/gitignore)

Рядок, що починається з `#`, є коментарем. Тому `# .swift` нічого не робить. Дивіться `man gitignore`.

#### Q17. Після внесення змін до локального сховища виконайте таку команду. Що це дасть?

`git commit -a -m "Refactor code base"`

- [ ] Нічого, ви не можете використовувати кілька параметрів в одній команді
- [ ] Додає всі нові файли до робочої області
- [] Фіксує всі нові файли з повідомленням
- [x] Додає всі змінені файли до робочої області, а потім фіксує їх із повідомленням

#### Q18. Після перевірки git status ви отримаєте наступне, це показує що файл beta-notes.js присутній у коміті, але він також є unstaged. Як може статися така ситуація?

```shell
Change to be committed:

(use "git reset HEAD <file>..." to unstage)
modified: beta-notes.js
Changes not staged for commit:
(use "git add <file>..." to update what will be committed)
(use "git checkout --<file>..." to discard changes in working directory)

modified: beta-notes.js
```

- [ ] Було дві копії beta-notes.js, але одну було видалено
- [x] beta-notes.js було створено, а потім змінено, створюючи дві різні версії файлу
- [ ] Було створено дві копії beta-notes.js, але лише одна відстежується
- [ ] Є дві відстежувані копії beta-notes.js, але одну було видалено з коміту

[Довідка](https://git-scm.com/book/uk/v2/Основи-Git-Запис-змін-до-репозиторія)

#### Q19. Де зберігаються файли до того, як вони зафіксовані в локальному сховищі?

- [ ] У збережених файлах
- [ ] У документах git
- [x] У Staging зоні
- [] У git кеш

[Довідка](https://www.geeksforgeeks.org/what-is-a-git-repository/)

#### Q20. Які команди ви б використали, щоб примусово перезаписати ваші локальні файли master гілкою?

- [ ] ⠀

```bash
  git pull --all
  git reset --hard origin/master
```

- [ ] ⠀

```bash
  git pull -u origin master
  git reset --hard master
```

- [ ] ⠀

```bash
  git pull origin master
  git reset --hard origin/myCurrentBranch
```

- [x] ⠀

```bash
  git fetch --all
  git reset --hard origin/master
```

**Примітка**: - Команда `pull` — це `fetch`, за якою слідує `merge` або `rebase` (у цьому випадку `merge`). Ми не хочемо мержити. Злиття було б дією для нашого **репозиторію**. Ми просто хочемо перезаписати наші **локальні файли**.

#### Q21. Ви виявили, що ваш проект має тег і гілку з однаковою назвою push-notifications, що викликає плутанину під час спроби роздрукувати дане посилання. Як вказати, яку гілку ви бажаєте переглянути?

- [ ] Скористатися git show refs/push-notifications
- [ ] Скористатися git show push-notifications
- [ ] Скористатися git show heads/refs/push-notifications
- [x] Скористатися git show refs/heads/push-notifications

[Довідка](https://geedew.com/fixing-git-branch-and-tag-name-collision/)

#### Q22. Перед виконанням rebase керівнику вашої команди потрібен перелік усіх комітів, які буде переміщено. За допомогою якої команди можна отримати доступ до цієї інформації?

- [ ] git rebase -log
- [x] git rebase -i
- [ ] git rebase -verbose
- [ ] git rebase -all

#### Q23. Що трапляється з наведеними нижче командами Git?

```
git bisect start
git bisect bad 5d41402abc4b2a76b9719d911017c592
git bisect good 69faab6268350295550de7d587bc323d
```

- [ ] Злиття доброго коміту, який виявляється за допомогою відомого поганого та відомого доброго комітів
- [ ] Позначається коміт для видалення, використовуючи відомий поганий і відомий добрий коміти, щоб визначити, який коміт містить помилку
- [ ] Визначає поганий коміт і скидає HEAD, використовуючи відомий поганий і відомий добрий коміт
- [x] Виконує бінарний пошук, використовуючи відомий поганий і відомий добрий коміти, щоб визначити, який коміт привніс помилку

#### Q24. У ситуації, коли у вас є кілька комітів для одного завдання, який найефективніший спосіб реструктуризувати вашу історію комітів?

- [ ] Перенести за допомогою сherry pick пов’язані коміти до іншої гілки.
- [ ] Видалити передані коміти та повторно передати з новим повідомленням.
- [x] Стиснути пов’язані коміти разом у єдиний узгоджений коміт.
- [ ] Сховати пов’язані коміти під новим хешем.

[Довідка](https://git-scm.com/docs/git-rebase#_interactive_mode)

#### Q25. Що з наведеного нижче вірно для команди git push?

**Примітка.** Яке твердження вірне щодо команди `git push`?

- [x] За замовчуванням push не надсилає теги до віддаленого рипозиторію.
- [ ] Коміти можна позначати тегами лише тоді, коли вони створені.
- [ ] Теги надсилаються до віддаленого сховища разом із відповідними комітами.
- [ ] Лише анотовані теги автоматично надсилаються до віддаленого сховища за допомогою коміту.

[Довідка](https://git-scm.com/book/en/v2/Git-Basics-Tagging#:~:text=Sharing%20Tags)

#### Q26. Яку скорочену команду ви можете використовувати в майбутньому після першого надсилання комітів до віддаленого сховища за допомогою наведеної нижче команди?

```bash
git push -u origin master
```

- [ ] git push master
- [ ] git push origin
- [ ] Як і раніше, git push -u origin master
- [x] git push

[Довідка](https://git-scm.com/docs/git-push)

#### Q27. Як би ви створили спеціальний ярлик або команду в середовищі Git?

- [ ] Запустите `git hotfix` з назвою ярлика.
- [ ] Призначите ярлик або команду за допомогою файлу параметрів git.
- [ ] Використаєте команду `git custom-key`.
- [x] Створите псевдонім за допомогою команди `git config`.

[Довідка](https://git-scm.com/docs/git-config)

#### Q28. Який статус файлу beta-notes.js у наведеному нижче виводі?

```shell
Changes not staged for commit:
(use "git add <file>..." to update what will be committed)
(use "git checkout -- <file>..." to discard changes in working directory)

modified: beta-notes.js
```

- [ ] beta-notes.js не відстежується та був змінений.
- [x] beta-notes.js є відстежуваним файлом, який було змінено, але не додано до поточного коміту.
- [ ] beta-notes.js не відстежується, але його додано до поточного коміту.
- [ ] beta-notes.js відстежується, а змінений файл додано до поточного коміту.

[Довідка](https://git-scm.com/book/uk/v2/Основи-Git-Запис-змін-до-репозиторія)

#### Q29. Яка команда дозволить вам змінити попередній коміт?

- [ ] --fix
- [ ] --quickfix
- [ ] --modify
- [x] --amend

[Довідка](https://git-scm.com/book/uk/v2/Інструменти-Git-Переписування-історії)

#### Q30. Який вираз найкраще характеризує структуру git commit?

- [ ] Масив даних
- [ ] Журнал даних
- [x] Знімок даних
- [ ] Словник даних

[Довідка](https://git-scm.com/book/uk/v2/Галуження-в-git-Гілки-у-кількох-словах)

#### Q31. Які зміни внесе така команда у файли проміжної області?

`git rm --cached testfile.js`

- [x] testfile.js буде видалено з проміжної області, а його зміни більше не відстежуватимуться.
- [ ] testfile.js буде видалено з проміжної області, але його зміни все одно відстежуватимуться.
- [ ] Копія testfile.js буде кешована на вашому робочому столі.
- [ ] Поточна копія testfile.js буде збережена в робочій області.

[Довідка](https://git-scm.com/docs/git-rm)

#### Q32. Після того, як ви успішно об’єднали дві гілки та внесли зміни, що буде наступним кроком у підтримці вашої структури git у порядку?

- [ ] Скористатися git reset --soft HEAD, щоб відкотити один коміт.
- [x] Запустіти git branch -d `<назва гілки>`, щоб видалити об’єднану гілку.
- [ ] Скористатися git clear-all, щоб очистити будь-які завислі файли.
- [ ] Запустіти git rebase, щоб перемістити поточний коміт у вихідне розташування.

[Довідка](https://www.w3docs.com/snippets/git/how-to-delete-already-merged-git-branches.html#:~:text=Make%20sure%20you%20are%20on,branches%20you%20want%20to%20delete.)

#### Q33. Під час редагування файлу вам несподівано призначено термінове виправлення помилки в іншій гілці. Як ви можете тимчасово зберегти вашу локальну роботу без зобов’язань?

- [ ] Це неможливо, оскільки ви не можете зберегти локально без коміту.
- [ ] Запустити git hold, щоб зберегти локальну копію того, що ви робите, та повернутися до нього пізніше.
- [ ] Зберегти свою роботу за допомогою git local-cache.
- [x] Скористатися git stash, щоб зберегти вашу роботу, а потім повернутися пізніше та повторно застосувати прихований коміт.

[Довідка](https://git-scm.com/docs/git-stash)

#### Q34. Яку команду ви б використали для створення нового репозиторію git?

- [ ] git add
- [ ] git start
- [ ] git new
- [x] git init

[Довідка](https://git-scm.com/book/uk/v2/Основи-Git-Створення-Git-репозиторія)

#### Q35. Під час роботи над гілкою функції ви намагаєтеся скористатися «git rerere» для вирішення повторюваного конфлікту злиття, але нічого не відбувається. Що може бути причиною цієї проблеми?

- [ ] Параметр "-all" не додано до команди.
- [x] "rerere.enabled" не ввімкнено у конфігураційному файлі.
- [ ] Хеш коміту відсутній.
- [ ] Шлях до файлу не вказано.

[Довідка](https://git-scm.com/docs/git-rerere)

#### Q36. Яке налаштування визначає, який пейджер використовується під час виведення сторінок Git?

- [ ] core.page
- [ ] page
- [ ] pager
- [x] core.pager

#### Q37. Що містить об’єкт commit?

- [ ] Набір файлів, що представляють стан проекту на певний момент часу.
- [ ] Посилання на батьківські об’єкти коміту.
- [ ] Ім’я SHA1, рядок із 40 символів, який унікально ідентифікує об’єкт коміту.
- [x] Посилання на батьківські об’єкти коміту та набір файлів, що представляють стан проекту на певний момент часу, а також ім’я SHA1, рядок із 40 символів, який унікально ідентифікує об’єкт коміту.

#### Q38. Який параметр дає змогу включати ім’я комітора у спеціальний формат журналу?

- [ ] %ce
- [ ] %cr
- [ ] %cd
- [x] %cn

[Довідка](https://git-scm.com/docs/pretty-formats)

#### Q39. Скільки способів є в Git для інтеграції змін з однієї гілки в іншу?

- [ ] 3
- [ ] 5
- [x] 2
- [ ] 4
  > У Git є два основних способи інтегрувати зміни з однієї гілки в іншу: злиття та перебазування. [Довідка](https://git-scm.com/book/uk/v2/Галуження-в-git-Перебазовування)

#### Q40. Якого користувача слід створити першим під час налаштування SSH?

- [ ] git
- [ ] admin
- [ ] root
- [x] Ніщо з цього

_note_: це питання недостатньо конкретне, щоб дати остаточну відповідь, оскільки воно залежить від конкретного випадку використання та конфігурації налаштування SSH.

#### Q41. Яка команда покаже список тегів серії 1.4.2?

- [ ] git tag 'v1.4.2'
- [x] git tag -l 'v1.4.2.\*'
- [ ] git tag-list 'v1.4.2\*'
- [ ] git tag 'v1.4.2\*'

#### Q42. Що з наведеного нижче є менеджером інтеграції?

- [ ] lieutenants
- [ ] benevolent dictator
- [x] Залежить від типу проекту
- [ ] Залежить від даних

#### Q43. Яка команда Git починає відстеження нового файлу?

- [x] add
- [ ] addfile
- [ ] begin
- [ ] track

[Довідка](https://git-scm.com/book/uk/v2/Основи-Git-Запис-змін-до-репозиторія)

#### Q44. Що з наведеного нижче називається німим протоколом?

- [ ] Все
- [ ] SSH
- [ ] Git
- [x] HTTP

[Довідка](https://git-scm.com/book/uk/v2/Git-зсередини-Протоколи-передачі)

#### Q45. Натискання якої клавіші повертає набір пропозицій для вибору під час написання команди Git?

- [ ] Control
- [ ] Shift
- [x] Tab
- [ ] Alt

#### Q46. Який із цих термінів найкраще описує Git?

- [x] Розподілена система керування версіями
- [ ] Система відстеження проблем
- [ ] Інтегроване середовище розробки
- [ ] Служба розміщення репозиторіїв

[Довідка](https://uk.wikipedia.org/wiki/Git)

#### Q47. Як Git думає про свої дані?

- [ ] Файл
- [ ] Ніщо з цього
- [x] Знімок
- [ ] Папка

[Довідка](https://git-scm.com/book/uk/v2/Галуження-в-git-Гілки-у-кількох-словах)

#### Q48. Яка опція дозволяє включати ім’я автора в спеціальний формат журналу?

- [ ] %am
- [ ] %ad
- [ ] %ae
- [x] %an

#### Q49. Яка з пізніших версій Git пропонувала повернути файл до того вигляду, який був під час останнього коміту?

- [ ] 1.7
- [x] 1.6
- [ ] 2.0
- [ ] 1.8

#### Q50. Яку стратегію використовує Git для об’єднання двох гілок?

- [ ] LIFO
- [ ] recursive
- [ ] FIFO
- [x] octopus

#### Q51. Що зберігає посилання?

- [ ] значення SHA-1
- [ ] Ніщо з цього
- [x] Назва гілки
- [ ] Назва проекту

[Довідка](https://git-scm.com/book/uk/v2/Git-зсередини-Посилання-Git)

#### Q52. Яка мова використовується в GIT?

- [x] C
- [ ] C++
- [ ] C#
- [ ] Java

#### Q53. Яке зазвичай розширення файлу, який має відкритий ключ?

- [ ] ssh
- [x] pub
- [ ] key
- [ ] pk

[Довідка](https://git-scm.com/book/uk/v2/Git-на-сервері-Генерація-вашого-публічного-ключа-SSH)

#### Q54. Яка різниця між ініціалізацією звичайного репо та чистого репо?

- [ ] Чисті репо зберігають свою історію git у підпапці .git.
- [ ] Чисті репозиторії не мають розширення .git.
- [x] Чисті репозиторії не постачаються з робочими або вилученими вихідними файлами.
- [ ] Чисті репозиторії слід використовувати для локальних, а не віддалених репозиторіїв.

#### Q55. Скільки окремих комітів може мати одне сховище?

- [x] будь-яка кількість комітів
- [ ] лише один локальний коміт на репозиторій
- [ ] лише три коміти на гілку
- [ ] лише один коміт на HEAD

#### Q56. Які типи тегів підтримує Git?

- [ ] важкий і стислий
- [ ] легкий і незмінний
- [ ] важкий і коментований
- [x] легкий і анотований

[Довідка](https://git-scm.com/book/uk/v2/Основи-Git-Теґування)

#### Q57. Після внесення серії змін до індексу, якою командою можна скористатися, щоб переглянути їх перед фіксацією?

- [x] git diff --cached
- [ ] git diff
- [ ] git diff --HEAD
- [ ] git status -v -v

#### Q58. Що робить команда git stash drop?

- [x] видаляє останній запис тайника
- [ ] видаляє тайник
- [ ] перераховує все, що є в тайнику
- [ ] викидає найстаріший запис

[Довідка](https://git-scm.com/docs/git-stash)

#### Q59. Яка команда створює нову гілку з поточної гілки?

- [ ] `git -b checkout <nameOfBranch>`
- [ ] `git branch`
- [ ] `git checkout <nameOfBranch>`
- [x] `git checkout -b <nameOfBranch>`

#### Q60. Після помилкового розміщення файлу з назвою myFile до індексу, як би ви вилучили його з індексу, так щоб виключити одночасно і з вашого наступного коміту?

- [ ] Скористатися git reset HEAD^.
- [x] Скористатися git reset myFile.txt.
- [ ] Скористатися git -rm myFile.txt.
- [ ] Скористатися git reset.

#### Q61. What happens if you run this command from your master branch?

```bash
git checkout -b beta-test
```

- [ ] The beta-test branch will be checked out of the current commit.
- [ ] The beta-test branch will be checked out and deleted.
- [x] A new branch called beta-test will be created and switched to.
- [ ] The beta-test branch will be merged with the master branch.

#### Q62. How does Git internally manage branches?

- [x] by creating a pointer to the most recent snapshot/commit for the branch.
- [ ] by creating a data array of branches in the same repository.
- [ ] by creating a data dictionary of code changes.
- [ ] be creating a debug log that stores repository changes.

#### Q63. You want to perform a git reset but cannot recall all of the available options. What command would you use to see a description of them?

- [x] git help reset
- [ ] git -h reset
- [ ] git options reset
- [ ] git reset help

#### Q64. What is a remote repository?

- [ ] a version of the repository that mirrors changes made in the local repository's master branch for open-source collaboration efforts
- [ ] the lead repository elected by the Git arbitrator found within local repositories of collaborating team members
- [ ] a read-only version of the repository stored on a backup server in case local repositories become lost or corrupted
- [x] a version of the repository hosted on the internet or network that is pushed to or pulled from by collaborators

#### Q65. After modifying some existing files in a repository, you decide to discard the changes. What command can you use?

- [ ] git restore
- [ ] git undo
- [ ] git clean
- [x] git checkout .

#### Q66. After starting to merge a feature branch into your master branch, you encounter a merge conflict and decide you do not want to perform the merge. How can you stop the merge and restore to the pre-merge state?

- [ ] Use git restore -p.
- [ ] Use git merge -u.
- [x] Use git merge --abort.
- [ ] Use git merge --undo.

#### Q67. Which command correctly creates a lightweight tag?

- [x] `git tag v3.8.1`
- [ ] `git tag --light "v3.8.1"`
- [ ] `git tag v3.8.1 —-annotate -m "<tagMessage>"`
- [ ] `git tag -l v3.8.1`

#### Q68. What is the main issue with using git rebase when working with multiple developers?

- [x] Rebase affects only your repository and creates a diff in the master branch.
- [ ] Rebase creates a temporary copy of the master branch in the remote repo.
- [ ] Rebase moves the HEAD of the remote master branch one commit forward.
- [ ] Rebase deletes all commit history for the new feature branch.

#### Q69. What Git workflow is used by teams that collaborate on a single branch and avoid creating long-lived development branches?

- [ ] Git flow
- [x] Mainline flow
- [ ] Trunk-Based Development
- [ ] GitHub flow

#### Q70. Which option on the git log command allows you to limit output to commits made after certain date?

- [x] `--since`
- [ ] `--sinceWhen`
- [ ] `-<n>`
- [ ] `--afterDate`

#### Q71. How would you delete unreachable objects older than a specified time from your project database?

- [ ] `git cache --obsolete <time>`
- [ ] `git branch --rebase <time>`
- [ ] `git delete --inert <time>`
- [x] `git prune --expire <time>`

#### Q72. What conflicts can occur when forcing a push after rebasing?

- [x] The remote master branch could have existing changes overwritten.
- [ ] The origin URL will be reset to its default value.
- [ ] The current HEAD will be deleted and can't be reinstated.
- [ ] Nothing, it's common practice to force a push after rebasing.

#### Q73. What is the difference between Git and SVN?

- [ ] Git works only on Linux, while SVN works on all operating systems.
- [ ] SVN works only on Linux, while Git works on all operating systems.
- [x] SVN is a centralized system, while Git is a distributed system.
- [ ] Git a centralized system, while SVN is a distributed system.

#### Q74. This command is an example of what kind of tag?

`git tag -a v1.4 -m "ABCD v1.5"`

- [ ] verbose
- [x] annotated
- [ ] lightweight
- [ ] deferred

#### Q75. What is the difference between a soft reset (`git reset --soft`) and a hard reset (`git reset –hard`) ?

- [x] A soft reset only changes the commit that HEAD points to, while a hard reset resets the index and working tree to match the specified commit, discarding any changes.
- [ ] A soft reset caches the old HEAD pointer, while a hard reset deletes it entirely.
- [ ] A hard reset changes only where the HEAD is pointing, while a soft reset changes the HEAD and index.
- [ ] A hard reset caches the old HEAD pointer, while a soft reset deletes it entirely.

[Reference](https://git-scm.com/docs/git-reset)

#### Q76. Consider the following Git workflow:

![image](images/Git-WorkFlow.png?raw=png)
Which of the following options is correct ?

- [ ] `1. Develop 2. Release 3. Hotfix 4. Feature 5. Master`
- [ ] `1. Master 2. Release 3. Hotfix 4. Feature 5. Develop`
- [ ] `1. Develop 2. Master 3. Hotfix 4. Feature 5. Develop`
- [x] `1. Master 2. Hotfix 3. Develop 4. Feature 5. Release`

#### Q77. What information does the git config file store?

- [ ] shell scripts and flags
- [ ] keychain and account information
- [x] local and global repository options
- [ ] pre-compile scripts and settings

[Reference](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-config#:~:text=The%20git%20config%20command%20is,modify%20a%20configuration%20text%20file.)

#### Q78. What is version control?

- [ ] a type of architecture used to manage large databases
- [x] a system that shows, tracks, and controls changes to a set of files over time
- [ ] a programmatic design pattern used to manage code between multiple engineering teams
- [ ] a type of software that links a project with a GitHub repository

#### Q79. What is the difference between using the `git stash` and `git stash pop` commands?

- [ ] `git stash` removes a commit from the repo history, while `git stash pop` saves changes to multiple branches.
- [ ] `git stash` saves changes to multiple branches, while `git stash pop` removes a commit from the repo history.
- [ ] `git stash` removes the most recent commit, while `git stash pop` saves current changes.
- [x] `git stash` creates a stash entry, while `git stash pop` places a saved state from the stash list onto the working directory.

#### Q80. Which command can be used to list the branches that have been merged into the currently checked-out branch?

- [ ] git master --status
- [ ] git branch --status
- [x] git branch --merged
- [ ] git status --merged

#### Q81. How would you configure Git to abort a commit if a smoke test script fails?

- [ ] Create a post-commit shell script that triggers the action.
- [ ] Create a post-commit hook to trigger the script.
- [x] Create a pre-commit hook to trigger the script.
- [ ] Create a pre-commit shell script that triggers the action.

#### Q82. Which use case is NOT a good candidate for a Git hook?

- [x] state dependent environment changes
- [ ] continuous integration
- [ ] increasing code coverage
- [ ] enforcing commit rules

#### Q83. What information do Git reflogs (reference logs) store?

- [ ] shell script pointers and keychain credentials
- [x] updates to branch tips and other references in the local repository
- [ ] release notes and hook script values
- [ ] tag and versioning information

#### Q84. You have just completed rebasing your master branch and need to manually update the remote master, even though there is a merge conflict. How can you accomplish this?

- [ ] `git push --overwrite`
- [ ] `git push --update`
- [ ] `git push --assert`
- [x] `git push --force-with-lease`

#### Q85. What is the difference between `git fetch` and `git pull`

- [ ] `git fetch` creates a new branch off the master branch, while `git pull` creates a new branch off the local repository's master branch.
- [ ] `git pull` downloads new data from a remote repository without integrating it into local files, while `git fetch` updates the current HEAD branch with the latest changes from the remote server.
- [x] `git fetch` updates remote tracking branches with changes from a remote repository, while `git pull` updates remote tracking branches with changes from a remote repository and merges them into their corresponding local branches.
- [ ] `git fetch` downloads and merges data from the local repository, while `git pull` informs your colleagues you are about to make changes to the master branch.

#### Q86. What command displays the difference between the working tree and the stage/index area, as well as files not tracked by Git?

- [ ] `git current`
- [x] `git status`
- [ ] `git local`
- [ ] `git context`

#### Q87. You would like to restore some previously stashed work to a new branch. How can you do that?

- [ ] Use `git branch <stash hash>`.
- [ ] Add the stashed commits to the current commit, then create a new branch.
- [ ] Use `git checkout -b`.
- [x] Run `git stash branch <branch name>`.

[reference here](https://stackoverflow.com/questions/6925099/git-stash-changes-apply-to-new-branch)

#### Q88. What is the difference between git branch -d and git branch -D?

- [ ] -D deletes the local branch, while -d deletes the branch regardless of push and merge status.
- [ ] -d deletes the current commit head, while -D deletes the entire branch.
- [x] -d deletes the local branch, while -D deletes the local branch regardless of push and merge status.
- [ ] -D deletes the current commit head, while -d deletes the entire branch.

#### Q89. You stashed three sets of changes but cannot remember the contents of the first stash entry. What command would you use to see the details of the changes in the first of the three stash entries?

- [ ] git stash show -p stash@{2}
- [ ] git stash list
- [ ] git stash show -p stash@{1}
- [x] git stash show -p

[reference here](https://git-scm.com/docs/git-stash)

#### Q90. How would you delete a remote branch in your repository?

- [ ] Use `git --delete <branch_name>`.
- [ ] Use `git push <remote_name> --d <branch_name>`.
- [ ] Use `git push <remote_name> --D`.
- [x] Use `git push <remote_name> --delete <branch_name>`.

[reference here](https://stackoverflow.com/questions/2003505/how-do-i-delete-a-git-branch-locally-and-remotely)

#### Q91. What is the default setting of `git reflog` when no subcommands are specified?

- [ ] delete
- [ ] expire
- [x] show
- [ ] update

[reference here](https://git-scm.com/docs/git-reflog)

#### Q92. How does the `-p` option change the behavior of the `git add` command

- [ ] It causes tracked files in the parent directory to be included in the staged files.
- [x] It allows developers to interactively choose which changes to tracked files are staged and outputs the differences for review.
- [ ] It automatically pushes changes to the corresponding branch on the remote repository.
- [ ] It allows developers to interactively choose which files are committed and outputs the differences for review.

[reference here](https://git-scm.com/docs/git-add#Documentation/git-add.txt--p)

#### Q93. After checking out a specific commit, you receive a warning message indicating You are in 'detached HEAD' state. What is Git warning you of?

- [ ] You are not working on the most recent commit of a branch.
- [ ] A teammate has flagged the code with an issue.
- [x] The commit does not have a parent.
- [ ] The branch has not been pushed to the remote repository.

[reference here](https://www.git-tower.com/learn/git/faq/detached-head-when-checkout-commit)

#### Q94. After accidentally deleting a branch in your local repository, how can you recover it?

- [ ] It cannot be recovered.
- [ ] Find the hash of the branch with the `log` command, then execute `git checkout -b <branchname> <hash>`.
- [x] Find the hash of the branch with the `reflog` command, then execute `git checkout -b <branchname> <hash>`.
- [ ] Execute `git checkout -b <branchname>`.

[Reference](https://stackoverflow.com/questions/1992364/git-recover-deleted-remote-branch)

#### Q95. How would you display a histogram showing inserts, deletion, and modifications per file for a specific commit along with its general commit information?

- [ ] Use `git stat`.
- [ ] Use `git debug --prettyprint`.
- [ ] Query the remote repository with the commit hash.
- [x] Use `git show <commit> --stat`.

[Reference](https://git-scm.com/docs/git-show#Documentation/git-show.txt---statltwidthgtltname-widthgtltcountgt)

#### Q96. What features do repository managers such as GitHub provide beyond Git?

- [ ] Repository managers are proprietary versions of Git that do not include enhanced features.
- [ ] Repository managers provide an enhanced command-line tool that is used to manage multiple local repositories.
- [x] Repository managers provide an online service for hosting Git repositories that include collaboration features such as pull requests, issue tracking, and peer reviews.
- [ ] Repository managers distribute repositories across multiple locations on a user's workstation, providing redundant storage that allows for quick backup and recovery.

[reference](https://www.theserverside.com/video/Git-vs-GitHub-What-is-the-difference-between-them)

#### Q97. What command finds the HEAD of the current branch?

- [ ] `git head --verify`
- [ ] `git log --head`
- [ ] `git hash --head`
- [x] `git show-ref --head`

[reference](https://git-scm.com/docs/git-show-ref)

#### Q98. When Git Workflows contain a long-running branch, what purpose does the long-running branch serve?

- [ ] Long-running branches store unstable code until it os peer reviewed for integration into a feature branch.
- [ ] Long-running branches correspond to agile sprints and are used to store related to features developed in the sprint.
- [ ] Long-running branches contain code related to experimental feature development that is merged into short-lived branches such as master.
- [x] Long-running branches correspond to different stages of development and are always open for topic/feature branches to be pulled into.

Note: master is not a short-lived branch, as answer "C" states. Answer "D" is the correct one.
[Reference](https://git-scm.com/book/en/v2/Git-Branching-Branching-Workflows#:~:text=Long%2DRunning%20Branches,them%20into%20others.)

#### Q99. What command takes changes from the master branch on the remote repository origin and merges then to the local checked-out branch?

- [ ] `git commit -u origin`
- [ ] `git checkout origin`
- [x] `git pull origin master`
- [ ] `git push origin master`

#### Q100. While pushing changes to a remote repository, you receive the following message. How do you resolve this issue?

```bash
error: failed to push some refs to 'https://github.com/myrepo/simple.git'
hint: Updates were rejected because the remote contains work that you do not hint: not have locally.
```

- [ ] Use the --atomic option with the push command.
- [x] Execute a pull, then resolve any merge conflicts and execute another push.
- [ ] Execute a fetch, then execute another push.
- [ ] Use the --force option with the push command.

#### Q101. What does the -p option add to the output of the `git log` command?

- [x] It adds patch output that shows the differences introduced in each commit.
- [ ] It adds patch output that shows a summary listing modified files.
- [ ] It adds padding to the output and displays a histogram showing the number of lines changed in each commit.
- [ ] It adds the full commit message and notes associated with each commit.

#### Q102. What is the staging area or index?

- [ ] an area that stores commits prior to them being pushed to the remote repository
- [ ] an area containing stash entries that can applied to the working files
- [ ] an area where changes from a branch in the remote repository are stored before they are applied to a local branch
- [x] an area that stores information about changes that will be included in the next commit

[Reference](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)

#### Q103. What command would you use to stage changes to the index strictly for properties files in the current directory?

- [x] `git add *.properties`
- [ ] `git add %.properties`
- [ ] `git add .properties`
- [ ] `git add properties`

#### Q104. What are untracked files?

- [ ] files in the local repository that have not been merged into the master branch
- [ ] staged files that Git does not know about because the have not been committed
- [x] files in the working directory that Git does not know about because they have not been staged or committed
- [ ] files in the remote repository that Git does not know about because they have not been tagged

[Reference](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)

#### Q105. What type of Git hook could be used to validate that a commit message contains a ticket number?

- [ ] pre-commit
- [x] commit-msg
- [ ] applypatch-msg
- [ ] prepare-commit-msg

#### Q106. What is the difference between git stash pop and git stash apply?

- [ ] git stash pop pushes the topmost commit to the current branch, while git stash apply caches the last commit in the current branch.
- [x] git stash pop applies the topmost entry in the stash to the working files and removes it from the stash, while git stash apply applies the topmost entry in the stash to the working files but leaves it in the stash.
- [ ] git stash pop merges the topmost commit to the current branch, while git stash apply merges the last commit in the current branch.
- [ ] git stash pop applies the topmost entry in the stash to the working files but leaves it in the stash, while git stash apply applies the topmost entry in the stash to the working files and removes it from the stash.

#### Q107. After making some major changes to your code, you are a little nervous about committing. What command would you use to review the commit prior to making it?

- [ ] git commit --verify
- [ ] git notes show
- [ ] git commit preview
- [x] git commit --dry-run

#### Q108. What statement best describes Git's concept of HEAD?

- [ ] a pointer to the most recently changed file in the stage/index
- [ ] a pointer to the master branch
- [x] a pointer to the most recent commit in the currently checked-out branch
- [ ] a pointer to where the repository is stored in memory

#### Q109. After staging changes to several files, you realize the changes to the config.properties file are incorrect, and need to be removed from the stage and working directory. What command can you use to remove the staged changes to the file?

- [x] git reset HEAD^ -- config.properties
- [ ] git rm config.properties
- [ ] git rf config.properties
- [ ] git checkout HEAD -- config.properties

#### Q110. After a recent release with a stack trace, an issue is create that indicates the problem is with a newly added configuration property named MaxConnections. What command can find all commits that add or remove the string MaxConnections?

- [ ] git grep -a "MaxConnections"
- [ ] git log --search-string "MaxConnections"
- [x] git log -S "MaxConnections"
- [ ] git commit --with "MaxConnections"

#### Q111. Your company has moved its remote repository to GitHub at this location: https://github.com/yourcompany/core-api.git. What command updates the remote repository, named origin, to point to the new remote repository at this location?

- [ ] git remote create-update origin https://github.com/yourcompany/core-api.git
- [ ] git remote update origin https://github.com/yourcompany/core-api.git
- [x] git remote set-url origin https://github.com/yourcompany/core-api.git
- [ ] git remote add https://github.com/yourcompany/core-api.git

#### Q112. When is the cherry-pick command used?

- [x] when a commit from one branch needs to be copied into another branch
- [ ] when the HEAD needs to be reset to a specific commit
- [ ] when a specific commit needs to be pulled down from the remote repository
- [ ] when a hook script needs to be invoked

[reference](https://www.atlassian.com/git/tutorials/cherry-pick#:~:text=git%20cherry%2Dpick%20is%20a,be%20useful%20for%20undoing%20changes.)

#### Q113. How would you describe a forked repository?

- [ ] a deleted or archived copy of a repository
- [ ] a beta release branch of a repository
- [ ] a future branch of a repository
- [x] a separate copy of a repository

[reference](https://stackoverflow.com/a/9339460/1573267)
[reference](https://www.geeksforgeeks.org/git-fork/)

#### Q114. How can you exclude untracked files within the working directory from a Git repository?

- [ ] You cannot exclude the files from the repository.
- [ ] Tag the files with excluded.
- [x] Add a pattern matching the files to the .gitignore file.
- [ ] Add the files to the omitted branch

[reference](https://git-scm.com/docs/gitignore)

#### Q115. What command creates a near-exact copy of the entire repository from a server?

- [ ] `git checkout <url>`
- [ ] `git pull <url>`
- [x] `git clone <url>`
- [ ] `git replicate <url>`

[Reference](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository)

#### Q116. What would happen if you ran the `git reset testfile.js` command?

- [ ] testfile.js would be reverted to a blank file.
- [ ] testfile.js would be reset to its first saved state.
- [x] testfile.js would be reverted to its last saved copy.
- [ ] testfile.js would be removed from the stage/index area, if present.

[reference](https://www.atlassian.com/git/tutorials/undoing-changes/git-reset)

#### Q117. What situation can occur when attempting to combine branches containing changes to the same piece of code?

- [ ] lost code
- [ ] automatic override
- [ ] collisions
- [x] merge conflict

#### Q118. When Git workflows contain a topic branch, what purpose does the topic branch serve?

- [ ] Topic branches store unstable code until it is peer reviewed for integration into another feature branch.
- [ ] Topic branches correspond to different stages of development and are always open for long-running branches to be pulled into.
- [ ] Topic branches are used in waterfall development methodologies to track the state of the code during the various stages of waterfall.
- [x] Topic branches are short-lived branches used to store work related to a particular feature.

#### Q119. What practice can help reduce the chances of encountering a merge conflict?

- [ ] Provide detailed commit messages that describe the changes being introduced by the commit.
- [ ] make large commits that introduce multiple features.
- [x] Keep local repository branches in sync with upstream branches in the remote repository by committing,pushing and pulling frequently.
- [ ] Avoid frequent interaction with the remote repository to reduce the probability of pulling conflicts.

#### Q120. What command can you use to remove untracked files from the working directory?

- [ ] `git rm -all`
- [ ] `git rm --cached`
- [x] `git clean -d -f`
- [ ] `git checkout`

**Note:** In Git, when multiple short options are used together, you can combine them into a single option by omitting the space between them. So, `git clean -d -f` can be combined as `git clean -df`.

#### Q121. After making a commit, you notice that you forgot to include changes to the doge.txt file. What command or commands would you use to add the changes to the commit?

- [x] ⠀

```bash
  git add doge.txt
  git commit --amend --no-edit
```

- [ ] ⠀

```bash
  git commit --amend --no-edit
```

- [ ] ⠀

```bash
  git add doge.txt
  git commit --patch --no-edit
```

- [ ] ⠀

```bash
  git commit --patch --no-edit
```

#### Q122. Which command would remove a file named wrongfile from the current branch of a repository, the index, and working files?

- [x] ⠀

```bash
git rm wrongfile
git commit -m "Removed file"
```

- [ ] ⠀

```bash
  git forget -rf wrongfile
  git commit -m "Removed file"
```

- [ ] ⠀

```bash
  git untrack -rf wrongfile
  git commit -m "Removed file"
```

- [ ] ⠀

```bash
  git rm --cached wrongfile
  git commit -m "Removed file"
```

[Reference](https://git-scm.com/docs/git-rm)

#### Q123. What is the best way to report a bug to a GitHub project?

- [ ] Send an email to a project owner.
- [ ] I don't bother reporting software bugs because there's no transparency and they never get fixed anyway.
- [x] Search for the bug in the project's existing issues and create a new one if it hasn't been reported yet.
- [ ] Use git search -diff to compare all commits in your repository history.

Explanation: A project's issues are visible to anyone who has access to the project, so you may find a resolution is already planned or available. Otherwise, you can create and track the issue yourself.

#### Q124. Suppose you have created a bug fix on a new branch and want it to become part of the next production build generated from the main branch. What should you do next?

- [ ] Copy your branch changes and commit them directly to the main branch.
- [x] Create a pull request to merge your new branch into the main branch.
- [ ] On second thought, maybe I won't share this fix. I'll just put it in my own private version of the source code.
- [ ] Use git bisect to compare the buggy commit to an early commit that works as expected.

Explanation: Pull requests are the correct way to communicate that commits are ready for review and ultimate inclusion on the main branch.

#### Q125. What is GitHub?

- [ ] version control
- [x] A hosting platform for Git repositories
- [ ] for keeping images
- [ ] for social networking

#### Q126. Git Pull is a combination of?

- [ ] Add and commit.
- [ ] branch and checkout.
- [x] fetch and merge.
- [ ] None of these.

[Reference](https://www.atlassian.com/git/tutorials/syncing/git-pull#:~:text=The%20git%20pull%20command%20is%20actually%20a%20combination%20of%20two,will%20enter%20a%20merge%20workflow.)

#### Q127. What is the command to set the user email for the current repository?

- [ ] git email.user
- [x] git config user.email
- [ ] git config email
- [ ] All of the above.

[Reference](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/setting-your-commit-email-address)

#### Q128. **\_** will rewind your project to a specific point in time, losing all commits that came after it. **\_** will keep changes in those rewound commits as local modifications

- [ ] `git reset HEAD`; `git reset HEAD^`
- [x] `git reset --hard`; `git reset --soft`
- [ ] `git reset --soft`; `git reset --hard`
- [ ] `git rewind`; `git update`

#### Q129. Explain the concept of "Git blame" and when it is used in a version control workflow.

- [ ] Git blame is a command for finding and exposing the identity of contributors in a Git repository.
- [ ] It's used for blaming others for code issues in a collaborative project.
- [ ] Git blame is a feature for tracking the location of bugs in code.
- [x] Git blame is a tool for displaying who last modified each line of a file, helping to track changes and understand code history and authorship.

[Reference](https://www.freecodecamp.org/news/git-blame-explained-with-examples/)

#### Q130. What is the purpose of C++ move constructor, and when is it automatically generated?

- [ ] A move constructor creates deep copies of objects, improving memory efficiency.
- [ ] It is generated when you explicitly define a copy constructor.
- [ ] The move constructor is used for copying objects between different data types.
- [x] A move constructor allows efficient transfer of resources from one object to another,reducing unnecessary copying.

#### Q131. You have changed your mind about adding broccoli to your project. How should you remove it?

```
Untracked files:
(use "git add <file>..." to include in what will be committed)
broccoli
```

- [ ] `git remove .`
- [ ] `git remove broccoli`
- [ ] `git clean`
- [x] `git clean -f`

[Reference](https://git-scm.com/docs/git-clean)

#### Q132. You're creating an action for the Github marketplace. why is it importance to create a release?

- [x] to alow you to create .zip files that you can easily share
- [ ] to initiate a continuos integration process
- [x] to package your software so that it can become available through the Github marketplace
- [ ] to create workflows and automate the process of generating software

#### Q133. You're looking at a repository page and click a folder name to open it. You have code search on, so you land in the code view. What is the quickest way to find a file on a path in your repo?

- [x] Press the slash(/) key and then the T key.
- [ ] Go to advanced search.
- [ ] From the search menu, select Path.
- [ ] Press the T key.

#### Q134. How do you save a search that you use often using GitHub?

- [ ] Click Save on the Search box.
- [ ] Click Save in the advanced search menu.
- [x] Click Save on the search results page.
- [ ] Bookmark the search results page.

#### Q135. which of these is not a label that github creates by default?

- [ ] bug
- [ ] documentation
- [ ] wontfix
- [x] repo

#### Q136. What is the fastest way to start a search using Github web pages?

- [ ] Press the slash(/) key on any page of the site.
- [ ] Click the Search tab from the Github Version
- [ ] Click the advanced Search link.
- [x] Click the search box and type your searc query.

#### Q137. Assigning an issue to a person implies that they \_\_\_\_.

- [ ] will get a notification asking them to review the issue
- [x] are responsible for resolving the issue
- [ ] are being informed of the issue's details
- [ ] supervise the team resolving the issue

#### Q138. What does a Template repository do?

- [ ] It creates a live demo of the current repository for training.
- [x] It allows you to create a default structure and files based on the current repository.
- [ ] It lets you archive and store project settings.
- [ ] It imports another project’s settings to the current project.

#### Q139. You’re creating an action for the GitHub Marketplace. Why is it important to create a release?

- [ ] To allow you to create .zip files that you can easily share
- [ ] To initiate a continuous integration process
- [x] To package your software so that it can become available through the Github Marketplace
- [ ] To create workflows and automate the process of generating software

#### Q140. What are two ways to help Copilot give you more accurate suggestions?

- [ ] Add instructions in parentheses.
- [ ] Use shorthand, but accurate, descriptors.
- [x] Add context in comments.
- [ ] Use concise variable names.
- [x] Use descriptive function names.

#### Q141. What is the main purpose of the Chat panel?

- [ ] To search for answers in the current project’s repository
- [ ] To chat with other developers who are working at your company
- [x] To have a conversational discussion with the AI behind Copilot
- [ ] To get a list possible answers to a question

#### Q142. While doing a code review, you want to start an issue by highlighting a function that takes up several lines of code. What is the fastest way to do this in code view?

- [ ] Click the first line number with the function, click the last line number to select a range, then in the hamburger menu select Reference in new issues
- [ ] Copy the code and start a new issue, then use backticks around the function to create the issue
- [ ] Select the function with the mouse, then right click and select reference in new issue
- [ ] Click the line number with the function and select reference function in an issue

#### Q143. You’re reviewing a file in a repository and want to link to the current version of the file, even if it gets updated later. How can you achieve this?

- [ ] Go to the Code tab and click Download zip
- [ ] Right click the code text and select Permalink
- [x] Click Permalink on the code view
- [ ] Copy the URL from the address bar

#### Q144. You’re organizing a desktop application project. You want to use an overview f your project statuses and be able to drag and drop issues. Which view would you use?

- [x] Board
- [ ] Overview
- [ ] Roadmap
- [ ] Table

#### Q145. You’re in the repo for a specific project while working on an app module. You want to look for some of the docs you’ve been working on, which you wrote in markdown. To quickly look in your own repo for all files with a markdown extension, press the slash (/) button on the keyboard while on the repository page and type \_\_\_.

- [ ] Path:.md
- [ ] Grep:.md
- [x] Code:\*.md
- [ ] Ext:\*.md

#### Q146. In GitHub Projects, how can you assign an issue to a collaborator?

- [ ] Label the item with their username.
- [x] Select their username from the Assignees field.
- [ ] Move the item to their column in the Boards view.
- [ ] Add their handle in the comments.

#### Q147. Why should you include a descriptive function name when writing code with Copilot?

- [ ] It helps Copilot add more variables to a function.
- [ ] It trains the algorithm for the next time a GitHub client answers the question.
- [x] It helps Copilot have better context for code assistance and generation.
- [ ] The function names are not fed to Copilot and are ignored by the AI.

#### Q148. You are working on a project that uses a Python library and you want to find an example of how to use a function across all public repositories. Which part of GitHub’s platform would you use?

- [ ] Issues.
- [ ] Discussions
- [ ] Projects
- [x] Search

#### Q149. Working late on a project, you need to find an issue that was assigned to you. What query do you type?

- [x] Is:issue assignee:username
- [ ] Is:issue user:username
- [ ] Issue:issue user:username
- [ ] assignee:username is:rep

#### Q150. you are working on an AI app and need to add information on project tables about the AI model being targeted. What feature allows you to do this?

- [x] Custom fields
- [ ] Comments
- [ ] Pull requests
- [ ] Custom properties

#### Q151. What feature does the shortcut /table activate when used inside a GitHub comment section?

- [ ] A data visualization table
- [x] A markdown table structure
- [ ] An HTML table structure
- [ ] A table of contents

#### Q152. How can you get better suggestions when creating functions?

- [x] Type “function” and then add a detailed and expressive function name.
- [ ] Type “function” and then press Ctrl+/ (Windows) or Command +/ (Mac).
- [ ] Include variables in the parentheses.
- [ ] Use consistent formatting for your function names.

#### Q153. What does the RUN command do in a Dockerfile?

- [ ] It allows you to specify which type of machine to procure.
- [ ] It helps run your workflows.
- [ ] It fires up an additional container
- [x] It allows you to execute a shell command during the image generation process

#### Q154. How can you ensure that you are matching an exact combination of words?

- [ ] Enclose your query in parentheses
- [ ] Use the exact: qualifier
- [x] Put the series of words in quotes
- [ ] Add the AND operator to the end of your query

#### Q155. What is the main function of the Entrypoint instruction in a Dockerfile?

- [ ] It gives instructions to the Docker container to follow before it loads
- [x] It executes a script when the docker container starts.
- [ ] It serves as the first file that an editor opens when it loads the container.
- [ ] It indicates a specific command to be run during the Docker image build process

#### Q156. Inside a GitHub action, which keyword do you use to specify the operating system to run jobs?

- [ ] Hardware
- [x] Runs-on
- [ ] Machine
- [ ] Os

#### Q157. How can you get additional context from other files in your code?

- [ ] Right-click a file and add it to context
- [x] Open additional tabs with some of your codes; they will be in Copilot context
- [ ] Create a comment with the list of files you want Copilot to have context from
- [ ] Highlight the files you want to add context to form the file sidebar

#### Q158. When creating a release, which of these would count as a valid release format?

- [ ] \*3.2.4
- [ ] @3.2.4
- [ ] #3.2.4
- [x] V3.2.4
