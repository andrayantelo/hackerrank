# CSS colors are defined using a hexadecimal (HEX) notation for the
# combination of Red, Green, and Blue color values (RGB).

# Specifications of HEX Color Code
# It must start with a '#' symbol.
# It can have 3 or 6 digits.
# Each digit is in the range of 0 to F. (0 - 9 and A - F).
# A - F letters can be lower case.

# You are given  lines of CSS code. Your task is to print all valid
# Hex Color Codes, in order of their occurrence from top to bottom.

# CSS Code Pattern

# Input Format
# The first line contains n, the number of code lines.
# The next n lines contains CSS Codes.

# Constraints
# 0 < N < 50

# Output Format
# Output the color codes with '#' symbols on separate lines.


if __name__ == "__main__":
    import re
    
    n = int(input())
    regexp = []
    for _ in range(n):
        
        
        match_obj = re.findall(r'(?!^)(?![\s:])(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})', input(), re.I)
        regexp.extend(match_obj)
    for e in regexp:
        print(e)
