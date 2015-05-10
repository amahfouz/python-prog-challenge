'''
Created on Aug 15, 2014

@author: amahfouz

'''
def read_ints():
    return map(int, raw_input().strip().split(" "))

def list_to_dict(l):
    dict = {}
    for i in l:
        entry = dict.get(i)
        if (entry == None):
            dict[i] = 1
        else:
            dict[i] = dict[i] + 1
            
    return dict

n = int(raw_input())
a = read_ints()
 
m = int(raw_input())
b = read_ints()
 
adict = list_to_dict(a)
bdict = list_to_dict(b)

# diff the dicts

result = []
for k in bdict.keys():
    orig = bdict[k]
    if (orig != adict.get(k)):
        result.append(k)
        
for r in sorted(result): print r,        