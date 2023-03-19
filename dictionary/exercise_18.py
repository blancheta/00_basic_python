# TODO: Write a Python program
#       to filter students depending on height and weight

dict1 = {
    'Cierra Vega': (6.2, 70),
    'Alden Cantrell': (5.9, 65),
    'Kierra Gentry': (5.8, 65),
    'Pierre Cox': (5.8, 66)
}


def exercise_18(dict1, height, weight):
    res_list = []
    for key, value in dict1.items():
        if value[0] == height and value[1] == weight:
            res_list.append(key)
    return res_list


assert set(exercise_18(dict1, 6.2, 70)) == set(["Cierra Vega"])
assert set(exercise_18(dict1, 5.8, 66)) == set(["Pierre Cox"]) # not ["Cierra Vega", "Pierre Cox"]
