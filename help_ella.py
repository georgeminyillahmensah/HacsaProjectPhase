# 2.⁠ ⁠*Sort and Rank the Scores*
#     - Sort the list of scores in *descending order* and print the sorted list.
#     - Create a new list called ⁠ rankings ⁠ that assigns each score a rank, where 1 is the highest score. Print the rankings alongside the scores.
    
#     Example output:
    
    
# ⁠     Rank: 1, Score: 99
#     Rank: 2, Score: 93
#     Rank: 3, Score: 92
#     ...


scores = [88, 92, 75, 81, 67, 99, 85, 73, 93, 80]

new_score = sorted(scores,reverse=True)

rankings_1 = list(range(1,len(new_score)+1))
rankings = []
for i in range(len(rankings_1)):
    rankings.append([rankings_1[i],new_score[i]])
    
print(rankings)
# for i in range(len(new_score)):
#     rankings.append([i+1,new_score[i]])


# for j in rankings:
#     print(f"Rank: {j[0]}, Score: {j[1]}")



