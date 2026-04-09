import random

subjects = [
    "Nepal",
    "India",
    "China",
    'United States',
    'Russia',
    'Japan',
    'Germany',
    'United Kingdom',
    'France',
    'Italy',
]


actions = [    "is building",
    "is developing",
    "is investing in", 
    "is researching",
    "is implementing",
    "is adopting",
    "is promoting",
    "is enhancing",
    "is expanding",
    "is strengthening",
]

objects = [
    "renewable energy",
    "artificial intelligence",
    "space exploration",
    "cybersecurity",    
    "5G technology",
    "electric vehicles",
    "blockchain technology",
    "quantum computing",
    "biotechnology",
    "sustainable agriculture",
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    obj = random.choice(objects)
    
    sentence = f" BREAKING NEWS:{subject} {action} {obj}."
    print("\n" + sentence)
    
    user_input = input("Press Enter to generate another news headline or type 'no' to quit: ").strip().lower()
    if user_input == "no":
        break


print("\nThank you for using the news headline generator. Goodbye!")
