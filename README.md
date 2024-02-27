# time-in-telegram-name
a python code can add the exact time in your telegram account last name.
If you plan to use this template to make your own template or bot, you have to:
-   *Keep the credits, and a link to this repository in all the files that contains my code*
-   *Keep the same license for unchanged code*

## Support

Before requesting support, you should know that this code requires you to have at least a basic knowledge of Python and the library is made for advanced users. Do not use this code if you don't know the basics or some advanced topics such as API or pyrogram module. Here's a link for resources to [Learn pyrogram](https://docs.pyrogram.org/).

If you need some help for something, do not hesitate to [Email](farbod.habibzadegan1390@gmail.com) me 

## Installation

To run this script, you need to have Python 3 and Pyrogram installed on your system. You also need to obtain your own API credentials from Telegram.

To install Python 3, visit python.org and follow the instructions for your operating system.

To install Pyrogram and its dependencies, run the following command in your terminal:

```powershell
pip install pyrogram tgcrypto
```

To get your API credentials, follow the steps in this guide.

## Usage

To use this script, you need to create a .env file in the same folder as the script, and add your API credentials as follows:

`API_ID=Your_API_ID
API_HASH=Your_API_HASH`

#

Then, you can run the script by typing the following command in your terminal:

`python time_in_telegram_name.py`

The script will ask you to log in to your Telegram account using your phone number and a verification code. Once you are logged in, the script will run in the background and update your last name every minute with the current time in the following font:

`𝟎𝟏:𝟐𝟑`

You can change the font by modifying the font dictionary in the script. You can also change the time format by modifying the strftime argument in the script.

To stop the script, press `Ctrl+C` in your terminal.


