from pwn import *
from struct import *
import re
import threading

def getPrefix(r):
    text = r.recv()
    text += r.recv()
    prefix = re.findall(r"with([^,]*),",text)
    prefix = prefix[0].strip(' ').replace(' ','')
    return prefix

r = remote('52.69.244.164',9003)
prefix = getPrefix(r)

last = 0
print prefix
while(last < 256**4):
    hash_str = prefix.decode('hex') + struct.pack(">I",last)
    aa = hashlib.sha1(hash_str).hexdigest()
    
    if aa[:6] == "000000":
        print last
        break
    last = last + 1
    
print hash_str.encode("hex")
print "end"

p = 195589859419604305972182309315916027436941011486827038011731627454673222943892428912238183097741291556130905026403820602489277325267966860236965344971798765628107804393049178848883490619438682809554522593445569865108465536075671326806730534242861732627383004696136244305728794347161769919436748766859796527723

#using pow.sage
#2 * 3^336 * 4759647095086827597559114855685975263112106458932414012998147177848303887783492510354911068366203455488902018600593880874117783509946030773587965941
q = 4759647095086827597559114855685975263112106458932414012998147177848303887783492510354911068366203455488902018600593880874117783509946030773587965941
x = pow(2,q,p)

r.sendline(hash_str + " " +str(x))
data = r.recvrepeat()
print data

result = 76330748508434302948911811389582581821991628856573396875939665491436112259216518385549428479486803046688716209647162112374160557281493613562434598038831198998785672154884963029434409475216631801204644290518567711052531985788274092047888219286448792676928521370001329553409713430110222435245961441435742296538
r.close()

#using pow.sage
#1053194137440650777245209179832422069277215965401386954507182362226896709188340544607528308817298833089231689626065710717
log = 1053194137440650777245209179832422069277215965401386954507182362226896709188340544607528308817298833089231689626065710717

print format(log, 'x').decode("hex")