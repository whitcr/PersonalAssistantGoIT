from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
CONTACTS_FILE = DATA_DIR / "contacts.pkl"
NOTES_FILE = DATA_DIR / "notes.pkl"

DATA_DIR.mkdir(exist_ok=True)

WELCOME_MESSAGE = "Welcome to the personal assistant!"
GOODBYE_MESSAGE = "Good bye!"
HELP_MESSAGE = """
Available commands:
    Contacts:
        add <name> [number] [new@email.put] [DD.MM.YYYY] [address] - Add contact to  address book
        change <name> [old_number|new_number]([number_to_add]) [new@email.put] [DD.MM.YYYY] [address] - Change existing contact's data
        delete <name> - Remove contact from address book
        search <query> - Search contacts by name, phone, email and address
        all - Show all contacts
        add-birthday <name> <DD.MM.YYYY> - Add a birthday to a contact
        show-birthday <name> - Show contact's birthday
        birthdays [<days>] - Show upcoming birthdays within the next <days> days (default is 7 days)

    Notes:
        note-add <title> <content> [tags] - Add new note
        note-change <title> <new_content> - Edit note
        note-delete <title> - Delete note
        note-find <query> - Search notes

    General:
        help - Show this help
        exit - Exit the program
"""
PHONE_DELIMITER = "|"