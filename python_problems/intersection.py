if __name__ == "__main__":
    n = int(input())
    eng_students = set(map(int, input().rsplit()))
    
    b = int(input())
    fr_students = set(map(int, input().rsplit()))
    
    print(len(eng_students.intersection(fr_students)))
