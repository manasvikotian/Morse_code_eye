def checkKey(lang, key):
    if key in lang.keys():
        print('value = ', lang[key])
    else:
        print('not present')     
lang={'01':'A', '1000':'B', '1010':'C', '100':'D', '0':'E', '0010':'F', '110':'G', '0000':'H', '00':'I', '0111':'J', '101':'K', '0100':'L', '11':'M', '10':'N', '111':'O', '0110':'P', '1101':'Q', '010':'R', '000':'S', '1':'T', '001':'U', '0001':'V', '011':'W', '1001':'X', '1011':'Y', '1100':'Z'}
ar= '0'
ar1='1'
ar2='B'
ar3='0'
ar4='B'
ar=ar+ar1+ar2+ar3+ar4
print(ar)
import array
arr = [None]*0
arr = ar.split('B')
key=arr[0]
print(key)
checkKey(lang, key)
print(arr)


