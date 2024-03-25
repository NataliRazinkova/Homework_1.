import abc

class UserView(abc.ABC):
    @abc.abstractmethod
    def show_contacts(self, contacts):
        pass

    @abc.abstractmethod
    def show_message(self, message):
        pass

    @abc.abstractmethod
    def show_error(self, error):
        pass

class ConsoleUserView(UserView):
    def show_contacts(self, contacts):
        for contact in contacts:
            print(contact)

    def show_message(self, message):
        print(message)

    def show_error(self, error):
        print(f"Error: {error}")

class AddressBookConsole:
    def __init__(self, view):
        self.book = self.load_data()
        self.view = view

    def load_data(self):
        if file_path.is_file():
            with open(file_path, "rb") as file:
                return pickle.load(file)
        else:
            return AddressBook()

    def save_data(self):
        with open(file_path, "wb") as file:
            pickle.dump(self.book, file)

    def add_record(self, record):
        self.book.add_record(record)
        self.view.show_message("Contact added.")

    def find_record(self, name):
        return self.book.find(name)

    def delete_record(self, name):
        self.book.delete(name)
        self.view.show_message("Contact deleted.")

    def get_upcoming_birthdays(self):
        birthdays = self.book.get_upcoming_birthdays()
        if not birthdays:
            self.view.show_message("There are no upcoming birthdays.")
        else:
            self.view.show_contacts(birthdays)

    def process_command(self, command, args):
        try:
            if command == "add":
                self.add_record(args)
            elif command == "find":
                record = self.find_record(args)
                if record:
                    self.view.show_contacts([record])
                else:
                    self.view.show_message("Contact not found.")
            
            elif command == "exit":
                self.save_data()
                self.view.show_message("Goodbye!")
                return False
            else:
                self.view.show_error("Invalid command.")
            return True
        except Exception as e:
            self.view.show_error(str(e))
            return True

def main():
    view = ConsoleUserView()
    address_book = AddressBookConsole(view)
    view.show_message("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if not address_book.process_command(command, args):
            break

if __name__ == "__main__":
    main()
