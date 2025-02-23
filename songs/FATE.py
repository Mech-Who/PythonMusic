import musicpy as mp

from basic.notes import *
from basic.beats import Beat

f = Beat.FULL # 1/4
h = Beat.HALF # 1/8
q = Beat.QUAR # 1/16

notes_dict = {
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


def str2chord(mapping_dict, str_notes):
    """
    mapping_dict: {"your definition": "c1_1"}, every note will be used should be found in this dict. And the real note should be represent by 'cx_y', while 'x' means pitch, 'y' means name of the note in number.
    str_notes: notes represent by str.
    """
    notes = str_notes.split()
    chords = []
    final_notes = []
    for note in notes:
        if note == "0":
            if len(final_notes) > 0:
                note_size = len(final_notes)
                dura = [1/4]*note_size
                chord = mp.chord(notes=final_notes, duration=dura, interval=dura)
                chords.append(chord)
                final_notes.clear()
            chords.append(mp.rest(1/4))
        else:
            final_notes.append(eval(mapping_dict[note]))
    return chords


def fate():
    music = [
        "1,2,3,-,3,3,2,-",
        "7.-1,1,2,5,7.-1,1,r,r",
        "6.-1,7.-1,1,-,3,3,2,1",
        "2,3,r,r,r,r,r,r",
        "1,2,3,-,3,3,2,-",
        "7.-1,1,2,5,7.-1,1,r,r",
        "3,3,2,1,7.-1,1,-,-",
        "r,r,r,r",
        "1[.16;.],2[.8],3.,5[.4.],3,3,2,-",
        "7.-1[.16;.],1[.8],2.,5[.4.],7.-1,7.-1,1 ,-",
        "6.-1,7.-1,1,6.-1,3,3,2,1",
        "2,3,-,-,r,r,r,r",
        "1.1,7,5,-,2[.4.],1[.4.],-,-",
        "1.1,7,5,-,2[.4.],1[.4.],-,-",
        "2,2,1,2,2,1,1,-",
        "-,-,-,-",
        "1[.4.],2[.4.],3[.4.],5[.4.],6,r,r,6[.4.]",
        "5#[.4.],r,r,5#[.4.],6,-,3.,2.",
        "1.,-,r,r",
        "1[.4.],3[.4.],5[.4.],6[.4.],r,r,,6[.4.],5[.4.],r,r,5[.2],6,-,1.1,-,6,-,5[.4],6[.4],r,r",
        "6,-,1.1,-,7.,5,5[.4.],3[.16],6[.16],3,2,1[.16;.],1[.16],-,-",
        "6,6,6,6[.16;.],1.1.,1.1[.8;.],7,7,7[.16;.],1.1,6,-,-,-"
    ]

    chord = mp.S("C major").get(",".join(music).replace(" ",""))

    return {
        "name": "Fate.mid",
        "current_chord": chord,
        "bpm": 120
    }
