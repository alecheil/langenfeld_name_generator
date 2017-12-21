import random


list_of_marks = ["arc",
"ark",
"bark",
"dark",
"hark",
"lark",
"marque",
"narc",
"parc",
"park",
"quark",
"shark",
"spark",
"stark",
"snark",
"demark",
"embark"
]

def find_random_mark():
    last_int = len(list_of_marks)
    index = random.randint(0,last_int)
    return list_of_marks[index]