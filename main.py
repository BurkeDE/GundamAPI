import requests
from urllib.parse import unquote

def get_gundams(page):
    url = "https://gundam-api.pages.dev/api/gundams"
    response = requests.get(url, params={"page": page}, timeout=15)
    response.raise_for_status()
    return response.json()


while True:
    print("\n===== GUNDAM EXPLORER =====")
    print("1. Browse Gundams")
    print("2. Search for a Gundam")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        page = 1

        while True:
            try:
                data = get_gundams(page)

                print("\n===== GUNDAMS =====")
                print("Page:", page, "of", data["info"]["pages"])

                for gundam in data["results"]:
                    name = unquote(gundam["name"])
                    print(gundam["id"], "-", name)

                print("\nN - Next page")
                print("P - Previous page")
                print("M - Main menu")

                option = input("Choose an option: ").lower()

                if option == "n":
                    if data["info"]["next"]:
                        page += 1
                    else:
                        print("You are on the last page.")

                elif option == "p":
                    if page > 1:
                        page -= 1
                    else:
                        print("You are already on the first page.")

                elif option == "m":
                    break

                else:
                    print("Invalid option.")

            except (requests.RequestException, ValueError, KeyError) as error:
                print("Could not load Gundams:", error)
                break

    elif choice == "2":
        search = input(
            "Enter Gundam name or part of the name: "
        ).strip().lower()

        if not search:
            print("Please enter a name.")
            continue

        try:
            data = get_gundams(1)
            matches = []

            for gundam in data["results"]:
                name = unquote(gundam["name"])

                if search in name.lower():
                    matches.append(gundam)

            if matches:
                print("\n===== MATCHING GUNDAMS =====")

                for i, gundam in enumerate(matches, start=1):
                    print(i, "-", unquote(gundam["name"]))

                try:
                    selection = int(
                        input("\nChoose a Gundam by number: ")
                    )

                    if 1 <= selection <= len(matches):
                        gundam = matches[selection - 1]

                        print("\n===== GUNDAM INFORMATION =====")
                        print("Name:", unquote(gundam["name"]))
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
                print("No matching Gundams found on the first page.")

        except (requests.RequestException, ValueError, KeyError) as error:
            print("Could not load Gundams:", error)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please choose 1, 2, or 3.")