#!/usr/bin/env bash
set -euxo pipefail

curl -v -L -n \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/luispintomartins/github-training/issues \
  -d '{"title":"Found a bug","body":"I'\''m having a problem with this."}'

#   -H "Authorization: Bearer <YOUR-TOKEN>" \
#   -d '{"title":"Found a bug","body":"I'\''m having a problem with this.","assignees":["octocat"],"milestone":1,"labels":["bug"]}'

