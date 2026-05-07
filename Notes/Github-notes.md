# Git and GitHub

1.To initialize a git repository we use
```
git init
```
2.To know the status of the files that are staged,unstaged or untracked
```
git status
```
3.To put all the files in staging area
```
git add .
```
4.To put Individual file in staging area
```
git add fileName
```
5.To commit the changes and save the files permanently in git history
```
git commit -m "message"
```
-m means provide a message

6.When you added the file to staging area and want to remove from staging area we use this command
```
git restore --staged filename
```
7.To see all the commits made in the history we use
```
git log
```
8.To delete a file
```
rm -rf filename
```
9.To remove changes that are made by moving current branch to a specific commit
```
git reset <filepath>
```
10.To create a separate structure for files that are in staging area that are not meant to be committed in the git history
```
git stash
```
11.To move the files that are in stash area to unstaged area
```
git stash pop
```
12.To clear the files in stash area we use
```
git stash clear
```
13.To connect remote repository to local repository
```
git remote add origin URL
```
14.To show URLs that are connected to the folder
```
git remote -v
```
15.To push the changes to the URL or remote repository
```
git push origin main
```
16.To download project file from github(When we fork other project files)
```
git clone URL
```
17.To create a New branch
```
git branch branchName
```
~ Always add new changes to separate branch and not to main branch while working on a project

18.To change the pointer to another branch which is pointing to main branch or other
```
git checkout branchName
```
~ Pull Request: A message sent to owner of the repository to combine the branch code into main code

19.To Force push we use(In case the git commits is behind the github commits)
```
git push origin main -f
```
20.To make forked project even with main project fetch all the commits. Then reset the main branch 
of origin to main branch of upstream(upstream refers to main project URL)
```
git fetch --all --prune
git reset --hard upstream/main
```
or we can use this command to make even with the main project code
```
git pull upstream main
```