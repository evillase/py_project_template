# shellcheck shell=bash
## bash script when entering conda virtual env

# install pyproject environment and project
if [ -n "$(type -P poetry)" ]; then
  poetry install
else
  echo "Error: No poetry here."
fi

# update shell
hash -r

# install pre-commit hooks
# shellcheck disable=SC2154 # variables exist in environment
if [ -n "$git_root" ]; then
  if [ -n "$(type -P pre-commit)" ]; then
    if [ ! -e "$git_root/.git/hooks/commit-msg" ]; then
      pre-commit install -t commit-msg
    fi
    if [ ! -e "$git_root/.git/hooks/pre-commit" ]; then
      pre-commit install -t pre-commit
    fi
  fi
fi
