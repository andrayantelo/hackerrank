# Rupal has a huge collection of country stamps. She decided to count the
# total number of distinct country stamps in her collection. She asked
# for your help. You pick the stamps one by one from a stack of n country stamps.

# Find the total number of distinct country stamps.

# Input Format
# The first line contains n, the total number of country stamps.
# The next n lines contains the name of the country where the samp is from.

# Constraints
# 0 < n < 100

# Output Format
# Output the total number of distinct country stamps on a single line.

if __name__ == "__main__":
    n = int(input())
    stamps = set()
    for _ in range(int(n)):
        stamps.add(input())
	
    print(len(stamps))
