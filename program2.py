def decode_message( s: str, p: str) -> bool:

# write your code here
  
    def match(i, j):
        if i == len(s) and j == len(p):
            return True
        if j == len(p):
            return False
        if p[j] == '*':
            for k in range(i, len(s) + 1):
                if match(k, j + 1):
                    return True
            return False
        if p[j] == '?':
            if i < len(s):
                return match(i + 1, j + 1)
            else:
                return False
        if i < len(s) and p[j] == s[i]:
            return match(i + 1, j + 1)
        return False

    return match(0, 0)

# Example test cases
test_cases = [
    ("aa", "a"),  # False
    ("aa", "*"),  # True
    ("cb", "?a"), # False
    ("abc", "a*c"), # True
    ("abcd", "a*d"), # True
    ("abcd", "a?d"), # False
]

# Running the function on the test cases
for s, p in test_cases:
    print(f"Message: {s}, Pattern: {p} -> {decode_message(s, p)}")
        return False
