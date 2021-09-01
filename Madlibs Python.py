
# Init Variables

theMatrix = ""
system = ""
Neo = ""
enemy = ""
inside = ""
save = ""
unplugged = ""
inured = ""
dependent = ""
fight = ""

profession = ["", "", "", ""]
adj = ["",""]

# Get input from User

print("Welcome User")
print("Let's play a game fo Madlibs!")
neo = input("Please share with me your name: ")

print("Hello {Neo}! Are you ready?")
theMatrix = input("What is something you want to know more about: ")

print(f"Oooh! You want to know more about {theMatrix} huh: ")
print(f"Okay well first, tell me what you already know about {theMatrix}")
system = input(f"what noun would you categorise {theMatrix} as: ")

enemy = input(f"Give me an opposing noun to {system}: ")

inside = input(f"Now give me any relaxing noun to {system}: ")

print(f"Okay, now I need 4 professions relating to {system}")

for i in range(len(profession)):
    profession[i] = input(f"Profession (plural) {i+i} / {len(profession)}")

save = input(f"Give me a hero-related verb (present tense): ")

unplugged = input(f"Now give me a verb that makes you think about relief (past tense): ")

print(f"Lastly I need 2 dystopian adjectives: ")

for i in range(len(adj)):
    adj[i] = input(f"Adjective {i+i} / {len(adj)}: ")
    
# Init Story
madlibStory = (f"{theMatrix} is a {system}, {Neo}.That {system} is our {enemy}." +
f"But when you're {inside}, you look around, what do you see?" +
f"{profession[0]}, {profession[1]}, {profession[2]}, {profession[3]}." +
f"The very minds of the people we are trying to {save}." +
f"But until we do, these people are still a part of that {system} and that makes them our {enemy}." +
f"You have to understand, most of these people are not ready to be {unplugged}." +
f"And many of them are so {adj[0]}, so hopelessly {adj[1]} on the {system}, that they will {fight} to protect it.")

# Print Story
print (madlibStory)

