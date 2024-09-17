import random


class Die:
    
    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value

    def roll(self):
        new_value = random.randint(1, 6)
        self._value = new_value
        return new_value

    
class player:

    def __init__(self, die, is_computer=False):
        self._die = die
        self._counter = 10
        self._is_computer = is_computer

    @property
    def die(self):
        return self._die

    @property
    def is_computer(self):
        return self._is_computer

    @property
    def counter(self):
        return self._counter

    def increment_counter(self):
        self._counter += 1

    def decrement_counter(self):
        self._counter -= 1

    #aggregation
    def roll_die(self):
        return self._die.roll()


class DiceGame:
    def __init__(self, player, computer):
        self._player = player
        self._computer = computer

    def play(self):
        print("=============================")
        print("🎲🎲 welcome to roll the dice")
        print("=============================")
        while(True):
            self.play_round()
            game_over = self.check_game_over()
            if game_over:
                break


    def play_round(self):
        # Welcome the user
        self.print_round_welcome()

        # Roll the dice
        player_value = self._player.roll_die()
        computer_value = self._player.roll_die()

        # Show the roll
        self.show_dice(player_value, computer_value)


        # Determine winner
        if player_value > computer_value:
            print("You won the round. 🎉")
            self.update_counters(self._player, self._computer)

        elif computer_value > player_value:
            print("You lost. 💀")
            self.update_counters(self._computer, self._player)

        else:
            print("Its a tie 👔")

        # Show counters
        self.show_counters()


    def print_round_welcome(self):
        print("\n------ New Round ------")
        input("🎲🎲 Press any key to roll the dice. 🎲🎲")

    def show_dice(self, player_value, computer_value):
        print(f"Your die: {player_value}")
        print(f"Computer value: {computer_value}")

    def update_counters(self, winner, loser):
        winner.decrement_counter()
        loser.increment_counter()

    def show_counters(self):
        print(f"Your counter: {self._player.counter}")
        print(f"Computers conter: {self._computer.counter}")

    def check_game_over(self):
        if self._player.counter == 0:
            self.show_game_over(self._player)
            return True
            
        elif self._computer.counter == 0:
            self.show_game_over(self._computer)
            return True
        
        else:
            return False

    def show_game_over(self, winner):
        if winner.is_computer:
            print("\n=============================")
            print("G A M E  O V E R")
            print("=============================")
            print("💀 Computer won the game 💀")
            print("=============================")

        else:
            print("\n=============================")
            print("Y O U  W O N")
            print("=============================")
            print("Congrats 🎉🎉🎉")
            print("=============================")


player_die = Die()
computer_die = Die()

my_player = player(player_die)
computer_player = player(computer_die, True)

#Start the game
game = DiceGame(my_player, computer_player)
game.play()