# Simulated Annealing Algorithm

For this project I had to build a simulated annealing algorithm 
to find the highest point in a Minnesota altitude dataset.

## Setup

To use this code, you may have to set download the data file and set the
SRTM environment variable to the right path: export SRTM1_DIR=/path/to/srtm1/

## Notes
Increasing the alpha in the scheduling function increases the accuracy, but
slows down the algorithm substantially. For a faster function that is moderately
accurate, I would recommend alpha = 0.99999. For an extremely accurate function (most
of the time, because this algorithm still relies on randomness), I recommend alpha = 0.9999999.
I have not tried a larger alpha than that, but with that alpha, the majority of the results
are in the 698-700 range (we know the maximum is 700).

