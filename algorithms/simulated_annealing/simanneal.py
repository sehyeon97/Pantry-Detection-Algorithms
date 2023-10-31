import random
import string
import nltk
from nltk.corpus import wordnet as wn
import warnings

# Filter out the nltk redundant search warnings
warnings.filterwarnings("ignore", category=UserWarning, module="nltk.corpus.reader.wordnet")


food = wn.synset('food.n.02')

english_dictionary = list(set([w for s in food.closure(lambda s:s.hyponyms()) for w in s.lemma_names()]))

def generate_neighbor(word):
    # Randomly select one of the following operations: insert, delete, replace
    operation = random.choice(["insert", "delete", "replace"])
    
    if operation == "insert":
        # Insert a random letter at a random position in the word
        position = random.randint(0, len(word))
        letter = random.choice(string.ascii_lowercase)
        return word[:position] + letter + word[position:]
    
    elif operation == "delete":
        # Delete a random character from the word
        if len(word) > 1:
            position = random.randint(0, len(word) - 1)
            return word[:position] + word[position+1:]
        else:
            return word  # Don't delete if word length is 1

    else:
        # Replace a random character with a random letter
        position = random.randint(0, len(word) - 1)
        letter = random.choice(string.ascii_lowercase)
        return word[:position] + letter + word[position+1:]

def objective_function(word):
    # Calculate a simple score based on whether the word is in the dictionary
    return 1 if word in english_dictionary else 0

def simulated_annealing(word, initial_temperature, cooling_rate, num_iterations):
    current_solution = word
    current_score = objective_function(current_solution)
    best_solution = current_solution
    best_score = current_score

    for iteration in range(num_iterations):
        temperature = initial_temperature / (1 + iteration)
        
        neighbor_solution = generate_neighbor(current_solution)
        neighbor_score = objective_function(neighbor_solution)

        if neighbor_score > current_score or random.random() < pow(2.71828, (neighbor_score - current_score) / temperature):
            current_solution = neighbor_solution
            current_score = neighbor_score

            if current_score > best_score:
                best_solution = current_solution
                best_score = current_score

    return best_solution

# Example usage
misspelled_word = "asparahus"
corrected_word = simulated_annealing(misspelled_word, initial_temperature=10, cooling_rate=0.1, num_iterations=10000)
print(f"Misspelled word: {misspelled_word}")
print(f"Guessed correction: {corrected_word}")

