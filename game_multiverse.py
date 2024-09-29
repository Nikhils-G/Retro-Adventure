import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.path = []  # Track player achievements
        self.allies = []  # Track alliances with NPCs
        self.time_loops = 0  # Time loop count
        self.character_class = None  # For character customization

    def update_health(self, amount):
        self.health += amount
        self.health = max(0, self.health)

    def add_item(self, item):
        self.inventory.append(item)

    def add_ally(self, ally):
        if ally not in self.allies:
            self.allies.append(ally)

    def choose_class(self, character_class):
        self.character_class = character_class

def generate_random_monster():
    monsters = ["Antiva Monster", "Giga Monster", "Draconis", "Shadow Beast", "Specter Wraith"]
    return random.choice(monsters)

def generate_random_place():
    places = ["Seko", "Blue Sea", "Ancient Ruins", "Crystal Caverns", "Forgotten Temple"]
    return random.choice(places)

def quantum_choice(player, decision):
    response = ""
    ripple_effect = ""

    if decision == "explore":
        place_name = generate_random_place()
        player.add_item("Explored " + place_name)  # Add to inventory
        response = f"You explored {place_name} and discovered its secrets."
        player.path.append(f"explored a {place_name}")

    elif decision == "fight":
        monster_name = generate_random_monster()
        damage = random.randint(20, 40)
        player.update_health(-damage)
        player.add_ally(monster_name)  # Example: add the defeated monster as an ally
        response = f"You fought with a {monster_name} but took {damage} damage! Your health is now {player.health}."
        player.path.append(f"fought with a {monster_name}")

    elif decision == "investigate":
        investigation_item = random.choice(["a rock", "an ancient tablet", "a mysterious artifact"])
        player.add_item("Investigated " + investigation_item)  # Add to inventory
        response = f"You investigated {investigation_item} and uncovered hidden knowledge."
        player.path.append(f"investigated {investigation_item}")

    if player.health <= 0:
        response += " You have perished in your quest."
    else:
        response += " Your adventure continues."

    ripple_effect = f"The decision to {decision} caused ripples across time and space."
    return response, ripple_effect
