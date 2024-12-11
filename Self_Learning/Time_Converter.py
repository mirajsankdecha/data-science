class TimeConverter :
    def __init__ (self) :
        print("Simple Time Converter")
    def h_to_m(self,hours) :
        return hours * 60
    def m_to_s(self,min) :
        return min * 60
    def s_to_h(self,sec) :
        return sec / 3600
        