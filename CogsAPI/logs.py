from datetime import datetime
import colorama

def current_time_formatted():
    now = datetime.utcnow()
    return now.strftime('%H:%M:%S')

def process(message):
    send_console_message(f"<blue>{message}</>")

def send_console_message(message):
    """
    Send message to console.
    """
    message = message.replace("<blue>", colorama.Fore.BLUE)
    message = message.replace("<yellow>", colorama.Fore.YELLOW)
    message = message.replace("<red>", colorama.Fore.RED)
    message = message.replace("</>", colorama.Fore.RESET)
    print(f"{colorama.Fore.MAGENTA}{current_time_formatted()}){colorama.Fore.RESET} {colorama.Fore.GREEN}BOT: {colorama.Fore.YELLOW}{message}{colorama.Fore.RESET}")