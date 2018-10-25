# Given the names and grades for each student in a Physics class of
# n students, store them in a nested list and print the name(s) of any
# student(s) having the second lowest grade.

# Note: If there are multiple students with the same grade, order their
# names alphabetically and print each name on a new line.

# Input Format
# The first line contains an integer, n, the number of students. 
# The 2n subsequent lines describe each student over 2 lines;
# the first line contains a student's name, and the second line contains their grade.

# Output Format

# Print the name(s) of any student(s) having the second lowest grade in Physics;
# if there are multiple students, order their names alphabetically and print each one on a new line.

if __name__ == '__main__':
    
    arr = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name, score])
        
        
    
    lowest_score = min(arr, key=lambda a: a[1])
    # check if everyone has the same score
       
    arr = [e for e in arr if e[1] != lowest_score[1]]
    if arr:
        second_lowest = min(arr, key=lambda a: a[1])[1]
        runner_ups = [s[0] for s in arr if s[1] == second_lowest]
        runner_ups.sort()
        for elem in runner_ups:
            print(elem)
         

        
