#Task 1
seasons = ("Winter", "Spring", "Summer", "Autumn")


def get_season(month_number):
    if 1 <= month_number <= 3:
        return seasons[0]
    elif 4 <= month_number <= 6:
        return seasons[1]
    elif 7 <= month_number <= 9:
        return seasons[2]
    elif 10 <= month_number <= 12:
        return seasons[3]
    else:
        return "Invalid month number"


month_number = int(input("Enter a month number (1-12): "))

season = get_season(month_number)

print(f"The season for month {month_number} is {season}.")

#Task 2
names_set = set()

# Continue reading names until an empty string is entered
while True:
    name = input("Enter a name (or press Enter to finish): ").strip()

    if name == "":
        break  # Exit the loop if an empty string is entered

    if name in names_set:
        print("Existing name")
    else:
        print("New name")

    # Add the name to the set
    names_set.add(name)

# Print the list of input names
print("\nList of input names:")
for name in names_set:
    print(name)

#Task 3
airport_data = {}

def add_airport():
    icao_code = input("Enter the ICAO code of the airport: ").strip().upper()
    airport_name = input("Enter the name of the airport: ").strip()
    airport_data[icao_code] = airport_name
    print(f"Airport {icao_code} - {airport_name} added.")

# Function to fetch airport information
def fetch_airport_info():
    icao_code = input("Enter the ICAO code of the airport you want to fetch: ").strip().upper()
    if icao_code in airport_data:
        print(f"The name of the airport with ICAO code {icao_code} is {airport_data[icao_code]}.")
    else:
        print(f"No information found for ICAO code {icao_code}.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")

    choice = input("Select an option (1/2/3): ")

    if choice == "EFHK":
        add_airport()
    elif choice == "2":
        fetch_airport_info()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3).")
        