## Git

#### Q1. How can you check your current git version?

- [ ] git --v
- [x] git --version
- [ ] git --option
- [ ] git --current

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

#### Q4. Your current project has several branches; master, beta, and push-notifications. You've just finished the notification feature in the push-notification branch, and you want to commit it to beta branch. How can you accomplish this?

- [ ] Checkout the push-notifications branch and run git merge beta
- [ ] Checkout the master branch and run git merge beta -> push-notifications
- [ ] Delete the push-notifications branch and it will be committed to the master branch automatically
- [x] Checkout the beta branch and run git merge push-notifications

#### Q5. Which of the following is true you when you use the following command?

`git add -A`

- [x] All new and updated files are staged
- [ ] Files are staged in alphabetical order.
- [ ] All new files are staged
- [ ] Only updated files are staged

#### Q6. What will the following command print to the Terminal?

`git remote -v`

- [x] A list of remote repositories and their URLs
- [ ] The current git version you're running
- [ ] An inline editor for modifying remote repositories
- [ ] The last 5 git versions you've installed

#### Q7. Looking at the following commands, describe what is happening.

```bash
git checkout feature-user-location
git cherry-pick kj2342134sdf090093f0sdgasdf99sdfo992mmmf9921231
```

- [ ] The commit is being tagged for release on the feature-user-location branch
- [ ] A commit is being copied from its original branch over to the feature-user-location branch
- [x] The commit is being cherry picked as the new HEAD of the commit history
- [ ] A commit is being copied from the feature-user-location branch to the master branch
- [ ] The branch is switched to the feature-user-location branch, and the specified commit is applied to the branch.

