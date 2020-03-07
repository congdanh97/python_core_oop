class Cha():
    def show(self):
        print("Giong Ba")


class Me():
    def show(self):
        print("Giong Me")

    def chieu_cao(self):
        print("Cao")

class Con(Cha, Me):
    def show(self):
        print("Giong Ca Cha Me")

#run
obj_con = Con()
obj_con.show()
obj_con.chieu_cao()