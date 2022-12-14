from graphics import *


#Global Variable, creates the window for the game
win = GraphWin('Connect 4',500,500)

#Board constructor

class Board:
    #initializes the Board class
    def __init__(self):
        self.draw_Back()
        self.draw_cols()
        self.draw_rows()
        self.draw_buttons()
        self.draw_exit()
        self.draw_clear()
        self.draw_Title()
        self.draw_inst()
        #initializes the variables that keep track of moves made, both where and how many
        self.slots = [[' '] * 7 for row in range(6)]
        self.turns = 0
        self.col1 = 0
        self.col2 = 0
        self.col3 = 0
        self.col4 = 0
        self.col5 = 0
        self.col6 = 0
        self.col7 = 0
        #starts getting input for the game
        self.get_input()

    #draws the back of the window white
    def draw_Back(self):
        back = Rectangle(Point(0, 0), Point(500, 500))
        back.setFill('white')
        back.draw(win)
    #draws the exit button
    def draw_exit(self):
        rec = Rectangle(Point(1, 25), Point(75,75))
        rec.setOutline('Black')
        rec.setFill('Red')
        rec.draw(win)
        exit = Text(Point(38,50), 'Exit')
        exit.setTextColor('Black')
        exit.setSize(30)
        exit.draw(win)
    #draws the text for the title
    def draw_Title(self):
        title = Text(Point(250,40), 'Connect Four')
        title.setTextColor('Black')
        title.setSize(36)
        title.draw(win)
        sub = Text(Point(250,70), '(2 Player)')
        sub.setTextColor('Red')
        sub.setSize(20)
        sub.draw(win)
    #draws the clear board button
    def draw_clear(self):
        rec1 = Rectangle(Point(425,25), Point(499,75))
        rec1.setOutline('Black')
        rec1.setFill('Lime')
        rec1.draw(win)
        clear = Text(Point(462,50), 'Clear\nBoard')
        clear.setTextColor('Black')
        clear.setSize(20)
        clear.draw(win)
    #draws text for the instructions
    def draw_inst(self):
        tex = Text(Point(250,485), 'Press Button to Select Column')
        tex.setSize(18)
        tex.setTextColor('Black')
        tex.draw(win)
    #draws the columns for the board
    def draw_cols(self):
        line1 = Line(Point(40, 100), Point(40, 400))
        line1.setWidth(5)
        line1.draw(win)

        line2 = Line(Point(100, 100), Point(100, 400))
        line2.setWidth(5)
        line2.draw(win)

        line3 = Line(Point(160, 100), Point(160, 400))
        line3.setWidth(5)
        line3.draw(win)

        line4 = Line(Point(220, 100), Point(220, 400))
        line4.setWidth(5)
        line4.draw(win)

        line5 = Line(Point(280, 100), Point(280, 400))
        line5.setWidth(5)
        line5.draw(win)

        line6 = Line(Point(340, 100), Point(340, 400))
        line6.setWidth(5)
        line6.draw(win)

        line7 = Line(Point(400, 100), Point(400, 400))
        line7.setWidth(5)
        line7.draw(win)

        line8 = Line(Point(460, 100), Point(460, 400))
        line8.setWidth(5)
        line8.draw(win)
    #draws the rows for the boards
    def draw_rows(self):
        line1 = Line(Point(37, 100), Point(463,100))
        line1.setWidth(5)
        line1.draw(win)

        line2 = Line(Point(37, 150), Point(463,150))
        line2.setWidth(5)
        line2.draw(win)

        line3 = Line(Point(37, 200), Point(463,200))
        line3.setWidth(5)
        line3.draw(win)

        line4 = Line(Point(37, 250), Point(463,250))
        line4.setWidth(5)
        line4.draw(win)

        line5 = Line(Point(37, 300), Point(463,300))
        line5.setWidth(5)
        line5.draw(win)

        line6 = Line(Point(37, 350), Point(463,350))
        line6.setWidth(5)
        line6.draw(win)

        line7 = Line(Point(37, 400), Point(463,400))
        line7.setWidth(5)
        line7.draw(win)
    #draws the input buttons
    def draw_buttons(self):
        circ1 = Rectangle(Point(45, 420), Point(95,460))
        circ1.setOutline('Black')
        circ1.setWidth(2)
        circ1.setFill('Yellow')
        circ1.draw(win)

        circ2 = Rectangle(Point(105, 420), Point(155,460))
        circ2.setOutline('Black')
        circ2.setWidth(2)
        circ2.setFill('Yellow')
        circ2.draw(win)

        circ3 = Rectangle(Point(165, 420), Point(215,460))
        circ3.setOutline('Black')
        circ3.setWidth(2)
        circ3.setFill('Yellow')
        circ3.draw(win)

        circ4 = Rectangle(Point(225, 420), Point(275,460))
        circ4.setOutline('Black')
        circ4.setWidth(2)
        circ4.setFill('Yellow')
        circ4.draw(win)

        circ5 = Rectangle(Point(285, 420), Point(335,460))
        circ5.setOutline('Black')
        circ5.setWidth(2)
        circ5.setFill('Yellow')
        circ5.draw(win)

        circ6 = Rectangle(Point(345, 420), Point(395,460))
        circ6.setOutline('Black')
        circ6.setWidth(2)
        circ6.setFill('Yellow')
        circ6.draw(win)

        circ7 = Rectangle(Point(405, 420), Point(455,460))
        circ7.setOutline('Black')
        circ7.setWidth(2)
        circ7.setFill('Yellow')
        circ7.draw(win)

    #starts a while loop to constantly check for user input on any of the buttons
    def get_input(self):
        while True:
            p = win.getMouse()
            x = p.getX()
            y = p.getY()
            #print('x: ', x, ', y: ', y)
            #accepts input for the button for column 1
            if (45<x<95 and 420<y<460) and not (self.is_win('red') or self.is_win('black')):
                if self.col1 <6:
                    self.turns += 1
                    self.col1 += 1
                    self.add_data(0)
                    self.add_circ1()
            #accepts input for the button for column 2
            if 105<x<155 and 420<y<460 and not (self.is_win('red') or self.is_win('black')):
                if self.col2 <6:
                    self.turns += 1
                    self.col2 += 1
                    self.add_data(1)
                    self.add_circ2()
            #accepts input for the button for column 3
            if 165<x<205 and 420<y<460 and not (self.is_win('red') or self.is_win('black')):
                if self.col3 <6:
                    self.turns += 1
                    self.col3 += 1
                    self.add_data(2)
                    self.add_circ3()
            #accepts input for the button for column 4
            if 215<x<275 and 420<y<460 and not (self.is_win('red') or self.is_win('black')):
                if self.col4 < 6:
                    self.turns += 1
                    self.col4 += 1
                    self.add_data(3)
                    self.add_circ4()
            #accepts input for the button for column 5
            if 285<x<335 and 420<y<460 and not (self.is_win('red') or self.is_win('black')):
                if self.col5 < 6:
                    self.turns += 1
                    self.col5 += 1
                    self.add_data(4)
                    self.add_circ5()
            #accepts input for the button for column 6
            if 345<x<395 and 420<y<460 and not (self.is_win('red') or self.is_win('black')):
                if self.col6 < 6:
                    self.turns += 1
                    self.col6 += 1
                    self.add_data(5)
                    self.add_circ6()
            #accepts input for the button for column 7
            if 405<x<455 and 420<y<460 and not (self.is_win('red') or self.is_win('black')):
                if self.col7 < 6:
                    self.turns += 1
                    self.col7 += 1
                    self.add_data(6)
                    self.add_circ7()
            #accepts input for the exit button
            if 1<x<75 and 25<y<75:
                win.close()
            #accepts input for the clear board button
            if 425 < x < 500 and 25<y<75:
                self.draw_Back()
                self.draw_cols()
                self.draw_rows()
                self.draw_buttons()
                self.draw_exit()
                self.draw_clear()
                self.draw_Title()
                self.draw_inst()
                self.slots = [[' '] * 7 for row in range(6)]
                self.turns = 0
                self.col1 = 0
                self.col2 = 0
                self.col3 = 0
                self.col4 = 0
                self.col5 = 0
                self.col6 = 0
                self.col7 = 0
            self.result()

    #updates the list with the player's input
    def add_data(self, col):
        if self.turns % 2 == 0:
            found = False
            for row in range(6)[::-1]:
                if not found and self.slots[row][col] == ' ':
                    self.slots[row][col] = 'black'
                    found = True

        if self.turns % 2 != 0:
            found = False
            for row in range(6)[::-1]:
                if not found and self.slots[row][col] == ' ':
                    self.slots[row][col] = 'red'
                    found = True

    #draws a circle for column 1 depending on how many circles have already been drawn in column 1
    def add_circ1(self):
        if self.col1 == 1:
            circ = Circle(Point(70,375),20)
            circ.setOutline('Black')
            circ.setWidth(2)
            if self.turns%2 != 0:
                circ.setFill('Red')
                circ.draw(win)
            if self.turns%2 == 0:
                circ.setFill('Black')
                circ.draw(win)
        if self.col1 == 2:
            circ = Circle(Point(70,325),20)
            circ.setOutline('Black')
            circ.setWidth(2)
            if self.turns%2 != 0:
                circ.setFill('Red')
                circ.draw(win)
            if self.turns%2 == 0:
                circ.setFill('Black')
                circ.draw(win)
        if self.col1 == 3:
            circ = Circle(Point(70,275),20)
            circ.setOutline('Black')
            circ.setWidth(2)
            if self.turns%2 != 0:
                circ.setFill('Red')
                circ.draw(win)
            if self.turns%2 == 0:
                circ.setFill('Black')
                circ.draw(win)
        if self.col1 == 4:
            circ = Circle(Point(70,225),20)
            circ.setOutline('Black')
            circ.setWidth(2)
            if self.turns%2 != 0:
                circ.setFill('Red')
                circ.draw(win)
            if self.turns%2 == 0:
                circ.setFill('Black')
                circ.draw(win)
        if self.col1 == 5:
            circ = Circle(Point(70,175),20)
            circ.setOutline('Black')
            circ.setWidth(2)
            if self.turns%2 != 0:
                circ.setFill('Red')
                circ.draw(win)
            if self.turns%2 == 0:
                circ.setFill('Black')
                circ.draw(win)
        if self.col1 == 6:
            circ = Circle(Point(70,125),20)
            circ.setOutline('Black')
            circ.setWidth(2)
            if self.turns%2 != 0:
                circ.setFill('Red')
                circ.draw(win)
            if self.turns%2 == 0:
                circ.setFill('Black')
                circ.draw(win)
    #draws a circle for column 2 depending on how many circles have already been drawn in column 2
    def add_circ2(self):
        if self.col2 == 1:
            circ = Circle(Point(130,375),20)
            circ.setOutline('Black')
            circ.setWidth(2)
            if self.turns%2 != 0:
                circ.setFill('Red')
                circ.draw(win)
            if self.turns%2 == 0:
                circ.setFill('Black')
                circ.draw(win)
        if self.col2 == 2:
            circ = Circle(Point(130,325),20)
            circ.setOutline('Black')
            circ.setWidth(2)
            if self.turns%2 != 0:
                circ.setFill('Red')
                circ.draw(win)
            if self.turns%2 == 0:
                circ.setFill('Black')
                circ.draw(win)
        if self.col2 == 3:
            circ = Circle(Point(130,275),20)
            circ.setOutline('Black')
            circ.setWidth(2)
            if self.turns%2 != 0:
                circ.setFill('Red')
                circ.draw(win)
            if self.turns%2 == 0:
                circ.setFill('Black')
                circ.draw(win)
        if self.col2 == 4:
            circ = Circle(Point(130,225),20)
            circ.setOutline('Black')
            circ.setWidth(2)
            if self.turns%2 != 0:
                circ.setFill('Red')
                circ.draw(win)
            if self.turns%2 == 0:
                circ.setFill('Black')
                circ.draw(win)
        if self.col2 == 5:
            circ = Circle(Point(130,175),20)
            circ.setOutline('Black')
            circ.setWidth(2)
            if self.turns%2 != 0:
                circ.setFill('Red')
                circ.draw(win)
            if self.turns%2 == 0:
                circ.setFill('Black')
                circ.draw(win)
        if self.col2 == 6:
            circ = Circle(Point(130,125),20)
            circ.setOutline('Black')
            circ.setWidth(2)
            if self.turns%2 != 0:
                circ.setFill('Red')
                circ.draw(win)
            if self.turns%2 == 0:
                circ.setFill('Black')
                circ.draw(win)
    #draws a circle for column 3 depending on how many circles have already been drawn in column 3
    def add_circ3(self):
        if self.col3 == 1:
            circ = Circle(Point(190,375),20)
            circ.setOutline('Black')
            circ.setWidth(2)
            if self.turns%2 != 0:
                circ.setFill('Red')
                circ.draw(win)
            if self.turns%2 == 0:
                circ.setFill('Black')
                circ.draw(win)
        if self.col3 == 2:
            circ = Circle(Point(190,325),20)
            circ.setOutline('Black')
            circ.setWidth(2)
            if self.turns%2 != 0:
                circ.setFill('Red')
                circ.draw(win)
            if self.turns%2 == 0:
                circ.setFill('Black')
                circ.draw(win)
        if self.col3 == 3:
            circ = Circle(Point(190,275),20)
            circ.setOutline('Black')
            circ.setWidth(2)
            if self.turns%2 != 0:
                circ.setFill('Red')
                circ.draw(win)
            if self.turns%2 == 0:
                circ.setFill('Black')
                circ.draw(win)
        if self.col3 == 4:
            circ = Circle(Point(190,225),20)
            circ.setOutline('Black')
            circ.setWidth(2)
            if self.turns%2 != 0:
                circ.setFill('Red')
                circ.draw(win)
            if self.turns%2 == 0:
                circ.setFill('Black')
                circ.draw(win)
        if self.col3 == 5:
            circ = Circle(Point(190,175),20)
            circ.setOutline('Black')
            circ.setWidth(2)
            if self.turns%2 != 0:
                circ.setFill('Red')
                circ.draw(win)
            if self.turns%2 == 0:
                circ.setFill('Black')
                circ.draw(win)
        if self.col3 == 6:
            circ = Circle(Point(190,125),20)
            circ.setOutline('Black')
            circ.setWidth(2)
            if self.turns%2 != 0:
                circ.setFill('Red')
                circ.draw(win)
            if self.turns%2 == 0:
                circ.setFill('Black')
                circ.draw(win)
    #draws a circle for column 4 depending on how many circles have already been drawn in column 4
    def add_circ4(self):
        if self.col4 == 1:
            circ = Circle(Point(250,375),20)
            circ.setOutline('Black')
            circ.setWidth(2)
            if self.turns%2 != 0:
                circ.setFill('Red')
                circ.draw(win)
            if self.turns%2 == 0:
                circ.setFill('Black')
                circ.draw(win)
        if self.col4 == 2:
            circ = Circle(Point(250,325),20)
            circ.setOutline('Black')
            circ.setWidth(2)
            if self.turns%2 != 0:
                circ.setFill('Red')
                circ.draw(win)
            if self.turns%2 == 0:
                circ.setFill('Black')
                circ.draw(win)
        if self.col4 == 3:
            circ = Circle(Point(250,275),20)
            circ.setOutline('Black')
            circ.setWidth(2)
            if self.turns%2 != 0:
                circ.setFill('Red')
                circ.draw(win)
            if self.turns%2 == 0:
                circ.setFill('Black')
                circ.draw(win)
        if self.col4 == 4:
            circ = Circle(Point(250,225),20)
            circ.setOutline('Black')
            circ.setWidth(2)
            if self.turns%2 != 0:
                circ.setFill('Red')
                circ.draw(win)
            if self.turns%2 == 0:
                circ.setFill('Black')
                circ.draw(win)
        if self.col4 == 5:
            circ = Circle(Point(250,175),20)
            circ.setOutline('Black')
            circ.setWidth(2)
            if self.turns%2 != 0:
                circ.setFill('Red')
                circ.draw(win)
            if self.turns%2 == 0:
                circ.setFill('Black')
                circ.draw(win)
        if self.col4 == 6:
            circ = Circle(Point(250,125),20)
            circ.setOutline('Black')
            circ.setWidth(2)
            if self.turns%2 != 0:
                circ.setFill('Red')
                circ.draw(win)
            if self.turns%2 == 0:
                circ.setFill('Black')
                circ.draw(win)
    #draws a circle for column 5 depending on how many circles have already been drawn in column 5
    def add_circ5(self):
        if self.col5 == 1:
            circ = Circle(Point(310,375),20)
            circ.setOutline('Black')
            circ.setWidth(2)
            if self.turns%2 != 0:
                circ.setFill('Red')
                circ.draw(win)
            if self.turns%2 == 0:
                circ.setFill('Black')
                circ.draw(win)
        if self.col5 == 2:
            circ = Circle(Point(310,325),20)
            circ.setOutline('Black')
            circ.setWidth(2)
            if self.turns%2 != 0:
                circ.setFill('Red')
                circ.draw(win)
            if self.turns%2 == 0:
                circ.setFill('Black')
                circ.draw(win)
        if self.col5 == 3:
            circ = Circle(Point(310,275),20)
            circ.setOutline('Black')
            circ.setWidth(2)
            if self.turns%2 != 0:
                circ.setFill('Red')
                circ.draw(win)
            if self.turns%2 == 0:
                circ.setFill('Black')
                circ.draw(win)
        if self.col5 == 4:
            circ = Circle(Point(310,225),20)
            circ.setOutline('Black')
            circ.setWidth(2)
            if self.turns%2 != 0:
                circ.setFill('Red')
                circ.draw(win)
            if self.turns%2 == 0:
                circ.setFill('Black')
                circ.draw(win)
        if self.col5 == 5:
            circ = Circle(Point(310,175),20)
            circ.setOutline('Black')
            circ.setWidth(2)
            if self.turns%2 != 0:
                circ.setFill('Red')
                circ.draw(win)
            if self.turns%2 == 0:
                circ.setFill('Black')
                circ.draw(win)
        if self.col5 == 6:
            circ = Circle(Point(310,125),20)
            circ.setOutline('Black')
            circ.setWidth(2)
            if self.turns%2 != 0:
                circ.setFill('Red')
                circ.draw(win)
            if self.turns%2 == 0:
                circ.setFill('Black')
                circ.draw(win)
    #draws a circle for column 6 depending on how many circles have already been drawn in column 6
    def add_circ6(self):
        if self.col6 == 1:
            circ = Circle(Point(370,375),20)
            circ.setOutline('Black')
            circ.setWidth(2)
            if self.turns%2 != 0:
                circ.setFill('Red')
                circ.draw(win)
            if self.turns%2 == 0:
                circ.setFill('Black')
                circ.draw(win)
        if self.col6 == 2:
            circ = Circle(Point(370,325),20)
            circ.setOutline('Black')
            circ.setWidth(2)
            if self.turns%2 != 0:
                circ.setFill('Red')
                circ.draw(win)
            if self.turns%2 == 0:
                circ.setFill('Black')
                circ.draw(win)
        if self.col6 == 3:
            circ = Circle(Point(370,275),20)
            circ.setOutline('Black')
            circ.setWidth(2)
            if self.turns%2 != 0:
                circ.setFill('Red')
                circ.draw(win)
            if self.turns%2 == 0:
                circ.setFill('Black')
                circ.draw(win)
        if self.col6 == 4:
            circ = Circle(Point(370,225),20)
            circ.setOutline('Black')
            circ.setWidth(2)
            if self.turns%2 != 0:
                circ.setFill('Red')
                circ.draw(win)
            if self.turns%2 == 0:
                circ.setFill('Black')
                circ.draw(win)
        if self.col6 == 5:
            circ = Circle(Point(370,175),20)
            circ.setOutline('Black')
            circ.setWidth(2)
            if self.turns%2 != 0:
                circ.setFill('Red')
                circ.draw(win)
            if self.turns%2 == 0:
                circ.setFill('Black')
                circ.draw(win)
        if self.col6 == 6:
            circ = Circle(Point(370,125),20)
            circ.setOutline('Black')
            circ.setWidth(2)
            if self.turns%2 != 0:
                circ.setFill('Red')
                circ.draw(win)
            if self.turns%2 == 0:
                circ.setFill('Black')
                circ.draw(win)
    #draws a circle for column 7 depending on how many circles have already been drawn in column 7
    def add_circ7(self):
        if self.col7 == 1:
            circ = Circle(Point(430,375),20)
            circ.setOutline('Black')
            circ.setWidth(2)
            if self.turns%2 != 0:
                circ.setFill('Red')
                circ.draw(win)
            if self.turns%2 == 0:
                circ.setFill('Black')
                circ.draw(win)
        if self.col7 == 2:
            circ = Circle(Point(430,325),20)
            circ.setOutline('Black')
            circ.setWidth(2)
            if self.turns%2 != 0:
                circ.setFill('Red')
                circ.draw(win)
            if self.turns%2 == 0:
                circ.setFill('Black')
                circ.draw(win)
        if self.col7 == 3:
            circ = Circle(Point(430,275),20)
            circ.setOutline('Black')
            circ.setWidth(2)
            if self.turns%2 != 0:
                circ.setFill('Red')
                circ.draw(win)
            if self.turns%2 == 0:
                circ.setFill('Black')
                circ.draw(win)
        if self.col7 == 4:
            circ = Circle(Point(430,225),20)
            circ.setOutline('Black')
            circ.setWidth(2)
            if self.turns%2 != 0:
                circ.setFill('Red')
                circ.draw(win)
            if self.turns%2 == 0:
                circ.setFill('Black')
                circ.draw(win)
        if self.col7 == 5:
            circ = Circle(Point(430,175),20)
            circ.setOutline('Black')
            circ.setWidth(2)
            if self.turns%2 != 0:
                circ.setFill('Red')
                circ.draw(win)
            if self.turns%2 == 0:
                circ.setFill('Black')
                circ.draw(win)
        if self.col7 == 6:
            circ = Circle(Point(430,125),20)
            circ.setOutline('Black')
            circ.setWidth(2)
            if self.turns%2 != 0:
                circ.setFill('Red')
                circ.draw(win)
            if self.turns%2 == 0:
                circ.setFill('Black')
                circ.draw(win)

    #checks if the board is full, resulting in a tie
    def is_full(self):
        if self.turns==42:
            return True
        return False
    #checks if a player has won horizontally
    def is_horizontal_win(self, ind):
        for row in range(6):
            for col in range(4):
                if self.slots[row][col] == ind and self.slots[row][col + 1] == ind and self.slots[row][col + 2] == ind and self.slots[row][col + 3] == ind:
                    return True
        return False
    #checks if a player has won vertically
    def is_vertical_win(self,ind):
        for row in range(3):
            for col in range(7):
                if self.slots[row][col] == ind and self.slots[row+1][col] == ind and self.slots[row+2][col] == ind and self.slots[row+3][col] == ind:

                    return True
        return False
    #checks if a player has won on an increasing diagonal
    def is_up_diagonal_win(self,ind):
        for row in range(3, 6):
            for col in range(4):
                if self.slots[row][col] == ind and self.slots[row-1][col+1] == ind and self.slots[row-2][col+2] == ind and self.slots[row-3][col+3] == ind:
                    return True
        return False
    #checks if a player has won on a decreasing diagonal
    def is_down_diagonal_win(self,ind):
        for row in range(3):
            for col in range(4):
                if self.slots[row][col] == ind and self.slots[row+1][col+1] == ind and self.slots[row+2][col+2] == ind and self.slots[row+3][col+3] == ind:
                    return True
        return False
    #checks if a player has won
    def is_win(self, ind):
        if self.is_horizontal_win(ind) or self.is_vertical_win(ind) or self.is_up_diagonal_win(ind) or self.is_down_diagonal_win(ind):
            return True
        return False
    #draws text declaring a winner depending on who has won, and a tie if neither has
    def result(self):
        if self.is_win('red'):
            wht_box = Rectangle(Point(160,200),Point(340,300))
            wht_box.setOutline('Black')
            wht_box.setFill('White')
            wht_box.draw(win)
            wrd = Text(Point(250,250), 'Red Wins!')
            wrd.setTextColor('Red')
            wrd.setSize('36')
            wrd.draw(win)
        if self.is_win('black'):
            wht_box = Rectangle(Point(155,200),Point(345,300))
            wht_box.setOutline('Black')
            wht_box.setFill('White')
            wht_box.draw(win)
            wrd = Text(Point(250,250), 'Black Wins!')
            wrd.setTextColor('Black')
            wrd.setSize('36')
            wrd.draw(win)
        if self.is_full():
            wht_box = Rectangle(Point(160,200),Point(340,300))
            wht_box.setOutline('Black')
            wht_box.setFill('White')
            wht_box.draw(win)
            wrd = Text(Point(250,250), 'Tie!')
            wrd.setTextColor('Green')
            wrd.setSize('36')
            wrd.draw(win)

#plays the game by drawing a board
def play_con4():
    con = Board()

#calling the function to play the game
play_con4()
win.mainloop()
