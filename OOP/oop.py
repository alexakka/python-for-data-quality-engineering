"""
Create a tool, which will do user generated news feed:
1.User select what data type he wants to add
2.Provide record type required data
3.Record is published on text file in special format


You need to implement:
1.News – text and city as input. Date is calculated during publishing.
2.Privat ad – text and expiration date as input. Day left is calculated during publishing.
3.Your unique one with unique publish rules.
"""
from datetime import datetime, date, timedelta
from abc import ABC, abstractmethod
import sys


class Publication(ABC):
    def __init__(self):
        self.date = datetime.now()
        self.text = ''
        self.content = ''

    @abstractmethod
    def add_publication(self):
        pass

    @abstractmethod
    def format_publication(self):
        pass

    def write_to_file(self, target="magazine.txt"):
        with open(target, "a", encoding="utf-8") as f:
            f.write(self.content)


class News(Publication):
    def __init__(self):
        super().__init__()
        self.city = "Unknown"
    
    def add_publication(self):
        self.text = input("Please enter text of the news: ")
        self.city = input("Please enter the city of the news: ")
        self.format_publication()

    def format_publication(self):
        self.content = f"========== News ==========\n{self.text}\n{self.city}, {self.date.strftime('%d-%m-%Y %I.%M')}\n\n"
    

class Ad(Publication):
    def __init__(self):
        super().__init__()
        self.actual_date = date.today() + timedelta(days=14) # by default ad will be actual for the 14 days

    def add_publication(self):
        self.text = input("Please enter text of the ad: ")
        user_actual_date = input("Please enter actual date for the ad (format: dd-mm-yyyy): ")
        
        try:
            dt = user_actual_date.split("-")
            self.actual_date = date(*map(int, dt[::-1]))
        except ValueError:
            print("Something went wrong :( Actual date will be set for 14 days.")
        
        self.__calculate_remaining()
        self.format_publication()

    def __calculate_remaining(self):
        self.actual_date_until = self.actual_date - date.today()

    def format_publication(self):
        self.content = f"========== Private Ad ==========\n{self.text}\nActual until: {self.actual_date.strftime('%d-%m-%Y')}, {self.actual_date_until.days} days left.\n\n"
    

class Quote(Publication):
    def __init__(self):
        super().__init__()
        self.author = "Unknown"

    def add_publication(self):
        self.text = input("Please enter text of the quote: ")
        self.author = input("Please enter the author of the quote: ")
        self.format_publication()

    def format_publication(self):
        self.content = f"========== Quote ==========\n{self.text}\nAuthor - {self.author}\n\n"


def create_publication(pub_type):
    mapping = {
        "1": News(),
        "2": Ad(),
        "3": Quote()
    }
    return mapping.get(pub_type, None)

def main():
    instructions = """
Please type:
    1 to add a News;
    2 to add a Private Ad;
    3 to add a Quote
    4 to Exit.
"""
    while True:
        action = input(instructions)
        if action == '4':
            sys.exit()

        publication = create_publication(action)
        if publication:
            publication.add_publication()
            publication.write_to_file()
        else:
            print("No such an action! Try again.")


if __name__ == "__main__":
    main()