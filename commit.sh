#!/bin/bash
# 커밋 자동화 스크립트

status=($(git status --porcelain | awk '{print $2}' | head -n 3))
GIT=$(which git)

for stat in ${status[@]}
do
  if [[ -z $(echo ${stat} | grep "algorithm") ]]
  then
    continue
  fi

if [[ ! -e ${stat} ]]
then
  echo "${stat} File not Found"
  exit 1
fi

# Get Commit Message
commitMsg=$(find ${stat} -iname "*.py" -exec bash -c "cat {}" \; | head -n 3 | grep "[가-힣ㄱ-ㅎ]")

# Git Commit
${GIT} add -A
${GIT} status
${GIT} commit -m "'${commitMsg}'"
done

${GIT} push -u origin main
echo "${stat} Commit Done"
