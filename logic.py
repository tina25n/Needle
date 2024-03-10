import random
import women_package

# dictionary of questions and options


# randomly generate 2 numbers from 1-34
def q1_simple():
    answer = []
    for i in range(2):
        n = random.randint(1, 34)
        while (n in answer):
            n = random.randint(1, 34)
        answer.append(n)
    return answer


# randomly generate 5 numbers from 1-34
def q1_medium():
    answer = []
    for i in range(5):
        n = random.randint(1, 34)
        while (n in answer):
            n = random.randint(1, 34)
        answer.append(n)
    return answer


# randomly generate 10 numbers from 1-34
def q1_difficult():
    answer = []
    for i in range(10):
        n = random.randint(1, 34)
        while (n in answer):
            n = random.randint(1, 34)
        answer.append(n)
    return answer


# randomly generate 2 numbers from 1-1000
def q2_simple():
    answer = []
    for i in range(2):
        n = random.randint(1, 1000)
        while (n in answer):
            n = random.randint(1, 1000)
        answer.append(n)
    return answer


# randomly generate 5 numbers from 1-1000
def q2_medium():
    answer = []
    for i in range(5):
        n = random.randint(1, 1000)
        while (n in answer):
            n = random.randint(1, 1000)
        answer.append(n)
    return answer


# randomly generate 10 numbers from 1-1000
def q2_difficult():
    answer = []
    for i in range(10):
        n = random.randint(1, 1000)
        while (n in answer):
            n = random.randint(1, 1000)
        answer.append(n)
    return answer


def q3_simple():
    answer = []
    colors = ["Red", "Blue", "Green", "Yellow", "Orange", "Purple", "Pink", "Brown", "Black", "White"]
    for i in range(2):
        n = colors[random.randint(0, 9)]
        while (n in answer):
            n = colors[random.randint(0, 9)]
        answer.append(n)
    return answer


def q3_medium():
    answer = []
    colors = ["Red", "Blue", "Green", "Yellow", "Orange", "Purple", "Pink", "Brown", "Black", "White"]
    for i in range(5):
        n = colors[random.randint(0, 9)]
        while (n in answer):
            n = colors[random.randint(0, 9)]
        answer.append(n)
    return answer


def q3_difficult():
    colors = ["Red", "Blue", "Green", "Yellow", "Orange", "Purple", "Pink", "Brown", "Black", "White"]
    return colors


def q4_simple():
    answer = []
    directions = ["west", "east", "north", "south"]
    for i in range(2):
        n = directions[random.randint(0, 3)]
        while (n in answer):
            n = directions[random.randint(0, 3)]
        answer.append(n)
    return answer


def q4_medium():
    directions = ["west", "east", "north", "south"]
    return directions


def q4_difficult():
    directions = ["west", "east", "north", "south","northwest", "southwest", "northeast", "southeast"]
    return directions


# takes the user input when the buttons are clicked for user 1 and 2
def compare(a1, a2, scores):
    if (a1 == a2):
        scores.append(1)
    else:
        scores.append(0)


def sumSocre(scores):

    counter = 0
    for i in range(len(scores)):
        if scores[i] == 1:
            counter = 1
            for j in range(i+1, len(scores)):
                if scores[j] == 1:
                    counter += 1
                else:
                    break
            break

    # base_score
    base_score = 0
    for score in scores:
        base_score += score * round(random.uniform(0.9, 1.1), 2)

    bonus_score = base_score
    # four in a row: 1.1
    if counter == 4:
        bonus_score = base_score * 1.1

    # three in a row: 1.05
    elif counter == 3:
        bonus_score = base_score * 1.05

    if bonus_score > len(scores):
        bonus_score = len(scores)

    return round(bonus_score/len(scores), 2)


def main():


main()
