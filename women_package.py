import random


def women_q1_simple():
    options_present = []
    options_package = ["Marie Curie", "Frida Kahlo", "Simone de Beauvoir", "Ruth Bader Ginsburg", "Taylor Swift", "Michelle Obama"]
    for i in range(2):
        n = options_package[random.randint(0, len(options_package)-1)]
        while (n in options_present):
            n = options_package[random.randint(0, len(options_package)-1)]
        options_present.append(n)
    return options_present


def women_q1_medium():
    options_present = []
    options_package = ["Marie Curie", "Frida Kahlo", "Simone de Beauvoir", "Ruth Bader Ginsburg", "Taylor Swift", "Michelle Obama"]
    for i in range(4):
        n = options_package[random.randint(0, len(options_package)-1)]
        while (n in options_present):
            n = options_package[random.randint(0, len(options_package)-1)]
        options_present.append(n)
    return options_present


def women_q1_difficult():
    options_package = ["Marie Curie", "Frida Kahlo", "Simone de Beauvoir", "Ruth Bader Ginsburg", "Taylor Swift", "Michelle Obama"]
    return options_package


def women_q2_simple():
    options_present = []
    options_package = ["Rachel", "Monica", "Phoebe", "Penny", "Bernadette", "Amy"]
    for i in range(2):
        n = options_package[random.randint(0, len(options_package)-1)]
        while (n in options_present):
            n = options_package[random.randint(0, len(options_package)-1)]
        options_present.append(n)
    return options_present


def women_q2_medium():
    options_present = []
    options_package = ["Rachel", "Monica", "Phoebe", "Penny", "Bernadette", "Amy"]
    for i in range(4):
        n = options_package[random.randint(0, len(options_package)-1)]
        while (n in options_present):
            n = options_package[random.randint(0, len(options_package)-1)]
        options_present.append(n)
    return options_present


def women_q2_difficult():
    options_package = ["Rachel", "Monica", "Phoebe", "Penny", "Bernadette", "Amy"]
    return options_package


def women_q3_simple():
    options_present = []
    options_package = ["ocean", "button", "city", "coin", "seed", "bookshelf", "bed", "mirror", "curtain", "alarm clock"]
    for i in range(2):
        n = options_package[random.randint(0, len(options_package)-1)]
        while (n in options_present):
            n = options_package[random.randint(0, len(options_package)-1)]
        options_present.append(n)
    return options_present


def women_q3_medium():
    options_present = []
    options_package = ["ocean", "button", "city", "coin", "seed", "bookshelf", "bed", "mirror", "curtain", "alarm clock"]
    for i in range(4):
        n = options_package[random.randint(0, len(options_package)-1)]
        while (n in options_present):
            n = options_package[random.randint(0, len(options_package)-1)]
        options_present.append(n)
    return options_present


def women_q3_difficult():
    options_present = []
    options_package = ["ocean", "button", "city", "coin", "seed", "bookshelf", "bed", "mirror", "curtain", "alarm clock"]
    for i in range(6):
        n = options_package[random.randint(0, len(options_package)-1)]
        while (n in options_present):
            n = options_package[random.randint(0, len(options_package)-1)]
        options_present.append(n)
    return options_present


def women_q4_simple():
    options_present = []
    options_package = ["Ali Wong", "Hannah Gadsby", "Iliza Shlesinger", "Phoebe Robinson", "Tina Fey", "Mindy Kaling", "Wanda Sykes"]
    for i in range(2):
        n = options_package[random.randint(0, len(options_package)-1)]
        while (n in options_present):
            n = options_package[random.randint(0, len(options_package)-1)]
        options_present.append(n)
    return options_present


def women_q4_medium():
    options_present = []
    options_package = ["Ali Wong", "Hannah Gadsby", "Iliza Shlesinger", "Phoebe Robinson", "Tina Fey", "Mindy Kaling", "Wanda Sykes"]
    for i in range(4):
        n = options_package[random.randint(0, len(options_package)-1)]
        while (n in options_present):
            n = options_package[random.randint(0, len(options_package)-1)]
        options_present.append(n)
    return options_present


def women_q4_difficult():
    options_present = []
    options_package = ["Ali Wong", "Hannah Gadsby", "Iliza Shlesinger", "Phoebe Robinson", "Tina Fey", "Mindy Kaling", "Wanda Sykes"]
    for i in range(6):
        n = options_package[random.randint(0, len(options_package)-1)]
        while (n in options_present):
            n = options_package[random.randint(0, len(options_package)-1)]
        options_present.append(n)
    return options_present


def women_q5_simple():
    options_present = []
    options_package = ["Pikachu", "Charizard", "Bulbasaur", "Squirtle", "Jigglypuff", "Eevee", "Snorlax", "Mewtwo", "Gyarados", "Snorlax", "ditto", "mimikyu", "Gengar"]
    for i in range(2):
        n = options_package[random.randint(0, len(options_package)-1)]
        while (n in options_present):
            n = options_package[random.randint(0, len(options_package)-1)]
        options_present.append(n)
    return options_present


def women_q5_medium():
    options_present = []
    options_package = ["Pikachu", "Charizard", "Bulbasaur", "Squirtle", "Jigglypuff", "Eevee", "Snorlax", "Mewtwo", "Gyarados", "Snorlax", "ditto", "mimikyu", "Gengar"]
    for i in range(4):
        n = options_package[random.randint(0, len(options_package)-1)]
        while (n in options_present):
            n = options_package[random.randint(0, len(options_package)-1)]
        options_present.append(n)
    return options_present


def women_q5_difficult():
    options_present = []
    options_package = ["Pikachu", "Charizard", "Bulbasaur", "Squirtle", "Jigglypuff", "Eevee", "Snorlax", "Mewtwo", "Gyarados", "Snorlax", "ditto", "mimikyu", "Gengar"]
    for i in range(6):
        n = options_package[random.randint(0, len(options_package)-1)]
        while (n in options_present):
            n = options_package[random.randint(0, len(options_package)-1)]
        options_present.append(n)
    return options_present


questions_women = {"Q1": {
                    "question": "You are sitting in a magic cafe, who do you want to talk to?",
                    "simple": women_q1_simple,
                    "medium": women_q1_medium,
                    "difficult": women_q1_difficult
                    },
                    "Q2": {
                    "question": "Choose one person to go swimming with you from Friends or TBBT.",
                    "simple": women_q2_simple,
                    "medium": women_q2_medium,
                    "difficult": women_q2_difficult
                    },
                    "Q3": {
                    "question": "Choose a word to describe patriarchy?",
                    "simple": women_q3_simple,
                    "medium": women_q3_medium,
                    "difficult": women_q3_difficult},
                    "Q4": {
                    "question": "Choose one comedian to walk a dog with you.",
                    "simple": women_q4_simple,
                    "medium": women_q4_medium,
                    "difficult": women_q4_difficult
                    },
                    "Q5": {
                    "question": "Choose a pokemon to help realize your career goals.",
                    "simple": women_q5_simple,
                    "medium": women_q5_medium,
                    "difficult": women_q5_difficult
                    }
}
