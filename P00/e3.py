def seq_len(seq):
    secuencia = ''
    with open(seq, "r") as f:
        header = next(f)
        for line in f:
            secuencia += line.strip("\n")

    return (len(secuencia))