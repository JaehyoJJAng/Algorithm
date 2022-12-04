#!/bin/bash
# 커밋 자동화 스크립트

status=$(git status --porcelain | awk '{print $2}' | head -n 1)
GIT=$(which git)

if [[ ! -e ${status} ]]
then
  echo "${status} File not Found"
  exit 1
fi

# Get Commit Message
commitMsg=$(find ${PWD} -iname "*.py" -exec bash -c "cat {}" \; | grep "[가-힣ㄱ-ㅎ]")

# Git Commit
${GIT} add -A
${GIT} status
${GIT} commit -m "'${commitMsg}'"
${GIT} push -u origin main 1>/dev/null 2>./commit_err.log

echo "${status} Commit Done"
