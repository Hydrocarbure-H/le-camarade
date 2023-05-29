import random

import conf
from generation.chatgpt import gpt_answer
from resources.messages import Messages, messages
from generation.joke import get_gif
from db.db import connect


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


async def lecamarade_actions(message):
    """
    Send a message because of a insult. From chatgpt or from a list of messages
    :param message: Message object
    :return: Nothing
    """
    answer = gpt_answer(message.content)
    if answer is not None:
        await message.channel.send(message.author.mention + " " + answer)
    else:
        await message.channel.send(
            "Désolé camarade " + message.author.mention + " je n'ai pas compris ! Mon savoir est probablement "
                                                          "surchargé.")


async def insult_actions(message):
    """
    Send a message because of a insult. From chatgpt or from a list of messages
    :param message: Message object
    :return: Nothing
    """

    if str(conf.lecamarade_mentionned()) in message.content:
        answer = gpt_answer(message.content)
        if answer is not None:
            await message.channel.send(message.author.mention + " " + answer)

    # Test an answer from chatgpt
    answer = gpt_answer(message.content)
    if answer is not None:
        await message.channel.send(answer)
    else:
        if random.randint(0, 20) == 0:
            await message.add_reaction('👍')
        else:
            camarades = conf.camarades()
            if str(message.author) in camarades:
                if random.randint(0, 1) == 0:
                    await message.add_reaction('📝')
                else:
                    await message.channel.send(
                        "Très bien, " + message.author.mention + ", je note.")
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


def insert_user_action_db(message, value):
    db = connect()
    # Get user id
    sql = "UPDATE users SET score = score + %s WHERE pseudo = %s"
    cursor = db.cursor()
    cursor.execute(sql, (value, str(message.author)))
    db.commit()
