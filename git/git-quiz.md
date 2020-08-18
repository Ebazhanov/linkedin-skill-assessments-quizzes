## Git Assessment

#### Q1. How can you check your current git version?

- [ ] `git --v`
- [x] `git --version`
- [ ] `git --option`
- [ ] `git --current`

#### Q2. What command lets you create a connection between a local and remote repository?

- [ ] `git remote add new`
- [x] `git remote add origin`
- [ ] `git remote new origin`
- [ ] `git remote origin`

#### Q3. Describe what the following git commands do to the commit history.

`git reset --hard HEAD~5`
(Reset the current branch to the commit just before the last 5)

`git merge --squash HEAD@{1}`
(HEAD@{1} is where the branch was just before the previous command. This command sets the state of the index to be as it would just after a merge from that commit)

- [ ] Reset the HEAD to the 5th commit in the repo, then merges to the master branch
- [x] Reset the commit branch back before the last 5 commits, then squashes them into a single commit
- [ ] Delete the last 5 commits
- [ ] Merges the last 5 commits into a new branch

#### Q4. Your current project has several branches; master, beta, and push-notifications. You've just finished the notification feature in the push-notification branch, and you want to commit it to beta branch. How can you accomplish this?

- [ ] Checkout the push-notifications branch and run git merge beta
- [ ] Checkout the master branch and run git merge beta -> push-notification
- [ ] Delete the push-notification branch and it will be committed to the master branch automatically
- [x] Checkout the beta branch and run git merge push-notification

#### Q5. Which of the following is true you when you use the following command?

`git add -A`

- [ ] All new and updated files are staged
- [ ] Files are staged in alphabetical order.
- [x] All new files are staged
- [ ] Only updated files are staged

#### Q6. What will the following command print to the Terminal?

`git remote -v`

- [x] A list of remote repositories you are connected to
- [ ] The current git version you're running
- [ ] An inline editor for modifying remote repositories
- [ ] The last 5 git versions you've installed

#### Q7. Looking at the following commands, describe what is happening.

`git checkout feature-user-location`
`git cherry-pick {kj2342134sdf090093f0sdgasdf99sdfo992mmmf9921231}`

- [ ] The commit is being tagged for release on the feature-user-location-branch.
- [ ] A commit is being copied from its original branch over to the feature-user-location-branch
- [x] The commit is being cherry picked as the new HEAD of the commit history
- [ ] A commit is being copies from the feature-user-location branch to the master branch

#### Q8. What does the following command do to the git repository?

`git reset --soft HEAD^`

- [ ] Delete all previous commits and reset the repository history back to its initial state.
- [ ] Resets the working branch to the first commit.
- [ ] Keeps the HEAD at the current commit, but clears all previous commits.
- [x] Undoes the last commit in the working branch and sets the HEAD back one commit.

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
- [x] To execute a script when a remote receives a push that is triggered
  before any refs are updated
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

#### Q15. Suppose you needed to see a list of all files that had been modified or added to a specific commit over the course of a project. How would you accomplish this?
- [ ] Find the commit in the remote repository, as that's the only place that kind of information is stored.
- [x] Use the diff-tree command with the commit hash.
- [ ] Run git commit --info with the commit hash.
- [ ] Access the commit stash data with git stash.

#### Q16. What files is the following .gitignore programmed to leave out?
- [x] All files with a .swift, .txt, or metadata file extension, as well as the entire build directory
- [ ] Only the build directory
- [ ] All files in the build directory, as well as files ending with .txt or .metadata
- [ ] Only files with .swift and .txt extensions.

#### Q17. After you make changes to a tracked file, you run the following command. What will this do?

`git commit -a -m "Refactor code base`

- [ ] Nothing, you can't use multiple options in the same command
- [ ] Adds all new files to the staging area
- [ ] Commits all new files with a message
- [x] Add all modified files to the staging area, then commits them with a message

#### Q18. After checking your git status you get the following output, which shows the file beta-notes.js in the commit but also unstaged. How can this situation occur?

