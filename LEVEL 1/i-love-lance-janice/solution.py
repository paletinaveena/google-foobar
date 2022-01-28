def solution(x):
    n = len(x)
    for char in x:
        if char >= 'a' and char <= 'z':
            char = chr(ord('a') + 25 - (ord(char) - ord('a')))
        x += char
    return x[n:]
