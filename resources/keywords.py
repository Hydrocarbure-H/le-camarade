from enum import Enum

# All of the following keywods have been generated using the GithubCopilot AI
# Genere une liste de mots clés racistes
racists_keywords = ['nègre', 'négro', 'négros', 'négroes', 'négroïde', 'négroïdes', 'nègres', 'raciste', 'racistes',
                    'racisme', 'racismes', 'racialisé', 'racialisés', 'racialisée', 'race']
sexists_keywords = ['pute', 'putes', 'salope', 'salopes', 'salop', 'salops', 'saloperie', 'saloperies', 'salopette',
                    'salopettes', 'salopards', 'salopard', 'saloparde', 'salopardes', 'salopin']
homophobes_keywords = ['pd', 'pédé', 'pédés', 'pédé', 'pédés', 'pédéraste', 'pédérastes', 'pédérastie', 'pédérasties',
                       'pédérastique']
antisemites_keywords = ['youpin', 'youpins', 'youpines', 'youpine', 'youpines', 'youpinerie', 'youpiner']
machists_keywords = ['macho', 'machos', 'machisme', 'machiste', 'machistes', 'la place de la femme',
                     'femme à la maison', 'femme au foyer', 'femme de ménage', 'cuisine', 'femme', 'meuf']
insults_keywords = ['enfoiré', 'enfoirés', 'enfoirée', 'enfoirées', 'enculé', 'enculés', 'enculée', 'enculées',
                    'connard', 'connasse',
                    'connasses', 'débile', 'mongole', 'trisomique', 'poutre', 'merde', 'putain', 'chier', 'race',
                    'sa mère',
                    'pute', 'putes', 'salope', 'nain', 'sale petit']
drift_keywords = ['drift', 'glisse', 'glisser', 'glissé', 'glissée']
haha_keywords = ['mdr', 'lol', 'ptdr', 'haha']

keywords = [racists_keywords, sexists_keywords, homophobes_keywords, antisemites_keywords, machists_keywords,
            insults_keywords, drift_keywords, haha_keywords]


class Keywords(Enum):
    OTHER = 9
    RACIST = 0
    SEXIST = 1
    HOMOPHOBE = 2
    ANTISEMITE = 3
    MACHIST = 4
    INSULT = 5
    DRIFT = 6
    HAHA = 7
    CAMARADE = 8
