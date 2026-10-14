def longest_common_substring(s1: str, s2: str) -> str:
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    for length in range(len(s1), 0, -1):
        for i in range(len(s1) - length + 1):
            sub = s1[i:i+length]
             if s2.find(sub) != -1:
                return sub
return ""
