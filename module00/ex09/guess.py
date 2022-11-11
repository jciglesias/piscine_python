import random

if __name__=="__main__":
    num = random.randint(1, 99);
    print("This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType 'exit' to end the game.\nGood luck!");
    run = True;
    attempt = 1;
    while(run):
        cin = input("What's your guess between 1 and 99?\n");
        if cin.isnumeric():
            if num == int(cin):
                run = False;
                if num == 42: print("The answer to the ultimate question of life, the universe and everything is 42");
                if attempt == 1: print("Congratulations! You got it on your first try!");
                else: print(f"Congratulations, you've got it!\nYou won in {attempt} attempts!");
            elif num > int(cin):
                print("Too low!");
            else:
                print("Too high!");
        elif cin == "exit":
            run = False;
            print("Goodbye!");
        else:
            print("That's not a number.");
        attempt += 1;