**Explanation:** Commits aren't copied when cherry picking, they are cherry picked. The changes introduced by the commit are applied and a new commit is then created. This allow us to get specific changes as if they were patches (in the GIT's book, this is actually called [Patching](https://git-scm.com/book/en/v2/Appendix-C:-Git-Commands-Patching "See this in the GIT's book")). As a new commit is created upon feature-user-location, HEAD also changes to match it. You can see this in `cat .git/HEAD` and `cat .git/refs/heads/feature-user-location` for this case. See `man git-cherry-pick` for details.

**NOTE**: There are two versions of this question so far. The task is always "describe what is happening", the commands are always a `checkout` and a `cherry-pick`, and the correct answer is always the same.

#### Q8. What does the following command do to the git repository?

`git reset --soft HEAD^`

- [ ] It deletes all previous commits and reset the repository history back to its initial state.
- [ ] It resets the working branch to the first commit.
- [ ] It keeps the HEAD at the current commit, but clears all previous commits.
- [x] It sets HEAD to the previous commit and leaves changes from the undone commit in the stage/index.

#### Q9. You find a bug in your project, but can't locate where it was introduced in the commit history. How would you diagnose this problem?

- [ ] Manually backtrack through your commit history.
- [ ] Use git search -diff to compare all commits in your repository history.
- [ ] Run a git rebase to find the buggy commit.
- [x] Use git bisect to compare the buggy commit to an early commit that works as expected.

#### Q10. Why would the following command be used?

`git rebase -i HEAD~10`

- [ ] To run a comparative search of the last 10 commits for differences
- [x] To list the last 10 commits and modify them with either the squash or fixup command
- [ ] To delete the last 10 commits and reset the HEAD
- [ ] In order to locally cache the last 10 commits

#### Q11. Why would you use a pre-receive hook in your remote repository?

- [ ] You wouldn't, you would use it in the local repository
- [x] To execute a script when a remote receives a push that is triggered before any refs are updated
- [ ] To fire a script after updates are made to the remote repository
- [ ] To debug all commit tags and release versions

#### Q12. What option can you use to apply git configurations across your entire git environment?

- [ ] `--all`
- [ ] `--master`
- [x] `--global`
- [ ] `--update`

#### Q13. How could you squash multiple commits together without using git merge --squash?

- [ ] Caching
- [ ] You can't. git merge --squash is the only git command for that operation.
- [x] Rebasing
- [ ] Reflogging

#### Q14. If you cloned an existing git repository, what would happen?

- [ ] A new copy would overwrite the central repository
- [x] A copy of the repository would be created on your local machine
- [ ] Nothing, cloning is not a supported git function
- [ ] A copy of the repository would be created on the hosting platform

#### Q15. How can you display a list of files added or modified in a specific commit?

- [ ] Find the commit in the remote repository, as that's the only place that kind of information is stored.
- [x] Use the `diff-tree` command with the commit hash.
- [ ] Run `git commit --info` with the commit hash.
- [ ] Access the commit stash data with `git stash`.

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

#### Q19. Where are files stored before they are committed to the local repository?

- [ ] Saved files
- [ ] git documents
- [x] Staging area
- [ ] git cache

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

- [ ]
```bash
  git pull origin master
  git reset --hard origin/myCurrentBranch
```

- [x]
```bash
  git fetch --all
  git reset --hard origin/master
```

**Note**: - The command `pull` is `fetch` followed by either `merge` or `rebase` (in this case, `merge`). We don't want to merge. Merge would be an action to our **repository**. We just want to overwrite our **local files**.

#### Q21. Which statement is true when you use the git add -A command?

- [ ] Only new files in the working directory are staged to the index.
- [x] All new and updated files from the working directory are staged to the index.
- [ ] All files in the working directory are staged to the index in alphabetical order.
- [ ] Only updated files in the working directory are staged to the index.

#### Q22. You find that your project has a tag and branch both named push-notifications, which causes confusion when trying to print out given reference. How can you specify which branch you want to look at?

- [ ] use git show refs/push-notifications
- [ ] use git show push-notifications
- [ ] use git show head/refs/push-notifications
- [x] use git show refs/head/push-notifications

[Reference](https://geedew.com/fixing-git-branch-and-tag-name-collision/)

#### Q23. Your team lead needs a list of all commits that will be moved before you perform a rebase. Which command can you use to access that information?

- [ ] git rebase -log
- [x] git rebase -i
- [ ] git rebase -verbose
- [ ] git rebase -all

#### Q24. What is the operation doing given the Git commands below?

```
git bisect start
git bisect bad 5d41402abc4b2a76b9719d911017c592
git bisect good 69faab6268350295550de7d587bc323d
```

- [ ] It runs a merge of a good commit that is discovered using a known bad commit and known good commit
- [ ] It marks a commit for deletion using a known bad commit and known good commit to determine which commit introduced a bug
- [ ] It defines a bad commit and resets the HEAD using a known bad commit and known good commit
- [x] It performs a binary search using a known bad commit and known good commit to determine which commit introduced a bug

#### Q25. In a situation where you have several commits for a single task, what is the most efficient way to restructure your commit history?

- [ ] Cherry pick the related commits to another branch.
- [ ] Delete the task commits and recommit with a new message.
- [x] Squash the related commits together into a single coherent commit.
- [ ] Stash the related commits under a new hash.

#### Q26. Which of the following is true of the git push command?

- [x] By default a push doesn't send tags to the remote repository.
- [ ] Commits can only be tagged when they are created.
- [ ] Tags are pushed to the remote repository with their respective commits.
- [ ] Only annotated tags are automatically pushed to the remote repository with a commit.

[Reference](https://git-scm.com/book/en/v2/Git-Basics-Tagging#_sharing_tags)

#### Q27. After pushing commits to the remote repository for the first time using the command below, what shorthand command can you use in future?

```bash
git push -u origin master
```

- [ ] git push master
- [ ] git push origin
- [ ] Same as before, git push -u origin master
- [x] git push

#### Q28. How would you create a custom shortcut or command across your git environment?

- [ ] Run git hotfix with the shortcut name.
- [ ] Assign a shortcut or command using git options file.
- [ ] Use the git custom-key command.
- [x] Create an alias using the git config command.

#### Q29. What is the status of the beta-notes.js file in the following output?

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

#### Q30. What command would let you modify your previous commit?

- [ ] --fix
- [ ] --quickfix
- [ ] --modify
- [x] --amend

#### Q31. What is the best way to characterize the git commit structure?

- [ ] Data array
- [x] Data log
- [ ] Data snapshot
- [ ] Data dictionary

#### Q32. What change will the following command make to the staging area files?

`git rm --cached testfile.js`

- [x] testfile.js will be removed from the staging area and its changes no longer tracked.
- [ ] testfile.js will be removed from the staging area but its changes will still be tracked.
- [ ] A copy of testfile.js will be cached on your desktop.
- [ ] The current copy of testfile.js will be saved in the staging area.

#### Q33. After you've successfully merged two branches and committed the changes, what is the next step in keeping your git structure organized?

- [ ] Use the git reset --soft HEAD to roll back one commit.
- [x] Run git branch -d `<branch name>` to delete the merged branch.
- [ ] Use git clear-all to clean up any hanging files.
- [ ] Run git rebase to move the current commit to its original location.

#### Q34. While modifying a file, you're unexpectedly assigned an urgent bug fix on another branch. How can you temporarily save your local work without committing?

- [ ] This is not possible, as you cannot save locally without committing.
- [ ] Run git hold to save a local copy of what you're doing to return to later.
- [ ] Save your work with git local-cache.
- [x] Use git stash to save your work and come back later and reapply the stashed commit.

#### Q35. What command would you use to create a new git repository?

- [ ] git add
- [ ] git start
- [ ] git new
- [x] git init

#### Q36. While working on a feature branch you try to use "git rerere" to solve a recurring merge conflict but nothing is happening. What could be causing this issue?

- [ ] The "-all" option isn't added to the command.
- [x] "rerere.enabled" isn't enable in the config file.
- [ ] The commit hash is missing.
- [ ] The filepath isn't specified.

#### Q37. Which setting determines what pager is used when Git pages output?

- [ ] core.page
- [ ] page
- [ ] pager
- [x] core.pager

#### Q38. What does commit object contain?

- [ ] A set of files, representing the state of a project at a given point of time.
- [ ] Reference to parent commit objects.
- [x] An SHA1 name, a 40-character string that uniquely identifies the commit object.

#### Q39. Which option enables inclusion of committer name in custom log format?

- [ ] %ce
- [ ] %cr
- [ ] %cd
- [x] %cn

#### Q40. How many ways are present in Git to integrate changes from one branch into another?

- [ ] 3
- [ ] 5
- [x] 2
- [ ] 4

[Reference link](https://git-scm.com/book/en/v2/Git-Branching-Rebasing)
`In Git, there are two main ways to integrate changes from one branch into another: the merge and the rebase.`

#### Q41. Which user should be created first during setting up of SSH?

- [x] git
- [ ] admin
- [ ] root
- [ ] None of these

#### Q42. Which command will list tags with the 1.4.2 series?

- [ ] git tag 'v1.4.2'
- [x] git tag -I 'v1.4.2.\*'
- [ ] git tag-list 'v1.4.2\*'
- [ ] git tag 'v1.4.2\*'

#### Q43. Which of the following is an integration manager?

- [ ] lieutenants
- [x] benevolent dictator
- [ ] Depends upon project type
- [ ] Depends upon data

#### Q44. Which Git command begins tracking of a new file?

- [x] add
- [ ] addfile
- [ ] begin
- [ ] track

#### Q45. Which of the following is called dumb protocol?

- [ ] All of these
- [ ] SSH
- [ ] Git
- [x] HTTP

#### Q46. Which key press returns a set of suggestions to pick from, when writing a Git command?

- [ ] Control
- [ ] Shift
- [x] Tab
- [ ] Alt

#### Q47. Which of these terms best describes Git?

- [x] Distributed Version Control System
- [ ] Issue Tracking System
- [ ] Integrated Development Environment
- [ ] Web-Based Repository Hosting Service

#### Q48. Which command gets a copy of an existing Git repository?

- [ ] duplicate
- [ ] replicate
- [ ] copy
- [x] clone

#### Q49. How does Git think of its data?

- [ ] File
- [ ] None of these
- [x] Snapshot
- [ ] Folder

#### Q50. Which option enables inclusion of author name in custom log format?

- [ ] %am
- [ ] %ad
- [ ] %ae
- [x] %an

#### Q51. Which version onwards did Git offer reversing a file back to what it looked like when last committed?

- [ ] 1.7
- [x] 1.6
- [ ] 2.0
- [ ] 1.8

#### Q52. Which strategy is used by Git for merging two branches?

- [ ] LIFO
- [x] recursive
- [ ] FIFO
- [ ] octopus

#### Q53. What does refs store?

- [x] SHA-1 value
- [ ] None of these
- [ ] Branch name
- [ ] Project name

#### Q54. What Language is used in GIT?

- [x] C
- [ ] C++
- [ ] C#
- [ ] Java

#### Q55. What is usually the extension of file which has the public key?

- [ ] ssh
- [x] pub
- [ ] key
- [ ] pk

#### Q56. What is the difference between initializing a normal repo and a bare repo?

- [ ] Bare repos store their git history in a .git subfolder.
- [ ] Bare repos do not have the .git extension.
- [x] Bare repos do not come with working or checked-out source files.
- [ ] Bare repos should be used for local rather than remote repos.

#### Q57. How many individual commits can a single repository have?

- [x] any number of commits
- [ ] only one commit local per repository
- [ ] only three commits per branch
- [ ] only one commit per HEAD

#### Q58. What types of tags does Git support?

- [ ] heavy and concise
- [ ] lightweight and immutable
- [ ] heavy and annotated
- [x] lightweight and annotated

#### Q59. After staging a series of changes to the index, which command could you use to review them prior to a commit?

- [x] git diff --cached
- [ ] git diff
- [ ] git diff --HEAD
- [ ] git status -v -v

#### Q60. What does the git stash drop command do?

- [x] removes the most recent stash entry
- [ ] deletes the stash
- [ ] lists everything in the stash
- [ ] throws away the oldest entry

#### Q61. What command creates a new branch from the currently checked-out branch?

- [ ] `git -b checkout <nameOfBranch>`
- [ ] `git branch`
- [ ] `git checkout <nameOfBranch>`
- [x] `git checkout -b <nameOfBranch>`

#### Q62. After mistakenly staging a file named myFile to the index, how would you remove it from the index to exclude it from your next commit?

- [ ] Use git reset HEAD^.
- [x] Use git reset myFile.txt.
- [ ] Use git -rm myFile.txt.
- [ ] Use git reset.

#### Q63. What happens if you run this command from your master branch?

```bash
git checkout -b beta-test
```

- [ ] The beta-test branch will be checked out of the current commit.
- [ ] The beta-test branch will be checked out and deleted.
- [x] A new branch called beta-test will be created and switched to.
- [ ] The beta-test branch will be merged with the master branch.

#### Q64. How does Git internally manage branches?

- [x] by creating a pointer to the most recent snapshot/commit for the branch.
- [ ] by creating a data array of branches in the same repository.
- [ ] by creating a data dictionary of code changes.
- [ ] be creating a debug log that stores repository changes.

#### Q65. You want to perform a git reset but cannot recall all of the available options. What command would you use to see a description of them?

- [x] git help reset
- [ ] git -h reset
- [ ] git options reset
- [ ] git reset help

#### Q66. What is a remote repository?

- [ ] a version of the repository that mirrors changes made in the local repository's master branch for open-source collaboration efforts
- [ ] the lead repository elected by the Git arbitrator found within local repositories of collaborating team members
- [ ] a read-only version of the repository stored on a backup server in case local repositories become lost or corrupted
- [x] a version of the repository hosted on the internet or network that is pushed to or pulled from by collaborators

#### Q67. After modifying some existing files in a repository, you decide to discard the changes. What command can you use?

- [x] git restore
- [ ] git undo
- [ ] git clean
- [ ] git checkout

#### Q68. After starting to merge a feature branch into your master branch, you encounter a merge conflict and decide you do not want to perform the merge. How can you stop the merge and restore to the pre-merge state?

- [ ] Use git restore -p.
- [ ] Use git merge -u.
- [x] Use git merge --abort.
- [ ] Use git merge --undo.

#### Q69. If you have several commits for a single feature, what is the most efficient way to restructure your commit history?

- [ ] Use git stash to consolidate the commits under a new hash.
- [x] Use git squash to consolidate the commits together into a single coherent commit.
- [ ] Delete the task commits and recommit with a new message.
- [ ] Use git cherry-pick to place the commits in another branch.

#### Q70. Which command correctly creates a lightweight tag?

- [x] `git tag v3.8.1`
- [ ] `git tag --light "v3.8.1"`
- [ ] `git tag v3.8.1 —-annotate -m "<tagMessage>"`
- [ ] `git tag -l v3.8.1`

#### Q71. What is the main issue with using git rebase when working with multiple developers?

- [ ] Rebase affects only your repository and creates a diff in the master branch.
- [ ] Rebase creates a temporary copy of the master branch in the remote repo.
- [ ] Rebase moves the HEAD of the remote master branch one commit forward.
- [x] Rebase deletes all commit history for the new feature branch.

#### Q72. What Git workflow is used by teams that collaborate on a single branch and avoid creating long-lived development branches?

- [ ] Git flow
- [ ] Mainline flow
- [x] Trunk-Based Development
- [ ] GitHub flow

#### Q73. Which option on the git log command allows you to limit output to commits made after certain date?

- [x] `--since`
- [ ] `--sinceWhen`
- [ ] `-<n>`
- [ ] `--afterDate`

#### Q74. How would you delete unreachable objects older than a specified time from your project database?

- [ ] `git cache --obsolete <time>`
- [ ] `git branch --rebase <time>`
- [ ] `git delete --inert <time>`
- [x] `git prune --expire <time>`

#### Q75. What conflicts can occur when forcing a push after rebasing?

- [x] The remote master branch could have existing changes overwritten.
- [ ] The origin URL will be reset to its default value.
- [ ] The current HEAD will be deleted and can't be reinstated.
- [ ] Nothing, it's common practice to force a push after rebasing.

#### Q76. How does this command alter the currently checked-out branch?

`git reset --soft HEAD^`

- [ ] It resets the working branch to the first commit.
- [x] It sets HEAD to previous commit and leaves changes from the undone commit in the stage/index.
- [ ] It deletes all previous commits and resets the repository history back to its initial state.
- [ ] It keeps the HEAD at the current commit, but clears all previous commits.

#### Q77. What is the difference between Git and SVN?

- [ ] Git works only on Linux, while SVN works on all operating systems.
- [ ] SVN works only on Linux, while Git works on all operating systems.
- [x] SVN is a centralized system, while Git is a distributed system.
- [ ] Git a centralized system, while SVN is a distributed system.

#### Q78. This command is an example of what kind of tag?

`git tag -a v1.4 -m "ABCD v1.5"`

- [ ] verbose
- [x] annotated
- [ ] lightweight
- [ ] deferred

#### Q79. What is the difference between a soft reset (`git reset --soft`) and a hard reset (`git reset –hard`) ?

- [x] A soft reset only changes the commit that HEAD points to, while a hard reset resets the index and working tree to match the specified commit, discarding any changes.
- [ ] A soft reset caches the old HEAD pointer, while a hard reset deletes it entirely.
- [ ] A hard reset changes only where the HEAD is pointing, while a soft reset changes the HEAD and index.
- [ ] A hard reset caches the old HEAD pointer, while a soft reset deletes it entirely.

#### Q80. Consider the following Git workflow:

![image](images/Git-WorkFlow.png?raw=png)
Which of the following options is correct ?

- [ ] `1. Develop 2. Release 3. Hotfix 4. Feature 5. Master`
- [ ] `1. Master 2. Release 3. Hotfix 4. Feature 5. Develop`
- [ ] `1. Develop 2. Master 3. Hotfix 4. Feature 5. Develop`
- [x] `1. Master 2. Hotfix 3. Develop 4. Feature 5. Release`

#### Q81. What information does the git config file store?

- [ ] shell scripts and flags
- [ ] keychain and account information
- [x] local and global repository options
- [ ] pre-compile scripts and settings

[Reference](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-config#:~:text=The%20git%20config%20command%20is,modify%20a%20configuration%20text%20file.)

#### Q82. What is version control?

- [ ] a type of architecture used to manage large databases
- [x] a system that shows, tracks, and controls changes to a set of files over time
- [ ] a programmatic design pattern used to manage code between multiple engineering teams
- [ ] a type of software that links a project with a GitHub repository

#### Q83. What is the difference between using the git stash and git stash pop commands?

- [ ] git stash removes a commit from the repo history, while git stash pop saves changes to multiple branches.
- [ ] git stash saves changes to multiple branches, while git stash pop removes a commit from the repo history.
- [ ] git stash removes the most recent commit, while git stash pop saves current changes.
- [x] git stash creates a stash entry, while git stash pop places the saved state onto the working directory.

#### Q84. Which command can be used to list the branches that have been merged into the currently checked-out branch?

- [ ] git master --status
- [ ] git branch --status
- [x] git branch --merged
- [ ] git status --merged

#### Q85. How would you configure Git to abort a commit if a smoke test script fails?

- [ ] Create a post-commit shell script that triggers the action.
- [ ] Create a post-commit hook to trigger the script.
- [x] Create a pre-commit hook to trigger the script.
- [ ] Create a pre-commit shell script that triggers the action.

#### Q86. Which use case is NOT a good candidate for a Git hook?

- [x] state dependent environment changes
- [ ] continuous integration
- [ ] increasing code coverage
- [ ] enforcing commit rules

#### Q87. After starting to work on a new feature and creating new files in the working directory related to it, the customer determined the feature was no longer required. What command can be used to remove the untracked files from the working directory ?

- [x] `git clean -f`
- [ ] `git rm .`
- [ ] `git reset HEAD`
- [ ] `git checkout .`

#### Q88. What information do Git reflogs (reference logs) store?

- [ ] shell script pointers and keychain credentials
- [x] updates to branch tips and other references in the local repository
- [ ] release notes and hook script values
- [ ] tag and versioning information

#### Q89. You have just completed rebasing your master branch and need to manually update the remote master, even though there is a merge conflict. How can you accomplish this?

- [ ] `git push --overwrite`
- [ ] `git push --update`
- [ ] `git push --assert`
- [x] `git push --force-with-lease`

#### Q90. What is the difference between `git fetch` and `git pull`

- [ ] `git fetch` creates a new branch off the master branch, while `git pull` creates a new branch off the local repository's master branch.
- [ ] `git pull` downloads new data from a remote repository without integrating it into local files, while `git fetch` updates the current HEAD branch with the latest changes from the remote server.
- [x] `git fetch` updates remote tracking branches with changes from a remote repository, while `git pull` updates remote tracking branches with changes from a remote repository and merges them into their corresponding local branches.
- [ ] `git fetch` downloads and merges data from the local repository, while `git pull` informs your colleagues you are about to make changes to the master branch.

#### Q91. What command displays the difference between the working tree and the stage/index area, as well as files not tracked by Git?

- [ ] `git current`
- [x] `git status`
- [ ] `git local`
- [ ] `git context`

#### Q92. You would like to restore some previously stashed work to a new branch. How can you do that?

- [ ] Use `git branch <stash hash>`.
- [ ] Add the stashed commits to the current commit, then create a new branch.
- [ ] Use `git checkout -b`.
- [x] Run `git stash branch <branch name>`.

[reference here](https://stackoverflow.com/questions/6925099/git-stash-changes-apply-to-new-branch)

#### Q93. What is the difference between git branch -d and git branch -D?

- [ ] -D deletes the local branch, while -d deletes the branch regardless of push and merge status.
- [ ] -d deletes the current commit head, while -D deletes the entire branch.
- [x] -d deletes the local branch, while -D deletes the local branch regardless of push and merge status.
- [ ] -D deletes the current commit head, while -d deletes the entire branch.

#### Q94. You stashed three sets of changes but cannot remember the contents of the first stash entry. What command would you use to see the details of the changes in the first of the three stash entries?

- [x] git stash show -p stash@{2}
- [ ] git stash list
- [ ] git stash show -p stash@{1}
- [ ] git stash show -p

[reference here](https://stackoverflow.com/questions/10725729/see-whats-in-a-stash-without-applying-it)

#### Q95. How would you delete a remote branch in your repository?

- [ ] Use `git --delete <branch_name>`.
- [ ] Use `git push <remote_name> --d <branch_name>`.
- [ ] Use `git push <remote_name> --D`.
- [x] Use `git push <remote_name> --delete <branch_name>`.

[reference here](https://stackoverflow.com/questions/2003505/how-do-i-delete-a-git-branch-locally-and-remotely)

#### Q96. What is the default setting of `git reflog` when no subcommands are specified?

- [ ] delete
- [ ] expire
- [x] show
- [ ] update

[reference here](https://git-scm.com/docs/git-reflog)

#### Q97. How does the `-p` option change the behavior of the `git add` command

- [ ] It causes tracked files in the parent directory to be included in the staged files.
- [x] It allows developers to interactively choose which changes to tracked files are staged and outputs the differences for review.
- [ ] It automatically pushes changes to the corresponding branch on the remote repository.
- [ ] It allows developers to interactively choose which files are committed and outputs the differences for review.

[reference here](https://git-scm.com/docs/git-add#Documentation/git-add.txt--p)

#### Q98. After checking out a specific commit, you receive a warning message indicating You are in 'detached HEAD' state. What is Git warning you of?

- [x] You are not working on the most recent commit of a branch.
- [ ] A teammate has flagged the code with an issue.
- [ ] The commit does not have a parent.
- [ ] The branch has not been pushed to the remote repository.

[reference here](https://www.git-tower.com/learn/git/faq/detached-head-when-checkout-commit)

#### Q99. After accidentally deleting a branch in your local repository, how can you recover it?

- [ ] It cannot be recovered.
- [ ] Find the hash of the branch with the `log` command, then execute `git checkout -b <branchname> <hash>`.
- [x] Find the hash of the branch with the `reflog` command, then execute `git checkout -b <branchname> <hash>`.
- [ ] Execute `git checkout -b <branchname>`.

[Reference](https://stackoverflow.com/questions/1992364/git-recover-deleted-remote-branch)

#### Q100. How would you display a histogram showing inserts, deletion, and modifications per file for a specific commit along with its general commit information?

- [ ] Use `git stat`.
- [ ] Use `git debug --prettyprint`.
- [ ] Query the remote repository with the commit hash.
- [x] Use `git show <commit> --stat`.

[Reference](https://git-scm.com/docs/git-show#Documentation/git-show.txt---statltwidthgtltname-widthgtltcountgt)

#### Q101. What features do repository managers such as GitHub provide beyond Git?

- [ ] Repository managers are proprietary versions of Git that do not include enhanced features.
- [ ] Repository managers provide an enhanced command-line tool that is used to manage multiple local repositories.
- [x] Repository managers provide an online service for hosting Git repositories that include collaboration features such as pull requests, issue tracking, and peer reviews.
- [ ] Repository managers distribute repositories across multiple locations on a user's workstation, providing redundant storage that allows for quick backup and recovery.

[reference](https://www.theserverside.com/video/Git-vs-GitHub-What-is-the-difference-between-them)

#### Q102. What command finds the HEAD of the current branch?

- [ ] `git head --verify`
- [ ] `git log --head`
- [ ] `git hash --head`
- [x] `git show-ref --head`

[reference](https://git-scm.com/docs/git-show-ref)

#### Q103. When Git Workflows contain a long-running branch, what purpose does the long-running branch serve?

- [ ] Long-running branches store unstable code until it os peer reviewed for integration into a feature branch.
- [ ] Long-running branches correspond to agile sprints and are used to store related to features developed in the sprint.
- [ ] Long-running branches contain code related to experimental feature development that is merged into short-lived branches such as master.
- [x] Long-running branches correspond to different stages of development and are always open for topic/feature branches to be pulled into.

#### Q104. What command takes changes from the master branch on the remote repository origin and merges then to the local checked-out branch?

- [ ] `git commit -u origin`
- [ ] `git checkout origin`
- [x] `git pull origin master`
- [ ] `git push origin master`

#### Q105. While pushing changes to a remote repository, you receive the following message. How do you resolve this issue?

```bash
error: failed to push some refs to 'https://github.com/myrepo/simple.git'
hint: Updates were rejected because the remote contains work that you do not hint: not have locally.
```

- [ ] Use the --atomic option with the push command.
- [x] Execute a pull, then resolve any merge conflicts and execute another push.
- [ ] Execute a fetch, then execute another push.
- [ ] Use the --force option with the push command.

#### Q106. What does the -p option add to the output of the `git log` command?

- [x] It adds patch output that shows the differences introduced in each commit.
- [ ] It adds patch output that shows a summary listing modified files.
- [ ] It adds padding to the output and displays a histogram showing the number of lines changed in each commit.
- [ ] It adds the full commit message and notes associated with each commit.

#### Q107. What is the staging area or index?

- [ ] an area that stores commits prior to them being pushed to the remote repository
- [ ] an area containing stash entries that can applied to the working files
- [ ] an area where changes from a branch in the remote repository are stored before they are applied to a local branch
- [x] an area that stores information about changes that will be included in the next commit

#### Q108. What command would you use to stage changes to the index strictly for properties files in the current directory?

- [x] `git add *.properties`
- [ ] `git add %.properties`
- [ ] `git add .properties`
- [ ] `git add properties`

#### Q109. What are untracked files?

- [ ] files in the local repository that have not been merged into the master branch
- [ ] staged files that Git does not know about because the have not been committed
- [x] files in the working directory that Git does not know about because the have not been staged or committed
- [ ] files in the remote repository that Git does not know about because they have not been tagged

#### Q110. What type of Git hook could be used to validate that a commit message contains a ticket number?

- [ ] pre-commit
- [x] commit-msg
- [ ] applypatch-msg
- [ ] prepare-commit-msg

#### Q111. What is the difference between git stash pop and git stash apply?

- [ ] git stash pop pushes the topmost commit to the current branch, while git stash apply caches the last commit in the current branch.
- [x] git stash pop applies the topmost entry in the stash to the working files and removes it from the stash, while git stash apply applies the topmost entry in the stash to the working files but leaves it in the stash.
- [ ] git stash pop merges the topmost commit to the current branch, while git stash apply merges the last commit in the current branch.
- [ ] git stash pop applies the topmost entry in the stash to the working files but leaves it in the stash, while git stash apply applies the topmost entry in the stash to the working files and removes it from the stash.

#### Q112. After making some major changes to your code, you are a little nervous about committing. What command would you use to review the commit prior to making it?

- [ ] git commit --verify
- [ ] git notes show
- [ ] git commit preview
- [x] git commit --dry-run

#### Q113. What statement best describes Git's concept of HEAD?

- [ ] a pointer to the most recently changed file in the stage/index
- [ ] a pointer to the master branch
- [x] a pointer to the most recent commit in the currently checked-out branch
- [ ] a pointer to where the repository is stored in memory

#### Q114. After staging changes to several files, you realize the changes to the config.properties file are incorrect, and need to be removed from the stage and working directory. What command can you use to remove the staged changes to the file?

- [ ] git reset HEAD^ -- config.properties
- [ ] git rm config.properties
- [ ] git rf config.properties
- [x] git checkout HEAD -- config.properties

#### Q115. After a recent release with a stack trace, an issue is create that indicates the problem is with a newly added configuration property named MaxConnections. What command can find all commits that add or remove the string MaxConnections?

- [ ] - git grep -a "MaxConnections"
- [ ] - git log --search-string "MaxConnections"
- [x] - git log -S "MaxConnections"
- [ ] - git commit --with "MaxConnections"

#### Q116. Your company has moved its remote repository to GitHub at this location: https://github.com/yourcompany/core-api.git. What command updates the remote repository, named origin, to point to the new remote repository at this location?

- [ ] - git remote create-update origin https://github.com/yourcompany/core-api.git
- [ ] - git remote update origin https://github.com/yourcompany/core-api.git
- [x] - git remote set-url origin https://github.com/yourcompany/core-api.git
- [ ] - git remote add https://github.com/yourcompany/core-api.git

#### Q117. When is the cherry-pick command used?

- [x] - when a commit from one branch needs to be copied into another branch
- [ ] - when the HEAD needs to be reset to a specific commit
- [ ] - when a specific commit needs to be pulled down from the remote repository
- [ ] - when a hook script needs to be invoked

#### Q118. How would you describe a forked repository?

- [ ] - a deleted or archived copy of a repository
- [ ] - a beta release branch of a repository
- [ ] - a future branch of a repository
- [x] - a separate copy of a repository

[reference](https://stackoverflow.com/a/9339460/1573267)

#### Q119. How can you exclude untracked files within the working directory from a Git repository?

- [ ] - You cannot exclude the files from the repository.
- [ ] - Tag the files with excluded.
- [x] - Add a pattern matching the files to the .gitignore file.
- [ ] - Add the files to the omitted branch

[reference](https://git-scm.com/docs/gitignore)

#### Q120. What command creates a near-exact copy of the entire repository from a server?

- [ ] `git checkout <url>`
- [ ] `git pull <url>`
- [x] `git clone <url>`
- [ ] `git replicate <url>`

#### Q121. What would happen if you ran the `git reset testfile.js` command?

- [ ] testfile.js would be reverted to a blank file.
- [ ] testfile.js would be reset to its first saved state.
- [x] testfile.js would be reverted to its last saved copy.
- [ ] testfile.js would be removed from the stage/index area, if present.

#### Q122. What situation can occur when attempting to combine branches containing changes to the same piece of code?

- [ ] lost code
- [ ] automatic override
- [ ] collisions
- [x] merge conflict

#### Q123. When Git workflows contain a topic branch, what purpose does the topic branch serve?

- [ ] Topic branches store unstable code until it is peer reviewed for integration into another feature branch. <url>
- [x] Topic branches correspond to different stages of development and are always open for long-running branches to be pulled into. <url>
- [ ] Topic branches are used in waterfall development methodologies to track the state of the code during the various stages of waterfall. <url>
- [ ] Topic branches are short-lived branches used to store work related to a particular feature. <url>

#### Q124. What practice can help reduce the chances of encountering a merge conflict?

- [ ] Provide detailed commit messages that describe the changes being introduced by the commit. <url>
- [ ] make large commits that introduce multiple features. <url>
- [x] Keep local repository branches in sync with upstream branches in the remote repository by committing,pushing and pulling frequently. <url>
- [ ] Avoid frequent interaction with the remote repository to reduce the probability of pulling conflicts. <url>

#### Q125. You have changed your mind about adding broccoli to your project. How should you remove it?

```bash
Untracked files:
  (use "git add <file>..." to include in what will be committed)
  brccoli
```

- [x] `git remove broccoli`
- [ ] `git clean -f`
- [ ] `git clean`
- [ ] `git remove .`

#### Q126. What command can you use to remove untracked files from the working directory?

- [ ] `git rm -all`
- [ ] `git rm --cached`
- [x] `git clean -d -f`
- [ ] `git checkout`

#### Q127. After making a commit, you notice that you forgot to include changes to the doge.txt file. What command or commands would you use to add the changes to the commit ?

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

#### Q128. Which command would remove a file named wrongfile from the current branch of a repository, the index, and working files?

- [ ] ⠀

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
- [x] ⠀

```bash
  git rm --cached wrongfile
  git commit -m "Removed file"
```

#### Q129. What is the best way to report a bug to a GitHub project?

- [ ] Send an email to a project owner.
- [ ] I don't bother reporting software bugs because there's no transparency and they never get fixed anyway.
- [x] Search for the bug in the project's existing issues and create a new one if it hasn't been reported yet.
- [ ] Use git search -diff to compare all commits in your repository history.

Explanation: A project's issues are visible to anyone who has access to the project, so you may find a resolution is already planned or available. Otherwise, you can create and track the issue yourself.

#### Q130. Suppose you have created a bug fix on a new branch and want it to become part of the next production build generated from the main branch. What should you do next?

- [ ] Copy your branch changes and commit them directly to the main branch.
- [x] Create a pull request to merge your new branch into the main branch.
- [ ] On second thought, maybe I won't share this fix. I'll just put it in my own private version of the source code.
- [ ] Use git bisect to compare the buggy commit to an early commit that works as expected.

Explanation: Pull requests are the correct way to communicate that commits are ready for review and ultimate inclusion on the main branch.

#### Q131. Which command would remove a file named wrongfile from the current branch of a repository, the index, and working files?

- [x] Fork the project's repository to your GitHub account, clone the forked repository to your local machine, push changes to your repository, and submit a pull request to the target (upstream) repository.
- [ ] Clone the project to your local machine and push updates directly to the project repository.
- [ ] Use git commands to make a copy of the project so that you can work locally. Submit an issue to get your changes into the target repository.
- [ ] Use git show push-notifications

Explanation: GitHub provides forking functionality designed to allow you to work with projects where you aren't an owner or don't have write access. Forking makes a remote copy of the project in your repository that you can then clone locally. To submit updates to the target repository (upstream repository) you can submit a pull request.

#### Q132. What is GitHub?

- [ ] version control
- [x] A hosting platform for Git repositories
- [ ] for keeping images
- [ ] for social networking

Explanation: GitHub is a popular hosting platform for developers to store their Git repositories and collaborate with other developers all around the world.

#### Q133. Which statement is true of the git push command?

- [x] By default, a push doesn’t send tags to the remote repository.
- [ ] Only annotated tags are automatically pushed to the remote repository with a commit.
- [ ] Tags are pushed to the remote repository with their respective commits.
- [ ] Commits can be tagged only when they are created.

#### Q134. Git Pull is a combination of?

- [ ] Add and commit.
- [ ] branch and checkout.
- [x] fetch and merge.
- [ ] None of these.

#### Q135. What is the command to set the user email for the current repository?

- [ ] git email.user
- [x] git config user.email
- [ ] git config email
- [ ] All of the above.
