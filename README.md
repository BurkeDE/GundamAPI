# GundamAPI
This allows me to browse gundams from the GundamAPI
Issue: The API sometimes returned an error when requesting information about a specific Gundam directly.

Solution: The program uses the Gundam list endpoint to retrieve Gundam entries and searches the returned results for an exact name match. When a match is found, the program displays the Gundam's available information.
