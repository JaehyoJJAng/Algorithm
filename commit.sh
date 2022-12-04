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

if [[ ! -e ${status} ]]
then
  echo "${status} File not Found"
  exit 1
fi

# Get Commit Message
commitMsg=$(find ${stat} -iname "*.py" -exec bash -c "cat {}" \; | head -n 3 | grep "[가-힣ㄱ-ㅎ]")
echo ${commitMsg}

# Git Commit
${GIT} add -A
${GIT} status
${GIT} commit -m "'${commitMsg}'"
${GIT} push -u origin main
echo "${stat} Commit Done"
done

