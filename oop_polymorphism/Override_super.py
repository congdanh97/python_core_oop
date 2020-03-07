class Cha():
    def show(self):
        print("Giong Ba")

class Con(Cha):
    def show(self):
        super().show()
        print("Giong Ca Cha Me")

#run
obj_con = Con()
obj_con.show()