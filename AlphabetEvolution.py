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
Mutation_Chance = 0.03
Population = []
for pop in range(Population_Size):
    new_pop = Create_Random_String(String_Size)
    Population.append(new_pop)
def Get_Highest_Score(Population):
    Highest_Scorer = random.choice(Population)
    Highest_Score = 0

    for pop in Population:
        Amount_right = 0
        for i in range(len(pop)):
            if pop[i] == HiddenString[i]:
                Amount_right += 1
        if Amount_right > Highest_Score:
            Highest_Score = Amount_right
            Highest_Scorer = pop




    return Highest_Scorer, Highest_Score, Highest_Score == String_Size



Completed = False
Generations = 0
while not Completed:

    Generations+= 1
    print(f"Generations: {Generations}")

    Second_Highest_Scorer = random.choice(Population)
    Second_Highest_Score = 0
    Highest_Scorer, Highest_Score, Completed = Get_Highest_Score(Population)
    Population.remove(Highest_Scorer)
    Second_Highest_Scorer, Second_Highest_Score, useless = Get_Highest_Score(Population)


    print(f"Highest Score = {Highest_Score}, Highest Scorer = {Highest_Scorer}")
    print(f"Second Highest Score = {Second_Highest_Score}, Second Highest Scorer = {Second_Highest_Scorer}")
    Population = []
    for pop in range(Population_Size):
        Population.append(Create_Children(Highest_Scorer, Second_Highest_Scorer))

    print(Population)









