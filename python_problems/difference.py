if __name__ == "__main__":
    n = int(input())
    eng_students = set(map(int, input().split()))
    
    b = int(input())
    fr_students = set(map(int, input().split()))
    
    # Output the total number of students who are subscribed to the English newspaper only.
    
    print(len(eng_students.difference(fr_students)))
