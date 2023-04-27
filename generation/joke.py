import random

import requests


def get_gif():
    """
    Get a random gif from the imgflip api
    :return: The url of the gif
    """
    res = requests.get("https://api.imgflip.com/get_memes")
    rand = random.randint(0, len(res.json()["data"]["memes"]) - 1)
    return res.json()["data"]["memes"][rand]["url"]
