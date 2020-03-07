class Do_vat_trong_moi_phong:
    def __init__(self, phong_khach, phong_tam, phong_ngu):
        self.phong_khach = list(phong_khach)
        self.buyer = phong_tam
        self.phong_ngu = phong_ngu

    def __len__(self):
        return len(self.phong_khach)

Obj_dovat = Do_vat_trong_moi_phong(['tivi', 'ghe_salon', 'loa'], 'bon_tam','giuong')
print(len(Obj_dovat))