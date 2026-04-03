def is_palindrome(s):
    cleaned =''
    for ch in s:
        if ch!=" ":
            cleaned+=ch.lower()
    reversed = ''
    for ch in cleaned:
        reversed = ch + reversed
    return cleaned == reversed
print(is_palindrome("dad"))
