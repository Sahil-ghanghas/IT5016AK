# gaming_zone.py
from abc import ABC, abstractmethod
from typing import List

# User Interface (ISP)
class UserInterface(ABC):
    @abstractmethod
    def display_menu(self):
        pass

    @abstractmethod
    def get_user_input(self):
        pass

# Concrete User Interface
class ConsoleInterface(UserInterface):
    def display_menu(self):
        print("1. Enter Gaming Zone")
        print("2. Exit Gaming Zone")
        print("3. Show Log")
        print("4. Quit")

    def get_user_input(self):
        return input("Select an option: ")

# Logger (SRP)
class Logger:
    def __init__(self, log_file: str):
        self.log_file = log_file

    def log(self, message: str):
        with open(self.log_file, "a") as file:
            file.write(message + "\n")

# User Management (SRP)
class UserManager:
    def __init__(self, logger: Logger):
        self.users = {}
        self.logger = logger

    def enter_zone(self, user_id: str):
        self.users[user_id] = True
        self.logger.log(f"User {user_id} entered the gaming zone.")

    def exit_zone(self, user_id: str):
        if user_id in self.users:
            del self.users[user_id]
            self.logger.log(f"User {user_id} exited the gaming zone.")

# Main Application (OCP, DIP)
class GamingZoneApp:
    def __init__(self, user_interface: UserInterface, user_manager: UserManager):
        self.user_interface = user_interface
        self.user_manager = user_manager

    def run(self):
        while True:
            self.user_interface.display_menu()
            choice = self.user_interface.get_user_input()

            if choice == '1':
                user_id = input("Enter User ID: ")
                self.user_manager.enter_zone(user_id)
            elif choice == '2':
                user_id = input("Enter User ID: ")
                self.user_manager.exit_zone(user_id)
            elif choice == '3':
                self.show_log()
            elif choice == '4':
                print("Exiting the application.")
                break
            else:
                print("Invalid option. Please try again.")

    def show_log(self):
        with open("gaming_zone_log.txt", "r") as file:
            print(file.read())

# Application Entry Point
if __name__ == "__main__":
    logger = Logger("gaming_zone_log.txt")
    user_manager = UserManager(logger)
    user_interface = ConsoleInterface()
    app = GamingZoneApp(user_interface, user_manager)
    app.run()