```
Change to be committed:

(use "git reset HEAD <file>..." to unstage)
modified: beta-notes.js
Changes not staged for commit:
(use "git add <file>..." to update what will be committed)
(use "git checkout --<file>..." to discard changes in working directory)

modified: beta-notes.js
```

- [ ] There were two copies of beta-notes.js but one was deleted.
- [x] beta notes.js was staged, then modified afterwards, creating two different versions of the file
- [ ] Two copies of beta-notes.js were created, but only one is being tracked
- [ ] There are two tracked copies of beta-notes.js, but one was removed from the commit.

#### Q19. Where are files stored before they are committed to the local repository?
- [ ] Saved files
- [ ] git documents
- [x] Staging area
- [ ] git cache

#### Q20. Which statement is true with git push command
- [ ] All tags are pushed to the remote

#### Q21. Which command would you use to force an overwrite of your local files with the master branch:
- [x] git fetch --all; git reset --hard origin/master
- [ ] git pull origin master; git reset --hard origin/myCurrentBranch
- [ ] git pull --all; git reset --hard origin/master
- [ ] git pull -u origin master; git reset --hard master

#### Q22. Which statement is true when you use the **git add -A** command?

- [ ] Only new files in the working directory are staged to the index.
- [x] All new and updated files from the working directory are staged to the index.
- [ ] All files in the working directory are staged to the index in alphabetical order.
- [ ] Only updated files in the working directory are staged to the index.

#### Q23. Describe what is happening given these commands:

```
git checkout feature-user-location
git cherry-pick {123safd23e}
```

- [ ] The commit is being tagged for release on the feature-user-location branch.
- [ ] A commit is being copied from the feature-user-location branch to the master branch.
- [ ] The commit is being cherry-picked as new HEAD of the commit history.
- [x] The branch is switched to the feature-user-location branch, and the specified commit is applied to the branch.

#### Q24. You find that your project has a tag and branch both named push-notifications, which causes confusion when trying to print out given reference. How can you specify which branch you want to look at?

- [ ] use git show ref/push-notifications
- [ ] use git show push-notifications
- [x] use git show head/refs/push-notifications <<--chose this one not sure though!
- [ ] use git show refs/head/push-notifications

#### Q25. Your team lead needs a list of all commits that will be moved before you perform a rebase. Which command can you use to access that information?
- [ ] git rebase -log
- [x] git rebase -i
- [ ] git rebase -verbose
- [ ] git rebase -all

#### Q26. What is the operation doing given the Git commands below?

```
$ git bisect start
$ git bisect bad 5d41402abc4b2a76b9719d911017c592
$ git bisect good 69faab6268350295550de7d587bc323d
```

- [ ] It runs a merge of a good commit that is discovered using a known bad commit and known good commit
- [ ] It marks a commit for deletion using a known bad commit and known good commit to determine which commit introduced a bug
- [ ] It defines a bad commit and resets the HEAD using a known bad commit and known good commit
- [x] It performs a binary search using a known bad commit and known good commit to determine which commit introduced a bug

#### Q27. In a situation where you have several commits for a single task, what is the most efficient way to restructure your commit history?

- [ ] Cherry pick the related commits to another branch.
- [ ] Delete the task commits and recommit with a new message.
- [x] Squash the related commits together into a single coherent commit.
- [ ] Stash the related commits under a new hash.

#### Q28. Which of the following is true of the git push command?

- [ ] By default a push doesn't send tags to the remote repository.
- [ ] Commits can only be tagged when they are created.
- [x] Tags are pushed to the remote repository with their respective commits.
- [ ] Only annotated tags are automatically pushed to the remote repository with a commit.

#### Q29. After pushing commits to the remote repository for the first time using the command below, what shorthand command can you use in future?
`
git push -u origin master
`

- [ ] git push master
- [ ] git push origin
- [ ] Same as before, git push -u origin master
- [x] git push

#### Q30. How would you create a custom shortcut or command across your git environment?

- [ ] Run git hotfix with the shortcut name.
- [ ] Assign a shortcut or command using git options file.
- [ ] Use the git custom-key command.
- [x] Create an alias in the git config file.

