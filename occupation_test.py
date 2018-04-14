'''
Created on 8 апр. 2018 г.

@author: jetrat
'''



import random



##########################################
##  FUNCTIONS
##########################################

def ask_for_seats_num():
    return int(input('Enter seats number (int):\n'))


def ask_for_own_probability():
    return float(input('Enter percent probability, that passenger will sit onto his own seat, while it\'s free (between 0 and 100):\n')) / 100


def ask_for_iterations_num():
    return int(input('Enter the number of iterations, that should be done: (int > 0)\n'))


def count_occupation(seats_count, own_probability, iterations_count):
    seats_stats = []
    
    for iteration_number in range(iterations_count):
        if iteration_number % 100 == 0:
            print('.', end='')
         
        free_seats = list(range(seats_count))
        seats_occupied_by = [None] * seats_count
        
        for own_seat in range(seats_count):
            
            if ((own_seat in free_seats) and ((random.random() < own_probability) or (len(free_seats) == 1))):
                choosen_seat = own_seat
            else:
                choosen_seat = random.choice(list(filter(lambda x: x != own_seat, free_seats)))
            
            free_seats.remove(choosen_seat)
            seats_occupied_by[choosen_seat] = own_seat
        
        seats_stats.append(seats_occupied_by[:])
    
    print('\n')
    
    return(seats_stats)


def tell_result(seats_stats, seats_count, iterations_count, results_wanted):
    result_types = {'own_frequencies': 'How frequent passenger sits on his own seat',
                    'occupied_when_sits': 'How frequent passenger own seat is occupied, when he tries to choose a seat'}
    
    for result_type in results_wanted:
        if result_type not in result_types:
            raise ValueError(result_type + ' is not in result_types set')
    
    result_stats = {}
    for result_type in result_types:
        result_stats[result_type] = [0] * seats_count
    
    for seat in range(seats_count):
        for iteration_number in range(iterations_count):
            if seats_stats[iteration_number][seat] == seat:
                result_stats['own_frequencies'][seat] +=1
            elif seats_stats[iteration_number][seat] < seat:
                result_stats['occupied_when_sits'][seat] +=1

    for result_type in results_wanted:
            result_stats[result_type] = list(map(lambda x: x / iterations_count, result_stats[result_type]))
    
    for result_type in results_wanted:
        print(str(result_types[result_type]) + ':')

        for seat in range(len(result_stats[result_type])):
            print(str(seat + 1) + ': ' + str(result_stats[result_type][seat]))
        
        print()



##########################################
##  MAIN
##########################################

if __name__ == '__main__':
    
    seats_count = ask_for_seats_num()

    own_probability = ask_for_own_probability()

    iterations_count = ask_for_iterations_num()

    seats_stats = count_occupation(seats_count, own_probability, iterations_count)

    tell_result(seats_stats, seats_count, iterations_count, ['own_frequencies', 'occupied_when_sits'])

    input()