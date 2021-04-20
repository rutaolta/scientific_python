import re
import sys


def calculate_number_of_occurances(seq, motif):
    matches = re.findall(motif, seq)
    return len(matches)

def process_line(seq_id, seq, motifs):
    for motif in motifs:
        noo = calculate_number_of_occurances(seq, motif)
        print(f"{seq_id: >15}{motif: >15}{noo: >5}")

def process_file(filename, motifs):
    print("SEQ_ID                |   MOTIF     |     NUMBER_of_occurances")

    with open(filename) as f:
        for line in f:
            line = line.strip()

            seq_id, seq = re.split(r'\s+', line)

            process_line(seq_id, seq, motifs)


def main():
    if len(sys.argv) < 3:
        print("Usage: script.py <path-to-seqs> <comma-separated-motifs>")
        exit()

    filename = sys.argv[1]
    motifs = sys.argv[2].split(',')

    process_file(filename, motifs)

if __name__ == '__main__':
    main()
