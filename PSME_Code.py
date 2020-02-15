# PSME Code.py

from tkinter import *;
import random as r;

"""
-start
-all rules are loaded to rules array
-by default, all rules should be added to pool list (all checkbuttons should be checked)
-window opens, choose which category of rules via checkButton
    - 1 to 3
    - 3 to 5
    - 5 to 10, etc
-add checked sections to pool, close and opens main window
-randomize question and 3 wrong answers for choices
-show question and choices in a new window


"""

rules = [];
pool = [];
cat_bool = [];
score = 0;
items = 0;
remarks = "black";
state = [];
cat = [];
percentage = 0;


class choices:
    buttonsize_x = 10;
    buttonsize_y = 5;

    def updateGrid():
        global rightx, righty, wrongx, wrongy;
        rightx = r.randint(0, 1);
        righty = r.randint(0, 1);

        if rightx == 0:
            wrongx = 1;
        else:
            wrongx = 0;

        if righty == 0:
            wrongy = 1;
        else:
            wrongy = 0;


    def __init__(self, window, text):
        def rightAnswer(event):
            global score, items, remarks, percentage;
            print("User has chosen the right answer");
            score += 1;
            items += 1;
            percentage = int((score / items) * 100);
            remarks = "green";
            mainWindow();

        choices.updateGrid();
        self = Button(window, text = ("Rule " + text), font = 100);
        self.grid(row = rightx, column = righty, ipadx = choices.buttonsize_x, ipady = choices.buttonsize_y, sticky = N+E+W+S);
        self.bind("<Button-1>", rightAnswer);

    def wrongAnswer():
        global items, remarks, score, percentage;
        print("WRONG, BRUH");
        items += 1;
        percentage = int((score / items) * 100);
        remarks = "red";
        mainWindow();


    @staticmethod
    def wrong1(window, text):
        self = Button(window, text = ("Rule " + text), command = choices.wrongAnswer, font = 100);
        self.grid(row = wrongx, column = wrongy, ipadx = choices.buttonsize_x, ipady = choices.buttonsize_y, sticky = N+E+W+S);

    @staticmethod
    def wrong2(window, text):
        self = Button(window, text = ("Rule " + text), command = choices.wrongAnswer, font = 100);
        self.grid(row = rightx, column = wrongy, ipadx = choices.buttonsize_x, ipady = choices.buttonsize_y, sticky = N+E+W+S);

    @staticmethod
    def wrong3(window, text):
        self = Button(window, text = ("Rule " + text), command = choices.wrongAnswer, font = 100);
        self.grid(row = wrongx, column = righty, ipadx = choices.buttonsize_x, ipady = choices.buttonsize_y, sticky = N+E+W+S);

class check:

    times_called = 0;


    def __init__(self, window, text, state): #Select category options
        self.var = BooleanVar();
        self.checkB = Checkbutton(window, text = text, variable = self.var);
        self.checkB.pack(padx = 20, pady = 3, anchor = W);
        self.state = state;
        if check.times_called == 0:
            self.checkB.select();
        elif self.state == True:
            self.checkB.select();
        else:
            pass;

    def getCheckstate(self):
        return self.var.get();

def about(event):
    ver = "Version: 1.02 \n\n";
    by = "Copyright © 2020 Solomon Castillo \n\n";
    cp = """This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. \n
 This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details. \n
 You should have received a copy of the GNU General Public License along with this program.  If not, see <https://www.gnu.org/licenses/>.""";
    bout = Toplevel();
    bout.title("About");

    about = Label(bout, text = (ver + by + cp), wraplength = 450, justify = CENTER);
    about.pack();

def poolInit():
    global pool;
    for i in range(34):
        pool.append(i);
    pool.remove(0);
    print(pool)

def update():
    answer = 0;
    def selectQuestion():
        global rules;
        nonlocal answer;
        answer = (r.randint(0, (len(pool) - 1)));
        print(pool);
        print(pool[answer]);
        return (rules[pool[answer]]);

    def notAnswer(x):
        nonlocal answer;
        y = x;
        notAns = r.choice(pool);
        if (notAns == 0):
            notAns += 1;
        elif (notAns == None):
            notAns = 1;

        if notAns == y:
            notAns += 1;
            return notAns;
        else:
            return notAns;

    question = Label(questionFrame, text = selectQuestion(), wraplength = 400, justify = CENTER);
    question.config(font = (30));
    question.pack(fill = BOTH);

    correctanswer = choices(choicesFrame, str(pool[answer]));
    wrongans1 = choices.wrong1(choicesFrame, str(notAnswer(pool[answer])));
    wrongans2 = choices.wrong2(choicesFrame, str(notAnswer(pool[answer])));
    wrongans3 = choices.wrong3(choicesFrame, str(notAnswer(pool[answer])));

