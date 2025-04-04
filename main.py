from build import key
def do(smt):
    if smt.key == key('USER_KEY').key:
        print("loged as admin")
        return 1
    else:
        print("loged as normal user")
        return 0
if __name__ == '__main__':
    KEY = key('USER_KEY')
    result = do(KEY)
    print(result, KEY)