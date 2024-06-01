Generating Random Code: The script generates a random code consisting of alphabetic characters (both uppercase and lowercase) with dashes inserted every 3 characters.

Tkinter Window: It creates a Tkinter window titled "Rooms" where users can input a code.

Checking Code: When the user enters a code and presses Enter, the script checks if the entered code matches the generated code:

If the entered code matches the generated code, it displays "You entered!" in the Tkinter window.
If the entered code is "command=<'re'>", "command=<'re'>", "reset.co" or "reset-code", it regenerates a new random code and displays "Code regenerated. Enter the new code." in the Tkinter window.
If the entered code doesn't match the generated code and is not "command=<'re'>", it displays "Error! Not a valid code." in the Tkinter window.
