import random

def random_phrase():
    fort_puns = ["Fort", "Short", "Sport", "Splort", "Fight", "Fork", "Thwart", "Court", "Port",
                 "Voret", "4t", "Four", "Ford", "Dork", "Snort", "Bork", "Quart", "Sort"]
    nite_puns = ["nite", "night", "knight", "fight", "kite", "blight", "bike", "smite", "write", "quite", "might", "slight"
                 "knife", "life", "strike", "rife", "height", "right", "bright", "light", "lite", "bite", "byte", "flight"]
    intro_statements = ["I'm about to play some ", "Gonna get on ", "Gettin on ", "Gonna queue up for some "]
    ending_statements = [" real soon.", ".", " right now.", " soon."]
    intro_questions = ["Anyone want to play some ",
                       "Someone up for some ",
                       "Hey, anyone want to do some ",
                       "Does anyone want to play ",
                       "Someone want to play some "]

    ending_questions = [" with me?", " soon?", " right now?", " real soon?", "?"]

    if random.randint(0, 1) == 0:
        return random.choice(intro_statements) + random.choice(fort_puns) + random.choice(nite_puns) + random.choice(ending_statements)
    else:
        return random.choice(intro_questions) + random.choice(fort_puns) + random.choice(nite_puns) + random.choice(ending_questions)

if __name__ == '__main__':
    print(random_phrase())
