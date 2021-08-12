# DNA
Program that takes in a database file and a sequence file in which it searches to see if it matches the database and outputs the name of the person if so.

In this case, it will accept a sequence file where it stores multiple names and their STR numbers (short tandem repeats) as well as a long dna sequence with no name attached to it.

The program will go through the sequence and count each consequetive STR and stores the longest one. It will then compare the counts with each person in the database csv file and outputs the name if the STR count matches with anyone else it will output "No match". Attached are sample database and sequence files.
