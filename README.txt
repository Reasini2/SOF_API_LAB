Stack Overflow API Lab 


Description:
The Stack Overflow API Lab is a versatile command-line application designed to interact with the Stack Exchange API, specifically targeting Stack Overflow, the popular Q&A platform for programmers. This app provides a range of features to facilitate the exploration, management, and tracking of Stack Overflow user data. Whether you're a developer, a data enthusiast, or just a curious user, this app allows you to seamlessly access and organize information about Stack Overflow.

Key Features:
1- Fetch and Display User Data:The app enables you to retrieve user data from Stack Overflow, including essential details like user ID,display name, reputation, and last access date. You can specify the page number and the number of users per page (up to 100) to fine-tune your search.

2- Save User Data to File: You can save the fetched user data to a file of your choice.The app supports both ascending and descending sorting orders, allowing you to organize user data as needed..

3- Bookmark Your Favorite Users:Bookmark users by their user IDs, making it easy to track and revisit specific Stack Overflow users of interest.Bookmarking helps you keep a list of users you want to follow or learn from.

4- Unbookmark Users:If you no longer wish to track a user, you can unbookmark them. The app provides this option for user management.

5- Display Bookmarked Users:Access a list of bookmarked users at any time. View details about your bookmarked users, such as their names, reputations, and last access dates.


Guide to run the app:

Prerequisites:
Before running the app, ensure you have the following prerequisites installed on your system:
-Python 3.x
-Required Python packages: requests, json, pandas, tabulate, pickle

You can install these packages using pip by running the following command:
-pip install requests json pandas tabulate pickle

Configure Your API Key:
-Open the main.py file in a text editor of your choice.
-Locate the following line in main.py:

api_key = "xrsZng3Cq90hSs4H5FMngQ(("

Replace "xrsZng3Cq90hSs4H5FMngQ((" with your own Stack Exchange API key. You can obtain an API key by signing up on the Stack Exchange API website.


Architecture of the app:
The Stack Overflow API Lab is structured as follows:

- main.py: The main entry point of the application.
-StackOverflowUsers class in main.py: Contains methods to interact with the Stack Exchange API, manage bookmarked users, and display user data.
-External libraries: The app utilizes external libraries such as requests for API requests, pandas for data manipulation, tabulate for tabular data presentation, and pickle for data serialization.


Choosing Third-Party Libraries

The app makes use of the following third-party libraries for specific purposes:
-requests: Used for making HTTP requests to the Stack Exchange API to fetch user data.
-pandas: Chosen for its data manipulation capabilities, making it easy to structure and display user data.
-tabulate: Used to format user data in a tabular format for a user-friendly display.
-pickle: Employed for saving and loading bookmarked users in a serialized format.


App Menu Options
Upon running the app, you will see a menu with the following options:

1-Fetch and Display Stack Overflow Users:
	Enter the page number.
	Enter the number of users per page (maximum is 100).

2-Save Users to File (Specify Sort Order: asc or desc):
	Enter a file name to save the user data.
	Choose the sorting order for user data (ascending or descending).

3-Bookmark a User:
	Enter the user ID to bookmark.

4-Unbookmark a User:
	Enter the user ID to unbookmark.

5-Display Bookmarked Users:
	View a list of bookmarked users.

6-Exit:
	Exit the app.


Stack Exchange API Version and Why It's Used:

The Stack Overflow Users app interacts with version 2.2 of the Stack Exchange API. This specific version of the API is used because it provides a well-documented and stable interface for accessing information about Stack Overflow users. Here are some key reasons why this version of the API is chosen:

1-Data Availability: Version 2.2 of the Stack Exchange API offers comprehensive data about Stack Overflow users, including user IDs, display names, reputations, and more. This data is valuable for the app's functionality.

2-Consistency: The API follows a consistent structure and provides predictable responses, making it easier to parse and display user data.

3-Community Support: This version of the API is well-established and widely used by the developer community, ensuring access to community support and resources.

4-Stability: Stack Exchange API versions are stable and backward compatible, minimizing the risk of breaking changes in the app.


note:in save file we cant provide the Age of the user because the Stack Overflow didnt provide age of users.




