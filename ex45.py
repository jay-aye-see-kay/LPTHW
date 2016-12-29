class Room(object):
    r_dict = {
        0:'Hallway',
        1:'Kitchen',
        2:'Bedroom',
        3:'Toilet',
        4:'Laundry'
    }

class Engine(object):
    """This defines the engine of the game, calls maps etc, basically main."""
    def __init__(self):
        self.f_dict = {
            0: Hallway(),
            1: Kitchen(),
            2: Bedroom(),
            3: Toilet(),
            4: Laundry()
        }

    def play(self):
        # intro, room loop, finished
        print "You're at a party and need to pee, good luck."
        # start looping through rooms until peed == true and in hallway
        n_room, peed = 0, False
        while n_room != 0 or peed == False:
            c_room = self.f_dict.get(n_room)
            n_room, peed = c_room.enter(peed)
        # games over
        print "You did it! Go grab some pussy."

class Hallway(Room):

    def enter(self, peed):
        if peed ==  True:
            return 0, False
        else:
            print "You're in the hallway, you can't pee here."
            print "Pick a door, 1 - 4"
            door_choice = 0
            while door_choice < 1 or door_choice > 5:
                door_choice = int(raw_input("> "))
            in_choice = ""
            print "You chose the %s, go in? (y/n)" % self.r_dict[door_choice]
            while in_choice != "y" and in_choice != "n":
                in_choice = raw_input("> ")
            if in_choice == "y": return door_choice, False
            if in_choice == "n": return 0, False

class Kitchen(Room):

    def enter(self, peed):
        in_choice = ""
        print "You're in the kitchen, pee in the sink?"
        while in_choice != "y" and in_choice != "n":
            in_choice = raw_input("> ")
        if in_choice == "y":
            print "Someone yells at you so you run back to the party."
            return 0, True
        if in_choice == "n":
            return 0, False

class Bedroom(Room):

    def enter(self, peed):
        in_choice = ""
        print "You're in someone's bedroom, pee in the corner?"
        while in_choice != "y" and in_choice != "n":
            in_choice = raw_input("> ")
        if in_choice == "y":
            print "Someone beats the shit out of you, and you limp back to the party."
            return 0, True
        if in_choice == "n":
            return 0, False

class Toilet(Room):

    def enter(self, peed):
        in_choice = ""
        print "You're in the toilet, pee in the sink?"
        while in_choice != "y" and in_choice != "n":
            in_choice = raw_input("> ")
        if in_choice == "y":
            return 0, True
        if in_choice == "n":
            return 0, False

class Laundry(Room):

    def enter(self, peed):
        in_choice = ""
        print "You're in the laundry, pee in the sink?"
        while in_choice != "y" and in_choice != "n":
            in_choice = raw_input("> ")
        if in_choice == "y":
            return 0, True
        if in_choice == "n":
            return 0, False

game0 = Engine()
game0.play()
