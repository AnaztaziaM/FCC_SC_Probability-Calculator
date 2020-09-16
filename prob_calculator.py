import copy
import random

class Hat:

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        for v in kwargs.values():
            if v < 1:
                v==1
            else:
                continue
        self.contents = []
        for k,v in kwargs.items():
            number_of_appearance = 0
            while v > number_of_appearance:
                number_of_appearance += 1
                self.contents.append(k)
        k_list = []
        v_list = []
        for k,v in kwargs.items():
            k_list.append(k)
            v_list.append(v)
        self.list = dict(zip(k_list, v_list))

    def __str__(self):
        arguments = self.list
        return arguments

    def draw(self, number):
        contents_pieces = len(self.contents)
        if contents_pieces < number:
            return self.contents
        else:
            number_of_drawing = 0
            list_of_items = []

            contents_new = self.contents

            while number_of_drawing < number:
                number_of_drawing +=1
                random_item = random.choice(self.contents)
                self.contents.remove(random_item)
                list_of_items.append(random_item)
            return list_of_items


#defind a funcion what compare two list even if its contains identilcal number.
def check_if_contains(a, b):
    a_sorted = sorted(a)
    b_sorted = sorted(b)
    it = iter(b_sorted)
    return all(c in it for c in a_sorted)

def experiment (hat, expected_balls, num_balls_drawn, num_experiments):

    # making a list of expected balls.
    experiment_hat = hat.__str__()
    contents_in_ex = []
    for k, v in experiment_hat.items():
        number_of_appearance = 0
        while v > number_of_appearance:
            number_of_appearance += 1
            contents_in_ex.append(k)
    expected_balls_list = []
    for k, v in expected_balls.items():
        number_of_appearance = 0
        while v > number_of_appearance:
            number_of_appearance += 1
            expected_balls_list.append(k)

    #
    find = 0
    experiment_count = 0
    while experiment_count < num_experiments:
        experiment_count +=1
        hat_copy = copy.deepcopy(hat)
        #drawing balls.
        drawed_balls = hat_copy.draw(num_balls_drawn)

        #increase the find if the expected balls are in drawed balls.
        true_false= check_if_contains(expected_balls_list, drawed_balls)
        if true_false == True:
            find += 1
        else:
            find += 0

    #Calculating the probability
    probability_num = find/num_experiments

    return probability_num
