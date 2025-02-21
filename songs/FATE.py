import musicpy as mp

from basic.notes import *
from basic.beats import Beat

f = Beat.FULL # 1/4
h = Beat.HALF # 1/8
q = Beat.QUAR # 1/16

notes_dict = {
    "0": "rest",
    "1_": "c2_1",
    "2_": "c2_2",
    "3_": "c2_3",
    "4_": "c2_4",
    "5_": "c2_5",
    "6_": "c2_6",
    "7_": "c2_7",
    "1": "c3_1",
    "2": "c3_2",
    "3": "c3_3",
    "4": "c3_4",
    "5": "c3_5",
    "6": "c3_6",
    "7": "c3_7",
    "_1": "c4_1",
    "_2": "c4_2",
    "_3": "c4_3",
    "_4": "c4_4",
    "_5": "c4_5",
    "_6": "c4_6",
    "_7": "c4_7",
}

def fate():

    notes = "_1 7 5 5 2 1"
    notes = str2note(notes_dict, notes)
    duration = [h, h, h, h, h, f]
    c1 = mp.chord(notes=notes, duration=duration, interval=duration)

    notes = "3_ 2 1 3 2 1 1"
    notes = str2note(notes_dict, notes)
    duration = [h, h, h, h, h, h, h]
    c2 = mp.chord(notes=notes, duration=duration, interval=duration)

    notes = "3 1"
    notes = str2note(notes_dict, notes)
    duration = [f, f]
    c3 = mp.chord(notes=notes, duration=duration, interval=duration)

    final_piece = mp.rest(h) | c1 | mp.rest(h) | c2 | mp.rest(f+f) | c3

    return {
        "name": "FATE.mid",
        "current_chord": final_piece,
        "bpm": 240
    }
