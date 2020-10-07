from itertools import groupby

list_= [1,1,2,2,4,4,8,8,16,16,32,32,]

print([list(j) for i, j in groupby(list_)])
