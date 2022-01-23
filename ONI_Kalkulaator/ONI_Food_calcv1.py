import json
# automaatne kalkuleerimine toidu genereerimise suhtes
# mealwood

fail = open("foods.json")
data = json.load(fail)

# ver = input("plant or cook calculation: ")

dupe_num = int(input("How many dupes: "))
plant_nam = input("What plant: ")
# plant_quant = int(input("In what quantity: "))
# 

# def calculation_cook(name):
#     if dif == "cook":
        # for i in data[plant]:
        #     for k in i["cook"]:
        #         for l in k[dif]:
        #             calory = l["calories"]
def calculation(dupe, plant):
    
    for i in data[plant]:
        calory = i["calories"]*i["quantity"]
    for i in data[plant]:
        cycle = i["cycle"]

    food = 1000*dupe

    req_plants_max = int((food*cycle)/calory)

    m = req_plants_max * calory
    n = food*int(cycle)
    division = int((m-n)//calory)
    req_plants = req_plants_max - division

    gen_food = req_plants*calory

    plant_data = [req_plants, food, gen_food, cycle, plant, calory, n]
    return plant_data

def switch_plant(i):
    switcher={
        "mealwood":calculation(dupe_num, i),
        "dusk cap":calculation(dupe_num, i),
        "bristle blossom":calculation(dupe_num, i),
        "sleet wheat":calculation(dupe_num, i),
        "waterweed":calculation(dupe_num, i),
        "nosh sprout":calculation(dupe_num, i),
        "bog bucket":calculation(dupe_num, i),
        "grubfruit":calculation(dupe_num, i),
        "spindly grubfruit":calculation(dupe_num, i)
        }
    return switcher.get(i ,"Invalid plant name, did you type it correctly?")

p = switch_plant(plant_nam)
print(p)
print()

print("You should have", p[0], p[4],"plants")
print("Calories required is following:", p[1], "per cycle and in", p[3],"cycles its", p[6])
print("Actually generated calories:", p[2], "in", p[3], "cycles.")
print("")

fail.close()
