def speedometer(pos1, pos2, time):
    dist = abs(pos2-pos1)
    speed = dist/time
    return speed

def animal_average_speed(animal_type):
    if animal_type == 0:
        return 68
    elif animal_type == 1:
        return 88
    elif animal_type == 2:
        return 50
    else:
        return "Invalid Input"
    
def animal_speed_compare(animal1_pos1, animal1_pos2, animal1_time, animal2_type):
    animalSpeed1 = speedometer(animal1_pos1, animal1_pos2, animal1_time)
    animalSpeed2 = animal_average_speed(animal2_type)

    if animalSpeed1 > animalSpeed2:
        return "The first animal is faster"
    else:
        return "The first animal is slower"




