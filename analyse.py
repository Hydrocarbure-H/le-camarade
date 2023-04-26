import random

from messages import Messages, messages
from keywords import Keywords, keywords
import conf


async def analyse(message):
    type = check_content(message.content)
    if type is not None:
        rand = random.randint(0, 2)
        if rand == 0:
            gif_or_msg = random.randint(0, 1)
            number = random.randint(0, len(messages[gif_or_msg]) - 1)
            await message.channel.send(messages[gif_or_msg][number])
        elif rand == 1:
            await message.add_reaction('👍')
            await message.channel.send("Pour le coup, entièrement d'accord avec toi !")
        elif rand == 2:
            camarades = conf.camarades()
            if message.author in camarades:
                await message.add_reaction('👍')
                await message.channel.send(
                    "Attention @" + message.author.name + ", tu as glissé ! N'oublies pas le social score board...!")


def check_content(text):
    # Do a switch case will all lists

    txt = text.lower()

    # Check if the txt contains a sexist keyword
    # Check if the txt contains a sexist keyword
    if any(x in txt for x in keywords[Keywords.SEXIST.value]):
        return Keywords.SEXIST

    # Check if the txt contains a racist keyword
    elif any(x in txt for x in keywords[Keywords.RACIST.value]):
        return Keywords.RACIST

    # Check if the txt contains a homophobe keyword
    elif any(x in txt for x in keywords[Keywords.HOMOPHOBE.value]):
        return Keywords.HOMOPHOBE

    # Check if the txt contains a antisemite keyword
    elif any(x in txt for x in keywords[Keywords.ANTISEMITE.value]):
        return Keywords.ANTISEMITE

    # Check if the txt contains a machist keyword
    elif any(x in txt for x in keywords[Keywords.MACHIST.value]):
        return Keywords.MACHIST

    # Check if the txt contains a insult keyword
    elif any(x in txt for x in keywords[Keywords.INSULT.value]):
        return Keywords.INSULT

    # Check if the txt contains a drift keyword
    elif any(x in txt for x in keywords[Keywords.DRIFT.value]):
        return Keywords.DRIFT
