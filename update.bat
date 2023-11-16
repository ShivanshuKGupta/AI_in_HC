@REM This script is for updating any changes to the git repo
@REM Change the below name with your branch name
@echo off
set branchName=testbranch
echo %branchName%
echo "Before running this script make sure that you have a branch named %branchName% and have all your changes commited only in that branch."
@echo on
git checkout %branchName%
git add .
git commit
git checkout main
git pull origin main
git merge %branchName%
git push -u origin main
git branch -d %branchName% 
git branch %branchName% 
git checkout %branchName%

@REM For any kind of conflict in merging you need to manage it manually.
