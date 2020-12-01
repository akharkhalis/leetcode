def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs:
        return ""
    shortest = min(strs, key=len)
    for i, ch in enumerate(shortest):
        print ("i",i)
        print ("ch",ch)
        for other in strs:
            if other[i] != ch:
                return shortest[:i]
                print("ch", ch)
                print(shortest)
        print ("---end---")
    return shortest

print (longestCommonPrefix(["flower","flow","flight"]))