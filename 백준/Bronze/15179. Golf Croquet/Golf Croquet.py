team_A = input()
team_B = input()
s = int(input())
shot = input()

A_Score, B_Score = 0, 0

for i in range(len(shot)):
    if i%2==0:
        if shot[i] == 'H':
            A_Score += 1
        elif shot[i] == 'D':
            A_Score += 2
        elif shot[i] == 'O':
            B_Score += 1
    elif i%2!=0:
        if shot[i] == 'H':
            B_Score += 1
        elif shot[i] == 'D':
            B_Score += 2
        elif shot[i] == 'O':
            A_Score += 1
    if A_Score >= 7 or B_Score >= 7:
        if A_Score > 7:
            A_Score = 7
        elif B_Score > 7:
            B_Score = 7
        break
            
print(f"{team_A} {A_Score} {team_B} {B_Score}.",end=" ")
if A_Score == B_Score:
    print("All square.")
elif A_Score > B_Score:
    if A_Score == 7:
        print(f"{team_A} has won.")
    else:
        print(f"{team_A} is winning.")
else:
    if B_Score == 7:
        print(f"{team_B} has won.")
    else:
        print(f"{team_B} is winning.")