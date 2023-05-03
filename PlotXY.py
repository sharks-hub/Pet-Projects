import matplotlib.pyplot as plt

def get_coordinate(axis_name):
    while True:
        try:
            coordinate = int(input(f"Enter {axis_name} coordinate (-9 to 9): "))
            if -9 <= coordinate <= 9:
                return coordinate
            else:
                print("Invalid input. Please enter a value between -9 and 9.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def plot_star(x, y):
    plt.figure(figsize=(5, 5))
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Gold Star Plot")

    plt.plot(x, y, marker='*', color='gold', markersize=10, linestyle='')

    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    x = get_coordinate("x")
    y = get_coordinate("y")
    plot_star(x, y)
