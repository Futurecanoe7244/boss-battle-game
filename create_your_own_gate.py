import random
from random import randint
import time
import sys
print("Welcom To The Final Boss!")
boss1 = "The Fatso"
boss2 = "The Skin Burner"
boss3 = "The Cursed Child"
print("You have to defeat the boss to finish the gate!")
print(f"The bosses you can face are: {boss1}, {boss2}, and {boss3}")
bosses = [boss1, boss2, boss3]
# --- Color image display inserted after line 12 ---
# Put a color image file at: images/title.png (relative to this script).
# Preferred: Rich (best terminal approximation). Fallback: Pillow + ANSI truecolor blocks.
def show_color_image(rel_path: str, width: int = 60) -> None:
    import os

    image_path = os.path.join(os.path.dirname(__file__), rel_path)

    # Try Rich first (renders nicely or approximates with colored blocks)
    try:
        from rich.console import Console
        from rich.image import Image as RichImage

        if os.path.exists(image_path):
            console = Console()
            console.print(RichImage(image_path, width=width))
            return
    except Exception:
        pass

    # Fallback: use Pillow to print ANSI truecolor blocks (most modern terminals support 24-bit color)
    try:
        from PIL import Image
    except Exception:
        Image = None

    if Image is None or not os.path.exists(image_path):
        print(f"[Image preview skipped: cannot find or open '{image_path}'. Install 'rich' and 'pillow' if not already installed.]")
        return

    try:
        img = Image.open(image_path).convert("RGB")
    except Exception as ex:
        print(f"[Image preview skipped: cannot open '{image_path}': {ex}]")
        return

    # Resize preserving aspect; terminals are taller than wide for characters -> compensate
    orig_w, orig_h = img.size
    aspect = orig_h / orig_w
    new_w = max(1, width)
    new_h = max(1, int(aspect * new_w * 0.5))  # 0.5 compensates for character aspect
    img = img.resize((new_w, new_h), Image.Resampling.LANCZOS if hasattr(Image, "Resampling") else Image.ANTIALIAS)
    pixels = img.load()

    reset = "\x1b[0m"
    # Use two spaces per pixel so output isn't too narrow
    for y in range(new_h):
        line_parts = []
        for x in range(new_w):
            r, g, b = pixels[x, y]
            # background color escape; using spaces makes blending look better
            part = f"\x1b[48;2;{r};{g};{b}m  {reset}"
            line_parts.append(part)
        print("".join(line_parts))
# call it � change path if you put a different filename
show_color_image("images/title.png", width=60)
# --- end insertion ---
time.sleep(5)



print("Choosing a random boss for you to face...")
chosen_boss = random.choice(bosses)
print("You have to defeat " + chosen_boss + " to finish the gate!")

# Display the chosen boss image
if chosen_boss == boss1:
    show_color_image("images/fatso.png", width=60)
elif chosen_boss == boss2:
    show_color_image("images/skin_burner.png", width=60)
elif chosen_boss == boss3:
    show_color_image("images/cursed_child.png", width=60)

playerhp = 200
health = 0
boss_attack_power = 0
if chosen_boss == boss1:
    health = 150
    while health > 0 and playerhp > 0:
        boss_attack_power = 15
        print(f"you have {playerhp}HP")
        player_move = input("Do you want to attack or defend yourself? (Type 'attack' or 'defend') ")
        bosshitormiss = random.randint(1, 2)
        if player_move == "defend":
            print("You defended yourself from " + chosen_boss + "'s attack!")
            bosshitormiss = 2
            print(f"{chosen_boss} has {health}HP left")
        if player_move == "attack":
            print("You attacked " + chosen_boss + "!")
            attack_damage = random.randrange(1, 10)
            health = max(0, health - attack_damage)
            print(f"{chosen_boss} has {health}HP left")
        if bosshitormiss == 1:
            enemy_attack = random.randrange(1, 15)
            print(f"{chosen_boss} attacks you and hits you for {enemy_attack}hp!")
            playerhp = max(0, playerhp - enemy_attack)
            print(f"you have {playerhp}HP")
            print(f"{chosen_boss} has {health}HP left")

    
if chosen_boss == boss2:
    health = 120
    while health > 0 and playerhp > 0:
        boss_attack_power = 5
        print(f"you have {playerhp}HP")
        player_move = input("Do you want to attack or defend yourself? (Type 'attack' or 'defend') ")
        bosshitormiss = random.randint(1, 2)
        if player_move == "defend":
            print("You defended yourself from " + chosen_boss + "'s attack!")
            bosshitormiss = 2
            print(f"{chosen_boss} has {health}HP left")
        if player_move == "attack":
            print("You attacked " + chosen_boss + "!")
            attack_damage = random.randrange(1, 15)
            health = max(0, health - attack_damage)
            print(f"{chosen_boss} has {health}HP left")
        if bosshitormiss == 1:
            enemy_attack = random.randrange(1, 10)
            print(f"{chosen_boss} attacks you and hits you for {enemy_attack}hp!")
            playerhp = max(0, playerhp - enemy_attack)
            print(f"you have {playerhp}HP")
            print(f"{chosen_boss} has {health}HP left")
if chosen_boss == boss3:
    health = 100
    while health > 0 and playerhp > 0:
        boss_attack_power = 15
        print(f"you have {playerhp}HP")
        player_move = input("Do you want to attack or defend yourself? (Type 'attack' or 'defend') ")
        bosshitormiss = random.randint(1, 4)
        if player_move == "defend":
            print("You defended yourself from " + chosen_boss + "'s attack!")
            bosshitormiss = 2
            print(f"{chosen_boss} has {health}HP left")
        if player_move == "attack":
            print("You attacked " + chosen_boss + "!")
            attack_damage = random.randrange(1, 12)
            health = max(0, health - attack_damage)
            print(f"{chosen_boss} has {health}HP left")
        if bosshitormiss == 1:
            enemy_attack = random.randrange(1, 7)
            print(f"{chosen_boss} attacks you and hits you for {enemy_attack}hp!")
            playerhp = max(0, playerhp - enemy_attack)
            print(f"you have {playerhp}HP")
            print(f"{chosen_boss} has {health}HP left")
        
if health <= 0:
    print("You have defeated " + chosen_boss + "! You can now finish the gate!")
    time.sleep(5)
    sys.exit()
if playerhp <= 0:
    print("You have been defeated by " + chosen_boss + "! Game Over.")
    time.sleep(5)
    sys.exit()