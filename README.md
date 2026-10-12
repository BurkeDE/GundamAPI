# GundamAPI
This allows me to browse gundams from the GundamAPI

## Issues
Issue 1: The API sometimes returned an error when requesting information about a specific Gundam directly.

Solution: The program uses the Gundam list endpoint to retrieve Gundam entries and searches the returned results for an exact name match. When a match is found, the program displays the Gundam's available information.

Issue 2: Searching for a Gundam required knowing its full name, which made it harder to find a Gundam if the user only knew part of its name.

Solution: I added a partial-name search that allows users to type a word or part of a name, such as "RX". The program displays matching Gundams as a numbered list, allowing the user to choose one and view its information.

Issue 3: Browse gundam option was only showing 20 options instead of all almost 900 and some of the names contained unicode.

Solution: I made it to where users could browse all of the gundmas through pages and imported something to change the unicode to look readable.
