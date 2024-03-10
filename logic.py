import random
import women_package

# dictionary of questions and options
class questionsDict:
    def init(self):
        #Dictionary
        self.qsDict = {"Q1": {
                    "question": "You are in an elevator, which floor are you going to?",
                    "simple": q1_simple,
                    "medium": q1_medium,
                    "hard": q1_difficult
                },
                "Q2": {
                    "question": "which number looks good to you?",
                    "simple": q2_simple,
                    "medium": q2_medium,
                    "hard": q2_difficult
                },
                "Q3": {
                    "question": "Pick your favorite color",
                    "simple": q3_simple,
                    "medium": q3_medium,
                    "hard": q3_difficult
                },
                "Q4": {
                    "question": "If you are stuck in a desert, which direction would you go?",
                    "simple": q4_simple,
                    "medium": q4_medium,
                    "hard": q4_difficult
                }
                }

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
    for i in range(4):
        n = random.randint(1, 34)
        while (n in answer):
            n = random.randint(1, 34)
        answer.append(n)
    return answer


# randomly generate 10 numbers from 1-34
def q1_difficult():
    answer = []
    for i in range(6):
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
    for i in range(4):
        n = random.randint(1, 1000)
        while (n in answer):
            n = random.randint(1, 1000)
        answer.append(n)
    return answer


# randomly generate 10 numbers from 1-1000
def q2_difficult():
    answer = []
    for i in range(6):
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
    for i in range(4):
        n = colors[random.randint(0, 9)]
        while (n in answer):
            n = colors[random.randint(0, 9)]
        answer.append(n)
    return answer


def q3_difficult():
    colors = ["Red", "Blue", "Green", "Yellow", "Orange", "Purple", "Pink", "Brown", "Black", "White"]
    for i in range(6):
        n = colors[random.randint(0, 9)]
        while (n in answer):
            n = colors[random.randint(0, 9)]
        answer.append(n)
    return answer


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

def q5_simple(): 
    answer = []
    length = ["20cm", "30cm", "40cm", "50cm", "60cm", "70cm", "80cm", "90cm", "1m", "2m"]
    for i in range(2):
        n = length[random.randint(0, 9)]
        while (n in answer):
            n = length[random.randint(0, 9)]
        answer.append(n)
    return answer

def q5_medium(): 
    answer = []
    length = ["20cm", "30cm", "40cm", "50cm", "60cm", "70cm", "80cm", "90cm", "1m", "2m"]
    for i in range(4):
        n = length[random.randint(0, 9)]
        while (n in answer):
            n = length[random.randint(0, 9)]
        answer.append(n)
    return answer

def q5_difficult(): 
    answer = []
    length = ["20cm", "30cm", "40cm", "50cm", "60cm", "70cm", "80cm", "90cm", "1m", "2m"]
    for i in range(6):
        n = length[random.randint(0, 9)]
        while (n in answer):
            n = length[random.randint(0, 9)]
        answer.append(n)
    return answer


def q6_simple():
    answer = []
    items = ["laptop", "book", "stuffed animal", "pen", "phone", "plant"]
    for i in range(2):
        n = items[random.randint(0, 5)]
        while (n in answer):
            n = items[random.randint(0, 5)]
        answer.append(n)
    return answer

def q6_medium():
    answer = []
    items = ["laptop", "book", "stuffed animal", "pen", "phone", "plant"]
    for i in range(4):
        n = items[random.randint(0, 5)]
        while (n in answer):
            n = items[random.randint(0, 5)]
        answer.append(n)
    return answer

def q6_difficult():
    
    items = ["laptop", "book", "stuffed animal", "pen", "phone", "plant"]
    return items

def q7_simple():
    answer = []
    emotions = ["Happiness", "Sadness", "Anger", "Fear", "Surprise", "Love", "Envy", "Confusion", "Excitement"];
    for i in range(2):
        n = emotions[random.randint(0, 8)]
        while (n in answer):
            n = emotions[random.randint(0, 8)]
        answer.append(n)
    return answer

def q7_medium():
    answer = []
    emotions = ["Happiness", "Sadness", "Anger", "Fear", "Surprise", "Love", "Envy", "Confusion", "Excitement"];
    for i in range(4):
        n = emotions[random.randint(0, 8)]
        while (n in answer):
            n = emotions[random.randint(0, 8)]
        answer.append(n)
    return answer


def q7_difficult():
    answer = []
    emotions = ["Happiness", "Sadness", "Anger", "Fear", "Surprise", "Love", "Envy", "Confusion", "Excitement"];
    for i in range(6):
        n = emotions[random.randint(0, 8)]
        while (n in answer):
            n = emotions[random.randint(0, 8)]
        answer.append(n)
    return answer