#### Q31. What is the status of the beta-notes.js file in the following output?

```
Changes not staged for commit:
(use "git add <file>..." to update what will be commited)
(use "git checkout -- <file>..." to discard changes in working directory)

modified:	beta-notes.js
```

- [ ] beta-notes.js is untracked and has been modified.
- [x] beta-notes.js is a tracked file and has been modified, but has not been added to the current commit.
- [ ] beta-notes.js is untracked but has been added to the current commit.
- [ ] beta-notes.js is tracked, and the modified file has been added to the current commit.

#### Q32. What command would let you modify your previous commit?

- [ ] --fix
- [ ] --quickfix
- [ ] --modify
- [x] --amend

#### Q33. What is the best way to characterize the git commit structure?

- [ ] Data array
- [x] Data log
- [ ] Data snapshot
- [ ] Data dictionary

#### Q34. What change will the following command make to the staging area files?

`
git rm --cached testfile.js
`

- [x] testfile.js will be removed from the staging area and its changes no longer tracked.
- [ ] testfile.js will be removed from the staging area but its changes will still be tracked. <
- [ ] A copy of testfile.js will be cached on your desktop.
- [ ] The current copy of testfile.js will be saved in the staging area.

#### Q35. After you've succesfully merged two branches and commited the changes, what is the next step in keeping your git structure organized?

- [ ] Use the git reset --soft HEAD to roll back one commit.
- [ ] Run git branch -d <branch name> to delete the merged branch.
- [ ] Use git clear-all to clean up any hanging files.
- [x] Run git rebase to move the current commit to its original location.

#### Q36. You're in the middle of modifying a file when you're unexpectedly assigned an urgent bug fix on another branch. What would you do to temporarily save the work your doing locally without commiting?

- [ ] You cannot save locally without commiting, so that is not possible.
- [ ] Run git hold to save a local copy of what you're doing to return to later.
- [ ] Save your work with git local-cache.
- [x] Use git stash to save your work and come back later and reapply the stashed commit.

#### Q37. What command would you use to create a new git repository?

- [ ] git add
- [ ] git start
- [ ] git new
- [x] git init

#### Q38. While working on a feature branch you try to use "git rerere" to solve a recurring merge conflict but nothing is happening. What could be causing this issue?

- [ ] The "-all" option isn't added to the command.
- [x] "rerere.enabled" isn't enable in the config file.
- [ ] The commit hash is missing.
- [ ] The filepath isn't specified.

#### Q39. What commands would you use to force an overwrite of your local files with the master branch?

- [ ] Option 1

```git
git pull --all
git reset --hard origin/master
```

- [ ] Option 2

```git
git pull -u origin master
git reset --hard master
```

- [] Option 3

```git
git pull origin master
git reset --hard origin/myCurrentBranch
```

- [x] Option 4

```git
git fetch --all
git reset --hard origin/master
```
#### Q40. While modifying a file, you're unexpectedly assigned an urgent bug fix on another branch. How can you temporarily save your local work without committing?

- [ ] Save your work with git local-cache.
- [x] Use git stash to save your work, then come back later and reapply the stashed commit.
- [ ] Run git hold to save a local copy of waht you're doing to return to later.
- [ ] This is not possible, as you cannot save locally without committing.

#### Q41. After staging a series of changes to the index, which command could you used to review prior to a commit.

- [ ] Save your work with git local-cache.
- [x] Use git stash to save your work, then come back later and reapply the stashed commit.
- [ ] Run git hold to save a local copy of waht you're doing to return to later.
- [ ] This is not possible, as you cannot save locally without committing.

#### Q42. Your current respository has three branches: master,beta and ousg-notifications. You've just finished the notification feature and commit the changes to the push-notification branch, and you want to include them in the beta branch. How can you acccomplish this?

- [x] Check out the master branch and run git merge beta -> push-notifications..
- [ ] Delete the push-notification branch;it will be committed to the mastre branch automatically.
- [ ] Check out the push-notifications branch and run git merge beta.
- [ ] Check out the beta branch and run git merge push-notifications.

