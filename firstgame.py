#Xp can be gained or lost 
# Enjoy!
import random

def line():
    print("-" * 48)

def get_choice(valid):
    """Ask until user types one of the valid strings (e.g. '1','2')."""
    while True:
        pick = input("> ").strip()
        if pick in valid:
            return pick
        print("Please type one of:", ", ".join(valid))

def play_game():
    name = input("Welcome to High School Adventure! What's your name? ")
    xp = 100

    print("=" * 48)
    print(f"   {name.upper()}'S HIGH SCHOOL DAY")
    print("=" * 48)
    print(f"Start strong, {name}! You have {xp} XP.\n")

    # -------------------------
    # Scene 1: Homeroom
    # -------------------------
    line()
    print("SCENE: Homeroom")
    print("1) Take a quick attendance quiz (+XP if lucky)")
    print("2) Doodle quietly (-small XP)")
    print("3) Sneak into the hallway (risk)")
    choice = get_choice(["1", "2", "3"])

    if choice == "1":
        if random.random() < 0.7:
            xp += 10
            print("Nice! The quiz was easy. +10 XP")
        else:
            xp -= 5
            print("Tricky question… -5 XP")
    elif choice == "2":
        xp -= 3
        print("Cool doodle, but you missed instructions. -3 XP")
    else:
        print("You slip into the hallway.")
        if random.random() < 0.3:
            xp -= 10
            print("Principal spots you wandering. Detention warning. -10 XP")

    print(f"{name}'s XP:", xp)

    # -------------------------
    # Scene 2: Hallway Hub
    # -------------------------
    line()
    print("SCENE: Hallway")
    print("Where to next?")
    print("1) Lockers (rumor of a bully)")
    print("2) Cafeteria (lunch time chaos?)")
    print("3) Science class (lab or worksheet)")
    print("4) Library (quiet zone)")
    choice = get_choice(["1", "2", "3", "4"])

    # -------------------------
    # Lockers (fight)
    # -------------------------
    if choice == "1":
        line()
        print("At your locker, someone bumps you on purpose.")
        print("Choose your action (fighting ALWAYS costs XP):")
        print("1) Fight")
        print("2) Walk away")
        print("3) Try to talk it out")
        sub = get_choice(["1", "2", "3"])

        if sub == "1":
            # Fighting always drains 8–18 XP, win or lose
            loss = random.randint(8, 18)
            xp -= loss
            print(f"You fight. It's exhausting. -{loss} XP")
        elif sub == "2":
            xp -= 5
            print("You walk away, but the stress lingers. -5 XP")
        else:
            if random.random() < 0.5:
                xp -= 3
                print("You calm things down. Still tense. -3 XP")
            else:
                xp -= 8
                print("They sneer and leave. Rough moment. -8 XP")

        print(f"{name}'s XP:", xp)

    # -------------------------
    # Cafeteria (food fight)
    # -------------------------
    elif choice == "2":
        line()
        print("Cafeteria options:")
        print("1) Grab a snack (+small XP)")
        print("2) Join a FOOD FIGHT (risky)")
        print("3) Study with a group (+steady XP)")
        sub = get_choice(["1", "2", "3"])

        if sub == "1":
            xp += 6
            print("Snack boosts your mood. +6 XP")
        elif sub == "2":
            print("FOOD FIGHT! Chaos erupts!")
            swing = random.randint(-25, 10)  # loss more likely than gain
            xp += swing
            if swing >= 0:
                print(f"You deflect pudding like a pro. +{swing} XP")
            else:
                print(f"Mashed potatoes nail you. {swing} XP")
            if random.random() < 0.3:
                xp -= 10
                print("Vice principal saw you. Detention slip. -10 XP")
        else:
            xp += 8
            print("Study session helps a lot. +8 XP")

        print(f"{name}'s XP:", xp)

    # -------------------------
    # Science class
    # -------------------------
    elif choice == "3":
        line()
        print("Science class:")
        print("1) Small lab (could gain or lose)")
        print("2) Quiet worksheet (+XP)")
        print("3) Ask for a hall pass and wander (risk)")
        sub = get_choice(["1", "2", "3"])

        if sub == "1":
            if random.random() < 0.2:
                xp -= 12
                print("Tiny spill—paperwork follows. -12 XP")
            else:
                xp += 10
                print("Lab goes well. +10 XP")
        elif sub == "2":
            xp += 10
            print("You focus and finish early. +10 XP")
        else:
            print("You walk the halls with a pass.")
            if random.random() < 0.25:
                xp -= 15
                print("Principal lecture about 'responsibility'. -15 XP")

        print(f"{name}'s XP:", xp)

    # -------------------------
    # Library (quiet)
    # -------------------------
    else:
        line()
        print("Library time:")
        print("1) Read quietly (+small XP)")
        print("2) Help the librarian (+steady XP)")
        print("3) Nap behind a shelf (risk of getting caught)")
        sub = get_choice(["1", "2", "3"])

        if sub == "1":
            xp += 6
            print("Peaceful reading session. +6 XP")
        elif sub == "2":
            xp += 9
            print("You shelve books like a champ. +9 XP")
        else:
            if random.random() < 0.35:
                xp -= 12
                print("Librarian catches you snoozing. -12 XP")
            else:
                xp += 4
                print("Power nap… unnoticed. +4 XP")

        print(f"{name}'s XP:", xp)

    # -------------------------
    # Final scene: Leaving
    # -------------------------
    line()
    print("FINAL BELL: Time to leave the building.")
    print("1) Main stairs (crowded—small chance of scuffle)")
    print("2) Side stairs (quiet—principal patrols sometimes)")
    print("3) Wait in library (safe and calm)")
    choice = get_choice(["1", "2", "3"])

    if choice == "1":
        if random.random() < 0.4:
            loss = random.randint(8, 18)  # fighting always costs XP
            xp -= loss
            print(f"Crowd jostle turns into a scuffle. -{loss} XP")
        else:
            xp += 4
            print("You slip through the crowd. +4 XP")
    elif choice == "2":
        if random.random() < 0.5:
            xp -= 15
            print("Principal catches you on the side stairs. -15 XP")
        else:
            xp += 5
            print("Quiet exit. +5 XP")
    else:
        xp += 6
        print("You chill a bit longer, then leave. +6 XP")

    # -------------------------
    # Ending
    # -------------------------
    line()
    print(f"DAY OVER! {name}'s Final XP: {xp}")
    if xp >= 85:
        print(f"S-tier: Awesome day, {name}!")
    elif xp >= 65:
        print("B-tier: Solid day with a few bumps.")
    elif xp >= 40:
        print("C-tier: You survived. Tomorrow will be better.")
    elif xp > 0:
        print("D-tier: Tough day. Avoid fights when you can.")
    else:
        print("F-tier: You ran out of XP. Rest up and try again!")

def main():
    while True:
        play_game()
        line()
        print("Play again? (y/n)")
        if input("> ").strip().lower() != "y":
            print("Thanks for playing!")
