# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math 


# Get the inputs from the user
def get_user_input():
    grade_list = []
    n_student = 5
    for _ in range(0, n_student):
        grade_list.append(int(input('Enter a number: ')))
    return grade_list

# Calculate the mean and standard deviation of the grades
def get_mean(grade_list):
    sum = 0
    for grade in grade_list:
        sum = sum + grade
    return sum / len(grade_list)


def print_stat():
    grade_list = get_user_input()
    get_mean(grade_list)
    sd = 0
    sum_of_sqrs = 0
    for grade in grade_list:
        sum_of_sqrs += (grade - mean) ** 2
    sd = math.sqrt(sum_of_sqrs / len(grade_list))
    # print out the mean and standard deviation in a nice format.
    print('****** Grade Statistics ******')
    print("The grades's mean is:", mean)
    print('The population standard deviation of grades is: ', round(sd, 3))
    print('****** END ******')

print_stat()