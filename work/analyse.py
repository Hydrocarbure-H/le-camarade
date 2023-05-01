import conf
from resources.keywords import Keywords, keywords
from work.process import haha_actions, drift_actions, insult_actions, default_actions, lecamarade_actions
from generation.chatgpt import gpt_talk


async def analyse(message):
    """
    Analyse the message to see if it contains a keyword
    :param message: The discord message object
    :return: Nothing
    """

    t = check_content(message.content)
    if t is not None:
        # Check for haha
        if t == Keywords.HAHA:
            await haha_actions(message)
            return
        # Check for drift (GIFTS)
        elif t == Keywords.DRIFT:
            await drift_actions(message)
            return
        # Check for insults
        elif t == Keywords.INSULT:
            await insult_actions(message)
            return
        # Check for other keywords (only discriminative)
        elif t == Keywords.OTHER:
            await default_actions(message)
            return
        elif t == Keywords.CAMARADE:
            await lecamarade_actions(message)
            return


def check_content(text):
    """
    Check the content of the message to see if it contains a keyword
    :param text: The full message
    :return: The keyword index if found, None otherwise
    """
    txt = text.lower()

    # Check if the txt contains a insult keyword
    if any(x in txt for x in keywords[Keywords.INSULT.value]):
        return Keywords.INSULT

    # Check if the txt contains a drift keyword
    elif any(x in txt for x in keywords[Keywords.DRIFT.value]):
        return Keywords.DRIFT

    # Check if the txt contains a haha keyword
    elif any(x in txt for x in keywords[Keywords.HAHA.value]):
        return Keywords.HAHA

    elif str(conf.lecamarade_mentionned()) in text:
        return Keywords.CAMARADE

    # Check if the txt contains a discriminative keyword in all the other keywords
    else:
        for i in range(0, len(keywords)):
            if i not in [Keywords.HAHA.value, Keywords.DRIFT.value, Keywords.INSULT.value]:
                if any(x in txt for x in keywords[i]):
                    return Keywords.OTHER


async def talk_with_gpt(message):
    """
    Talk with GPT
    :param message: Message object
    :return: Nothing
    """
    print("GPT is talking")
    answer = gpt_talk(message.content)
    if answer is not None:
        await message.channel.send(answer)
    else:
        await message.channel.send(
            "Je n'ai pas compris, camarade. Il est possible que mon savoir soit actuellement surchargé.")
    return
