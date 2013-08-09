'''
Class representing a chemical element

Created on 08.08.2013
@author: Alexey Bright
'''

class Element(object):
    ' Represents a chemical element '
    
    def __init__(self, atomic_mass, oxidation):
        ''' Constructs an element object
            @param mass: atomic mass of the element 
            @param oxidation: set of element's oxidation states '''
        Element.element_count += 1
        self.oxidation = oxidation
        self.atomic_mass = atomic_mass 
        self.atomic_number = Element.element_count
        self.metal = True
        
    # ----------------------------------------------------------------------- #
    
    def is_metal(self):
        ' Returns True if element is a metal, False otherwise'
        return self.metal
    
    element_count = 0
    
# =========================================================================== #     
    
class E(object):
    ' Contains elements data '
    
# symbol      atomic mass   oxidation states
    H   = Element(1.008,    {-1, 1})
    He  = Element(4.003,    {})
    Li  = Element(6.94,     {1})
    Be  = Element(9.012,    {2})
    B   = Element(10.81,    {-1, 1, 2, 3})
    C   = Element(12.01,    {-4, -3, -2, -1, 1, 2, 3, 4})
    N   = Element(14.01,    {-3, -2, -1, 1, 2, 3, 4, 5})
    O   = Element(16.0,     {-2, -1, 1, 2})
    F   = Element(19.0,     {-1})
    Ne  = Element(20.18,    {})
    Na  = Element(22.99,    {-1, 1})
    Mg  = Element(24.31,    {1, 2})
    Al  = Element(26.98,    {1, 3})
    Si  = Element(28.09,    {-4, -3, -2, -1, 1, 2, 3, 4})
    P   = Element(30.97,    {-3, -2, -1, 1, 2, 3, 4, 5})
    S   = Element(32.06,    {-2, -1, 1, 2, 3, 4, 5, 6})
    Cl  = Element(35.45,    {-1, 1, 2, 3, 4, 5, 6, 7})
    Ar  = Element(39.95,    {})
    K   = Element(39.1,     {1})
    Ca  = Element(40.08,    {2})
    Sc  = Element(44.96,    {1, 2, 3})
    Ti  = Element(47.88,    {-1, 2, 3, 4})
    V   = Element(50.94,    {-1, 1, 2, 3, 4, 5})
    Cr  = Element(52.0,     {-2, -1, 1, 2, 3, 4, 5, 6})
    Mn  = Element(54.94,    {-3, -2, -1, 1, 2, 3, 4, 5, 6, 7})
    Fe  = Element(55.85,    {-2, -1, 1, 2, 3, 4, 5, 6})
    Co  = Element(58.93,    {-1, 1, 2, 3, 4, 5})
    Ni  = Element(58.69,    {-1, 1, 2, 3, 4})
    Cu  = Element(63.55,    {1, 2, 3, 4})
    Zn  = Element(65.39,    {2})
    Ga  = Element(69.72,    {1, 2, 3})
    Ge  = Element(72.64,    {-4, 1, 2, 3, 4})
    As  = Element(74.92,    {-3, 2, 3, 5})
    Se  = Element(78.96,    {-2, 2, 4, 6})
    Br  = Element(79.9,     {-1, 1, 3, 4, 5, 7})
    Kr  = Element(83.79,    {2, 4})
    Rb  = Element(85.47,    {1})
    Sr  = Element(87.62,    {2})
    Y   = Element(88.92,    {1, 2, 3})
    Zr  = Element(91.22,    {1, 2, 3, 4})
    Nb  = Element(92.91,    {-1, 2, 3, 4, 5})
    Mo  = Element(95.96,    {-2, -1, 1, 2, 3, 4, 5, 6})
    Tc  = Element(98.0,     {-3, -1, 1, 2, 3, 4, 5, 6, 7})
    Ru  = Element(101.1,    {-2, 1, 2, 3, 4, 5, 6, 7, 8})
    Rh  = Element(102.9,    {-1, 1, 2, 3, 4, 5, 6})
    Pd  = Element(106.4,    {2, 4})
    Ag  = Element(107.9,    {1, 2, 3})
    Cd  = Element(112.4,    {2})
    In  = Element(114.8,    {1, 2, 3})
    Sn  = Element(118.7,    {-4, 2, 4})
    Sb  = Element(121.8,    {-3, 3, 5})
    Te  = Element(127.6,    {-2, 2, 4, 5, 6})
    I   = Element(126.9,    {-1, 1, 3, 5, 7})
    Xe  = Element(131.3,    {2, 4, 6, 8})
    Cs  = Element(132.9,    {1})
    Ba  = Element(137.3,    {2})
    La  = Element(138.9,    {2, 3})
    Ce  = Element(140.1,    {2, 3, 4})
    Pr  = Element(140.9,    {2, 3, 4})
    Nd  = Element(144.2,    {2, 3})
    Pm  = Element(145.0,    {3})
    Sm  = Element(150.4,    {2, 3})
    Eu  = Element(152.0,    {2, 3})
    Gd  = Element(157.2,    {1, 2, 3})
    Tb  = Element(158.9,    {1, 3, 4})
    Dy  = Element(162.5,    {2, 3})
    Ho  = Element(164.9,    {3})
    Er  = Element(167.3,    {3})
    Tm  = Element(168.9,    {2, 3})
    Yb  = Element(173.0,    {2, 3})
    Lu  = Element(175.0,    {3})
    Hf  = Element(178.5,    {2, 3, 4})
    Ta  = Element(180.9,    {-1, 2, 3, 4, 5})
    W   = Element(183.9,    {-2, -1, 1, 2, 3, 4, 5, 6})
    Re  = Element(186.2,    {-3, -1, 1, 2, 3, 4, 5, 6, 7})
    Os  = Element(190.2,    {-2, -1, 1, 2, 3, 4, 5, 6, 7, 8})
    Ir  = Element(192.2,    {-3, -1, 1, 2, 3, 4, 5, 6})
    Pt  = Element(195.1,    {2, 4, 5, 6})
    Au  = Element(197.0,    {-1, 1, 2, 3, 5})
    Hg  = Element(200.5,    {1, 2, 4})
    Tl  = Element(204.38,   {1, 3})
    Pb  = Element(207.2,    {-4, 2, 4})
    Bi  = Element(209.0,    {-3, 3, 5})
    Po  = Element(209.0,    {-2, 2, 4, 6})
    At  = Element(210.0,    {-1, 1, 3, 5})
    Rn  = Element(222.0,    {2})
    Fr  = Element(223.0,    {1})
    Ra  = Element(226.0,    {2})
    Ac  = Element(227.0,    {3})
    Th  = Element(232.0,    {2, 3, 4})
    Pa  = Element(231.0,    {3, 4, 5})
    U   = Element(238.0,    {3, 4, 5, 6})
    Np  = Element(237.0,    {3, 4, 5, 6, 7})
    Pu  = Element(244.0,    {3, 4, 5, 6, 7})
    Am  = Element(243.0,    {2, 3, 4, 5, 6})
    Cm  = Element(247.0,    {3, 4})
    Bk  = Element(247.0,    {3, 4})
    Cf  = Element(251.0,    {2, 3, 4})
    Es  = Element(252.0,    {2, 3})
    Fm  = Element(257.0,    {2, 3})
    Md  = Element(258.0,    {2, 3})
    No  = Element(259.0,    {2, 3})
    Lr  = Element(262.0,    {3})
    Rf  = Element(265.0,    {4})
    Db  = Element(268.0,    {5})
    Sg  = Element(271.0,    {6})
    Bh  = Element(270.0,    {7})
    Hs  = Element(277.0,    {8})
    
    # ----------------------------------------------------------------------- #
    
    @classmethod
    def prepare_table(cls):
        ' Prepare elements table to use '
        cls.table = set()
        for s in vars(cls):
            if len(s) < 3:
                e = getattr(cls, s)
                e.symbol = s
                cls.table.add(e)
                
        non_metals = {cls.H,
                      cls.He,
                      cls.B,
                      cls.C,
                      cls.N,
                      cls.O,
                      cls.F,
                      cls.Ne,
                      cls.Si,
                      cls.P,
                      cls.S,
                      cls.Cl,
                      cls.Ar,
                      cls.Ge,
                      cls.As,
                      cls.Se,
                      cls.Br,
                      cls.Kr,
                      cls.Te,
                      cls.I,
                      cls.Xe,
                      cls.At,
                      cls.Rn}
        for e in non_metals:
            e.metal = False

    # ----------------------------------------------------------------------- #
    
    @classmethod
    def get_elements(cls):
        ' Returns set of element objects '
        return cls.table
    
    # ----------------------------------------------------------------------- #
    
    @classmethod
    def get_element(cls, name):
        ' Returns element object by its name '
        return getattr(cls, name)
    
# =========================================================================== # 

E.prepare_table()

