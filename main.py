import random

import conf
import discord
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

        # Checks for social score board here

        if random.randint(0, 5) == 0:
            await message.add_reaction('👍')

        if str(message.channel) == "le-camarade-pété" or str(message.channel) == "discord":
            await analyse.talk_with_gpt(message)
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
