from enum import Enum

# Create a list from 2 files
with open("resources/keywords/insults/1.txt", 'r') as f:
    file1 = f.readlines()
with open("resources/keywords/insults/2.txt", 'r') as f:
    file2 = f.readlines()
with open("resources/keywords/insults/3.txt", 'r') as f:
    file3 = f.readlines()
with open("resources/keywords/insults/4.txt", 'r') as f:
    file4 = f.readlines()
with open("resources/keywords/insults/5.txt", 'r') as f:
    file5 = f.readlines()

insults_keywords = [x.strip() for x in file1] + [x.strip() for x in file2] + [x.strip() for x in file3] + [x.strip() for
                                                                                                           x in
                                                                                                           file4] + [
                       x.strip() for x in file5]
with open("resources/keywords/negative/1.txt", 'r') as f:
    file1 = f.readlines()

negative_keywords = [x.strip() for x in file1]
drift_keywords = ['drift', 'glisse', 'glissé']
haha_keywords = ['mdr', 'lol', 'ptdr', 'haha']

keywords = [insults_keywords, drift_keywords, haha_keywords, negative_keywords]


class Keywords(Enum):
    INSULT = 0
    DRIFT = 1
    HAHA = 2
    NEGATIVE = 3
    OTHER = 4
    CAMARADE = 5
