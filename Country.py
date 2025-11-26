# O'Tria Fee
# CIS261
# Country

def display_menu():
    """
    Function to display the heading and menu choices
    """

    # Display "The Country List Program" heading
    print("The Country List Program")
    print()

    #Display "COMMAND MENU"
    print("COMMAND MENU")

    #Display menu options: view, add, del, exit with descriptions
    print("view- View a country")
    print("add- Add a country")
    print("del- Delete a country")
    print("exit- Exit program")
    print()

def create_country_dictionary():
    """
    Function to prepopulate a dictionary with country key and name
    Returns:
    dict: Dictionary containing initial country codes and names
    """
    
    # Create and return a dictionary with at least 3 country entries
    # Format: {"US": " United States", "CA": "Canada",...}
    countries ={
        "US": "United States",
        "CA": "Canada",
        "MX": "Mexico"
    }
    return countries

def view_country(country_dict):
    """
    Function to view country
    Args:
    country_dict (dict): Dictionary of country codes and names
    """
    # Display all keys in the dictionary using a for .. in loop
    for code in country_dict:
        print(code, end=" ")
    print()

    # Prompt user to enter a country code
    code = input("Enter country code: ")

    # Check if key exists and display corresponding country name
    if code in country_dict:
        print(f"Country name: {country_dict[code]}")
    else:
        # If invlaid key, display error message
        print("Invalid country code.")
    print()

def add_country(country_dict):
    """ 
    Function to add a country to the dictionary
    Args:
    country_dict (dict): Dictionary of country codes and names
    """
    # Prompt user for country code
    code= input("Enter country code:  ")
    # Check if key already exists, display error if it does
    if code in country_dict:
        print("Country code already exists.")
    else:
        #If key doesn't exist, prompt for country name
        name= input("Enter country name:")
        # Add new country to dictionary
        country_dict[code]=name
        #Display confirmation message
        print(f"{name} was added.")
    print()

def delete_country(country_dict):
    """
    Function to delete a country from the dictionary
    Args:
    country_dict(dict): Dictionary of country codes and names
    """
    # Prompt user for country code to delete
    code = input("Enter country code: ")
    # Check if key exists in dictionary
    if code in country_dict:
        # If valid, remove country and display confirmation
        name=country_dict.pop(code)
        print(f"{name} was deleted.")
    else:
        # If invalid, display error message
        print("Invalid country code.")
    print()

def main():
    """
    Main program function
    """
    # Call display_menu function
    display_menu()
    # Call create_country_dictionary function to get initial dictionary
    countries= create_country_dictionary()
    # Main program loop
    while True:
        # Prompt user for command
        command = input("Command:")
        # Use if/elif statements to handle each command:
        if command == "view":
            # - "view": call view_country function
            view_country(countries)
        elif command == "add":
            # - "add": call add_country function
            add_country(countries)
        elif command == "del":
            # - "del": call delete_country function
            delete_country(countries)
        elif command == "exit":
            # - "exit": break from loop
            break
        else:
            # - invalid command: display error message
            print("Not a valid command. Please try again.")
            print()
    
    # Display goodbye message
    print("Bye!")

if __name__=="__main__":
     main()





















