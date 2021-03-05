# by Kami Bigdely
# Extract class
WELL_DONE = 3000
MEDIUM = 2500
COOKED_CONSTANT = 0.05


def is_cookeding_criteria_satisfied(food):
    return is_well_done(
            food.time, 
            food.temperature, 
            food.pressure, 
            food.desired_state
        ) or
        is_medium(
            food.time, 
            food.temperature, 
            food.pressure, 
            food.desired_state
        )


def is_well_done(food):    
    return get_cooking_progress(
        food.time, 
        food.temperature, 
        food.pressure) >= WELL_DONE


def is_medium(food):
    return get_cooking_progress(
            food.time, 
            food.temperature, 
            food.pressure
        ) >= MEDIUM

def get_cooking_progress(food):
    return food.time * food.temperature * food.pressure * food.COOKED_CONSTANT


my_steak = {
    time: 30
    temp: 103
    pressue: 20
    desired_state: 'well-done'
}

if is_cookeding_criteria_satisfied(my_steak):
    print('cooking is done.')
else:
    print('ongoing cooking.')