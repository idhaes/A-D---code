def isPalindroom(s):
    return helper_isPalindroom(s, 0, len(s)-1)

def helper_isPalindroom(s, low, high):
    if low >= high:
        return True
    elif s[low] != s[high]:
        return False
    else:
        return helper_isPalindroom(s,low+1, high-1)