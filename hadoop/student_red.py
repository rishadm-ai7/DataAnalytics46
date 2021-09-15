#!/usr/bin/python3

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Q1:Total marks Scored by each student?
#
# import sys
# currentname=None
# currentmark=0
#
# for line in sys.stdin:
#     line=line.strip()
#     name,mark = line.split("\t")
#     mark = int(mark)
#
#     if currentname==name:
#         currentmark+=mark
#
#     else:
#         if currentname!=None :
#             print("%s\t%s"%(currentname,currentmark))
#         currentname = name
#         currentmark = mark
#
# print("%s\t%s"%(currentname,currentmark))


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Q2:Average marks Scored by each student?

import sys
currentname=None
currentmark=0
count=1

for line in sys.stdin:
    line=line.strip()
    name,mark = line.split("\t")
    mark = int(mark)

    if currentname==name:
        currentmark+=mark
        count+=1

    else:
        if currentname!=None :
            currentmark/=count
            print("%s\t%s"%(currentname,currentmark))
        currentname = name
        currentmark = mark
        count = 1

currentmark/=count
print("%s\t%s"%(currentname,currentmark))


