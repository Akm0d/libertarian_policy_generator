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
    "gasoline"
)

action = (
    "to buy " + choice(products) + " without paying sales tax.",
    "to continue living on property they have already purchased without a continual property tax.",
    "to collect rainwater.",
    "to fire people based only on their " + choice(identity) + ".",
    "to hire people based only on their " + choice(identity) + ".",
    "to own and operate " + choice(objects) + ".",
    "to perform open heart surgery with " + choice(objects) + ".",
    "to defend their marijuana fields with " + choice(objects) + ".",
    "to sell " + choice(products) + " without a permit.",
    "to take down trees with " + choice(objects) + " on their own property.",
    "to paint their house without a city permit.",
    "to get married without the government's permission.",
    "to build " + choice(objects) + " in their backyard without a permit."
)



def get_policy():
    return choice(libertarian) + " " +  choice(subject) +  " " + choice(action)


if __name__ == "__main__":
    print(get_policy())

