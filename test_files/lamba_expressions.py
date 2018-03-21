scifi_authors = ["Isaac Asimov", "Ray Bradbury", "Jeremy Quentzel", "Bruce Peter Wainer", "Jaclyn Samantha Roumm"]
print(scifi_authors)
scifi_authors.sort(key=lambda x: x.split(" ")[-1].lower())
print(scifi_authors)
