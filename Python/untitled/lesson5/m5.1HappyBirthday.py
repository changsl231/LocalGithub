def happy():
    print("Happy birthday to you!")
def happyB(name):
    for i in range(5):
        happy()
    print("Happy birthday,dear{}".format(name))
    for i in range(5):
        happy()

happyB("Mike")
print()
happyB("Lily")