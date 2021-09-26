#!/usr/bin/python3

# Here I want to create a function that does the following actions:
# it takes a DNA sequence (both lower and upper cases) and it returns
# its DNA complement.

# Complement of base A --> T
# Complement of base G is --> C
# Complement of base T --> A
# Complement of base C is --> G

# Here I am transforming a string into a list
# of each of its letter. I tested this out here first 
# before putting this inside my function.
input_string = "TTAAAG"
dna_list= list(input_string)

# My two test cases are:
# a string with a letter not included in the above
test = test = "TTACCZ"
# an empty string
test_list= list(test)
empty_test = " "

# I create an empty list to find its length
empty_list = list()
len(empty_list)

# This is my function
def dna_complement(input_dna):
        output_dna_complement= list()
        dna_list= list(input_dna)
        if len(dna_list) == len(empty_list):
            return "None"
        else: 
            for i in dna_list:
                if i == "A":
                    output_dna_complement.append("T")
                elif i == "a":
                    output_dna_complement.append("T")
                elif i == "T":
                    output_dna_complement.append("A")
                elif i == "t":
                    output_dna_complement.append("A")
                elif i == "G":
                    output_dna_complement.append("C")
                elif i == "g":
                    output_dna_complement.append("C")
                elif i == "c":
                    output_dna_complement.append("G")
                elif i == "C":
                    output_dna_complement.append("G")
                else: 
                    return print("none")
        return print(output_dna_complement)

#These are my test cases
input_string = "TTAAAG"
test = "TTACCZ"
empty_test = " "

# Here I am calling the function with the inputs
dna_complement(input_string)
dna_complement(test)
dna_complement(empty_test)
