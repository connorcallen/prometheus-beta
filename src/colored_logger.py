from colorama import init, Fore, Style

# Initialize colorama for cross-platform colored output
init(autoreset=True)

def log_colored_message(message, color='green'):
    """
    Log a message in a specified color to the console.

    Args:
        message (str): The message to log.
        color (str, optional): Color of the message. 
            Supports 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan'. 
            Defaults to 'green'.

    Raises:
        ValueError: If an unsupported color is provided.
    """
    # Define supported colors mapping
    color_map = {
        'red': Fore.RED,
        'green': Fore.GREEN,
        'yellow': Fore.YELLOW,
        'blue': Fore.BLUE,
        'magenta': Fore.MAGENTA,
        'cyan': Fore.CYAN
    }

    # Validate color input
    if color.lower() not in color_map:
        raise ValueError(f"Unsupported color: {color}. Supported colors are: {', '.join(color_map.keys())}")

    # Print colored message
    print(f"{color_map[color.lower()]}{message}{Style.RESET_ALL}")