def q8_simple():
    answer = []
    times = ["6 AM", "9 AM", "Noon", "3 PM", "6 PM", "9 PM", "Midnight", "3 AM", "4:30 AM", "7:45 PM"]
    for i in range(2):
        n = times[random.randint(0, 9)]
        while (n in answer):
            n = times[random.randint(0, 9)]
        answer.append(n)
    return answer

def q8_medium():
    answer = []
    times = ["6 AM", "9 AM", "Noon", "3 PM", "6 PM", "9 PM", "Midnight", "3 AM", "4:30 AM", "7:45 PM"]
    for i in range(4):
        n = times[random.randint(0, 9)]
        while (n in answer):
            n = times[random.randint(0, 9)]
        answer.append(n)
    return answer


def q8_difficult():
    answer = []
    times = ["6 AM", "9 AM", "Noon", "3 PM", "6 PM", "9 PM", "Midnight", "3 AM", "4:30 AM", "7:45 PM"]
    for i in range(6):
        n = times[random.randint(0, 9)]
        while (n in answer):
            n = times[random.randint(0, 9)]
        answer.append(n)
    return answer


def q9_simple():
    answer = []
    drinks = ["Electric Lemonade", "Cosmic Cranberry Blast", "Mango Tango Twist", "Blueberry Blitz", "Raspberry Rapture", "Citrus Cyclone", "Pineapple Paradise Punch", "Watermelon Whirlwind", "Kiwi Kiss", "Guava Galaxy Splash"]
    for i in range(2):
        n = drinks[random.randint(0, 8)]
        while (n in answer):
            n = drinks[random.randint(0, 8)]
        answer.append(n)
    return answer

def q9_medium():
    answer = []
    drinks = ["Electric Lemonade", "Cosmic Cranberry Blast", "Mango Tango Twist", "Blueberry Blitz", "Raspberry Rapture", "Citrus Cyclone", "Pineapple Paradise Punch", "Watermelon Whirlwind", "Kiwi Kiss", "Guava Galaxy Splash"]
    for i in range(4):
        n = drinks[random.randint(0, 8)]
        while (n in answer):
            n = drinks[random.randint(0, 8)]
        answer.append(n)
    return answer


def q9_difficult():
    answer = []
    drinks = ["Electric Lemonade", "Cosmic Cranberry Blast", "Mango Tango Twist", "Blueberry Blitz", "Raspberry Rapture", "Citrus Cyclone", "Pineapple Paradise Punch", "Watermelon Whirlwind", "Kiwi Kiss", "Guava Galaxy Splash"]
    for i in range(6):
        n = drinks[random.randint(0, 8)]
        while (n in answer):
            n = drinks[random.randint(0, 8)]
        answer.append(n)
    return answer


def q10_simple(): 
    answer = []
    elements = ["earth", "water", "fire", "air", "space", "consciousness"]
    for i in range(2):
        n = elements[random.randint(0, 5)]
        while (n in answer):
            n = elements[random.randint(0, 5)]
        answer.append(n)
    return answer


def q10_medium(): 
    answer = []
    elements = ["earth", "water", "fire", "air", "space", "consciousness"]
    for i in range(4):
        n = elements[random.randint(0, 5)]
        while (n in answer):
            n = elements[random.randint(0, 5)]
        answer.append(n)
    return answer


def q10_difficult(): 
    elements = ["earth", "water", "fire", "air", "space", "consciousness"]
    return elements

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

#Dictionary
questions = {"Q1": {
                "question": "You are in an elevator, which floor are you going to?",
                "simple": q1_simple,
                "medium": q1_medium,
                "hard": q1_difficult
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
                    "question": "If you are stuck in a desert, which direction would you go?",
                    "simple": q4_simple,
                    "medium": q4_medium,
                    "difficult": q4_difficult
                },
                "Q5" : {
                    "question": "Imagine you have a tail, how long would it be?",
                    "simple": q5_simple,
                    "medium": q5_medium,
                    "difficult": q5_difficult

                },
                "Q6" : {
                    "question": "Look at your desk, what is the first thing you see",
                    "simple": q6_simple,
                    "medium": q6_medium,
                    "difficult": q6_difficult

                },
                "Q7": {
                    "question": "You are listening to the music, how do you feel?",
                    "simple": q7_simple,
                    "medium": q7_medium,
                    "difficult": q7_difficult
                },
                "Q8" : {
                    "question": "You are in a cave and you are going out after some uncountable time, what time is it now?",
                    "simple": q8_simple,
                    "medium": q8_medium,
                    "difficult": q8_difficult

                },
                "Q9" : {
                    "question": "Choose one drink to match the vibe",
                    "simple" : q9_simple,
                    "medium": q9_medium,
                    "difficult": q9_difficult

                },
                "Q10" : {
                    "question": "Thinking of your passion, which element come closer to your passion",
                    "simple" : q10_simple,
                    "medium": q10_medium,
                    "difficult": q10_difficult

                }

                }

