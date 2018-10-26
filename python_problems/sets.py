# Task
# Given 2 sets of integers, m and n, print their symmertric difference in
# ascending order. The term symmetric difference indicates those values
# that exist in either m or n but do not exist in both.

# Input Format
# The first line of input contains an integer, m.
# The second line contains m space-separated integers.
# The third line contains an integer, n.
# The fourth line contains n space-separated integers.

# Output Format
# Output the symmetric difference integers in ascending order, one per line.

if __name__ == '__main__':
	

    m, m_line, n, n_line = int(input()), input().split(), int(input()), input().split()
	
    m_line = set([int(x) for x in m_line])
    n_line = set([int(y) for y in n_line])

    diff = list(m_line.difference(n_line)) + list(n_line.difference(m_line))
	
    diff = sorted(diff)
    for e in diff:
		print(e)
	