#### Q43. You find that your project has a tag and branch both named push-notification,which causes confusion when trying to print out a given referance.How can you specify which branch you want to look at?

- [x] Use git show head/refs/push-notifications.
- [ ] Use git show push-notifications.
- [ ] Use git show refs/push-notifications.
- [ ] Use git show refs/head/push-notifications.

#### Q44. Which statement is true of the git push command?.

- [ ] Commits can be tagged only when they are created.
- [x] By default a push dosen't sent tags to the remote repository.
- [ ] Only annotated tags are automatically pushed to the remote repository with a commit.
- [ ] Tags are pushed to the remote repository with their respective commits.

#### Q45. How can you check your current Git version?

- [x] git --version
- [ ] git --options
- [ ] git --current
- [ ] git --v

#### Q46. Which setting determines what pager is used when Git pages output

- [ ] core.page
- [ ] page
- [ ] pager
- [x] core.pager

#### Q47. What does commit object contain?

- [ ] -
- [ ] A set of files, representing the state of a project at a given point of time.
- [ ] Referance to parent commit objects
- [x] An SHAI name, a 40 character string that uniquely identify the commit object.

#### Q48. Which option to git commit, will modify last commit message

- [ ] -replace
- [ ] -change
- [x] -amend
- [ ] -update

#### Q49. Which option is enables inclusion of commiter name in custom log format

- [ ] %ce
- [ ] %cr
- [ ] %cd
- [x] %cn

#### Q50. How many ways are present in Git to integrate changes from one branch into another

- [ ] 3.0
- [ ] 5.0
- [x] 2.0
- [ ] 4.0

#### Q51. Which user should be creating first during setting up of SSH

- [x] git
- [ ] admin
- [ ] root
- [ ] None of these

#### Q52. Which command will list tags with the 1.4.2 series

- [ ] git tag 'v1.4.2'
- [x] git tag -I 'v1.4.2.*'
- [ ] git tag-list 'v1.4.2*'
- [ ] git tag'v1.4.2*'

#### Q53. Which of the following is an integration manager

- [ ] lieutenants
- [x] benevolent dictator
- [ ] Depends upon project type
- [ ] Depends upon data

#### Q54. Which Git command begins tracking of a new file

- [x] add
- [ ] addfile
- [ ] begin
- [ ] track

#### Q55. Which of the following is called dumb protocol

- [ ] All of these
- [ ] SSH
- [ ] Git
- [x] HTTP

#### Q56. Which key press return a set of suggestions to pick from,  when writing a Git command

- [ ] Control
- [x] Shift
- [ ] Tab
- [ ] Alt

#### Q57. Which of these terms best describe Git

- [x] Distributed Version Control System
- [ ] Issue Tracking System
- [ ] Integrated Development Environment
- [ ] Web-Based Repository Hosting Service

#### Q58. Which command get a copy of an existing Git repository

- [ ] duplicate
- [ ] replicate
- [ ] copy
- [x] clone

#### Q59. How does Git thinks of its data

- [ ] File
- [ ] None of these
- [x] Snapshot
- [ ] Folder

#### Q60. Which option enables inclusion of author name in custom log format

- [ ] %am
- [ ] %ad
- [ ] %ae
- [x] %an

#### Q61. Which option enables inclusion of author name in custom log format

- [ ] %am
- [ ] %ad
- [ ] %ae
- [x] %an
#### Q62. Which version onwads did Git offered, revesting a file back to what it looked like when last committed

- [ ] 1.7
- [x] 1.6
- [ ] 2.0
- [ ] 1.8

#### Q63. which strategy is ued by Git for merging two branches 

- [ ] LIFO
- [x] recursive
- [ ] FIFO
- [ ] octopus

#### Q64. What does refs stores

- [x] SHA-1 value
- [ ] None of these
- [ ] Branch name
- [ ] Project name

#### Q65. What Language is used in GIT?

- [x] C
- [ ] C++
- [ ] C#
- [ ] Java

#### Q66. What is usually the extension of file which has the public key

- [ ] ssh
- [x] pub
- [ ] key
- [ ] pk
