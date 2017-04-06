#!/usr/bin/env python3
# coding=utf-8
from random import choice


libertarian = (
    "It is a natural human right for",
    "A government's principal duty is to protect the right of",
    "Hardcore libertarians believe that we should allow",
    "The difference between libertarianism and socialism is that libertarians will tolerate",
    "A truly free society must allow",
    "To truly be liberated we must enable",
    "It is a fundamental right for",
    "After we take over and leave everyone alone, we will authorize",
    "Only in a Libertarian utopia will we enable",
    "Unlike the Statists, we will allow"
)

subject = (
    "five year old children",
    "progressive liberals",
    "anyone",
    "Gary Johnson",
    "Austin Petersen",
    "radical conservatives",
    "ethnic minorities",
    "convicted felons",
    "college students",
    "priviliged white males",
    "Ron Paul, Rand Paul, and Ayn Rand",
    "the homeless",
    "business owners",
    "gay couples",
    "people driving cars",
    "large corporations",
    "the 1%"
)

identity = (
    "favorite color",
    "skill level",
    "ability",
    "education",
    "sexual orientation",
    "race",
    "religion",
    "gender",
    "political beliefs",
    "preferred brand of vehicle"
)

party = (
    "Independant",
    "Libertarian",
    "Republican",
    "Democrat",
    "Facist",
    "Communist",
    "Socialist",
    "statist",
    "Progressive",
    "Constitutionalist",
    "Nazi"
)

profession = (
    "school teacher",
    "programmer",
    "rocket scientist",
    "potato farmer",
    "mechanic",
    "medical doctor",
    "congress representative",
    "fast food server",
    "Professors",
    "Teachers",
    "Cultural[edit]",
    "Clergy",
    "Philosopher",
    "Medical[edit]",
    "Anesthesiologist",
    "Audiologist",
    "Chiropractor",
    "Dentist",
    "Dietitian",
    "Nurses",
    "Occupational therapist",
    "Pharmacist",
    "Operating Department Practitioner",
    "Optometrist",
    "Pharmacist",
    "Physical therapist",
    "Physician",
    "Podiatrist",
    "Psychologist",
    "Radiographer",
    "Radiotherapist",
    "Speech-language pathologist",
    "Surgeon",
    "Veterinarian",
    "Accountant",
    "Actuarie",
    "Architect",
    "Engineer",
    "Linguistic",
    "Translator",
    "Interpreter",
    "Surveyor",
    "Urban Planner",
    "Air traffic controller",
    "Aircraft pilot",
    "Sea captain",
    "Lawyers",
    "Social Workers",
    "Health inspector",
    "Park ranger",
    "Police officer",
    "Military officer",
    "Scientist",
    "Astronomer",
    "Biologist",
    "Botanist",
    "Ecologist",
    "Geneticist",
    "Immunologist",
    "Paleontologist",
    "Pharmacologist",
    "Virologist",
    "Zoologist",
    "Chemist",
    "Geologist",
    "Meteorologist",
    "Neuroscientist",
    "Oceanographer",
    "Physicist"
)

adjective = (
    "femminist",
    "chovenist",
    "polygymist"
)

objects = (
    "rocket launchers",
    "coat hangers",
    "fully automatic machine guns",
    "land mines",
    "gasoline",
    "explosives",
    "machetes",
    "3D printed medical equipment",
    "tractors",
    "robots",
    "paperclips",
    "a barn"
)

products = (
    "oranges",
    "whatever they want",
    "marijuana",
    "lemonade",
    "tamales",
    "firearms",
    "property",
    "gasoline",
    "rainwater"
)

without = (
    "paying a tax",
    "a permit",
    "government approval",
    "the government's permission",
    "consent",
    "a city permit"
)

action = (
    "to buy " + choice(products) + " without " + choice(without) + ".",
    "to continue living on property they have already purchased without " + choice(without) + ".",
    "to collect " + choice(products) + ".",
    "to fire " + choice(profession) + "s based only on their " + choice(identity) + ".",
    "to fire " + choice(profession) + "s soley because they may be " + choice(adjective + party) + ".",
    "to hire people based only on their " + choice(identity) + ".",
    "to own and operate " + choice(objects) + ".",
    "to perform open heart surgery with " + choice(objects) + ".",
    "to defend their marijuana fields with " + choice(objects) + ".",
    "to sell " + choice(products) + " without " + choice(without) + ".",
    "to take down trees with " + choice(objects) + " on their own property.",
    "to paint their house without " + choice(without) + ".",
    "to get married without " + choice(without) + ".",
    "to build " + choice(objects) + " in their backyard without " + choice(without) + "."
)



def get_policy():
    return choice(libertarian) + " " +  choice((choice(subject),choice(profession) + "s")) +  " " + choice(action)


if __name__ == "__main__":
    print(get_policy())

