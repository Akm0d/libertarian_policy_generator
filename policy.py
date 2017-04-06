#!/usr/bin/env python3
# coding=utf-8
from random import choice


libertarian = (
    "A truly free society must allow",
    "To truly be liberated we must enable",
    "It is a fundamental right for",
    "After we take over and leave everyone alone, we will authorize",
    "Only in a Libertarian utopia will we enable",
    "Unlike the Statists, we will allow"
)

subject = (
    "five year old children",
    "ethnic minorities",
    "convicted felons",
    "college students",
    "priviliged white males",
    "Ron Paul, Rand Paul, and Ayn Rand",
    "the homeless",
    "business owners",
    "gay couples"
)

action = (
    "to fire people based only on their #identity.",
    "to own and operate rocket launchers.",
    "to perform open heart surgery with a coat hanger.",
    "to defend their marijuana fields with fully automatic machine guns.",
    "to sell lemonade without a permit"
)

identity = (
    "sexual orientation",
    "race",
    "religion",
    "gender",
    "political beliefs"
)


def get_policy():
    return choice(libertarian) + " " +  choice(subject) +  " " + choice(action)


if __name__ == "__main__":
    print(get_policy())

