from classes.game import Person, bcolors

player_magic = [{"name": "Fira", "cost": 15, "dmg": 150},
                {"name": "Thundaga", "cost": 20, "dmg": 170},
                {"name": "Blizzard", "cost": 10, "dmg": 140},
                ]
player = Person(500, 95, 60, 34, player_magic)
enemy = Person(1200, 65, 45, 25, player_magic)

running = True
print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)
while running:
    print("----------------------------")
    player.choose_action()
    choice = input("Choose Action: ")
    index = int(choice) - 1
    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for ", dmg, " damage, Enemy HP = ", enemy.get_hp())
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose Magic: ")) - 1
        magic_dmg = player.generate_spelldmg(magic_choice)
        spell = player.get_spell(magic_choice)
        cost = player.get_spellmp(magic_choice)
        current_mp = player.get_mp()
        if cost > current_mp:
            print(bcolors.FAIL + "\nNOT ENOUGH MP TO CAST\n" + bcolors.ENDC)
            continue
        player.reduce_mp(cost)
        enemy.take_damage(magic_dmg)
        print(bcolors.OKBLUE + "\n" + spell + " has dealt " + str(magic_dmg) + " damage to your enemy." + bcolors.ENDC)

    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print(bcolors.FAIL + "You were attacked for", str(enemy_dmg), "damage." + bcolors.ENDC)

    print("----------------------------")
    print("Your HP: ", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_maxhp()) + bcolors.ENDC)
    print("Your MP: ", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_maxmp()) + bcolors.ENDC + "\n")
    print("Enemy HP: ", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_maxhp()) + bcolors.ENDC )

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "YOU HAVE DEFEATED THE ENEMY" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "YOU HAVE BEEN DEFEATED IN BATTLE" + bcolors.ENDC)
        running = False
