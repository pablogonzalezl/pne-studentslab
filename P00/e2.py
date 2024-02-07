
def seq_read_fasta(filename):
    from pathlib import Path

    file_contents = Path(filename).read_text()
    list_contents = file_contents.split("\n")

    for i in range(1, 21):
        print(list_contents[i])

seq_read_fasta("../sequences/U5_sequence.fa")

