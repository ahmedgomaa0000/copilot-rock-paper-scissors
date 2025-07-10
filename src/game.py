class Game:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']

    def play_round(self, user_choice):
        import random
        computer_choice = random.choice(self.choices)
        winner = self.determine_winner(user_choice, computer_choice)
        return computer_choice, winner

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return 'It\'s a tie!'
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            return 'You win!'
        else:
            return 'You lose!'