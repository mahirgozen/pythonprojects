import time


def timeCountdown(t):

    # Fonction de compte à rebours
    while t>0:
        min, sec = divmod(t,60)
        timer = '{:02d}:{:02d}'.format(min, sec)
        print(timer, end="\r") 
        time.sleep(1)
        t -=1

    print('\n*** Countdown completed! Get ready! ***')


def input_time():

    # Obtenir l'entrée de l'utilisateur pour le temps
    while True:

        try:
            inp = input("Enter the time in seconds (e.g., 60): ")
            if inp <0:
                return int(inp)
            
            else:
                return inp
        except ValueError:
            print("Invalid input! Please enter a valid integer.")



def main():
    # Fonction principale
        print("Welcome to Countdown Timer!")
        while True:
            t = get_user_input()  # Obtenir l'entrée de l'utilisateur pour le temps
            countdown(t)  # Démarrer le compte à rebours
            choice = input("Do you want to start another countdown? (yes/no):  ").lower()  # Demander si l'utilisateur veut démarrer un autre compte à rebours
            if choice != 'yes':
                print("Thank you for using Countdown Timer!")

if __name__ == "__main__":
    main()