#     print(questions["Q1"]["question"])
#     print("Q1 simple:", ', '.join(map(str, questions["Q1"]["simple"]()))) 
#     print("Q1 medium:", ', '.join(map(str, questions["Q1"]["medium"]())))
#     print("Q1 difficult:", ', '.join(map(str, questions["Q1"]["difficult"]())))

#     print(questions["Q2"]["question"])
#     print("Q2 simple:", ', '.join(map(str, questions["Q2"]["simple"]())))
#     print("Q2 medium:", ', '.join(map(str, questions["Q2"]["medium"]())))
#     print("Q2 difficult:", ', '.join(map(str, questions["Q2"]["difficult"]())))

#     print(questions["Q3"]["question"])
#     print("Q3 simple:", ', '.join(map(str, questions["Q3"]["simple"]())))
#     print("Q3 medium:", ', '.join(map(str, questions["Q3"]["medium"]())))
#     print("Q3 difficult:", ', '.join(map(str, questions["Q3"]["difficult"]())))

#     print(questions["Q4"]["question"])
#     print("Q4 simple:", ', '.join(map(str, questions["Q4"]["simple"]())))
#     print("Q4 medium:", ', '.join(map(str, questions["Q4"]["medium"]())))
#     print("Q4 difficult:", ', '.join(map(str, questions["Q4"]["difficult"]())))

#     print(questions["Q5"]["question"])
#     print("Q4 simple:", ', '.join(map(str, questions["Q5"]["simple"]())))
#     print("Q4 medium:", ', '.join(map(str, questions["Q5"]["medium"]())))
#     print("Q4 difficult:", ', '.join(map(str, questions["Q5"]["difficult"]())))

#     print(questions["Q6"]["question"])
#     print("Q4 simple:", ', '.join(map(str, questions["Q6"]["simple"]())))
#     print("Q4 medium:", ', '.join(map(str, questions["Q6"]["medium"]())))
#     print("Q4 difficult:", ', '.join(map(str, questions["Q6"]["difficult"]())))

#     print(questions["Q7"]["question"])
#     print("Q4 simple:", ', '.join(map(str, questions["Q7"]["simple"]())))
#     print("Q4 medium:", ', '.join(map(str, questions["Q7"]["medium"]())))
#     print("Q4 difficult:", ', '.join(map(str, questions["Q7"]["difficult"]())))

#     print(questions["Q8"]["question"])
#     print("Q4 simple:", ', '.join(map(str, questions["Q8"]["simple"]())))
#     print("Q4 medium:", ', '.join(map(str, questions["Q8"]["medium"]())))
#     print("Q4 difficult:", ', '.join(map(str, questions["Q8"]["difficult"]())))

#     print(questions["Q9"]["question"])
#     print("Q4 simple:", ', '.join(map(str, questions["Q9"]["simple"]())))
#     print("Q4 medium:", ', '.join(map(str, questions["Q9"]["medium"]())))
#     print("Q4 difficult:", ', '.join(map(str, questions["Q9"]["difficult"]())))

#     print(questions["Q10"]["question"])
#     print("Q4 simple:", ', '.join(map(str, questions["Q10"]["simple"]())))
#     print("Q4 medium:", ', '.join(map(str, questions["Q10"]["medium"]())))
#     print("Q4 difficult:", ', '.join(map(str, questions["Q10"]["difficult"]())))


#     print("0 to 5 in a row")
#     print(sumSocre([0, 0, 0, 0, 0]))
#     print(sumSocre([1, 0, 0, 0, 0]))
#     print(sumSocre([1, 1, 0, 0, 0]))
#     print(sumSocre([1, 1, 1, 0, 0]))
#     print(sumSocre([1, 1, 1, 1, 0]))
#     print(sumSocre([1, 1, 1, 1, 1]))

#     print("three in a row vs not")
#     print(sumSocre([1, 1, 1, 0, 0]))
#     print(sumSocre([1, 0, 0, 1, 1]))
#     print(sumSocre([1, 0, 1, 0, 1]))

#     print("four in a row vs not")
#     print(sumSocre([1, 1, 1, 1, 0]))
#     print(sumSocre([1, 1, 0, 1, 1]))


# main()
