# # help (SyntaxError)
# print(sys.platform)
# # assert False, "SOS"
#
#
# def linux_interaction():
#     assert ("linux" in sys.platform, "Works only with linux")
#     print("linux works")
#
#
# def win_interaction():
#     assert ("windows" in sys.platform, "Works only with windows")
#     print("windows works")
#
#
# # linux_interaction()
# # win_interaction()
#
#
# try:
#     win_interaction()
# except AssertionError as error:
#     print(error)
#     print("error transcription")
#
#
# try:
#     with open("file.log") as file:
#         read_data = file.read()
# except:
#     pass
# else:
#     print("There is no mistakes")
#
#
# try:
#     linux_interaction()
# except:
#     pass
# else:
#     print("There is no mistakes")
#
# try:
#     linux_interaction()
# except AssertionError as error:
#     print(error)
# else:
#     try:
#         with open("file.log") as file:
#             read_data = file.read()
#     except FileNotFoundError as fnf_error:
#         print(fnf_error)
# finally:
#     print("Always will be shown")
#
#
# x = 10
# if x > 5:
#     raise Exception('My exception "Nothing more than 5, x was {}"'.format(x))
#
# assert(x < 5), "x is greater than 5"

# filename = "prom.txt"
# motifs = [
#     "ACGT",
#     "[AC]CG[TC]"
# ]
import re
import sys


def calculate_number_of_occurances(seq, motif):
    matches = re.findall(motif, seq)
    return len(matches)


def process_line(seq_id, seq, motifs):
    for motif in motifs:
        noo = calculate_number_of_occurances(seq, motif)
        print(f"{seq_id: >25}{motif: >15}{noo: >5}")


def process_file(filename, motifs):
    print("SEQ_ID | MOTIF | NUMBER_OF_OCCURANCES")

    with open(filename) as f:
        for line in f:
            line = line.strip()

            seq_id, seq = re.split(r"\s+", line)

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

# example of usage
# python class.py prom.txt ATCG,GGCC