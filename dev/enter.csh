#
## tcsh/csh script when entering conda virtual env

# install pyproject environemnt and project
if ( "`where poetry`" != "" ) then
  poetry install
else
  echo "Error: No poetry here."
endif

# update shell
rehash

# install pre-commit hooks
if ( $?git_root ) then
  if ( "`where pre-commit`" != "" ) then
    if ( ! -e "$git_root/.git/hooks/commit-msg" ) then
      pre-commit install -t commit-msg
    endif
    if ( ! -e "$git_root/.git/hooks/pre-commit" ) then
      pre-commit install -t pre-commit
    endif
  else
  endif
endif
