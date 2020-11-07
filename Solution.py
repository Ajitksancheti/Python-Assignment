def getMaxDis(st, n):
    c = [0]*256
    for i in range(n):
        c[ord(st[i])] += 1
    mxd = 0
    for i in range(256):
        if c[i] != 0:
            mxd += 1
    return mxd


s = input()
n = len(s)
md = getMaxDis(s, n)
ans = n
for i in range(n):
    for j in range(n):
        sbs = s[i:j]
        sbl = len(sbs)
        sdc = getMaxDis(sbs, sbl)
        if sbl < ans and md == sdc:
            ans = sbl

print(ans)
