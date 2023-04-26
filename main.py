import conf
import discord
import analyse


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        await analyse.analyse(message)


def main(t):
    print(t)

    intents = discord.Intents.default()
    intents.message_content = True
    client = MyClient(intents=intents)
    client.run(t)


if "__main__" == __name__:
    token = conf.token()
    main(token)
