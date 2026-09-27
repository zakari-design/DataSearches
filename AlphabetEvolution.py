import random
import string




def Create_Random_String(size):
    Desired_String = ""
    for i in range(size):
        Desired_String += random.choice(string.ascii_lowercase)
    return  Desired_String
def Child_Factory(part):
    Child = ""
    for character in part:
        if random.random() < Mutation_Chance:
            Child+= random.choice(string.ascii_lowercase)
        else:
            Child+= character
    return Child
def Create_Children(bird, bee):
    mid_point = len(bird) //2
    left = bird[:mid_point]
    right = bee[mid_point:]
    return Child_Factory(left) + Child_Factory(right)
String_Size = 16
HiddenString = Create_Random_String(String_Size)
Population_Size = 10
Mutation_Chance = 0.05
Population = []
for pop in range(Population_Size):
    new_pop = Create_Random_String(String_Size)
    Population.append(new_pop)



Completed = False
Generations = 0
while not Completed:
    Generations+= 1
    print(f"Generations: {Generations}")
    Highest_Scorer = random.choice(Population)
    Highest_Score = 0
    Second_Highest_Scorer = random.choice(Population)
    Second_Highest_Score = 0
    for pop in Population:
        Amount_right = 0
        for i in range(len(pop)):
            if pop[i] == HiddenString[i]:
                Amount_right += 1
        if Amount_right > Highest_Score:
            Second_Highest_Score = Highest_Score
            Second_Highest_Scorer = Highest_Scorer
            Highest_Scorer = pop
            Highest_Score = Amount_right
            if Amount_right == String_Size:
                Completed = True

    print(f"Highest Score = {Highest_Score}, Highest Scorer = {Highest_Scorer}")
    print(f"Second Highest Score = {Second_Highest_Score}, Second Highest Scorer = {Second_Highest_Scorer}")
    Population = []
    for pop in range(Population_Size):
        Population.append(Create_Children(Highest_Scorer, Second_Highest_Scorer))

    print(Population)









