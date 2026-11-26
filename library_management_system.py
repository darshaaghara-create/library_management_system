allbooks = {
    1: ("Pride and Prejudice", "Jane Austen", "500", "Ancient Publisher", "ISBN001"),
    2: ("Moby Dick", "Herman Melville", "700", "Ancient Publisher", "ISBN002"),
    3: ("The Great Gatsby", "F. Scott Fitzgerald", "300", "Ancient Publisher", "ISBN003"),
    4: ("Jane Eyre", "Charlotte Bronte", "400", "Local Publisher", "ISBN004"),
    5: ("Wuthering Heights", "Emily Bronte", "450", "Local Publisher", "ISBN005"),
    6: ("Oliver Twist", "Charles Dickens", "350", "Local Publisher", "ISBN006"),
    7: ("David Copperfield", "Charles Dickens", "600", "Local Publisher", "ISBN007")
}

members = {}            
issued_books = {}       
transactions = []       

def recursive_search_books(keyword, books_list, index=0):
    if index >= len(books_list):
        return []
    current = books_list[index]
    if keyword in current[0].lower() or keyword in current[1].lower():
        return [current] + recursive_search_books(keyword, books_list, index + 1)
    else:
        return recursive_search_books(keyword, books_list, index + 1)

def count_issued_books(user):
    if user not in issued_books:
        return 0
    return len(issued_books[user])

def show_books():
    print("\n Books in Library:")
    print("-" * 70)
    print(f"{'ID':<5}{'Name':<20}{'Author':<15}{'Pages':<8}{'Publisher':<15}{'ISBN':<10}")
    print("-" * 70)
    for bid, details in allbooks.items():
        print(f"{bid:<5}{details[0]:<20}{details[1]:<15}{details[2]:<8}{details[3]:<15}{details[4]:<10}")
    print("-" * 70)

def add_book_admin():
    book_name = input("Enter Book Name: ").title().strip()
    for bid, details in allbooks.items():
        if details[0].lower() == book_name.lower():
            print(f"Book '{book_name}' already exists.")
            return
    author = input("Enter Author: ").title().strip()
    pages = input("Enter Pages: ").strip()
    publisher = input("Enter Publisher: ").title().strip()
    isbn = input("Enter ISBN: ").strip()
    new_id = max(allbooks.keys()) + 1 if allbooks else 1
    allbooks[new_id] = (book_name, author, pages, publisher, isbn)
    print(f"Book '{book_name}' added successfully.")

def update_book():
    book_name = input("Enter Book Name to Update: ").strip().title()
    for bid, details in allbooks.items():
        if details[0].lower() == book_name.lower():
            book = list(details)
            print("Current:", ", ".join(book))
            book[0] = input("Enter New Name (or press Enter): ") or book[0]
            book[1] = input("Enter New Author (or press Enter): ") or book[1]
            book[2] = input("Enter New Pages (or press Enter): ") or book[2]
            book[3] = input("Enter New Publisher (or press Enter): ") or book[3]
            book[4] = input("Enter New ISBN (or press Enter): ") or book[4]
            allbooks[bid] = tuple(book)
            print("Book updated successfully.")
            return
    print("Book not found.")

def delete_book():
    book_name = input("Enter Book Name to Delete: ").strip().title()
    for bid, details in list(allbooks.items()):
        if details[0].lower() == book_name.lower():
            removed = allbooks.pop(bid)
            print(f"Book '{removed[0]}' deleted successfully.")
            return
    print("Book not found.")

def show_my_books(user):
    print("\nIssued Books:")
    if user in issued_books and issued_books[user]:
        for bid in issued_books[user]:
            if bid in allbooks:
                details = allbooks[bid]
                print(" - " + ", ".join(details))
    else:
        print("None")

def search_books():
    keyword = input("Enter keyword to search: ").strip().lower()
    results = recursive_search_books(keyword, list(allbooks.values()))
    if results:
        print("\n Search Results:")
        for r in results:
            print(", ".join(r))
    else:
        print("No books found.")

