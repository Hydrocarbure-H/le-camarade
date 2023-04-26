from enum import Enum

ironic_phrases = [
    "Ah, bien sûr, c'est vraiment mal de dire la vérité. Mais bon, on peut tous convenir que vivre dans un monde de mensonges est tellement plus agréable, n'est-ce pas ?",
    "Oh, dire du mal des autres, c'est vraiment mal... mais avouons-le, ça donne un petit piment à nos vies, un peu comme un feuilleton dramatique sans fin.",
    "Oui, oui, critiquer les goûts des autres, c'est vraiment mal, mais bon, il est tellement amusant de se sentir intellectuellement supérieur en rabaissant les choix artistiques d'autrui.",
    "On ne devrait jamais rire des malheurs des autres, c'est vraiment pas bien. Mais soyons honnêtes, un petit éclat de rire discret ne fait de mal à personne, n'est-ce pas ?",
    "\"Ne juge pas un livre par sa couverture\", c'est bien connu. Mais sérieusement, qui a besoin de s'embêter à lire quand on peut juste juger les gens sur leur apparence ?",
    "Critiquer la nourriture des autres, c'est vraiment mal élevé. Cependant, on peut tous admettre que c'est tellement amusant de se plaindre des plats lors d'un dîner, ça crée une ambiance légère, n'est-ce pas ?",
    "Bien sûr, il ne faut jamais se moquer des rêves et des ambitions des autres. Mais sérieusement, qui n'aime pas éclater de rire devant une liste de résolutions du Nouvel An qui n'a jamais été suivie ?",
    "Oui, il est mal de juger les livres par leur popularité, mais soyons honnêtes, rien ne vaut le plaisir de se sentir supérieur en critiquant un best-seller.",
    "Bien sûr, se moquer des modes et des tendances, c'est vraiment pas bien. Mais admettons-le, ça fait tellement du bien de se sentir rebelle en refusant de suivre les dernières tendances.",
    "Oui, il est mal de généraliser, mais franchement, qui n'aime pas faire des généralisations de temps en temps ? C'est tellement pratique et ça économise tellement d'énergie intellectuelle.",
    "Loin des yeux, loin du cœur, mais bien sûr, l'ignorance totale est la clé d'une relation solide.",
    "Les voyages forment la jeunesse, à moins que vous ne préfériez rester confortablement installé sur votre canapé toute votre vie.",
    "Un homme averti en vaut deux, mais soyons honnêtes, qui a besoin de prévoir et de se préparer quand on peut improviser dans l'anarchie la plus totale ?",
    "La patience est une vertu, mais passons à autre chose, la vie est trop courte pour attendre.",
    "Rien ne sert de courir, sauf si vous voulez épuiser complètement votre énergie et arriver en sueur et hors d'haleine.",
    "Mieux vaut prévenir que guérir, sauf si vous aimez vivre dangereusement et prendre des risques insensés.",
    "Tel est pris qui croyait prendre, mais ne vous inquiétez pas, vous pouvez toujours vous rattraper en prétendant que vous le saviez depuis le début.",
    "L'argent ne fait pas le bonheur, mais soyons réalistes, il peut certainement vous acheter beaucoup de choses agréables.",
    "La curiosité est un vilain défaut, mais franchement, qui peut résister à l'envie de tout savoir et de se mêler de ce qui ne le regarde pas ?",
    "La vérité sort de la bouche des enfants, mais sérieusement, qui a besoin d'entendre des choses honnêtes et sans filtre ?",
    "Le célibat, c'est tellement génial qu'on se demande pourquoi tout le monde se précipite pour être en couple.",
    "Être célibataire, c'est la meilleure façon de garantir une tranquillité absolue et un contrôle total de la télécommande.",
    "Rien de tel que le célibat pour se sentir libre comme l'air et éviter les disputes interminables sur le choix du restaurant.",
    "Le célibat offre une merveilleuse occasion de passer du temps avec soi-même et de s'adonner à ses propres excentricités sans jugement.",
    "Les relations sont bien trop compliquées de toute façon, alors autant profiter de l'indépendance et de la simplicité du célibat.",
    "Qui a besoin d'un partenaire quand on peut se réveiller tous les matins sans avoir à justifier l'emplacement du couvercle des toilettes ?",
    "Le célibat permet de préserver son espace personnel et de s'endormir en étoile sur le lit sans se soucier de l'autre moitié.",
    "Les avantages du célibat : pas de compromis, pas de drame, et un réfrigérateur rempli exclusivement de sa nourriture préférée.",
    "Être célibataire, c'est comme avoir une licence de liberté totale sans aucune restriction de date d'expiration.",
    "Le célibat est la voie royale vers l'autonomie, l'épanouissement personnel et la maîtrise de l'art de regarder des séries en pyjama.",
    "Oh, super, je suis absolument ravi de répondre à la même question pour la dixième fois aujourd'hui. C'est exactement comme ça que je voulais passer ma journée.",
    "Oui, bien sûr, prenez votre temps pour répondre. Je suis ici depuis des heures de toute façon, et je n'ai rien d'autre à faire que d'attendre.",
    "Ah, bravo ! Vous avez vraiment surpassé toutes les attentes en posant une question évidente. Je suis émerveillé par votre perspicacité.",
    "Génial, maintenant vous avez réussi à me faire douter de ma propre existence. Je suis tellement impressionné par votre capacité à remettre en question la réalité.",
    "Félicitations, vous avez réussi à formuler la remarque la plus brillante et pertinente de la journée. Je ne sais pas comment je vais me remettre de tant d'intelligence concentrée.",
    "Oh, je vois, vous êtes le seul expert mondial dans ce domaine. Je devrais m'agenouiller devant votre immense savoir et abandonner toute prétention d'avoir une opinion différente.",
    "Parfait, maintenant que vous avez exprimé votre opinion de manière extrêmement bruyante, je suppose que cela signifie que vous avez automatiquement raison. Je devrais renoncer à tout raisonnement logique et me prosterner devant votre supériorité.",
    "Vous avez raison, je suis tellement stupide de penser différemment de vous. Je vais immédiatement abandonner ma pensée indépendante et me conformer à vos brillantes idées.",
    "Oh, je suis ravi de voir que vous avez décidé de jouer au jeu du débat en utilisant uniquement des insultes personnelles. C'est tellement constructif et mature.",
    "Votre argumentation est tellement convaincante que je suis prêt à abandonner toutes mes convictions et à me prosterner devant votre sagesse infinie. Ou peut-être pas."
]

liens_gifs_drifts = [
    "https://media.giphy.com/media/69iv77x8e5NMA/giphy.gif",
    "https://media.giphy.com/media/10cXff6xep02Na/giphy.gif",
    "https://media.giphy.com/media/qQM7QHr3TYFwI/giphy.gif",
    "https://media.giphy.com/media/k2evHZ2EvAV5m/giphy.gif",
    "https://media.giphy.com/media/xB8Q4ILnknAgm4H5tq/giphy.gif",
    "https://media.giphy.com/media/Y8dKrq2sDjQ5y/giphy.gif",
    "https://media.giphy.com/media/9F2VWRiJypeBq/giphy.gif",
    "https://media.giphy.com/media/WJZbQEoljvfxK/giphy.gif",
    "https://media.giphy.com/media/Y1Fd98SJo8TlK8W9cr/giphy.gif",
]

messages = [
    ironic_phrases,
    liens_gifs_drifts
]


class Messages(Enum):
    PHRASES = 0
    GIFS = 1
