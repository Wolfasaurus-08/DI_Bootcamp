from game import Game

def get_user_menu_choice():
    menu = """
    Menu:
    1. Play a new game
    2. Show scores
    3. Quit
    """
    print(menu)
    choice = input("Enter your choice: ").strip()
    valid_choices = ['1', '2', '3']
    while choice not in valid_choices:
        print("Invalid choice. Please select 1, 2, or 3.")
        choice = input("Enter your choice: ").strip()
    return choice

def print_results(results):
    print("\nGame Results:")
    print(f"Wins: {results.get('win', 0)}")
    print(f"Losses: {results.get('loss', 0)}")
    print(f"Draws: {results.get('draw', 0)}")
    print("\nThank you for playing!\n")

def main():
    results = {'win': 0, 'loss': 0, 'draw': 0}
    
    while True:
        choice = get_user_menu_choice()
        
        if choice == '1':
            game = Game()
            result = game.play()
            results[result] += 1
        
        elif choice == '2':
            print_results(results)
        
        elif choice == '3':
            print_results(results)
            break

if __name__ == "__main__":
    main()
