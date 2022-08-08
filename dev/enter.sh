# shellcheck shell=bash
if [ -e "$PWD/poetry.lock" ] && [ -n "$(type -P poetry)" ] && [ -z "$(type -P pre-commit)" ]; then
  if poetry install; then
    poetry update
  fi
elif [ -n "$(type -P poetry)" ] && [ -z "$(type -P pre-commit)" ]; then
  poetry update
fi
hash -r

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
