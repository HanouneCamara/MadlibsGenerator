# Ouvre le fichier "story.txt" en mode lecture et le stocke dans la variable f
with open("story.txt", "r") as f:
    # Lit tout le contenu du fichier et le stocke dans la variable story
    story = f.read()

# Crée un ensemble vide pour stocker les mots extraits du texte
words = set()

# Initialise la position de début de mot à -1
start_of_word = -1

# Définit les chaînes cibles pour repérer le début et la fin des mots
target_start = "<"
target_end = ">"

# Parcours chaque caractère du texte avec son index
for i, char in enumerate(story):
    # Si le caractère actuel est le début d'un mot
    if char == target_start:
        # Enregistre la position actuelle comme début du mot
        start_of_word = i
    
    # Si le caractère actuel est la fin d'un mot et qu'un début de mot a été trouvé
    if char == target_end and start_of_word != -1:
        # Extrait le mot du texte en utilisant les indices start_of_word et i
        word = story[start_of_word: i + 1]
        # Ajoute le mot extrait à l'ensemble words
        words.add(word)
        # Réinitialise la position de début de mot
        start_of_word = -1

# Crée un dictionnaire vide pour stocker les réponses de l'utilisateur
answers = {}

# Demande à l'utilisateur d'entrer des réponses pour chaque mot extrait
for word in words:
    answer = input("Enter a word for " + word + ": ")
    # Stocke la réponse de l'utilisateur dans le dictionnaire answers
    answers[word] = answer

# Parcours à nouveau les mots extraits et remplace chaque occurrence dans le texte
for word in words:
    story = story.replace(word, answers[word])

# Affiche la nouvelle version de l'histoire avec les mots remplacés
print(story)
