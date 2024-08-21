sightings = []
def add_sighting ():
    species = input("enter your species: ")
    location = input("enter your location: ")
    date = input("enter your date: ")
    time = input("enter your time: ")
    sighting = {
        "species": species,
        "location": location,
        "date": date,
        "time": time
    }

    sightings.append(sighting)
    print(sightings)

# function to display all sightings
def view_sightings():
        if not sightings:
            print("No sightings found.")
        else:
            for sighting in sightings:
                print("Species:", sighting["species"])
                print("Location:", sighting["location"])
                print("Date:", sighting["date"])
                print("Time:", sighting["time"])
def search_sightings():
    search_species = input("Enter the species name to search for: ")
    found = False
    for sighting in sightings:
        if sighting["species"].lower() == search_species.lower():
            print("\nSpecies:", sighting["species"])
            print("Location:", sighting["location"])
            print("Date:", sighting["date"])
            print("Time:", sighting["time"])
            found = True
    if not found:
        print(f"No sightings found for species: {search_species}")
 #welcome messege here
print("welcome to wildlife tracking system!")
                
while True:
    choice = input("1. add species name\n 2. view\n 3. search by specie name\n 4. exit\n")
    if choice == "1":
        add_sighting()
    elif choice == "2":
        view_sightings()
    elif choice == "3":
        search_sightings()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
        
