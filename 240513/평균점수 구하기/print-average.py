scores = list(map(float, input().split()))
total_score = sum(scores)

average_score = total_score / len(scores)
print("{:.1f}".format(average_score))