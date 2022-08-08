if ( -e $PWD/poetry.lock && "`where poetry`" != "" && "`where pre-commit`" == "" ) then
  poetry install
  if ( $? ) then
    poetry update
  endif
else if ( "`where  poetry`" != "" && "`where pre-commit`" == "" ) then
  poetry update
endif
rehash

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
