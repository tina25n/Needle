import random

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

    questions = {"Q1": {
                    "question": "You are in an elevator, which floor are you going to?",
                    "simple": q1_simple,
                    "medium": q1_medium,
                    "difficult": q1_difficult
                },
                "Q2": {
                    "question": "which number looks good to you?",
                    "simple": q2_simple,
                    "medium": q2_medium,
                    "difficult": q2_difficult
                },
                "Q3": {
                    "question": "Pick your favorite color",
                    "simple": q3_simple,
                    "medium": q3_medium,
                    "difficult": q3_difficult
                },
                "Q4": {
                    "question": "If you are stuck in dessert, which direction would you go?",
                    "simple": q4_simple,
                    "medium": q4_medium,
                    "difficult": q4_difficult
                }
                }

    print(questions["Q1"]["question"])
    print("Q1 simple:", ', '.join(map(str, questions["Q1"]["simple"]()))) 
    print("Q1 medium:", ', '.join(map(str, questions["Q1"]["medium"]())))
    print("Q1 difficult:", ', '.join(map(str, questions["Q1"]["difficult"]())))

    print(questions["Q2"]["question"])
    print("Q2 simple:", ', '.join(map(str, questions["Q2"]["simple"]())))
    print("Q2 medium:", ', '.join(map(str, questions["Q2"]["medium"]())))
    print("Q2 difficult:", ', '.join(map(str, questions["Q2"]["difficult"]())))

    print(questions["Q3"]["question"])
    print("Q3 simple:", ', '.join(map(str, questions["Q3"]["simple"]())))
    print("Q3 medium:", ', '.join(map(str, questions["Q3"]["medium"]())))
    print("Q3 difficult:", ', '.join(map(str, questions["Q3"]["difficult"]())))

    print(questions["Q4"]["question"])
    print("Q4 simple:", ', '.join(map(str, questions["Q4"]["simple"]())))
    print("Q4 medium:", ', '.join(map(str, questions["Q4"]["medium"]())))
    print("Q4 difficult:", ', '.join(map(str, questions["Q4"]["difficult"]())))

    print("0 to 5 in a row")
    print(sumSocre([0, 0, 0, 0, 0]))
    print(sumSocre([1, 0, 0, 0, 0]))
    print(sumSocre([1, 1, 0, 0, 0]))
    print(sumSocre([1, 1, 1, 0, 0]))
    print(sumSocre([1, 1, 1, 1, 0]))
    print(sumSocre([1, 1, 1, 1, 1]))

    print("three in a row vs not")
    print(sumSocre([1, 1, 1, 0, 0]))
    print(sumSocre([1, 0, 0, 1, 1]))
    print(sumSocre([1, 0, 1, 0, 1]))

    print("four in a row vs not")
    print(sumSocre([1, 1, 1, 1, 0]))
    print(sumSocre([1, 1, 0, 1, 1]))


main()
