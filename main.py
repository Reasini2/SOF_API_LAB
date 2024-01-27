import requests
import json
import pandas as pd
from tabulate import tabulate
import pickle
import datetime


class StackOverflowUsers:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.stackexchange.com/2.2"
        self.bookmarked_users = set()
        self.last_displayed_users = []
        self.load_bookmarked_users()

    def load_bookmarked_users(self):
        try:
            with open("bookmarked_users.pkl", "rb") as file:
                self.bookmarked_users = pickle.load(file)
        except FileNotFoundError:
            pass

    def save_bookmarked_users(self):
        with open("bookmarked_users.pkl", "wb") as file:
            pickle.dump(self.bookmarked_users, file)

    def fetch_users(self, page=1, pagesize=100, sort_order="desc"):
        pagesize = min(pagesize, 100)
        try:
            response = requests.get(
                f"{self.base_url}/users",
                params={
                    "key": self.api_key,
                    "order": sort_order,
                    "site": "stackoverflow",
                    "page": page,
                    "pagesize": pagesize
                },
            )
            response.raise_for_status()
            data = response.json()
            users = data["items"]
            return users
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error: {e.response.content}")
            return []
        except requests.exceptions.RequestException as e:
            print(f"Error fetching users: {str(e)}")
            return []

    def display_users(self, users):
        if not users:
            print("No users to display.")
            return

        self.last_displayed_users = users
        user_data = []
        counter = 1
        for user in users:
            last_access_date = datetime.datetime.fromtimestamp(
                user.get("last_access_date", 0)
            ).strftime('%Y-%m-%d %H:%M:%S')

            user_data.append(
                {
                    "User Number": counter,
                    "Name": user.get("display_name", "Null"),
                    "UserID": user.get("user_id", "Null"),
                    "Reputation": user.get("reputation", "Null"),
                    "LastAccessDate": last_access_date,
                }
            )
            counter += 1

        df = pd.DataFrame(user_data)
        print(tabulate(df, headers="keys", tablefmt="psql", showindex=False))

    def save_users_to_file(self, file_name, sort_order="asc"):
        if not self.last_displayed_users:
            print("No users to save. Display users first.")
            return

        if sort_order == "asc":
            self.last_displayed_users.sort(key=lambda user: user.get("user_id", 0))
        elif sort_order == "desc":
            self.last_displayed_users.sort(key=lambda user: user.get("user_id", 0), reverse=True)

        if not file_name.endswith(".sofusers"):
            file_name += ".sofusers"

        try:
            with open(file_name, "w") as file:
                file.write("Total Count of Users Fetched: " + str(len(self.last_displayed_users)) + "\n")
                file.write("UserID\tAccountID\tDisplayName\tUserAge\tReputation\tLocation\tUserType\tLastAccessDate\n")
                for user in self.last_displayed_users:
                    user_id = str(user.get("user_id", "Null"))
                    account_id = str(user.get("account_id", "Null"))
                    display_name = user.get("display_name", "Null").replace("\t", " ")
                    user_age = str(user.get("age", "Null"))
                    reputation = str(user.get("reputation", "Null"))
                    location = user.get("location", "Null").replace("\t", " ") if user.get("location") else "Null"
                    user_type = user.get("user_type", "Null")
                    last_access_date = datetime.datetime.fromtimestamp(
                        user.get("last_access_date", 0)
                    ).strftime('%Y-%m-%d %H:%M:%S')
                    file.write("\t".join([user_id, account_id, display_name, user_age, reputation, location, user_type,
                                          last_access_date]) + "\n")
        except Exception as e:
            print(f"Error saving users to file: {str(e)}")

    def bookmark_user(self, user_id):
        self.bookmarked_users.add(user_id)
        self.save_bookmarked_users()

    def unbookmark_user(self, user_id):
        if user_id in self.bookmarked_users:
            self.bookmarked_users.remove(user_id)
            self.save_bookmarked_users()
        else:
            print(f"User with ID {user_id} is not bookmarked.")

    def display_bookmarked_users(self):
        if not self.bookmarked_users:
            print("No users are bookmarked.")
            return

        bookmarked_users = []
        for user in self.last_displayed_users:
            if str(user.get("user_id")) in self.bookmarked_users:
                bookmarked_users.append(user)

        if bookmarked_users:
            print("Bookmarked Users:")
            self.display_users(bookmarked_users)
        else:
            print("No bookmarked users in the last displayed list.")


if __name__ == "__main__":
    api_key = "xrsZng3Cq90hSs4H5FMngQ(("
    manager = StackOverflowUsers(api_key)

    while True:
        print("\nMenu:")
        print("1. Fetch and display Stack Overflow users")
        print("2. Save users to file (Specify sort order: asc or desc)")
        print("3. Bookmark a user")
        print("4. Unbookmark a user")
        print("5. Display bookmarked users")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            pageNum = input("Enter the page number: ")
            pagesize = input("Enter the number of users per page (Max number of users per page = 100): ")
            users = manager.fetch_users(page=int(pageNum), pagesize=int(pagesize))
            manager.display_users(users)
        elif choice == "2":
            file_name = input("Enter the file name to save users: ")
            sort_order = input("Enter sort order (asc or desc): ")
            manager.save_users_to_file(file_name, sort_order)
        elif choice == "3":
            user_id = input("Enter the user ID to bookmark: ")
            manager.bookmark_user(user_id)
            print(f"User with ID {user_id} has been bookmarked.")
        elif choice == "4":
            user_id = input("Enter the user ID to unbookmark: ")
            manager.unbookmark_user(user_id)
        elif choice == "5":
            manager.display_bookmarked_users()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
