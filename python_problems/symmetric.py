# Output total number of students who have subscriptions to the English or the French newspaper but not both.

if __name__ == "__main__":
    n = int(input())
    eng_students = set(map(int, input().split()))
    
    b = int(input())
    fr_students = set(map(int, input().split()))

    print(len(eng_students.symmetric_difference(fr_students)))
