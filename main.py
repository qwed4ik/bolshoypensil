import random
choices = ["Женя", "Саня", "Олег"]
computer = random.choice(choices)
player = False
pc_score = 0
player_score = 0
while True:
    player = input("Женя, Саня или Олег?").capitalize()
    ## Conditions of Женя,Саня и Олег
    if player == computer:
        print("Победила дружба!")
    elif player == "Женя":
        if computer == "Саня":
            print("Ты лох!", computer, "сильнее чем", player)
            pc_score+=1
        else:
            print("Ты победил!", player, "Быстрее чем", computer)
            player_score+=1
    elif player == "Саня":
        if computer == "Олег":
            print("Ты лох", "Популярней-", computer)
            pc_score+=1
        else:
            print("Харош!", computer, "Лаки")
            player_score+=1
    elif player == "Олег":
        if computer == "Женя":
            print("Ты лох", computer, "сильнее чем", player)
            pc_score+=1
        else:
            print("Харооош!", player, "умнее чем", computer)
            player_score+=1
    elif player=='Счет':
        print("Счет:")
        print(f"ПК:{pc_score}")
        print(f"Ты:{player_score}")
        break