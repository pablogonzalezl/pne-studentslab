class Seq:

    def __init__(self, strbases=""):
        bases_list = ["A", "C", "G", "T"]
        valid = True
        for i in strbases:
            if i not in bases_list:
                self.strbases = 'ERROR'
                valid = False
            break
        if strbases = "":
            self.strbases = "NULL"





        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):
        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        return len(self.strbases)


    def pruebacomit6