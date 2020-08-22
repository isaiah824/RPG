from classes.game import Person, bcolors

player_magic = [{"name": "Fira", "cost": 15, "dmg": 50},
                {"name": "Thundaga", "cost": 20, "dmg": 70},
                {"name": "Blizzard", "cost": 10, "dmg": 40},
                ]
player = Person(500, 95, 60, 34, player_magic)
enemy = Person(1200, 65, 45, 25, player_magic)

running = True
print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)
while running:
    pass