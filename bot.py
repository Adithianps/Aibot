from pyrogram import Client, filters
import openai
import random
import os

# Load OpenAI API key from the 'key.txt' file
api_key_path = os.path.join(os.path.dirname(__file__), "key.txt")
with open(api_key_path, "r") as key_file:
    openai.api_key = key_file.read().strip()

# Set up your Telegram bot API token
api_id = '22923523'
api_hash = 'd52c7824d0e66903a0724b800a16ce2c'
bot_token = '6824486125:AAGskYeykeWvs_J9nruWKxlQyoyb-PcFdAA'

# Initialize the Pyrogram client
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Define a function to solve fluid mechanics problems
def solve_fluid_mechanics_problem(question):
    # Use OpenAI to generate a solution based on the input question
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Solve the following fluid mechanics problem:\n{question}\nSolution:",
        temperature=0.7,
        max_tokens=150,
        n=1,
        stop=None
    )
    return response.choices[0].text.strip()

# Define a handler for the /start command
@app.on_message(filters.command("start"))
def start_command(client, message):
    message.reply("Hello! I am your Fluid Mechanics Problem Solver bot. Send me a fluid mechanics problem, and I'll solve it for you!")

# Define a handler for messages containing fluid mechanics problems
@app.on_message(filters.text & ~filters.command("start"))
def handle_fluid_mechanics_problem(client, message):
    # Extract the problem from the user's message
    problem = message.text.strip()

    # Solve the problem using the OpenAI model
    solution = solve_fluid_mechanics_problem(problem)

    # Reply to the user with the solution
    message.reply(f"Solved! Here is the solution:\n{solution}")

# Start the bot
app.run()
