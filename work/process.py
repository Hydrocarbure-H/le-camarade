import random

import conf
from generation.chatgpt import gpt_answer
from resources.messages import Messages, messages
from generation.joke import get_gif


async def haha_actions(message):
    """
    Send a message or a gif because of a haha
    :param message: Message object
    :return: Nothing
    """
    if random.randint(0, 1) == 0:
        response = random.randint(0, len(messages[Messages.HAHA.value]) - 1)
        await message.channel.send(messages[Messages.HAHA.value][response])
        return
    else:
        await message.channel.send(get_gif())
        return


async def drift_actions(message):
    """
    Send a gif because of a drift
    :param message: Message object
    :return: Nothing
    """
    response = random.randint(0, len(messages[Messages.GIFS.value]) - 1)
    await message.channel.send(messages[Messages.GIFS.value][response])
    return


async def insult_actions(message):
    """
    Send a message because of a insult. From chatgpt or from a list of messages
    :param message: Message object
    :return: Nothing
    """

    # Check if Le Camarade is mentionned
    if str(conf.lecamarade()) in message.content:
        answer = gpt_answer(message.content)
        if answer is not None:
            await message.channel.send(message.author.mention + " " + answer)

    # Test an answer from chatgpt
    answer = gpt_answer(message.content)
    if answer is not None:
        await message.channel.send(answer)
    else:
        response = random.randint(0, len(messages[Messages.IRNONIC.value]) - 1)
        await message.channel.send("*" + messages[Messages.IRNONIC.value][response] + "*")
    return


async def default_actions(message):
    """
    Send a message because of a discriminative keyword
    Will decrease the score (Or increase if Le Camarade is in Dark mode)
    :param message: Message object
    :return: Nothing
    """

    # Test an answer from chatgpt
    answer = gpt_answer(message.content)
    if answer is not None:
        await message.channel.send(answer)
    else:
        if random.randint(0, 1) == 0:
            await message.add_reaction('👍')
        else:
            camarades = conf.camarades()
            if str(message.author) in camarades:
                await message.add_reaction('📝')
                await message.channel.send(
                    "Attention " + message.author.mention + ", tu as glissé ! Tu veux que ton score baisse ?!")
                # Decrease score TODO
