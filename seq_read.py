# seq_read.py by mohammed

def read_seq(inputfile):
    with open(inputfile, "r") as f:
        seq = f.read()
    seq = seq.replace("\n", "")
    seq = seq.replace("\r", "")
    return seq

print(read_seq("dna.txt"))
