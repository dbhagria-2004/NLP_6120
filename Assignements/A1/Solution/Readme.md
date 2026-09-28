# Assignment 1 — DNA/RNA Parser

## How to Run

Navigate to the solution directory:

```bash
cd A1/Solution
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the program:

```bash
python parsing.py
```

The FASTA file paths are provided in `config.yaml`.

## Implementation

The program:

* Parses FASTA files and merges multiline sequences.
* Uses `^>` regex to identify FASTA headers.
* Classifies sequences as DNA, RNA, or Invalid.
* Finds in-frame ORFs using the specified start/stop codons.
* Counts nucleotides and ambiguous bases.
* Calculates mean DNA/RNA sequence lengths and invalid sequence counts.

## Assumptions

* DNA contains `T` and no `U`; RNA contains `U` and no `T`.
* Sequences containing both `T` and `U`, or neither, are Invalid.
* Ambiguous nucleotides are allowed and counted separately.
* ORFs are searched in reading frame 1 (`0, 3, 6, ...`).
* Ambiguous codons do not match start or stop codons.

## Sample Output

Paste the console output from running the program here:

```text
(.venv) deepanshu@Deepanshus-MacBook-Pro Solution % python parsing.py 
--------------------Solution to part 1------------------------------------
>Seq_1
ACGTACGT
Type: DNA

>Seq_2
AUGCUG
Type: RNA

>Seq_3
TUUUU
Type: Invalid

>Seq_4
ACGNRYACGT
Type: DNA

>Seq_5
AUGUNACG
Type: RNA

>Seq_6
TTTTTTT
Type: DNA

>Seq_7
UUUNNN
Type: RNA

>Seq_8
XYZXYZ
Type: Invalid

>Seq_9
ACGTU
Type: Invalid

>Seq_10
NRYYNN
Type: Invalid

>Seq_11
AGCUA
Type: RNA

>Seq_12
UAGT
Type: Invalid

--------------------Solution to part 2------------------------------------
>DNA_1
ATGAAATGATAA
Type: DNA
Found 1 ORF(s):
- Start at 0, Stop at 6, ORF: ATGAAATGA

>DNA_2
ACGTACGT
Type: DNA
Found 0 ORF(s):

>DNA_3
ATGCCCTGATGA
Type: DNA
Found 1 ORF(s):
- Start at 0, Stop at 6, ORF: ATGCCCTGA

>RNA_1
AUGAAACCCUGA
Type: RNA
Found 1 ORF(s):
- Start at 0, Stop at 9, ORF: AUGAAACCCUGA

>RNA_2
AUGUGA
Type: RNA
Found 1 ORF(s):
- Start at 0, Stop at 3, ORF: AUGUGA

>INVALID_1
ATGU
Type: Invalid
No ORFs found.

>DNA_4
TTTATGCCCTAA
Type: DNA
Found 1 ORF(s):
- Start at 3, Stop at 9, ORF: ATGCCCTAA

>RNA_3
AUGAUGUAG
Type: RNA
Found 2 ORF(s):
- Start at 0, Stop at 6, ORF: AUGAUGUAG
- Start at 3, Stop at 6, ORF: AUGUAG

>DNA_5
ATGCCCTAGTAA
Type: DNA
Found 1 ORF(s):
- Start at 0, Stop at 6, ORF: ATGCCCTAG

>RNA_4
CCCAGGAUGUAGUAA
Type: RNA
Found 1 ORF(s):
- Start at 6, Stop at 9, ORF: AUGUAG

>INVALID_2
TTUUA
Type: Invalid
No ORFs found.

>DNA_6
ATGAAATAGTAGACGT
Type: DNA
Found 1 ORF(s):
- Start at 0, Stop at 6, ORF: ATGAAATAG

--------------------Solution to part 3------------------------------------
>SEQ_DNA_1
Type: DNA
Length: 12
Counts: {'A': 7, 'C': 0, 'G': 2, 'ambiguous': 0, 'T': 3}
Number of ORFs: 1

>SEQ_RNA_1
Type: RNA
Length: 12
Counts: {'A': 7, 'C': 0, 'G': 2, 'ambiguous': 0, 'U': 3}
Number of ORFs: 1

>SEQ_DNA_2
Type: DNA
Length: 8
Counts: {'A': 2, 'C': 2, 'G': 2, 'ambiguous': 0, 'T': 2}
Number of ORFs: 0

>SEQ_DNA_3
Type: DNA
Length: 8
Counts: {'A': 0, 'C': 0, 'G': 0, 'ambiguous': 0, 'T': 8}
Number of ORFs: 0

>SEQ_INVALID_1
Skipped (invalid sequence)

>SEQ_RNA_2
Type: RNA
Length: 9
Counts: {'A': 2, 'C': 3, 'G': 2, 'ambiguous': 0, 'U': 2}
Number of ORFs: 1

>SEQ_DNA_4
Type: DNA
Length: 9
Counts: {'A': 2, 'C': 3, 'G': 2, 'ambiguous': 0, 'T': 2}
Number of ORFs: 1

>SEQ_INVALID_2
Skipped (invalid sequence)

>SEQ_RNA_3
Type: RNA
Length: 15
Counts: {'A': 6, 'C': 3, 'G': 4, 'ambiguous': 0, 'U': 2}
Number of ORFs: 1

>SEQ_DNA_5
Type: DNA
Length: 6
Counts: {'A': 1, 'C': 0, 'G': 1, 'ambiguous': 3, 'T': 1}
Number of ORFs: 0

>SEQ_DNA_6
Type: DNA
Length: 18
Counts: {'A': 6, 'C': 3, 'G': 4, 'ambiguous': 0, 'T': 5}
Number of ORFs: 1

>SEQ_RNA_4
Type: RNA
Length: 13
Counts: {'A': 7, 'C': 0, 'G': 2, 'ambiguous': 0, 'U': 4}
Number of ORFs: 0

--Summary----
Valid DNA sequences 6
Mean DNA length: 10.166666666666666
Valid RNA sequences 4
Mean RNA length: 12.25
Invalid sequences: 2
```
