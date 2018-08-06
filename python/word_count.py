import jieba

ret = open('kkbox_top50.txt', "r" , encoding="utf8").read()
seglist = jieba.cut(ret, cut_all=False)

import json
hash = {}
for item in seglist: 
    print(item)
    if item in hash:
        hash[item] += 1
    else:
        hash[item] = 1
json.dump(hash,open("count_kkbox.json","w"))
print(hash)

fd = open("count_kkbox.csv","w")
fd.write("word,count\n")
for k in hash:
    fd.write("%s,%d\n"%(k,hash[k]))

