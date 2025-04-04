# Bakine
Anti leak tool, Making your secrets safe
> [!NOTE]
> it still new, so please use it with caution

# how it works?
currently its just python libary, it works by defining an class (key) and file (where all secrets is), and using the class you may access the espefic key
it also automaically detects if is an .git and put *.bk into .gitignore to prevent keys to removed
it also dont break your code without *.bk as if dont exist it will be basically an placeholder

# feactures
- [X] auto run by just importing
- [X] somewhere stored
- [ ] become server (so it runs even if aplication ends)
- [ ] prevent git push if key exposed
- [ ] rewrite program to something else then python
