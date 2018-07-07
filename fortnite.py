import random

def random_forkknife():
    common_fort = ["Bork", "Cork", "Court", "Dork", "Fork", "Fort", "Port",
        "Quart", "Short", "Slorp", "Snort", "Sort", "Splort", "Sport",]
    uncommon_fort = ["4t", "Abort", "Force", "Ford", "Forest", "Four", "Fourty",
        "Horse", "New York", "Pitchfork", "Thwart", "Voret", "Ψ"]
    common_nite = ["bike", "bite", "blight", "bright", "byte", "fight",
        "flight", "height", "kite", "knife", "knight", "life", "light","lite",
        "might", "night", "nite", "quite", "rife", "right", "slight", "smite",
        "sprite", "strike", "write",]
    uncommon_nite = ["invite", "despite", "goodnight", "excite", "ignite",
        "alight", "upright", "overwrite", "allright", "unite", "tonight", "🔪"]
    fort = random.choice(common_fort) if random.random() > 0.1 else random.choice(uncommon_fort)
    nite = random.choice(common_nite) if random.random() > 0.1 else random.choice(uncommon_nite)

    if random.random() > 0.99:
        return "🍴"
     
    return fort + nite

def random_about_to_play():
    intro_statements = ["I'm about to play some ", "Gonna get on ", "Gettin on ", "Gonna queue up for some "]
    ending_statements = [" real soon.", ".", " right now.", " soon."]
    intro_questions = ["Anyone want to play some ",
                       "Someone up for some ",
                       "Hey, anyone want to do some ",
                       "Does anyone want to play ",
                       "Someone want to play some "]

    ending_questions = [" with me?", " soon?", " right now?", " real soon?", "?"]

    if random.randint(0, 1) == 0:
        return random.choice(intro_statements) + random_forkknife() + random.choice(ending_statements)
    else:
        return random.choice(intro_questions) + random_forkknife() + random.choice(ending_questions)

def random_drop():
    group_names = ["boys", "girls", "enbies", 
                   "folks", "folxs", "comrades", "mortals"]
    sentances = ["Alright, SQUAD, where we dropping?",
                 "Where we droppin SQUAD?",
                 "You SQUAD ready to drop at LOCATION?",
                 "Yo SQUAD, we droppin at LOCATION?"]
    sentance = random.choice(sentances)
    sentance = sentance.replace("SQUAD", random.choice(group_names))
    sentance = sentance.replace("LOCATION", random_location())
    return sentance

def random_location():
    adjectives =  ["Anarchy", "Dusty", "Fatal", "Flush", "Greasy",
                   "Haunted", "Junk", "Lonely", "Loot", "Lucky", "Moisty",
                   "Pleasant", "Retail", "Risky", "Shifty", "Snobby", "Tomato"]
    locations = ["Acres", "Divot", "Fields", "Factory",
                 "Grove", "Hills", "Junction" "Lodge", "Lake",
                 "Landing", "Mire", "Park", "Row", "Reels",
                 "Shafts", "Shores", "Town"]

    special_names = ["the crates",
                     "the bridge",
                     "that hill",
                     "the house on the hill",
                     "the worst possible location",
                     "that town",]

    if random.random() > 0.1:
        return random.choice(adjectives) + " " + random.choice(locations)
    else:
        return random.choice(special_names)

def random_phrase():
    choice = random.randint(0, 1)
    if choice == 0:
        return random_about_to_play()
    else:
        return random_drop()

if __name__ == '__main__':
    print(random_phrase())
