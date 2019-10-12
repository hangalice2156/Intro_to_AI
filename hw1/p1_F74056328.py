import sys
from functions import func

# func might be a 3 dimension space denote a plane that z is the height at (x, y)

def main():
    argv = sys.argv
    print(argv)

    x_range = []
    y_range = []
    initial_points = []
    # argv[1] should be input file
    with open(argv[1], 'r') as input:
        # get range of x
        x_range = [int(x) for x in input.readline().strip().split(',')]
        # print(x)
        # get range of y
        y_range = [int(y) for y in input.readline().strip().split(',')]
        # print(y)
        # get points count
        point_count = int(input.readline().strip())
        # find all points
        for i in range(point_count):
            initial_points.append([int(p) for p in input.readline().strip().split(',')])
        # print(initial_points)
    # argv[2] should be output file
    # output the results for 2 different kind of solution 
    with open(argv[2], 'w') as output:
        answer_fs = force_solution(x_range, y_range)
        print(answer_fs)
        output.write(answer_fs + "\n")

        for i in range(point_count):
            # print(initial_points[i])
            answer_hc = hill_climbing(x_range, y_range, initial_points[i])
            print(answer_hc)
            output.write(answer_hc + "\n")

def force_solution(x_range, y_range):
    ans = float('inf') # as we want to find minimum, should start from positive inf
    iteration = 0
    for i in range(min(x_range), max(x_range)+1):
        for j in range(min(y_range), max(y_range)+1):
            iteration += 1
            z = func(i, j)
            # update answer if lesser than original value
            if z < ans:
                ans = z
    print("force solution iteration:", iteration)
    ans = round(ans, 3)
    return "{:.3f}".format(ans)

def hill_climbing(x_range, y_range, initial_point):
    step_size = 1 # may change into different value to get other answer
    iteration = 0
    [x, y] = initial_point
    z = func(x, y)
    while x in range(min(x_range), max(x_range)+1) and y in range(min(y_range), max(y_range)+1):
        next = [float('inf'), float('inf'), float('inf'), float('inf')]
        if (x + step_size) <= max(x_range):
            iteration += 1
            next[0] = func(x + step_size, y)
        if (x - step_size) >= min(x_range):
            iteration += 1
            next[1] = func(x - step_size, y)
        if (y + step_size) <= max(y_range):
            iteration += 1
            next[2] = func(x, y + step_size)
        if (y - step_size) >= min(y_range):
            iteration += 1
            next[3] = func(x, y - step_size)
        # if there is any step that makes z smaller, take that step
        if z > min(next):
            z = min(next)
            # find which direction is smaller
            if next.index(min(next)) is 0:
                x += step_size
            elif next.index(min(next)) is 1:
                x -= step_size
            elif next.index(min(next)) is 2:
                y += step_size
            elif next.index(min(next)) is 3:
                y -= step_size
            else:
                print('an error occured while taking steps')
        # if there is no step that go smaller, z is the minimum
        else:
            break
    print("hill climbing iteration: ", iteration)
    z = round(z, 3)
    return "{:.3f}".format(z)
                
if __name__ == '__main__':
    main()