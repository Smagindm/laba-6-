def longest_common_substring(s1, s2):
    max_len = 0
    start_idx = 0
len1 = len(s1)
len2 = len(s2)

for i in range(len1):
for j in range(len2):
k = 0
while (i + k < len1) and (j + k < len2) and (s1[i + k] == s2[j + k]):
k += 1

if k > max_len:
max_len = k
start_idx = i

result = ""
for i in range(max_len):
result += s1[start_idx + i]

return result