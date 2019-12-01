import math
import stdio


# Reads in the displacements produced by bead_tracker.py from standard
# input; computes an estimate of Boltzmann's constant and Avogadro's number;
# and writes those estimates to standard output.
def main():

    # Calculate var as the sum of the squares of the n displacements (each
    # converted from pixels to meters) read from standard input.
    n = 0
    var = 0.0
    while not stdio.isEmpty():
        r = stdio.readFloat() * 0.175 * 10 ** -6
        var += r * r
        n += 1

    # Divide var by 2 * n.
    var = var / (2 * n)

    # Initialize eta, rho, T, and R to appropriate values.
    eta = 9.135 * 10 ** -4
    rho = 0.5 * 10 ** -6
    T = 297.0
    R = 8.31457

    # Estimate Boltzman constant k as 6 * math.pi * var * eta * rho / T
    k = 6 * math.pi * var * eta * rho / T

    # Estimate Avogadro's number N_A as R / k
    N_A = R / k

    # Write k and N_A using format string '%e' (for scientific notation)
    stdio.writef('Boltzman = %e\nAvogadro = %e\n', k, N_A)


if __name__ == '__main__':
    main()
