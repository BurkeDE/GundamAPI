
import requests

while True:
    print("\n===== GUNDAM EXPLORER =====")
    print("1. Browse Gundams")
    print("2. Search for a Gundam")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        url = "https://gundam-api.pages.dev/api/gundams"
        response = requests.get(url)
        data = response.json()

        print("\n===== GUNDAMS =====")
        print("Total Gundams:", data["info"]["count"])

        for gundam in data["results"]:
            print(gundam["id"], "-", gundam["name"])

    elif choice == "2":
        search = input("Enter Gundam name: ")

        url = "https://gundam-api.pages.dev/api/gundams"
        response = requests.get(url)
        data = response.json()

        found = False

        for gundam in data["results"]:
            if gundam["name"].lower() == search.lower():
                print("\n===== GUNDAM INFORMATION =====")
                print("Name:", gundam["name"])
                print("ID:", gundam["id"])
                print("Information:", gundam.get("header"))
                print("Pilots:", gundam.get("pilots"))
                print("Image:", gundam.get("imgUrl"))
                print("Wiki:", gundam.get("wikiUrl"))
                found = True
                break

        if not found:
            print("Gundam not found. Enter the exact name.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please choose 1, 2, or 3.")