#!/usr/bin/env python3

class Set_Point:
    def __init__ (self,lenght,breath):
        self.breath = breath
        self.lenght = lenght

def Check_Overlaps(L_rect, R_rect, T_rect, B_rect):
    ## Check if they overlap
    if (L_rect.breath > R_rect.breath or R_rect.breath < L_rect.breath) or (T_rect.lenght > B_rect.lenght or B_rect.lenght < T_rect.lenght):
        return True

    return False


