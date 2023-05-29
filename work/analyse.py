import conf
from resources.keywords import Keywords, keywords
from work.process import haha_actions, drift_actions, insult_actions, default_actions, lecamarade_actions, \
    insert_user_action_db
from generation.chatgpt import gpt_talk
from db.db import connect


async def analyse(message, social_score=False):
    """
    Analyse the message to see if it contains a keyword
    :param message: The discord message object
    :return: Nothing
    """

    t = check_content(message.content)
    if t is not None:
        # Check for haha
        if t == Keywords.HAHA:
            print("HAHA KEYWORD")
            if social_score:
                insert_user_action_db(message, 10)
            await haha_actions(message)
            return
        # Check for drift (GIFTS)
        elif t == Keywords.DRIFT:
            print("DRIFT KEYWORD")
            if social_score:
                insert_user_action_db(message, 5)
            await drift_actions(message)
            return
        # Check for insults
        elif t == Keywords.INSULT:
            print("INSULT KEYWORD")
            if social_score:
                insert_user_action_db(message, -10)
            await insult_actions(message)
            return
        # Check for other keywords (only discriminative)
        elif t == Keywords.OTHER:
            print("OTHER KEYWORD")
            if social_score:
                insert_user_action_db(message, -5)
            await default_actions(message)
            return
        elif t == Keywords.CAMARADE:
            print("CAMARADE KEYWORD")
            if social_score:
                insert_user_action_db(message, 1)
            await lecamarade_actions(message)
            return


def check_content(text):
    """
    Check the content of the message to see if it contains a keyword
    :param text: The full message
    :return: The keyword index if found, None otherwise
    """
    txt = text.lower()

    # # Check if the txt contains a insult keyword
    if any(x in txt for x in keywords[Keywords.INSULT.value]):
        return Keywords.INSULT

    # Check if the txt contains a drift keyword
    if any(x in txt for x in keywords[Keywords.DRIFT.value]):
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
    answer = gpt_talk(message.content)
    if answer is not None:
        await message.channel.send(answer)
    else:
        await message.channel.send(
            "Je n'ai pas compris, camarade. Il est possible que mon savoir soit actuellement surchargé.")
    return


def display_scoreboard():
    """
    Display the scoreboard
    :return: Nothing
    """
    db = connect()
    cursor = db.cursor()
    # Get the users
    cursor.execute("SELECT pseudo,score FROM users")
    users = cursor.fetchall()
    db.close()

    # Sort the list by score
    users.sort(key=lambda x: x[1], reverse=True)

    # format the result for discord

    response = "Voici le social scoreboard actuel cher camarades ! \n"
    response += "**==============================**\n"
    response += "**         :heart: : Les camarades :heart:**\n"
    response += "                                  \n"
    response += "                                  \n"
    for user in users:
        username, score = user
        # If the value is negative, add an emoji
        if score < 0:
            response += f"- ||:skull: - {username} : **{score}**||\n"
        else:
            response += f"- ||:flag_cn: - {username} : **{score}**||\n"
    response += "                                  \n"
    response += "                                  \n"
    print("Nous devons donc maintenant prendre exemple sur " + users[0][0] + " qui est le meilleur camarade !")
    response += "                                  \n"
    response += "                                  \n"
    response += "**==============================**\n"

    return response
