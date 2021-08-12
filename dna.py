import csv
import sys

def main():
    if len(sys.argv) != 3: # Check for proper usage
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)
    else:
        dna = []
        with open(sys.argv[1], "r") as csvf: # Open CSV and write in list
            reader = csv.reader(csvf)
            for row in reader:
                dna.append(row)

        with open(sys.argv[2], "r") as txtf: # Open data file in variable
            data = txtf.read()

    for i in range(1, len(dna)): # Loop and compare the output of calc and the list
        ans = int_to_str(dna[i][1:])
        if ans == calc(data, dna[0][1:]):
            print(dna[i][0])
            sys.exit(0)
    print("No match")
    sys.exit(0)

def calc(s, dna_input): # Find the largest consecutive STR
    count = 0
    count2 = 0
    count3 = []
    j = 0
    for i in range(len(dna_input)):
        while j <= len(s):
            if dna_input[i] == s[j:j+len(dna_input[i])]:
                count += 1
                j += len(dna_input[i])
            else:
                if count2 < count:
                    count2 = count
                count = 0
                j += 1
        count3.append(count2)
        count2 = 0
        count = 0
        j = 0
    return count3

def int_to_str(str_list): # Turn an integer list to a string list
    n = 0
    while n < len(str_list):
        str_list[n] = int(str_list[n])
        n += 1
    return(str_list)

if __name__ == '__main__':
    main()