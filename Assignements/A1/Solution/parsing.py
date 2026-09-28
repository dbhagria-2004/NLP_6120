from collections import defaultdict
import yaml
import re
"""
Function to read the file path
"""
def read(file_path):
    file = open(file_path, "r")
    return file

"""
Function to parse the file, and put every sequence into a dictionary
"""
def parse(file):
    seq_dict = defaultdict(str)
    header = None
    sequence = ""
    for f in file:
        line = f.strip()

        if re.match(r"^>", line):
            if header:
                seq_dict[header] = sequence

            header = line
            sequence = ""

        else:
            sequence += line

## save the last sequence, why? because the current loop logic saved the last 
# after you encounter the new sequence, making the last sequence unsaved, so we do it at the end.
    if header:
         seq_dict[header] = sequence
    return seq_dict


"""
Function to iterate te sequence dict, return the type
"""
def getType(sequence):
# Note: Here we know that, if T and U are in one sequence it is invalid, and T and U deterimies if its a
# dna or rna, and, else it is a invalid again.

    if "T" in sequence.upper() and "U" in sequence.upper(): 
        return "Invalid"

    elif "T" in sequence.upper():
        return "DNA"

    elif "U" in sequence.upper():
        return "RNA"
    else:
        return "Invalid"

####
####  PART 1
####

"""
Function to iterate te sequence dict, check the type and print for part1
"""
def filterAndPrint(seq_dict):
    for k, v in seq_dict.items():
        sequence = v.upper()
        seq_type = getType(sequence)

        print(k)
        print(sequence)
        print("Type:", seq_type)
        print()


####
####  PART 2
####

"""
Function to find the orf's in a given sequence
Assumption: We iterate every index to find the start colon, and once the start colon is found,
we move in batches of 3 to match for end colon, one we find a match, it is a subsequence we need, we append it to
the list of orf's

"""
def findORF(sequence):
    list_of_orf = []
    sequence = sequence.upper()

    seq_type = getType(sequence)
    if seq_type == "DNA":
        start_codon  = "ATG"
        end_codons = ["TAA", "TAG", "TGA"]
    elif seq_type == "RNA":
        start_codon  = "AUG"
        end_codons = ['UAA', 'UAG', 'UGA' ]

    else:
        return []

    for i in range(0, len(sequence)-2, 3):
        codon = sequence[i:i+3]

        if codon == start_codon:
            for j in range(i+3, len(sequence)-2, 3):
                end_codon = sequence[j:j+3] 

                if end_codon in end_codons:
                    orf_sequence = sequence[i:j+3]

                    list_of_orf.append((i, j, orf_sequence))

                    break
    return list_of_orf


"""
Print ORF information for each valid sequence.
"""
def printORFs(seq_dict):

    for k, v in seq_dict.items():

        sequence = v.upper()
        sequence_type = getType(sequence)

        print(k)
        print(sequence)
        print("Type:", sequence_type)

        if sequence_type == "Invalid":
            print("No ORFs found.")
            print()
            continue

        ## call to the function
        orfs = findORF(sequence)

        ## Formatting asked for in the assignment
        print("Found", len(orfs), "ORF(s):")

        for start, stop, orf_sequence in orfs:
            print(
                f"- Start at {start}, "
                f"Stop at {stop}, "
                f"ORF: {orf_sequence}"
            )
    ## start  new line
        print()
            

####
####  PART 3
####

"""
Function to count the Nucleotide, and append them to a dict
"""
def countFreq(sequence):
    sequence = sequence.upper()
    seq_type = getType(sequence)
    count = {"A": 0,
             "C": 0,
             "G": 0,
             "ambiguous":0}

    ## instead of hardcoding T or U, we check if it is a DNA or RNA, and then we append only the relevent one
    dna_or_rna = "T" if seq_type == "DNA" else "U"
    count[dna_or_rna] = 0

    for c in sequence:
        if c in count:
            count[c] +=1
        else:
            count["ambiguous"] +=1

    return count

"""
Function to iterate the sequence dictionary and print the Nucleotide Frequencies & Summary Report 
"""
def printNucleotideAndSummary(seq_dict):
    dna_len, rna_len, invalid_count = [], [], 0

    for k, v in seq_dict.items():
        sequence = v.upper()
        seq_type = getType(sequence)
        if seq_type == "Invalid":
            print(k)
            invalid_count += 1
            print("Skipped (invalid sequence)")
            print()
            continue
        print(k)
        print("Type:", seq_type)
        print("Length:", len(sequence))
        print("Counts:", countFreq(sequence))
        print("Number of ORFs:", len(findORF(sequence)))


        if seq_type == "DNA":
            dna_len.append(len(sequence))
        else:
            rna_len.append(len(sequence))
        print()
    mean_dna = sum(dna_len) / len(dna_len) if dna_len else 0
    mean_rna = sum(rna_len) / len(rna_len) if rna_len else 0    
    print("--Summary----")
    print("Valid DNA sequences", len(dna_len))
    print("Mean DNA length:", mean_dna)
    print("Valid RNA sequences", len(rna_len))
    print("Mean RNA length:", mean_rna)
 
    print("Invalid sequences:", invalid_count)



def main():
    ## instead of hardcoding the paths, you load the file from a config file
    with open("config.yaml", "r") as config_file:
        config = yaml.safe_load(config_file)

    part1_fasta_path = config["part1_fasta_path"]
    
    file1 = read(part1_fasta_path)

    seq_dict_p1 = parse(file1)

    print("--------------------Solution to part 1------------------------------------")

    filterAndPrint(seq_dict_p1)

    print("--------------------Solution to part 2------------------------------------")

    # part2_fasta_path = config["part2_fasta_path"]
    part2_fasta_path = config["part2_fasta_path"]
    
    file2 = read(part2_fasta_path)
    # file2 = read(r"/Users/deepanshu/Documents/NLP_6120/Assignements/A1/test_files-2/test_part2_in.fasta")

    seq_dict_p2 = parse(file2)

    printORFs(seq_dict_p2)
    
    print("--------------------Solution to part 3------------------------------------")
    # file3 = read(r"/Users/deepanshu/Documents/NLP_6120/Assignements/A1/test_files-2/test_part3_in.fasta")
    part3_fasta_path = config["part3_fasta_path"]
    
    file3 = read(part3_fasta_path)
    seq_dict_p3 = parse(file3)

    printNucleotideAndSummary(seq_dict_p3)

if __name__ == "__main__":
    main()