def issue_book(user):
    book_name = input("Enter Book Name to Issue: ").strip().title()
    for bid, details in allbooks.items():
        if details[0].lower() == book_name.lower():
            if user not in issued_books:
                issued_books[user] = set()
            
            # Fix: Check if user already has the book
            if bid in issued_books[user]:
                print(f"You have already issued '{details[0]}'.")
                return
                
            issued_books[user].add(bid)
            print(f"Book '{details[0]}' issued to {user}.")
            transactions.append({"user": user, "action": "Issued", "book": details[0]})
            return
    print("Book not found.")

def return_book(user):
    book_name = input("Enter Book Name to Return: ").strip().title()
    if user in issued_books:
        for bid, details in allbooks.items():
            # Fix: Use bid to match exactly what is in the user's set
            if details[0].lower() == book_name.lower() and bid in issued_books[user]:
                issued_books[user].remove(bid)
                print(f"Book '{book_name}' returned by {user}.")
                transactions.append({"user": user, "action": "Returned", "book": book_name})
                return
    print("Book not issued by you or not found.")

def show_transactions(user):
    print(f"\nTransaction History for {user}:")
    user_trans = [t for t in transactions if t["user"] == user]
    if user_trans:
        print("-" * 50)
        print(f"{'Action':<15}{'Book':<20}")
        print("-" * 50)
        for t in user_trans:
            print(f"{t['action']:<15}{t['book']:<20}")
        print("-" * 50)
    else:
        print("No transactions yet.")

# --- MAIN PROGRAM LOOP ---
print("Welcome to Simple Library System")

while True:
    print("\nMain Menu:")
    print("1. Admin")
    print("2. User")
    print("3. Exit")

    role_choice = input("Enter Choice: ")

    if role_choice == "1":
        admin_name = input("Enter Admin Name: ").strip()
        password = input("Enter Admin Password: ")
        
        if admin_name == "admin" and password == "admin123":
            print("Welcome Back, Admin!") # Fixed printf -> print
            while True:
                print("\nAdmin Menu:")
                print("1. Show Books")
                print("2. Add Book")
                print("3. Update Book")
                print("4. Delete Book")
                print("5. Exit Admin")
                admin_choice = input("Enter Choice: ")
                
                if admin_choice == "1":
                    show_books()
                elif admin_choice == "2":
                    add_book_admin()
                elif admin_choice == "3":
                    update_book()
                elif admin_choice == "4":
                    delete_book()
                elif admin_choice == "5":
                    break
                else:
                    print("Invalid Choice.")
        else:
            print("Wrong Admin credentials. Returning to Main Menu.")

    elif role_choice == "2":
        user = input("Enter Your Name: ").title().strip()
        password = input("Enter User Password: ")
        
        # Logic for existing user
        if user in members:
            if members[user] == password:
                is_logged_in = True
            else:
                print("Wrong Password. Returning to Main Menu.")
                is_logged_in = False
        # Logic for new user
        else:
            members[user] = password
            print(f"New user '{user}' registered successfully.")
            is_logged_in = True
            
        if is_logged_in:
            while True:
                print(f"\nUser Menu ({user}):")
                print("1. Show My Books")
                print("2. Search Books")
                print("3. Issue Book")
                print("4. Return Book")
                print("5. Count My Issued Books")
                print("6. Show Transactions")
                print("7. Exit User")
                user_choice = input("Enter Choice: ")
                
                if user_choice == "1":
                    show_my_books(user)
                elif user_choice == "2":
                    search_books()
                elif user_choice == "3":
                    show_books()
                    issue_book(user)
                elif user_choice == "4":
                    return_book(user)
                elif user_choice == "5":
                    print(f"Total Issued Books: {count_issued_books(user)}")
                elif user_choice == "6":
                    show_transactions(user)
                elif user_choice == "7":
                    break
                else:
                    print("Invalid Choice.")

    elif role_choice == "3":
        print("Thank you for using the Library System. Goodbye!")
        break
    else:
        print("Invalid Choice. Please select 1, 2, or 3.")