from src.Ackermann import ackermann
import matplotlib.pyplot as plt

def test_ackermann():

    test_list = [  # examples with different (m,n)
        (0, 0),
        (0, 5),
        (1, 0),
        (1, 3),
        (2, 2),
        (2, 4),
        (3, 2),
        (3, 4)
    ]

    for m, n in test_list:
        try:
            print(f"A({m}, {n}) = {ackermann(m, n)}")
        except RecursionError:
            print(f"A({m}, {n}) = too big")

def plot_ackermann():

    max_m=3
    max_n=20

    plt.figure(figsize=(14, 7))
    
    for m in range(max_m + 1):

        x_vals = []
        y_vals = []

        for n in range(max_n + 1):
            try:
                y = ackermann(m, n)
                x_vals.append(n)
                y_vals.append(y)
            except RecursionError:
                break  # Too big

        plt.plot(x_vals, y_vals, label=f"m = {m}", marker='o')

    plt.title("Ackermann function for different m values")
    plt.xlabel("n")
    plt.ylabel("A(m, n)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


# ================================
# Main
# ================================
          
test_ackermann()
plot_ackermann()