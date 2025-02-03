import instaloader
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Initialize Instaloader
bot = instaloader.Instaloader()

# Function to fetch Instagram profile details
def get_instagram_profile_details(username: str):
    try:
        profile = instaloader.Profile.from_username(bot.context, username)
        profile_details = f"""
        Username: {profile.username}
        Bio: {profile.biography}
        Followers Count: {profile.followers}
        Following Count: {profile.followees}
        """
        return profile_details
    except Exception as e:
        return f"Error fetching details for {username}: {e}"

# Define the /start command
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Welcome to the Instagram Profile Info Bot! Send /profile <username> to get profile details.")

# Define the /profile command
async def profile(update: Update, context: CallbackContext):
    if len(context.args) == 1:
        username = context.args[0]
        details = get_instagram_profile_details(username)
        await update.message.reply_text(details)
    else:
        await update.message.reply_text("Please provide an Instagram username. Usage: /profile <username>")

# Main function to set up the bot
def main():
    # Your bot's token (use your actual token here)
    token = "7773033132:AAHfi2ZdENI75dJ6FeDYUDIg_GmkvW7Cyvk"  # Use your token here

    # Initialize the application with the token
    application = Application.builder().token(token).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("profile", profile))

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()