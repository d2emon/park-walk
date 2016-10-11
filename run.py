class Player:
    strength = 0
    stamina = 0
    luck = 0
    damage = 0.1
    money = 15
    food = 0
    items = []

    def roll(self):
        import dice

        self.strength = dice.d(1, 6)
        self.stamina = dice.d(1, 6)
        self.luck = dice.d(1, 6)


player = Player()


def load_point(id=0):
    import yaml
    filename = "data/rooms/{}.yml".format(id)
    try:
        with open(filename) as room:
            point = yaml.load(room)
    except:
        point = {"description": "No description", }

    if id == 0:
        player.roll()

    return point


def show_point(point):
    print(point)
    print("-"*80)
    print(point.get("description"))

    dialogue = point.get("dialogue")
    if dialogue:
        print()
        print(dialogue)
        for replica in dialogue:
            print()
            print(replica.get("text"))
            for answer_id, answer in enumerate(replica.get("answers")):
                print("{}. {}".format(answer_id + 201, answer.get("text")))
    print("-"*80)


def show_player(player):
    print("Stregth:\t{}\tDamage:\t{}".format(player.strength, player.damage))
    print("Stamina:\t{}\tMoney:\t{}".format(player.stamina, player.money))
    print("Luck:\t\t{}\tFood:\t{}".format(player.luck, player.food))
    print("Items:\t{}".format(player.items))


def show_exits(point):
    exits = point.get("exits", dict())

    print("-"*80)
    print(exits)
    print("-"*80)
    print("0. Quit")
    if exits.get("next"):
        print("1. Next")
    if exits.get("left"):
        print("2. Left")
    if exits.get("forward"):
        print("3. Forward")
    if exits.get("right"):
        print("4. Right")
    if exits.get("enter"):
        print("5. Enter")
    if exits.get("exit"):
        print("6. Exit")
    if exits.get("other"):
        print("7. Other")
    if exits.get("north"):
        print("8. North")
    if exits.get("east"):
        print("9. East")
    if exits.get("south"):
        print("10. South")
    if exits.get("west"):
        print("11. West")
    if exits.get("yes"):
        print("20. Yes")
    if exits.get("no"):
        print("21. No")

    doors = point.get('doors', [])
    for door_id, door in enumerate(doors):
        print("{}. {}".format(door_id + 101, door.get('description')))

    print("-"*80)


def get_choice():
    choice = input("Enter your choice: ")
    return int(choice)


def run():
    show_player(player)
    print("-"*80)
    point_id = 0

    while True:
        point = load_point(point_id)

        print("-"*80)
        show_point(point)
        show_player(player)
        show_exits(point)
        print("-"*80)

        choice = get_choice()
        exits = point.get("exits")
        if choice == 0:
            break
        elif choice == 1:
            point_id = exits.get("next")
        elif choice == 2:
            point_id = exits.get("left")
        elif choice == 3:
            point_id = exits.get("forward")
        elif choice == 4:
            point_id = exits.get("right")
        elif choice == 5:
            point_id = exits.get("enter")
        elif choice == 6:
            point_id = exits.get("exit")
        elif choice == 7:
            point_id = exits.get("other")
        elif choice == 8:
            point_id = exits.get("north")
        elif choice == 9:
            point_id = exits.get("east")
        elif choice == 10:
            point_id = exits.get("south")
        elif choice == 11:
            point_id = exits.get("west")
        elif choice == 20:
            point_id = exits.get("yes")
        elif choice == 21:
            point_id = exits.get("no")
        elif choice > 200:
            dialogue = point.get("dialogue", [])
            if dialogue:
                replica = dialogue[0]
                answers = replica.get("answers")
                answer = answers[choice - 201]
                print(answer.get("text"))
                point_id = answer.get('room')
        elif choice > 100:
            doors = point.get("doors", [])
            door = doors[choice - 101]
            point_id = door.get('room')

        print("Going to {}".format(point_id))


if __name__ == "__main__":
    run()
