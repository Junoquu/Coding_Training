keyborad={'fdsajkl;':'in-out',
          'jkl;fdsa':'in-out',
          'asdf;lkj':'out-in',
          ';lkjasdf':'out-in',
          'asdfjkl;':'stairs',
          ';lkjfdsa':'reverse'}

n=input()
if n in keyborad:
    print(keyborad[n])
else:
    print('molu')