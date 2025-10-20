## Git

#### Q1. How can you check your current git version?

- [ ] git --v
- [x] git --version
- [ ] git --option
- [ ] git --current

[Reference](https://www.howtogeek.com/759319/how-to-check-and-update-your-git-version/)

#### Q2. What command lets you create a connection between a local and remote repository?

- [ ] git remote add new
- [x] git remote add origin
- [ ] git remote new origin
- [ ] git remote origin

[Reference](https://stackoverflow.com/questions/20291731/how-to-connect-to-a-remote-git-repository)

#### Q3. Describe what these Git commands do to the commit history:

```bash
git reset --hard HEAD~5
git merge --squash HEAD@{1}
```

- [ ] They reset the HEAD to the fifth commit in the repo, then merge to the master branch.
- [x] The current branch's HEAD is reset back five commits, then prior commits are squashed into a single commit.
- [ ] They delete the last five commits.
- [ ] They merge the last five commits into a new branch.

**Explanation:**

- `git reset --hard HEAD~5` resets the current branch to the commit just before the last 5 (see `man gitrevisions` for details about this notation and other cool alternatives like `HEAD@{2 days ago}`). As it is a hard reset, it will also overwrite every change in the working tree as well. See `man git-reset`.
- `git merge --squash HEAD@{1}` HEAD@{1} is where the branch was just before the previous command (again, see `man gitrevisions`). This command sets the state of the index to be as it would just after a merge from that commit. This whole operation could be a way to take 5 commits from a branch in which you started a new feature and squash them to a single commit, a meaningful one.

[Reference](https://stackoverflow.com/questions/70962338/documentation-of-default-target-of-git-merge-squash)

#### Q4. Your current project has several branches; master, beta, and push-notifications. You've just finished the notification feature in the push-notification branch, and you want to commit it to beta branch. How can you accomplish this?

- [ ] Checkout the push-notifications branch and run git merge beta
- [ ] Checkout the master branch and run git merge beta -> push-notifications
- [ ] Delete the push-notifications branch and it will be committed to the master branch automatically
- [x] Checkout the beta branch and run git merge push-notifications

[Reference](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)

#### Q5. Which of the following is true when you use the following command?

`git add -A`

- [x] All new and updated files are staged
- [ ] Files are staged in alphabetical order.
- [ ] All new files are staged
- [ ] Only updated files are staged

[Reference](https://git-scm.com/docs/git-add)
[Reference](https://www.geeksforgeeks.org/difference-between-git-add-a-and-git-add/)

#### Q6. What will the following command print to the Terminal?

`git remote -v`

- [x] A list of remote repositories and their URLs
- [ ] The current git version you're running
- [ ] An inline editor for modifying remote repositories
- [ ] The last 5 git versions you've installed

[Reference](https://git-scm.com/docs/git-remote)
[Reference](https://www.javatpoint.com/git-remote)

#### Q7. Looking at the following commands, describe what is happening.

```bash
git checkout feature-user-location
git cherry-pick kj2342134sdf090093f0sdgasdf99sdfo992mmmf9921231
```

- [ ] The commit is being tagged for release on the feature-user-location branch
- [ ] A commit is being copied from its original branch over to the feature-user-location branch
- [ ] The commit is being cherry picked as the new HEAD of the commit history
- [ ] A commit is being copied from the feature-user-location branch to the master branch
- [x] The branch is switched to the feature-user-location branch, and the specified commit is applied to the branch.

Explanation:

'git checkout feature-user-location' switches to the 'feature-user-location' branch.
'git cherry-pick kj2342134sdf090093f0sdgasdf99sdfo992mmmf9921231' applies the changes from the specified commit ('kj2342134sdf090093f0sdgasdf99sdfo992mmmf9921231') to the current branch (feature-user-location). This effectively copies the commit from its original branch to the feature-user-location branch.
So, this sequence of commands is cherry-picking a specific commit onto the feature-user-location branch.

#### Q8. What does the following command do to the git repository?

`git reset --soft HEAD^`

- [ ] It deletes all previous commits and resets the repository history back to its initial state.
- [ ] It resets the working branch to the first commit.
- [ ] It keeps the HEAD at the current commit but clears all previous commits.
- [x] It sets HEAD to the previous commit and leaves changes from the undone commit in the stage/index.

[Reference](https://git-scm.com/docs/git-reset)
[Reference](https://stackoverflow.com/questions/24568936/what-is-the-difference-between-git-reset-hard-head1-and-git-reset-soft-head)

#### Q9. You find a bug in your project, but can't locate where it was introduced in the commit history. How would you diagnose this problem?

- [ ] Manually backtrack through your commit history.
- [ ] Use git search -diff to compare all commits in your repository history.
- [ ] Run a git rebase to find the buggy commit.
- [x] Use git bisect to compare the buggy commit to an early commit that works as expected.

[Reference](https://git-scm.com/docs/git-bisect)
[Reference](https://stackoverflow.com/questions/69552866/how-to-diagnose-a-problem-in-git-commit-history)

#### Q10. Why would the following command be used?

`git rebase -i HEAD~10`

- [ ] To run a comparative search of the last 10 commits for differences
- [x] To list the last 10 commits and modify them with either the squash or fixup command
- [ ] To delete the last 10 commits and reset the HEAD
- [ ] In order to locally cache the last 10 commits

[Reference](https://git-scm.com/docs/git-rebase#_interactive_mode)
[Reference](https://stackoverflow.com/questions/363908/how-do-i-use-git-rebase-i-to-rebase-all-changes-in-a-branch)

#### Q11. Why would you use a pre-receive hook in your remote repository?

- [ ] You wouldn't, you would use it in the local repository
- [x] To execute a script when a remote receives a push that is triggered before any refs are updated
- [ ] To fire a script after updates are made to the remote repository
- [ ] To debug all commit tags and release versions

[Reference](https://git-scm.com/docs/githooks)
[Reference](https://docs.github.com/en/enterprise-server@3.10/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/working-with-pre-receive-hooks)

#### Q12. What option can you use to apply git configurations across your entire git environment?

- [ ] `--all`
- [ ] `--master`
- [x] `--global`
- [ ] `--update`

[Reference](https://git-scm.com/docs/git-config)
[Reference](https://www.git-scm.com/book/en/v2/Customizing-Git-Git-Configuration)

#### Q13. How could you squash multiple commits together without using git merge --squash?

- [ ] Caching
- [ ] You can't. git merge --squash is the only git command for that operation.
- [x] Rebasing
- [ ] Reflogging

[Reference](https://git-scm.com/docs/git-rebase#_interactive_mode)
[Reference](https://stackoverflow.com/questions/31409736/squash-commits-directly-on-feature-without-rebase-or-merge)

#### Q14. If you cloned an existing git repository, what would happen?

- [ ] A new copy would overwrite the central repository
- [x] A copy of the repository would be created on your local machine
- [ ] Nothing, cloning is not a supported git function
- [ ] A copy of the repository would be created on the hosting platform

[Reference](https://git-scm.com/docs/git-clone)
[Reference](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

#### Q15. How can you display a list of files added or modified in a specific commit?

- [ ] Find the commit in the remote repository, as that's the only place that kind of information is stored.
- [x] Use the `diff-tree` command with the commit hash.
- [ ] Run `git commit --info` with the commit hash.
- [ ] Access the commit stash data with `git stash`.

[Reference](https://git-scm.com/docs/git-diff-tree)
[Reference](https://stackoverflow.com/questions/424071/how-do-i-list-all-the-files-in-a-commit#:~:text=If%20you%20want%20to%20get%20the%20list%20of,you%20can%20use%20git%20ls-tree%20--name-only%20-r%20%3Ccommit-ish%3E)

#### Q16. What files is this .gitignore programmed to leave out?

```shell
#.swift
build/

*.txt
*.metadata
```

- [ ] All files with a .swift, .txt, or metadata file extension, as well as the entire build directory
- [ ] Only the build directory
- [x] All files in the build directory, as well as files ending with .txt or .metadata
- [ ] Only files with .swift and .txt extensions.

[Reference](https://git-scm.com/docs/gitignore)

A line starting with `#` serves as a comment. Hence `# .swift` does not do anything. See `man gitignore`.

#### Q17. After you make changes to a local repository, you run the following command. What will this do?

`git commit -a -m "Refactor code base"`

- [ ] Nothing, you can't use multiple options in the same command
- [ ] Adds all new files to the staging area
- [ ] Commits all new files with a message
- [x] Adds all modified files to the staging area, then commits them with a message

#### Q18. After checking your git status you get the following output, which shows the file beta-notes.js in the commit but also unstaged. How can this situation occur?

```shell
Change to be committed:

(use "git reset HEAD <file>..." to unstage)
modified: beta-notes.js
Changes not staged for commit:
(use "git add <file>..." to update what will be committed)
(use "git checkout --<file>..." to discard changes in working directory)

modified: beta-notes.js
```

- [ ] There were two copies of beta-notes.js but one was deleted
- [x] beta-notes.js was staged, then modified afterwards, creating two different versions of the file
- [ ] Two copies of beta-notes.js were created, but only one is being tracked
- [ ] There are two tracked copies of beta-notes.js, but one was removed from the commit

[Reference](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)

#### Q19. Where are files stored before they are committed to the local repository?

- [ ] Saved files
- [ ] git documents
- [x] Staging area
- [ ] git cache

[Reference](https://www.geeksforgeeks.org/what-is-a-git-repository/)

#### Q20. What commands would you use to force an overwrite of your local files with the master branch?

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

**Note**: - The command `pull` is `fetch` followed by either `merge` or `rebase` (in this case, `merge`). We don't want to merge. Merge would be an action to our **repository**. We just want to overwrite our **local files**.

#### Q21. You find that your project has a tag and branch both named push-notifications, which causes confusion when trying to print out given reference. How can you specify which branch you want to look at?

- [ ] use git show refs/push-notifications
- [ ] use git show push-notifications
- [ ] use git show heads/refs/push-notifications
- [x] use git show refs/heads/push-notifications

[Reference](https://geedew.com/fixing-git-branch-and-tag-name-collision/)

#### Q22. Your team lead needs a list of all commits that will be moved before you perform a rebase. Which command can you use to access that information?

- [ ] git rebase -log
- [x] git rebase -i
- [ ] git rebase -verbose
- [ ] git rebase -all

#### Q23. What is the operation doing given the Git commands below?

```
git bisect start
git bisect bad 5d41402abc4b2a76b9719d911017c592
git bisect good 69faab6268350295550de7d587bc323d
```

- [ ] It runs a merge of a good commit that is discovered using a known bad commit and known good commit
- [ ] It marks a commit for deletion using a known bad commit and known good commit to determine which commit introduced a bug
- [ ] It defines a bad commit and resets the HEAD using a known bad commit and known good commit
- [x] It performs a binary search using a known bad commit and known good commit to determine which commit introduced a bug

#### Q24. In a situation where you have several commits for a single task, what is the most efficient way to restructure your commit history?

- [ ] Cherry pick the related commits to another branch.
- [ ] Delete the task commits and recommit with a new message.
- [x] Squash the related commits together into a single coherent commit.
- [ ] Stash the related commits under a new hash.

[Reference](https://git-scm.com/docs/git-rebase#_interactive_mode)

#### Q25. Which of the following is true of the git push command?

**Note:** Which statement is true of the `git push` command?

- [x] By default a push doesn't send tags to the remote repository.
- [ ] Commits can only be tagged when they are created.
- [ ] Tags are pushed to the remote repository with their respective commits.
- [ ] Only annotated tags are automatically pushed to the remote repository with a commit.

[Reference](https://git-scm.com/book/en/v2/Git-Basics-Tagging#:~:text=Sharing%20Tags)

#### Q26. After pushing commits to the remote repository for the first time using the command below, what shorthand command can you use in future?

```bash
git push -u origin master
```

- [ ] git push master
- [ ] git push origin
- [ ] Same as before, git push -u origin master
- [x] git push

[Reference](https://git-scm.com/docs/git-push)

#### Q27. How would you create a custom shortcut or command across your Git environment?

- [ ] Run `git hotfix` with the shortcut name.
- [ ] Assign a shortcut or command using git options file.
- [ ] Use the `git custom-key` command.
- [x] Create an alias using the `git config` command.

[Reference](https://git-scm.com/docs/git-config)

#### Q28. What is the status of the beta-notes.js file in the following output?

```shell
Changes not staged for commit:
(use "git add <file>..." to update what will be committed)
(use "git checkout -- <file>..." to discard changes in working directory)

modified: beta-notes.js
```

- [ ] beta-notes.js is untracked and has been modified.
- [x] beta-notes.js is a tracked file and has been modified, but has not been added to the current commit.
- [ ] beta-notes.js is untracked but has been added to the current commit.
- [ ] beta-notes.js is tracked, and the modified file has been added to the current commit.

[Reference](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)

#### Q29. What command would let you modify your previous commit?

- [ ] --fix
- [ ] --quickfix
- [ ] --modify
- [x] --amend

[Reference](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History)

#### Q30. What is the best way to characterize the git commit structure?

- [ ] Data array
- [ ] Data log
- [x] Data snapshot
- [ ] Data dictionary

[Reference](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)

#### Q31. What change will the following command make to the staging area files?

`git rm --cached testfile.js`

- [x] testfile.js will be removed from the staging area and its changes no longer tracked.
- [ ] testfile.js will be removed from the staging area but its changes will still be tracked.
- [ ] A copy of testfile.js will be cached on your desktop.
- [ ] The current copy of testfile.js will be saved in the staging area.

[Reference](https://git-scm.com/docs/git-rm)

#### Q32. After you've successfully merged two branches and committed the changes, what is the next step in keeping your git structure organized?

- [ ] Use the git reset --soft HEAD to roll back one commit.
- [x] Run git branch -d `<branch name>` to delete the merged branch.
- [ ] Use git clear-all to clean up any hanging files.
- [ ] Run git rebase to move the current commit to its original location.

[Reference](https://www.w3docs.com/snippets/git/how-to-delete-already-merged-git-branches.html#:~:text=Make%20sure%20you%20are%20on,branches%20you%20want%20to%20delete.)

#### Q33. While modifying a file, you're unexpectedly assigned an urgent bug fix on another branch. How can you temporarily save your local work without committing?

- [ ] This is not possible, as you cannot save locally without committing.
- [ ] Run git hold to save a local copy of what you're doing to return to later.
- [ ] Save your work with git local-cache.
- [x] Use git stash to save your work and come back later and reapply the stashed commit.

[Reference](https://git-scm.com/docs/git-stash)

#### Q34. What command would you use to create a new git repository?

- [ ] git add
- [ ] git start
- [ ] git new
- [x] git init

[Reference](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository)

#### Q35. While working on a feature branch you try to use "git rerere" to solve a recurring merge conflict but nothing is happening. What could be causing this issue?

- [ ] The "-all" option isn't added to the command.
- [x] "rerere.enabled" isn't enable in the config file.
- [ ] The commit hash is missing.
- [ ] The filepath isn't specified.

[Reference](https://git-scm.com/docs/git-rerere)

#### Q36. Which setting determines what pager is used when Git pages output?

- [ ] core.page
- [ ] page
- [ ] pager
- [x] core.pager

#### Q37. What does commit object contain?

- [ ] A set of files, representing the state of a project at a given point of time.
- [ ] Reference to parent commit objects.
- [ ] An SHA1 name, a 40-character string that uniquely identifies the commit object.
- [x] Reference to parent commit objects and a set of files, representing the state of a project at a given point of time, and an SHA1 name, a 40-character string that uniquely identifies the commit object.

#### Q38. Which option enables inclusion of committer name in custom log format?

- [ ] %ce
- [ ] %cr
- [ ] %cd
- [x] %cn

[Reference](https://git-scm.com/docs/pretty-formats)

#### Q39. How many ways are present in Git to integrate changes from one branch into another?

- [ ] 3
- [ ] 5
- [x] 2
- [ ] 4
      [Reference](https://git-scm.com/book/en/v2/Git-Branching-Rebasing)

#### Q40. Which user should be created first during setting up of SSH?

- [ ] git
- [ ] admin
- [ ] root
- [x] None of these

_note_: The question is not specific enough to give a definitive answer, as it depends on the specific use case and configuration of the SSH setup.

#### Q41. Which command will list tags with the 1.4.2 series?

- [ ] git tag 'v1.4.2'
- [x] git tag -l 'v1.4.2.\*'
- [ ] git tag-list 'v1.4.2\*'
- [ ] git tag 'v1.4.2\*'

#### Q42. Which of the following is an integration manager?

- [ ] lieutenants
- [ ] benevolent dictator
- [x] Depends upon project type
- [ ] Depends upon data

#### Q43. Which Git command begins tracking of a new file?

- [x] add
- [ ] addfile
- [ ] begin
- [ ] track

[Reference](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)

#### Q44. Which of the following is called dumb protocol?

- [ ] All of these
- [ ] SSH
- [ ] Git
- [x] HTTP

[Reference](https://git-scm.com/book/en/v2/Git-Internals-Transfer-Protocols)

#### Q45. Which key press returns a set of suggestions to pick from, when writing a Git command?

- [ ] Control
- [ ] Shift
- [x] Tab
- [ ] Alt

#### Q46. Which of these terms best describes Git?

- [x] Distributed Version Control System
- [ ] Issue Tracking System
- [ ] Integrated Development Environment
- [ ] Web-Based Repository Hosting Service

[Reference](https://en.wikipedia.org/wiki/Git)

#### Q47. How does Git think of its data?

- [ ] File
- [ ] None of these
- [x] Snapshot
- [ ] Folder

[Reference](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)

#### Q48. Which option enables inclusion of author name in custom log format?

- [ ] %am
- [ ] %ad
- [ ] %ae
- [x] %an

#### Q49. Which version onwards did Git offer reversing a file back to what it looked like when last committed?

- [ ] 1.7
- [x] 1.6
- [ ] 2.0
- [ ] 1.8

#### Q50. Which strategy is used by Git for merging two branches?

- [ ] LIFO
- [ ] recursive
- [ ] FIFO
- [x] octopus

#### Q51. What does refs store?

- [ ] SHA-1 value
- [ ] None of these
- [x] Branch name
- [ ] Project name

[Reference](https://git-scm.com/book/en/v2/Git-Internals-Git-References)

#### Q52. What Language is used in GIT?

- [x] C
- [ ] C++
- [ ] C#
- [ ] Java

#### Q53. What is usually the extension of file which has the public key?

- [ ] ssh
- [x] pub
- [ ] key
- [ ] pk

[Reference](https://git-scm.com/book/en/v2/Git-on-the-Server-Generating-Your-SSH-Public-Key)

#### Q54. What is the difference between initializing a normal repo and a bare repo?

- [ ] Bare repos store their git history in a .git subfolder.
- [ ] Bare repos do not have the .git extension.
- [x] Bare repos do not come with working or checked-out source files.
- [ ] Bare repos should be used for local rather than remote repos.

#### Q55. How many individual commits can a single repository have?

- [x] any number of commits
- [ ] only one commit local per repository
- [ ] only three commits per branch
- [ ] only one commit per HEAD

#### Q56. What types of tags does Git support?

- [ ] heavy and concise
- [ ] lightweight and immutable
- [ ] heavy and annotated
- [x] lightweight and annotated

[Reference](https://git-scm.com/book/en/v2/Git-Basics-Tagging)

#### Q57. After staging a series of changes to the index, which command could you use to review them prior to a commit?

- [x] git diff --cached
- [ ] git diff
- [ ] git diff --HEAD
- [ ] git status -v -v

#### Q58. What does the git stash drop command do?

- [x] removes the most recent stash entry
- [ ] deletes the stash
- [ ] lists everything in the stash
- [ ] throws away the oldest entry

[Reference](https://git-scm.com/docs/git-stash)

#### Q59. What command creates a new branch from the currently checked-out branch?

- [ ] `git -b checkout <nameOfBranch>`
- [ ] `git branch`
- [ ] `git checkout <nameOfBranch>`
- [x] `git checkout -b <nameOfBranch>`

#### Q60. After mistakenly staging a file named myFile to the index, how would you remove it from the index to exclude it from your next commit?

- [ ] Use git reset HEAD^.
- [x] Use git reset myFile.txt.
- [ ] Use git -rm myFile.txt.
- [ ] Use git reset.

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
- [x] Click the search box and type your search query.

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

#### Q159. What is the maximum number of suggestions the completions panel gives at one time?

- [ ] 100
- [ ] 5
- [x] 10
- [ ] 8

#### Q160. You are looking for markdown files in a project, so you type in the following search: repo:planetoftheweb/slides_vue3 \*.md. What does the commits section in the filter by siderbar show?

- [ ] Any commits that you are mentioned on
- [x] The commits that match your search query
- [ ] The most recent commits
- [ ] All the commits you personally made

#### Q161. Your company worked on a popular utility module and you remember that it had between 100 and 200 stars. How would you write qualifiers that would limit that search?

- [x] Stars:100..200
- [ ] Stars: 100 or 200
- [ ] Stars:100,200
- [ ] Stars:100-200

#### Q162. What’s a good way to use the filter feature to display only the issues that are assigned to a specific user?

- [ ] Owner: username
- [ ] Assigned:username
- [x] Assignee:username
- [ ] User: username

#### Q163. Which feature is enabled for a checklist when added to the description of an issue?

- [ ] You can convert an individual checklist item to a GitHub issue.
- [x] You can mark the checklist items as completed
- [ ] You can link directly to an issue and show a popup with issue information
- [ ] You can reorder the checklist items
- [ ]

#### Q164. You are building a visual studio code extension and you remember that microsoft has sample code you could learn from. Which search would yield the fewest results while searching all of GitHub for “vscode” repos from “microsoft”?

- [x] Owner:microsoft repo:vscode
- [ ] Vscode
- [ ] Company:microsoft repo:vscode
- [ ] Microsoft/vscode

#### Q165. What is the purpose of the git clone command?

- [ ] To create a new repository from scratch
- [ ] To initialize a new repository
- [x] To copy an existing repository
- [ ] To delete a repository

**Explanation**

- The git clone command is used to create a local copy of an existing Git repository. It downloads the entire repository, including its history and all branches, from a remote location. The other options describe actions that git clone does not perform.

#### Q166. Which of the following is used to stage changes for the next commit?

- [ ] git stage
- [x] git add
- [ ] git push
- [ ] git commit

**Explanation**

- git add stages the changes, making them ready to be committed in the next commit. It tells Git which changes you want to include in the commit. git commit is used after staging changes to actually create the commit, git push uploads changes to a remote repository, and git stage is not a valid Git command.

#### Q167. How can you create a new branch and switch to it immediately?

- [x] git checkout -b <branch-name>
- [ ] git branch <branch-name>
- [ ] git switch <branch-name>
- [ ] git merge <branch-name>

**Explanation**

- git checkout -b <branch-name> creates a new branch and switches to it in one step. git branch <branch-name> only creates the branch but doesn't switch to it. git switch can switch branches but cannot create them. git merge is used to combine branches, not create or switch between them.

#### Q168. What is the purpose of the `git rebase` command?

- [ ] To merge two branches and create a new commit
- [ ] To delete a branch and its commit history
- [x] To move the base of a branch to a different commit
- [ ] To create a new branch from the current commit

**Explanation:**
The `git rebase` command is used to move the base of a branch to a different commit. This is useful for keeping a branch up-to-date with the main branch or for cleaning up the commit history by squashing or rearranging commits. It does not merge branches or delete branch history, as the other options suggest.

#### Q169. Which Git command is used to view the commit history of a repository?

- [ ] `git status`
- [ ] `git diff`
- [x] `git log`
- [ ] `git show`

**Explanation:**
The `git log` command is used to view the commit history of a Git repository. It displays the commit messages, authors, dates, and other metadata for each commit. `git status` shows the current state of the working directory and staging area, `git diff` shows the changes between commits or the working directory, and `git show` displays the changes introduced by a specific commit.
