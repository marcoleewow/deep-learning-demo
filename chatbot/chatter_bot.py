# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, UbuntuCorpusTrainer


# Create a new instance of a ChatBot
bot = ChatBot(
    "Terminal",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.BestMatch"
    ],
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    database="../database.db"
)

bot.set_trainer(ChatterBotCorpusTrainer)
bot.train(
    "chatterbot.corpus.english",
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations"
)

# # this takes way too long to download and train, dont use it!
# bot.set_trainer(UbuntuCorpusTrainer)
# bot.train()

print("Type something to begin...")

# The following loop will execute each time the user enters input
while True:
    try:
        # We pass None to this method because the parameter
        # is not used by the TerminalAdapter
        bot_input = bot.get_response(None)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
