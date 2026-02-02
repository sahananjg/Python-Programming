import math
def GCS(str1,str2):
    if str1 + str2 != str2 + str1:
        return ""

    len1 = len(str1)
    len2 = len(str2)

    g = math.gcd(len1, len2)

    return str1[:g]

print(GCS("AAAAAA","AAA"))