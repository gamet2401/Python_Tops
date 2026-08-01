user_bio = "Music lover | Foodie | Traveller"
count = 0

for ch in user_bio:
    if ch != " ":   # space skip करो
        count += 1

print("Character count (excluding spaces):", count)
