def reverse(s):
    return s[::-1]

def isPalindrome(s):
    """Calling reverse of function"""
    rev = reverse(s)

    if (s==rev):
        return True
    return False

s = "toot"
ans = isPalindrome(s)

if ans == 1:
    print("Yes")
else:
    print("No")