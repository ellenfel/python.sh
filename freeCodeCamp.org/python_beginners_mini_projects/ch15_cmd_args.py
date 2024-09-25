#Command Line Arguments
"""
Command line arguments are inputs provided to a program when 
it is executed from a command line interface (CLI). 
They allow users to specify options or parameters that can 
influence the program's behavior or output.
"""


def hello(name, lang):
    # Dictionary mapping languages to their respective greetings
    greetings = {
        "English": "Hello",
        "Spanish": "Hola",
        "German": "Hallo",
    }
    # Construct the greeting message using the provided name and language
    msg = f"{greetings[lang]} {name}!"
    # Print the greeting message
    print(msg)


if __name__ == '__main__':
    import argparse

    # Create an ArgumentParser object to handle command-line arguments
    parser = argparse.ArgumentParser(
        description="Provides a personal greeting."
    )

    # Add a required argument for the name of the person to greet
    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person to greet."
    )

    # Add a required argument for the language of the greeting
    parser.add_argument(
        "-l", "--lang", metavar="language",
        required=True, choices=["English", "Spanish", "German"],
        help="The language of the greeting."
    )

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the hello function with the parsed arguments
    hello(args.name, args.lang)