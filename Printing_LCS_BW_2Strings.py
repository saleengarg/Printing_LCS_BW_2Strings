def longest_common_subsequence(x,y,m,n):
    rows,cols=m+1,n+1
    t= [[0 for i in range(cols)] for j in range(rows)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                t[i][j]=0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i-1]==y[j-1]:
                t[i][j]=(1+t[i-1][j-1])
            else:
                t[i][j]=max(t[i-1][j],t[i][j-1])
    return t
def print_LCS(x,y,m,n):
    t=longest_common_subsequence(x,y,m,n)
    i,j=m,n
    s=""
    while(i>0 and j>0):
        if x[i-1]==y[j-1]:
            s+=x[i-1]
            i=i-1
            j=j-1
        else:
            if t[i][j-1]>t[i-1][j]:
                j=j-1
            else:
                i=i-1
    return s[-1::-1]



x,m="acbcf",5
y,n="abcdaf",6
res=print_LCS(x,y,m,n)
print(res)

##OUTPUT
abcf