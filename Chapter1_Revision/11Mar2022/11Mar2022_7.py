"""Write a program that uses a nested if else"""

def get_choice(options: tuple):
    for i, element in enumerate(options):
        print("{}. {}".format(i + 1, element))
    while True:
        try:
            chosen = int(input("Please choose an option: (1 to {}): ".format(len(options))))
            assert 1 <= chosen <= len(options)
            break
        except Exception as e:
            print(f"Please enter a valid number between 1 and {len(options)}.\n")
    print()
    return chosen - 1


print("Welcome to this interactive adventure!\nChoose your character name from the following:")
name_options = ("Arun", "Siva", "Dhanyamol", "Asha")
name = name_options[get_choice(name_options)]

print(f"Hello {name}! Let's start.\n\n")
print("You were walking along a forest path when you were faced with two paths to continue on.")
if get_choice(("Choose the path on your left", "Choose the path on your right")) == 0:
    print("You chose to walk along the path on your left.")
    print("You kept walking and walking, until you reached a fast-flowing river. There were no bridges around.")
    print("However, you see a small, slightly damaged raft. What will you do?")
    if get_choice(("Try to swim across the river", "Use the raft")) == 0:
        print("You decided to try to swim accross the river.")
        print("As you start to swim, the water pushes you harder and harder until you fall off a waterfall.")
        print("GAME OVER")
    else:
        print("You decided to use the raft.")
        print("You sat on the raft and started to cross the river, but the water was so strong that it broke the raft and you fell off a waterfall.")
        print("GAME OVER")
else:
    print("You chose to walk along the path on your right.")
    print("You walk for several hours but you only end up going deeper into the forest. Soon, you don't know where you are.")
    print("You are now faced with two options:")
    if get_choice(("Teleport home using a device you found in the path", "Walk further")) == 0:
        print("You choose to teleport home, and the device works!")
        print("Congratulations on completing the game successfully!")
    else:
        print("You choose to walk further along the path.")
        print("But within a few minutes, you stumble upon a tiger's tail.")
        print("GAME OVER")