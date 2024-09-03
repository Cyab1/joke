# importing the random module. 
import random

# Create a list of jokes.
jokes = [
    "why don't skeletons fight each other? They don't have the guts.",
    "I used to play piano by ear, but now I use my hands",
    "I'm reading a book on anti-gravity. It's impossible to put down!",
    "Parallel lines have so much in common. It's a shame they'll never meet.",
    "Why did the bicycle fall over? Because it was two-tired!",
    "Why did the math book look sad? Because it had too many problems.",
    "I told my computer I needed a break. Now it won't stop sending me vacation ads!",
]


# Use the random module to select a joke randomly.
random_joke = random.choice(jokes)

# Print out the randomly selected joke.
print(random_joke)
