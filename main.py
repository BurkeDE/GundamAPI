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
        search = input("Enter Gundam name or part of the name: ").strip().lower()

        url = "https://gundam-api.pages.dev/api/gundams"
        response = requests.get(url)
        data = response.json()

        matches = []

        for gundam in data["results"]:
            if search in gundam["name"].lower():
                matches.append(gundam)

        if matches:
            print("\n===== MATCHING GUNDAMS =====")

            for i, gundam in enumerate(matches, start=1):
                print(i, "-", gundam["name"])

            try:
                selection = int(input("\nChoose a Gundam by number: "))

                if 1 <= selection <= len(matches):
                    gundam = matches[selection - 1]

                    print("\n===== GUNDAM INFORMATION =====")
                    print("Name:", gundam["name"])
                    print("ID:", gundam["id"])
                    print("Information:", gundam.get("header"))
                    print("Pilots:", gundam.get("pilots"))
                    print("Image:", gundam.get("imgUrl"))
                    print("Wiki:", gundam.get("wikiUrl"))
                else:
                    print("Invalid selection.")
            except ValueError:
                print("Please enter a number.")
        else:
            print("No Gundams found matching that name.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please choose 1, 2, or 3.")