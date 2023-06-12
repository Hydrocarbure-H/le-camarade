import random

import conf
import discord

from db import db
from db.db import check_all_users_score
from resources import emojis
from work import analyse


class MyClient(discord.Client):
    """
    Client class (From Discord.py documentation)
    """

    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        """
        Handle every message
        :param message: Message object
        :return: Nothing
        """

        if message.author == self.user:
            return

        # Check the date : if it is the first message of the week, send the social score board and reset the db
        current_day_of_week = message.created_at.weekday()
        if current_day_of_week == 0 and check_all_users_score() and 1 == 2:
            await message.channel.send("C'est Lundi ! Voyons voir quel camarade a été le meilleur de la semaine !\n\n")
            await message.channel.send(analyse.display_scoreboard())
            db.connectfirsttime()
            await message.channel.send("\n\nLe tableau des scores a été réinitialisé ! Que le meilleur camarade gagne !")
            return

        # Check for special messages
        if message.content == "RESET ALL DB":
            await message.channel.send("Resetting all DB...")
            await message.channel.send(db.connectfirsttime())
            return
        if message.content == "DISPLAY SCOREBOARD":
            await message.channel.send("Fetching informations...")
            await message.channel.send(analyse.display_scoreboard())
            return

        # Analyse the message for social score board
        await analyse.analyse(message, social_score=True)

        # Random reaction
        if random.randint(0, 4) == 0:
            await message.add_reaction(emojis.get_random_emoji())

        # Talk with GPT
        if str(message.channel) == "le-camarade-pété" or str(message.channel) == "discord":
            await analyse.talk_with_gpt(message)

        # For trash talk channels
        elif str(message.channel) == "le-goulag":
            await analyse.analyse(message)


def main(t):
    """
    Main function
    :param t: token
    :return: Nothing
    """

    intents = discord.Intents.default()
    intents.message_content = True
    client = MyClient(intents=intents)
    client.run(t)


if "__main__" == __name__:
    token = conf.token()
    main(token)
