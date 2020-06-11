import random
import time
import getch
import os
import sys

loop = True

def scramble():
    face = ["F", "B", "L", "R", "U", "D"]
    move = [" ", "\' ", "2 "]
    loop = True
    i = 1
    scram = ""
    prev_face = ""
    prev_prev_face = ""

    while loop:
        cur_face = random.choice(face)
        if prev_face != cur_face and prev_prev_face != cur_face:
            scram = scram + cur_face+random.choice(move)
            i += 1
            prev_prev_face = prev_face
            prev_face = cur_face
            if i == 20:
                loop = False
        else:
            pass
    if i == 20:
        return scram

def space():
    start_time = time.time()
    chur = getch.getch()
    end_time = time.time()
    time_lapsed = end_time - start_time
    t = str(time_lapsed)
    t = t[0:5]
    return t

def delt():
    readFile = open("times.txt")
    lines = readFile.readlines()
    readFile.close()
    w = open("times.txt", 'w')
    w.writelines([item for item in lines[:-1]])
    w.close()

def main():
    while loop:
        scr = scramble()
        print(scr)
        char = getch.getch()
        if char == " ":
            time = space()
            f = open("times.txt", "a")
            f.write(scr+"      "+time+"\n")
            f.close()
        elif char == "d":
            delt()
        elif char == "e":
            sys.exit()
        os.system('clear')
        print("\n\n")
        g = open("times.txt", "r")
        print(g.read())
        g.close()

if __name__ == '__main__':
    main()
