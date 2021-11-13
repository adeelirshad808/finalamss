import re

f = open('test4.txt', 'r')
a = f.readlines()
mystr = ''.join([line.strip() for line in a])

b=re.sub("TTL => 'FOREVER'", "TTL => org.apache.hadoop.hbase.HConstants::FOREVER", mystr)
c=re.sub('Table', 'create', b)
d=re.sub('"', '', c)
e=re.sub('{NA', ',{NA', d)
#f=re.sub('^ is.ENABLED.+.*.+.COLUMN FAMILIES DESCRIPTION,', ', ', e)








print(e)
