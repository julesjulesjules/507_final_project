class Remember:

    def __init__(self, nm, pw):
        self.name = nm
        self.password = pw

    def collection(self, addition):
        f_add = open("{}_{}_collection.txt".format(self.name, self.password),"a")
        for item in addition:
            f_add.write("%s\n" % item)
        f_add.close()
