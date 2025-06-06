import random
game_status = True
player_life = 10
player_attack = 1
level = 1
enemy_life = 1
enemy_attack = 0
score = 0
turn = 0
while game_status:
    
    if player_life > 0:
        print("sigue adelante..")
        print(f"enemy lvl: {level}\nenemy life: {enemy_life}")
        print(f"Player attack: {player_attack}")
        player_attack = random.randint(0,level)
        enemy_life -= player_attack
        turn += 1
        if enemy_life <= 0:
            print("ganaste")
            level += 1
            enemy_life += level + 1
            player_attack += 1
        print(f"status:\nturn: {turn}\nenemy life: {enemy_life}")
        input("continuar>?")
    else:
        game_status = False
        print(f"adios, puntos: {score} ")