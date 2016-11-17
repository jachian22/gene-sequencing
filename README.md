# DNA Sequence Combinatorics

## Steps: FUNCTIONAL PROGRAMMING
For this takehome, I started with functional programming and 3 main functions: the Fasta reader, two fragment combiner, and the fragment list combiner.

### Fasta reader
The Fasta reader is fairly straight forward. It uses "with open..." and various string manipulations to split and strip the text in the file to give the sequence fragments and the ID's for the fragments.

### Two fragment combiner
This function checks if one sequence engulfs the other, and finds the maximum overlap between the two sequences. If the overlap exceeds half the length of the smaller sequence, it will return the combined sequence.

### Fragment list combiner
This function passes over the list of all the fragments to combine them if the requirements of the two fragment combiner are met. The indices of the combined fragments are stored in a set to ensure that fragments aren't combined multiple times with other sequences. Once all the fragments have been passed over, the larger fragments produced from the first pass are iterated over recursively until a single sequence is left. 

### Error handling
If an incorrect file type is passed to the Fasta reader, the error, "Wrong file type. You dun goofed!" pops up. In order to ensure that sequences that don't combine don't iterate infinitely in the recursive loop, the error "Fragments did not join correctly!" appears when a file of sequences doesn't converge to a single chromosome correctly.

## Steps: OOP
After testing the functional programming version on the example and text file, I began to tweak the functions to behave in a get-set paradigm with a bit of commented documentation for the functions. 
