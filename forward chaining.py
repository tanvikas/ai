# Knowledge Base
facts = [
    ("Parent", "John", "Mary"),
    ("Parent", "Mary", "Sam")
]

print("Knowledge Base:")
for f in facts:
    print(f)

# Forward Reasoning
new_facts = []

for f1 in facts:
    for f2 in facts:
        if f1[2] == f2[1]:
            fact = ("Grandparent", f1[1], f2[2])
            if fact not in facts and fact not in new_facts:
                new_facts.append(fact)

# Display New Facts
print("\nNew Facts:")
for f in new_facts:
    print(f)

# Goal
goal = ("Grandparent", "John", "Sam")

print("\nGoal:", goal)

if goal in new_facts:
    print("Goal Proved!")
else:
    print("Goal Not Proved!")