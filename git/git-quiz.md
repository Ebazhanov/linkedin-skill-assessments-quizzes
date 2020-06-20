Git Assessment
--------------

#### Q1. How can you check your current git version?
- `git --v`
- `git --version` // Correct
- `git --option`
- `git --current`

#### Q2. What command lets you create a connection between a local and remote repository?
- `git remote add new`
- `git remote add origin` // Correct
- `git remote new origin`
- `git remote origin`

#### Q3. Describe what the following git commands do to the commit history.

`git reset --hard HEAD~5` (Reset the current branch to the commit just before the last 5)

`git merge --squash HEAD@{1}` (HEAD@{1} is where the branch was just before the previous command.
                               # This command sets the state of the index to be as it would just
                               # after a merge from that commit)

- Reset the HEAD to the 5th commit in the repo, then merges to the master branch
- Reset the commit branch back before the last 5 commits, then squashes them into a single commit <<--Correct
- Delete the last 5 commits
- Merges the last 5 commits into a new branch

#### Q4. Your current project has several branches; master, beta, and push-notifications. You've just finished the notification feature in the push-notification branch, and you want to commit it to beta branch. How can you accomplish this?
- Checkout the push-notifications branch and run git merge beta
- Checkout the master branch and run git merge beta -> push-notification
- Delete the push-notification branch and it will be committed to the master branch automatically
- Checkout the beta branch and run git merge push-notification <<--- Correct

#### Q5. Which of the following is true you when you use the following command?
`git add -A`
- All new and updated files are staged
- Files are staged in alphabetical order.
- All new files are staged << -- Correct
- Only updated files are staged

#### Q6. What will the following command print to the Terminal?
`git remote -v`
- A list of remote repositories you are connected to <<<--- Correct
- The current git version you're running
- An inline editor for modifying remote repositories
- The last 5 git versions you've installed

#### Q7. Looking at the following commands, describe what is happening.
`git checkout feature-user-location`
`git cherry-pick {kj2342134sdf090093f0sdgasdf99sdfo992mmmf9921231}`
- The commit is being tagged for release on the feature-user-location-branch.
- A commit is being copied from its original branch over to the feature-user-location-branch
- The commit is being cherry picked as the new HEAD of the commit history <<<--- Correct
- A commit is being copies from the feature-user-location branch to the master branch

#### Q8. What does the following command do to the git repository?
`git reset --soft HEAD^`
- Delete all previous commits and reset the repository history back to its initial state.
- Resets the working branch to the first commit.
- Keeps the HEAD at the current commit, but clears all previous commits.
- Undoes the last commit in the working branch and sets the HEAD back one commit. <<<--- Correct

#### Q9. You find a bug in your project, but can't locate where it was introduced in the commit history. How would you diagnose this problem?
- Manually backtrack through your commit history.
- Use git search -diff to compare all commits in your repository history.
- Run a git rebase to find the buggy commit.
- Use git bisect to compare the buggy commit to an early commit that works as expected. <<<<---Correct

#### Q10. Why would the following command be used?
`git rebase -i HEAD~10`
- To run a comparative search of the last 10 commits for differences
- To list the last 10 commits and modify them with either the squash or fixup command <<<---Correct
- To delete the last 10 commits and reset the HEAD
- In order to locally cache the last 10 commits

#### Q11. Why would you use a pre-receive hook in your remote repository?
- You wouldn't, you would use it in the local repository
- To invoke a hook script when commits are pushed but before any references are updated <<<---Correct
- To fire a script after updates are made to the remote repository
- To debug all commit tags and release versions

#### Q12. What option can you use to apply git configurations across your entire git environment?
- `--all`
- `--master`
- `--global` // Correct
- `--update`

#### Q13. How could you squash multiple commits together without using git merge --squash?
- Caching
- You can't. git merge --squash is the only git command for that operation
- Rebasing <<<<---Correct
- Reflogging

#### Q14. If you cloned an existing git repository, what would happen?
- A new copy would overwrite the central repository
- A copy of the repository would be created on your local machine <<<<---Correct
- Nothing, cloning is not a supported git function
- A copy of the repository would be created on the hosting platform

#### Q15. Suppose you needed to see a list of all files that had been modified or added to a specific commit over the course of a project. How would you accomplish this?
- Find the commit in the remote repository, as that's the only place that kind of information is stored.
- Use the diff-tree command with the commit hash. <<<<---Correct
- Run git commit --info with the commit hash.
- Access the commit stash data with git stash.

#### Q16. What files is the following .gitignore programmed to leave out?
- All files with a .swift, .txt, or metadata file extension, as well as the entire build directory <<<---Correct
- Only the build directory
- All files in the build directory, as well as files ending with .txt or .metadata
- Only files with .swift and .txt extensions.

#### Q17. After you make changes to a tracked file, you run the following command. What will this do?
`git commit -a -m "Refactor code base`
- Nothing, you can't use multiple options in the same command
- Adds all new files to the staging area
- Commits all new files with a message
- Add all modified files to the staging area, then commits them with a message <<<---Correct

#### Q18. After checking your git status you get the following output, which shows the file beta-notes.js in the commit but also unstaged. How can this situation occur?
`Change to be committed:
(use "git reset HEAD <file>..." to unstage)
modified: beta-notes.js 
Changes not staged for commit:
(use "git add <file>..." to update what will be committed)
(use "git checkout --<file>..." to discard changes in working directory)
modified: beta-notes.js`
- There were two copies of beta-notes.js but one was deleted.
- beta notes.js was staged, then modified afterwards, creating two different versions of the file <<<---Correct
- Two copies of beta-notes.js were created, but only one is being tracked
- There are two tracked copies of beta-notes.js, but one was removed from the commit.

#### Q19. Where are files stored before they are committed to the local repository?
- Saved files
- git documents
- Staging area <<< ---Correct
- git cache

#### Q20. Which statement is true with **git push** command
- All tags are pushed to the remote

#### Q21. Which command would you use to force an overwrite of your local files with the master branch:
- git fetch --all; git reset --hard origin/master  <<< ---Correct
- git pull origin master; git reset --hard origin/myCurrentBranch
- git pull --all; git reset --hard origin/master
- git pull -u origin master; git reset --hard master

#### Q22. Which statement is true when you use the **git add -A** command?
- Only new files in the working directory are staged to the index.
- All new and updated files from the working directory are staged to the index. <<< ---Correct
- All files in the working directory are staged to the index in alphabetical order.
- Only updated files in the working directory are staged to the index.

#### Q23. Describe what is happening given these commands:
git checkout feature-user-location
git cherry-pick {123safd23e}
- The commit is being tagged for release on the feature-user-location branch.
- A commit is being copied from the feature-user-location branch to the master branch.
- The commit is being cherry-picked as new HEAD of the commit history.
- The branch is switched to the feature-user-location branch, and the specified commit is applied to the branch. <<< ---Correct

#### Q24. You find that your project has a tag and branch both named push-notifications, which causes confusion when trying to print out given reference. How can you specify which branch you want to look at?
- use git  show ref/push-notifications
- use git show push-notifications
- use git show head/refs/push-notifications << ---- chose thise one not sure though!
- use git show refs/head/push-notifications
