import tkinter as tk
import random
import json
from tkinter import messagebox

def load_wellness_tips(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        messagebox.showerror("Error", "The file could not be found.")
    except json.JSONDecodeError:
        messagebox.showerror("Error", "The file is not a valid JSON.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")
    return []

def setup_gui(root, wellness_tips):
    root.grid_columnconfigure(0, weight=1)

    # Main Frame
    main_frame = tk.Frame(root)
    main_frame.grid(row=0, column=0, sticky="nsew")
    main_frame.grid_columnconfigure(0, weight=1)

    favorites = []
    tip_text = tk.StringVar(value="Welcome to the Daily Wellness Tip App! Click a button to get a tip.")

    def update_tip_display(tip):
        tip_text.set(f"Category: {tip['category']}\nTip: {tip['tip']}")

    def show_random_tip():
        if wellness_tips:
            selected_tip = random.choice(wellness_tips)
            update_tip_display(selected_tip)
            if selected_tip not in favorites:
                add_to_favorites_button.grid(row=3, sticky="ew", padx=80, pady=10)
            else:
                add_to_favorites_button.grid_remove()
        else:
            tip_text.set("No tips available.")

    def show_random_favorite_tip():
        if favorites:
            selected_tip = random.choice(favorites)
            update_tip_display(selected_tip)
            remove_from_favorites_button.grid(row=5, sticky="ew", padx=80, pady=10)

    def show_tips_by_category(category):
        category_tips = [tip for tip in wellness_tips if tip['category'] == category]
        if category_tips:
            selected_tip = random.choice(category_tips)
            update_tip_display(selected_tip)
            if selected_tip not in favorites:
                add_to_favorites_button.grid(row=3, sticky="ew", padx=80, pady=10)
            else:
                add_to_favorites_button.grid_remove()
        else:
            tip_text.set("No tips available for this category.")

    def add_to_favorites():
        tip_info = tip_text.get()
        for tip in wellness_tips:
            if tip['tip'] in tip_info and tip not in favorites:
                favorites.append(tip)
                messagebox.showinfo("Favorite Added", "This tip has been added to your favorites.")
                return
        messagebox.showinfo("Already Favorited", "This tip is already in your favorites.")

    def remove_from_favorites():
        tip_info = tip_text.get()
        for tip in favorites:
            if tip['tip'] in tip_info:
                favorites.remove(tip)
                messagebox.showinfo("Favorite Removed", "This tip has been removed from your favorites.")
                tip_text.set("Select another tip.")
                remove_from_favorites_button.grid_remove()
                return

    def show_favorites():
        if favorites:
            show_random_favorite_tip()
        else:
            tip_text.set("No favorite tips to show.")

    tk.Label(main_frame, textvariable=tip_text, justify=tk.LEFT, font=('Arial', 12)).grid(row=1, sticky="ew", pady=10)
    random_tip_button = tk.Button(main_frame, text="Show Random Tip", command=show_random_tip)
    random_tip_button.grid(row=2, sticky="ew", padx=80, pady=10)
    add_to_favorites_button = tk.Button(main_frame, text="Add to Favorites", command=add_to_favorites)
    remove_from_favorites_button = tk.Button(main_frame, text="Remove from Favorites", command=remove_from_favorites)
    show_favorites_button = tk.Button(main_frame, text="Show A Favorite Tip", command=show_favorites)
    show_favorites_button.grid(row=4, sticky="ew", padx=80, pady=10)

    row = 6
    for category in set(tip['category'] for tip in wellness_tips):
        button = tk.Button(main_frame, text=f"{category.title()} Tips", command=lambda c=category: show_tips_by_category(c))
        button.grid(row=row, sticky="ew", padx=80, pady=10)
        main_frame.grid_rowconfigure(row, weight=1)
        row += 1

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Daily Wellness Tip App")
    root.geometry("700x600")
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)
    wellness_tips = load_wellness_tips('wellness_tips.json')
    setup_gui(root, wellness_tips)
    root.mainloop()
