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

if __name__=='__main__':
    left_rectangle=Set_Point(10,15)
    right_rectangle=Set_Point(9,20)
    top_rectangle=Set_Point(11,10)
    bottom_rectangle = Set_Point(11, 15)

    Result=Check_Overlaps(left_rectangle,right_rectangle,top_rectangle,bottom_rectangle)

    if (Result == False):
        print("No overlap")
    else:
        print("There is an overlap")
