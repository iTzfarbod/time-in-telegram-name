from pyrogram import Client
from datetime import datetime
import time

# Define the font dictionary
font = {'0': '𝟎', '1': '𝟏', '2': '𝟐', '3': '𝟑', '4': '𝟒', '5': '𝟓', '6': '𝟔', '7': '𝟕', '8': '𝟖', '9': '𝟗', ':': ':', ' ': ' '}

# Your API credentials
api_id = Your_API_ID
api_hash = "Your_API_HASH"

# Create a Pyrogram client
app = Client("my_account", api_id, api_hash)

# Function to convert the time to the specified font
def convert_to_font(time_str):
    converted_str = ""
    for char in time_str:
        if char in font:
            converted_str += font[char]
        else:
            converted_str += char
    return converted_str

# Run the client and update the last name with the current time in the specified font
with app:
    while True:
        current_time = datetime.now().strftime("%H:%M")
        converted_time = convert_to_font(current_time)
        app.update_profile(last_name=converted_time)
        time.sleep(60)
