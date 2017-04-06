#!/usr/bin/env python3
# coding=utf-8
from random import choice


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
    "Conservative",
    "Liberal",
    "Leftist",
    "Republican",
    "Democrat",
    "Facist",
    "Communist",
    "Socialist",
    "statist",
    "Progressive",
    "Nazi"
)

profession = (
    "school teacher",
    "programmer",
    "rocket scientist",
    "potato farmer",
    "mechanic",
    "medical doctor",
    "fast food server",
    "professor",
    "teacher",
    "philosopher",
    "anesthesiologist",
    "audiologist",
    "chiropractor",
    "dentist",
    "dietitian",
    "nurse",
    "occupational therapist",
    "pharmacist",
    "optometrist",
    "pharmacist",
    "physical therapist",
    "physician",
    "podiatrist",
    "psychologist",
    "radiographer",
    "radiotherapist",
    "speech-language pathologist",
    "surgeon",
    "veterinarian",
    "accountant",
    "actuarie",
    "architect",
    "engineer",
    "linguistic",
    "translator",
    "interpreter",
    "surveyor",
    "urban Planner",
    "air traffic controller",
    "aircraft pilot",
    "scientist",
    "astronomer",
    "biologist",
    "botanist",
    "ecologist",
    "geneticist",
    "immunologist",
    "paleontologist",
    "pharmacologist",
    "virologist",
    "zoologist",
    "chemist",
    "geologist",
    "meteorologist",
    "neuroscientist",
    "oceanographer",
    "physicist"
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
    "paying a sales tax",
    "being fined",
    "a permit",
    "government approval",
    "a license",
    "being investigated",
    "competing with a government created monopoly",
    "the government's permission",
    "full body searches",
    "background checks",
    "a city permit"
)

libertarian = (
    "Libertarians fundamentaly allow",
    "It is a natural human right for",
    "A government's principal duty is to protect the right of",
    "Hardcore libertarians believe that we should allow",
    "Unlike the " + choice(party) + "s, libertarians would allow",
    "A truly free society must allow",
    "To truly be liberated we must enable",
    "It is a fundamental right for",
    "After we take over and leave everyone alone, we will authorize",
    "Only in a Libertarian utopia will we enable"
)

action = (
    "to refuse to bake a cake for someone based on their " + choice(identity) + ".",
    "to walk their dog without " + choice(without) + ".",
    "to board an airplane without " + choice(without) + ".",
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

