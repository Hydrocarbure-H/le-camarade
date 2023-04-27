from keywords import Keywords, keywords
from process import haha_actions, drift_actions, insult_actions, default_actions


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
            haha_actions(message)
            return
        # Check for drift (GIFTS)
        elif t == Keywords.DRIFT:
            drift_actions(message)
            return
        # Check for insults
        elif t == Keywords.INSULT:
            insult_actions(message)
            return
        # Check for other keywords (only discriminative)
        else:
            default_actions(message)


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
    else:
        return None
