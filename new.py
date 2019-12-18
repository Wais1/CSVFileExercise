import csv
import os
import statistics
import matplotlib.pyplot as plt

with open('activity.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    steps_per_day = {}
    steps_per_day_with_zeros = {}
    max_steps = 0
    max_interval = 0
    num_NA = 0
    weekday = {}
    weekend = {}
    # Part C implementation starts here.
    dirname = os.path.dirname(__file__)
    new_file = os.path.join(dirname, 'new_file.csv')
    with open(new_file, "w") as csv_writer:
        writer = csv.writer(csv_writer)

        for line in csv_reader:
            if line[1] in steps_per_day.keys():
                if line[0] != 'NA':
                    curr_steps = int(line[0])
                    steps_per_day[line[1]] += curr_steps
                    steps_per_day_with_zeros[line[1]] += curr_steps
                    if curr_steps > max_steps:
                        max_steps = curr_steps
                        max_interval = line[2]
                    last_digits = line[1].split('-')
                    # Implementation of Part D
                    # Checks if weekend, by checking remainder of 7. if 0, is Saturday, else if 1, is Sunday
                    if int(last_digits[2]) % 7 == 0 or int(last_digits[2]) == 1:
                        if line[1] in weekend.keys():
                            weekend[line[1]] += curr_steps
                        else:
                            weekend[line[1]] = curr_steps
                    else:
                        if line[1] in weekday.keys():
                            weekday[line[1]] += curr_steps
                        else:
                            weekday[line[1]] = curr_steps
                else:
                    num_NA += 1
                    line[0] = 0
                    steps_per_day_with_zeros[line[1]] += 0
                writer.writerow(line)

            else:
                steps_per_day[line[1]] = 0
                steps_per_day_with_zeros[line[1]] = 0

    # Prints total steps per day, mean and median in order.
    steps = list(steps_per_day.values())
    print(steps)
    print(statistics.mean(steps))
    print(statistics.median(steps))

    # Displays histogram.
    plt.hist(steps)
    plt.show()

    ######################
    # PART B
    intervals = [i * 5 for i in range(len(steps))]
    print("Max interval: " + max_interval + ", Max steps: " + str(max_steps))
    plt.plot(intervals, steps)
    plt.show()

    # PART C
    # Implemented in Part A. Marked as (Part C with comments)
    print("Number of NA lines: " + str(num_NA))
    plt.hist(steps_per_day_with_zeros.values())
    plt.show()
    print(statistics.mean(steps_per_day_with_zeros.values()))
    print(statistics.median(steps_per_day_with_zeros.values()))

    # PART D
    print("Weekdays: ")
    print(weekday.keys())
    print("Weekends: ")
    print(weekend.keys())
    intervals = [i * 5 for i in range(len(weekend.values()))]
    plt.plot(intervals, list(weekend.values()))
    plt.show()

