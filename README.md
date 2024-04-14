
# Daily Wellness Tip App

## Overview
The Daily Wellness Tip App is a simple desktop application built with Python and Tkinter. It provides users with random wellness tips, the ability to filter tips by category, and manage a personal list of favorite tips. The tips are loaded from a JSON file, and the application is designed to be user-friendly with an intuitive interface.

## Requirements
- Python 3.x
- Tkinter module (usually comes with Python)
- json module (comes with Python)

## Installation

1. Clone the repository or download the source code:
   ```
   git clone https://github.com/Jameel-Ali/Wellness-Tip
   ```

2. Navigate to the directory containing the app:

3. Ensure Python and Tkinter are installed on your system

4. Prepare the wellness tips data:
   - Create a JSON file named `wellness_tips.json` in the application directory.
   - Populate the file with wellness tips structured as follows:
     ```json
     [
       {"category": "Exercise", "tip": "Take a brisk 20-minute walk every day."},
       {"category": "Nutrition", "tip": "Drink at least 8 glasses of water a day."},
       {"category": "Mindfulness", "tip": "Practice 10 minutes of meditation each morning."}
     ]
     ```

## Usage

To run the application, execute the following command in the terminal:
```
python path/to/daily_wellness_tip.py
```

The application window will open. You can interact with the following features:
- **Show Random Tip**: Displays a random wellness tip.
- **Add to Favorites**: Adds the currently displayed tip to your favorites.
- **Remove from Favorites**: Removes the currently displayed tip from your favorites.
- **Show A Favorite Tip**: Displays a random tip from your favorites.
- **Category Tips**: Displays a tip from a selected category.

