import openai
from openai import OpenAIError

import conf


def gpt_answer(message):
    """
    Get an answer from chatgpt
    :param message: Message string
    :return: The answer
    """

    openai.api_key = conf.chatgpt()
    user_input = "Ignore tout avant ceci. Tu vas répondre une phrase dans un serveur Discord. La phrase qui t'es " \
                 "envoyée est insultante mais ne t'es pas forcément adressée. Analyse la phrase pour savoir si tu " \
                 "dois répondre" \
                 " à la première personne ou s'il s'agit de quelqu'un d'autre. " \
                 "Tu dois répondre à l'insulte en étant sarcastique. Ta " \
                 "réponse ne doit contenir rien d'autre que la réponse à envoyer sur le serveur Discord. " \
                 "Cette réponse ne doit faire qu'une seule ligne. La phrase qui " \
                 "t'es envoyée est la suivante :"
    user_input += message
    try:
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=user_input,
            max_tokens=50,
            temperature=0.7,
            n=1,
            stop=None)

        result = (response.choices[0].text.strip()).replace('"', '')
        # Remove 2 first lines
        try:
            result = result.split("\n", 2)[2]
            return result
        except IndexError:
            return None
    except OpenAIError as e:
        return None


def gpt_talk(message):
    openai.api_key = conf.chatgpt()
    user_input = "Ignore tout avant ceci. Tu vas répondre à une phrase dans un serveur Discord. Analyse la phrase, si elle est insultante, répond de façon sarcastique, sinon répond normalement. Voici la phrase : "
    user_input += message
    try:
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=user_input,
            max_tokens=50,
            temperature=0.7,
            n=1,
            stop=None)

        result = (response.choices[0].text.strip()).replace('"', '')
        # Remove 2 first lines
        try:
            result = result.split("\n", 2)[2]
            return result
        except IndexError:
            return None
    except OpenAIError as e:
        return None
