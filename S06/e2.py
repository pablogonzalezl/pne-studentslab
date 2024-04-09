class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        if strbases.count('A') + strbases.count('C') + strbases.count('G') + strbases.count('T') == len(strbases):
            self.strbases = strbases
            print("New sequence created!")
        else:
            self.strbases = 'ERROR'
            print("INCORRECT Sequence detected")

    def __str__(self):
        """Method called when the object is being printed"""
        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)

    def print_seqs(seq_list):




# --- Main program
s1 = Seq("AGTACACTGGT")
s2 = Seq("CGTAAC")

# -- Printing the objects
print(f"Sequence 1: {s1}")

print(f"Sequence 2: {s2}")




