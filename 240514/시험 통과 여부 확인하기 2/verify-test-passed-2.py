def check_pass(score):
    average = sum(score) / len(score)
    if average >= 60:
        return "pass"
    else:
        return "fail"

def main():
    num_students = int(input())
    pass_count = 0
    
    for _ in range(num_students):
        scores = list(map(int, input().split()))
        result = check_pass(scores)
        print(result)
        if result == "pass":
            pass_count += 1
    
    print(pass_count)

if __name__ == "__main__":
    main()