""" Created by Shahen Kosyan 2/14/17"""

if __name__ == '__main__':
    
    obfuscation = input()
    letters = 'abcdefghijklmnopqrstuvwxyz'
    
    obfuscation = list(obfuscation)
    letters = list(letters)
    
    i = len(obfuscation)
    posibility = 'NO'
    
    while i:
        if obfuscation[0] != letters[0]:
            posibility = 'NO'
            break
        else:
            while letters[0] in obfuscation:
                obfuscation.remove(letters[0])
                i -= 1
                if len(obfuscation) == 0:
                    posibility = 'YES'
                    break
            letters.remove(letters[0])

    print(posibility)
