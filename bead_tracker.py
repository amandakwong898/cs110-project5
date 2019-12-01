import stdio
import sys
from blob_finder import BlobFinder
from picture import Picture


# Takes an integer P, a float tau, a float delta, and a sequence of JPEG
# filenames as command-line arguments; identifies the beads in each JPEG
# image using BlobFinder; and writes out (one per line, formatted with 4
# decimal places to the right of decimal point) the radial distance that
# each bead moves from one frame to the next (assuming it is no more than
# delta).
def main():

    # Read command-line arguments P, tau, and delta.
    P = int(sys.argv[1])
    tau = float(sys.argv[2])
    delta = float(sys.argv[3])

    # Construct a BlobFinder object for the frame sys.argv[4] and from it
    # get a list of beads prevBeads that have at least P pixels.
    bf = BlobFinder(Picture(sys.argv[4]), tau)
    prevBeads = bf.getBeads(P)

    # For each frame starting at sys.argv[5]:
    for i in range(5, len(sys.argv)):

        # Construct a BlobFinder object and from it get a list of beads
        # currBeads that have at least P pixels.
        bf = BlobFinder(Picture(sys.argv[i]), tau)
        currBeads = bf.getBeads(P)

        # For each bead currBead in currBeads, find a bead prevBead from
        # prevBeads that is no further than delta and is closest to currBead,
        # and if such a bead is found, write its distance (using format string
        # '%.4f\n') to currBead.
        for currBead in currBeads:
            closest = float('inf')
            for prevBead in prevBeads:
                d = currBead.distanceTo(prevBead)
                if d <= delta and d < closest:
                    closest = d
            if not closest == float('inf'):
                stdio.writef('%.4f\n', closest)

        # Write a newline character, and set prevBeads to currBeads.
        stdio.writeln()
        prevBeads = currBeads


if __name__ == '__main__':
    main()
