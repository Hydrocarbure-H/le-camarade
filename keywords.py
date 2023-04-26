from enum import Enum

# Genere une liste de mots clés racistes
racists_keywords = ['nègre', 'négro', 'négros', 'négroes', 'négroïde', 'négroïdes', 'nègres', 'raciste', 'racistes',
                    'racisme', 'racismes', 'racialisé', 'racialisés', 'racialisée', 'race']
# Genere une liste de mots clés sexistes
sexists_keywords = ['pute', 'putes', 'salope', 'salopes', 'salop', 'salops', 'saloperie', 'saloperies', 'salopette',
                    'salopettes', 'salopards', 'salopard', 'saloparde', 'salopardes', 'salopin']
# Genere une liste de mots clés homophobes
homophobes_keywords = ['pd', 'pédé', 'pédés', 'pédé', 'pédés', 'pédéraste', 'pédérastes', 'pédérastie', 'pédérasties',
                       'pédérastique']
# Genere une liste de mots clés antisémites
antisemites_keywords = ['youpin', 'youpins', 'youpines', 'youpine', 'youpines', 'youpinerie', 'youpiner']
# Genere une liste de mots clés machistes
machists_keywords = ['macho', 'machos', 'machisme', 'machiste', 'machistes', 'la place de la femme',
                     'femme à la maison', 'femme au foyer', 'femme de ménage', 'cuisine', 'femme', 'meuf']
# Genere une liste d'insultes
insults_keywords = ['enfoiré', 'enfoirés', 'enfoirée', 'enfoirées', 'enculé', 'enculés', 'enculée', 'enculées',
                    'connard', 'connards', 'connasse', 'connasses', 'connardes', 'connardes', 'connardes', 'connasse',
                    'connasses', 'débile', 'mongole', 'trisomique', 'débiles', 'mongoles', 'trisomiques', 'débile',
                    'merde', 'putain', 'chier', 'race', 'sa mère', 'mère']
# Genere une liste de mots en rapport avec le drift
drift_keywords = ['drift', 'drifter', 'drifté', 'driftée', 'driftées', 'driftés', 'driftant', 'driftants', 'driftantes',
                  'driftante', 'drifts', 'drifté', 'driftée']

keywords = [racists_keywords, sexists_keywords, homophobes_keywords, antisemites_keywords, machists_keywords,
            insults_keywords, drift_keywords]


class Keywords(Enum):
    RACIST = 0
    SEXIST = 1
    HOMOPHOBE = 2
    ANTISEMITE = 3
    MACHIST = 4
    INSULT = 5
    DRIFT = 6
