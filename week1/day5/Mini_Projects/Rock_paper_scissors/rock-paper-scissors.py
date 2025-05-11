from game import Game

def get_user_menu_choice():
    print("\nMenu:")
    print("(p) Play a new game")
    print("(s) Show scores")
    print("(q) Quit")
    choice = input("Enter your choice (p/s/q): ").lower()
    if choice in ['p', 's', 'q']:
        return choice
    else:
        print("Invalid input. Please enter 'p', 's', or 'q'.")
        return get_user_menu_choice()


def print_results(results):
    print("\nGame Results Summary:")
    print(f"Wins: {results['win']}")
    print(f"Losses: {results['loss']}")
    print(f"Draws: {results['draw']}")
    total_games = results['win'] + results['loss'] + results['draw']
    print(f"Total games played: {total_games}")
    print("\nThank you for playing!")


def main():
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choice = get_user_menu_choice()

        if choice == 'p':
            game = Game()
            result = game.play()
            results[result] += 1

        elif choice == 's':
            print_results(results)

        elif choice == 'q':
            print_results(results)
            break


main()