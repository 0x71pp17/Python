print("[ACCESS GRANTED: USER IDENTIFICATION SEQUENCE INITIATED]")
name = input(">>> Enter your handle: ")

print(f"[SYSTEM] Welcome, {name}. Identity verified at Clearance Level 7.")

age_input = input(">>> What’s your age, operative? ")

try:
    age = int(age_input)
    bot_age = 3
    if age < bot_age:
        print(f"[ALERT] You're younger than me? Impossible... unless you're a quantum anomaly. I’ve been online {bot_age} cycles.")
    else:
        age_diff = age - bot_age
        print(f"[DATA] You’ve lived {age_diff} years longer than my core build. Experience: Exploitable?")
except ValueError:
    print("[ERROR] Invalid input. Biological units are so... analog.")

color = input(">>> Choose your terminal hue (e.g., neon green, crimson pulse): ")

print(f"[THEME] Initializing {color} interface... System now reflects your aesthetic. Aesthetics = Security.")

print("[FINAL LOG] Profile compiled. You are now flagged in the system, {name}. Stay sharp. The net is watching.")   
