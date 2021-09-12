def swap_case(s):
    ans = ""
    
    for ch in s:
        if ch.islower():
            ans += ch.upper()
        elif ch.isupper():
            ans += ch.lower()
        else:
            ans += ch
            
    return ans

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
