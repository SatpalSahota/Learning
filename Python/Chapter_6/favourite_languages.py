favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}


for n, l in favourite_languages.items():
    print(n.title() + "'s favourite language is " +
    l.title() + ".")
print("\n")

for name in favourite_languages.keys():
    print(name.title())
print("\n")

for language in favourite_languages.values():
    print(language.title())
print("\n")

for name in sorted(favourite_languages.keys()):
    print(name.title() + ", thank you for taking the poll!.")
print("\n")

if 'erin' not in favourite_languages.keys():
    print("Erin, please take our poll!")
print("\n")

print("The following languages have been mentioned:")
for language in set(favourite_languages.values()):
    print(language.title())
print("\n")

favourite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': 'c',
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favourite_languages.items():
    print("\n" + name.title() + "'s favourite languages are:")
    for language in languages:
        print("\t" + language.title())