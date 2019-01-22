favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("Sarah's favourite language is " + 
    favourite_languages['sarah'].title() + ".")

for n, l in favourite_languages.items():
    print(n.title() + "'s favourite language is " +
    l.title() + ".")

for name in favourite_languages.keys():
    print(name.title())

for language in favourite_languages.values():
    print(language.title())

if 'erin' not in favourite_languages.keys():
    print("Erin, please take our poll!")