def mainWindow():
    global root, questionFrame, choicesFrame, menuFrame;

    questionFrame = LabelFrame(root, text = "Question", width = 400, height = 200);
    questionFrame.grid(row = 0, column = 0, sticky = N+E+W+S, ipadx = 10, ipady = 10);
    Grid.columnconfigure(questionFrame, 0, weight = 1);
    Grid.rowconfigure(questionFrame, 0, weight = 1);

    choicesFrame = LabelFrame(root, text = "Choices", width = 400, height = 200, bg = "gray");
    choicesFrame.grid(row = 1, column = 0, sticky = N+E+W+S, ipadx = 10, ipady = 10);
    Grid.columnconfigure(choicesFrame, 0, weight = 1);
    Grid.columnconfigure(choicesFrame, 1, weight = 1);
    Grid.rowconfigure(choicesFrame, 0, weight = 1);
    Grid.rowconfigure(choicesFrame, 1, weight = 1);
    choicesFrame.propagate(False);

    menuFrame = Frame(root, width = 400, height = 50, bg = "white");
    menuFrame.grid(row = 2, column =0, sticky = N+E+W+S, ipadx = 10);
    Grid.columnconfigure(menuFrame, 2, weight = 1);
    Grid.rowconfigure(menuFrame, 0, weight = 1);

    settings = Button(menuFrame, text = "Settings", command = selectCategory);
    settings.grid(row = 0, column = 0, padx = 1);

    refresh = Button(menuFrame, text = "Refresh", command = mainWindow);
    refresh.grid(row = 0, column = 1, padx = 1);

    grade = Label(menuFrame, text = ("Score: " + str(score) + " / " + str(items) + "   (" + str(percentage) + "%)"), bg = remarks, fg = "white");
    grade.grid(row = 0, column = 2, sticky = W+E);

    update();

def selectCategory():

    def checkCategory(event):
        global pool;
        pool = [];
        if cat[0].getCheckstate():
            state[0] = cat[0].getCheckstate();
            for i in range(1, 5):
                pool.append(i);
        else:
            state[0] = False;

        if cat[1].getCheckstate():
            state[1] = cat[1].getCheckstate();
            for i in range(5, 9):
                pool.append(i);
        else:
            state[1] = False;

        if cat[2].getCheckstate():
            state[2] = cat[2].getCheckstate();
            for i in range(9, 12):
                pool.append(i);
        else:
            state[2] = False;

        if cat[3].getCheckstate():
            state[3] = cat[3].getCheckstate();
            for i in range(12, 15):
                pool.append(i);
        else:
            state[3] = False;

        if cat[4].getCheckstate():
            state[4] = cat[4].getCheckstate();
            for i in range(15, 21):
                pool.append(i);
        else:
            state[4] = False;

        if cat[5].getCheckstate():
            state[5] = cat[5].getCheckstate();
            for i in range(21, 31):
                pool.append(i);
        else:
            state[5] = False;

        if cat[6].getCheckstate():
            state[6] = cat[6].getCheckstate();
            for i in range(31, 34):
                pool.append(i);
        else:
            state[6] = False;

        check.times_called += 1;

        print("button state", cat[0].getCheckstate());
        print("saved", cat[0].state);

        print(pool);
        category_win.destroy();

    def selectAll():
        if var.get() == True:
            for i in range(7):
                cat[i].checkB.select();
        else:
            for i in range(7):
                cat[i].checkB.deselect();


    category_win = Toplevel();
    category_win.title("Select Category");
    category_win.resizable(0, 0);

    toptext = Label(category_win, text = "Which categories do you want to be a part of the reviewer?", bg = "#94a197");
    toptext.config(font = ("Courier", 12));
    toptext.pack(padx = 5, pady = 5);

    var = BooleanVar();
    select_butt = Checkbutton(category_win, text = "Select All", command = selectAll, variable = var);
    select_butt.pack(padx = 20, pady = 3, anchor = W);

    cat[0] = check(category_win, "GENERAL PRINCIPLES [Rule 1 - 4]", state[0]);
    cat[1] = check(category_win, "RELATIONS WITH THE STATE [Rule 5 - 8]", state[1]);
    cat[2] = check(category_win, "RELATIONS WITH THE COMMUNITY [Rule 9 - 11]", state[2]);
    cat[3] = check(category_win, "RELATIONS WITH LABOR [Rule 12 - 14]", state[3]);
    cat[4] = check(category_win, "RELATIONS WITH CLIENTS AND EMPLOYERS [Rule 15 - 20]", state[4]);
    cat[5] = check(category_win, "RELATIONS WITH COLLEAGUES AND ASSOCIATES [Rule 21 - 30]", state[5]);
    cat[6] = check(category_win, "PENAL PROVISIONS & EFFECTIVITY [Rule 31 - 33]", state[6]);

    save_button = Button(category_win, text = "Save", width = 20);
    save_button.pack(pady = 10, side = LEFT, padx = 10);
    save_button.bind("<Button-1>", checkCategory);

    about_button = Button(category_win, text = "About", width = 10);
    about_button.pack(side = RIGHT, padx = 10);
    about_button.bind("<Button-1>", about);

def loadRules():
    rules.append(None); #setting index 0 to nothing for simplicity
    with open("PSME_Code.txt", 'r') as f:
        for i in range(1, 34): #second arg should be the number of rules plus 1
            rules.append(f.readline().strip());

def program():
    global root;
    root = Tk();
    root.geometry("400x300+450+200");
    root.minsize(400, 300);
    root.title("PSME Code reviewer");
    Grid.columnconfigure(root, 0, weight = 1);
    Grid.rowconfigure(root, 0, weight = 1);

    for i in range(7):
        state.append(True);
        cat.append(None);

    loadRules();
    poolInit();
    mainWindow();

    root.mainloop();

program();
