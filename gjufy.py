def find_substring(s1,s2):
    res = ""
    for i in range (len(s1)):
        for j in range (i, len(s1)):
            sub = s1[i : j + 1]
            if sub in s2 and len (sub) > len (res):
                res=sub
    return res