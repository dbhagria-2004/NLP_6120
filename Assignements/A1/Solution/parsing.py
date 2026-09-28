from collections import defaultdict
import yaml
"""
Function to read the file path
"""
def read(file_path):
    file = open(file_path, "r")
    return file

"""
Function to parse the file, and put every sequence into a dictionarys
"""
def parse(file):
    seq_dict = defaultdict(str)
    header = None
    sequence = ""
    for f in file:
        line = f.strip()

        if line.startswith(">"):
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
Function to iterate te sequence dict, and print the TYPE
"""
def filterAndPrint(seq_dict):
    for k, v in seq_dict.items():
        print(k)
        if "T" in v.upper() and "U" in v.upper(): 
            print(v)
            print("Invalid")

        elif "T" in v.upper():
            print(v)
            print("Type : DNA")
        elif "U" in v.upper():
             print(v)
             print("Type: RNA")
        else:
            print(v)
            print("Type: Invalid")


def findORF(sequence):
    pass


def main():
    ## instead of hardcoding the paths, you load the file from a config file
    with open("config.yaml", "r") as config_file:
        config = yaml.safe_load(config_file)
    part1_fasta_path = config["part1_fasta_path"]
    file1 = read(part1_fasta_path)

    seq_dict_p1 = parse(file1)
    # filterAndPrint(seq_dict_p1)


    part2_fasta_path = config["part2_fasta_path"]
    file2 = read(part2_fasta_path)

    seq_dict_p2 = parse(file2)
        
        
if __name__ == "__main__":
    main()
