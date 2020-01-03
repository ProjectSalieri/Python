# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file ThinkLayer1st.py
# @note 思考層1st 本能

class ThinkLayer1st:

    def __init__(self):
        pass
    # def __init__

    def update(self, params):
        for param in params:
            if "Hp" in param:
                hp = param["Hp"]

                print("                                     ", end="\r")
                if hp < 450:
                    print("hungry. hp : %d" % (hp), end='\r')
                else:
                    print("no hungry. hp : %d" %(hp), end='\r')
                # 
            # if
        # for
    # def update

if __name__ == "__main__":
    pass
