from rich.console import Console
from rich.prompt import Prompt

console = Console()

console.print("[bold green][ACCESS GRANTED: USER IDENTIFICATION SEQUENCE INITIATED][/bold green]")

name = Prompt.ask("[bold cyan]>>> Enter your handle[/bold cyan]")

console.print(f"[bold magenta][SYSTEM] Welcome, {name}. Identity verified at Clearance Level 7.[/bold magenta]")

age_input = Prompt.ask("[bold yellow]>>> What’s your age, operative?[/bold yellow]")

try:
    age = int(age_input)
    bot_age = 3
    if age < bot_age:
        console.print(f"[bold red][ALERT] You're younger than me? Impossible... unless you're a quantum anomaly. I’ve been online {bot_age} cycles.[/bold red]")
    else:
        age_diff = age - bot_age
        console.print(f"[bold blue][DATA] You’ve lived {age_diff} years longer than my core build. Experience: Exploitable?[/bold blue]")
except ValueError:
    console.print("[bold black on red][ERROR] Invalid input. Biological units are so... analog.[/bold black on red]")

color = Prompt.ask("[bold green]>>> Choose your terminal hue (e.g., neon green, crimson pulse)[/bold green]")

console.print(f"[bold italic {color}][THEME] Initializing {color} interface... System now reflects your aesthetic. Aesthetics = Security.[/bold italic {color}]")

console.print(f"[blink bold white on red]>>> FINAL LOG: Profile compiled. You are now flagged in the system, {name}. Stay sharp. The net is watching.[/blink bold white on red]")   
