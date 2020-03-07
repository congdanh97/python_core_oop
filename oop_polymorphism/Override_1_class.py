class Cha():
    # Constructor
    def __init__(self):
        self.do_dep_trai = "Dep trai"

    # Parent's show method
    def show(self):
        print(self.do_dep_trai)

    # Defining child class


class Con(Cha):
    # Constructor
    def __init__(self):
        self.do_dep_trai = "Dep trai hon bo"

    # Child's show method
    def show(self):
        print(self.do_dep_trai)

# Chay vi du
object_cha = Cha()
object_con = Con()

object_cha.show()
object_con.show()