def main():
    import random
    from game import Game

    print("Welcome to Rock, Paper, Scissors!")
    game = Game()

    while True:
        user_choice = input("Enter your choice (rock, paper, scissors) or 'quit' to exit: ").lower()
        if user_choice == 'quit':
            print("Thanks for playing!")
            break
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print(f"Computer chose: {computer_choice}")

        result = game.play_round(user_choice, computer_choice)
        print(result)

if __name__ == "__main__":
    main()