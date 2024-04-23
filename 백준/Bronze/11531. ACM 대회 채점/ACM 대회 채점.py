submissions = []

while True:
    try:
        line = input().strip()
        if line == "-1":
            break
        submissions.append(line.split())
    except EOFError:
        break

problems = {}

for submission in submissions:
    time, problem, result = int(submission[0]), submission[1], submission[2]
        
    if problem not in problems:
        problems[problem] = {
            "first_correct_time": None,
            "wrong_attempts": 0
        }
        
    if result == "right":
        if problems[problem]["first_correct_time"] is None:
            problems[problem]["first_correct_time"] = time
    elif result == "wrong":
        if problems[problem]["first_correct_time"] is None:
            problems[problem]["wrong_attempts"] += 1

solved_problems = 0
total_penalty = 0

for problem, data in problems.items():
    if data["first_correct_time"] is not None:
        solved_problems += 1
        penalty = data["first_correct_time"] + 20 * data["wrong_attempts"]
        total_penalty += penalty

print(solved_problems, total_penalty)