
class ElementWeightPerArea():
    def __init__(self, name_english, unitweight):
        self.name_english = name_english
        self.names = None
        self.unitweight = unitweight
        self.units = None

class UnitWeight():
    def __init__(self):
        self.name_english = None
        self.unitweight = 0
        self.units = None

hollow_core_slab_NL_150 = ElementWeightPerArea("hollowcoreslab 150 mm",2.65)
hollow_core_slab_NL_200 = ElementWeightPerArea("hollowcoreslab 200 mm",3.03)
hollow_core_slab_NL_260 = ElementWeightPerArea("hollowcoreslab 260 mm",3.76)
hollow_core_slab_NL_320 = ElementWeightPerArea("hollowcoreslab 320 mm",4.43)
hollow_core_slab_NL_400 = ElementWeightPerArea("hollowcoreslab 400 mm",5.48)
nebi_slab_NL = ElementWeightPerArea("nebi",1.8)


