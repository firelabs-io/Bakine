import os

def ensure_gitignore_has_bk(path='.'):
    git_path = os.path.join(path, '.git')
    if not os.path.isdir(git_path):
        return

    gitignore_path = os.path.join(path, '.gitignore')
    if not os.path.exists(gitignore_path):
        with open(gitignore_path, 'w') as f:
            f.write('*.bk\n')
        return

    with open(gitignore_path, 'r') as f:
        lines = f.read().splitlines()

    if '*.bk' not in lines:
        with open(gitignore_path, 'a') as f:
            f.write('\n*.bk\n')
        
ensure_gitignore_has_bk()
FILE_EXT = '.BK'
SECRETS = {}
class key:
    def __init__(self, keyn):
        self.key = SECRETS[keyn]
    def __str__(self, ind=0):
        print(f"\nERROR: ATTEMPT LEAK KEY <{self.__class__.__name__} at {hex(id(self))}>")
        exit(1)
with open('main' + FILE_EXT, 'r') as f:
    for l in f:
        sep = l.index(':')
        SECRETS[l[:sep]] = l[sep+1:-1]
