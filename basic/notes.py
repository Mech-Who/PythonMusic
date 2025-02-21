from enum import StrEnum, IntEnum, auto

import musicpy as mp


class Pitch(IntEnum):
    LOWEST = auto() # 1
    LOWER = auto()  # 2
    LOW = auto()    # 3
    BASE = auto()   # 4
    HIGH = auto()  # 5
    HIGHER = auto() # 6
    HIGHEST = auto()# 7


class Note(StrEnum):
    """
    1234567
    CDEFGAB
    """
    n1 = "C"
    n2 = "D"
    n3 = "E"
    n4 = "F"
    n5 = "G"
    n6 = "A"
    n7 = "B"

def str2note(mapping_dict, str_notes):
    """
    mapping_dict: {"your definition": "c1_1"}, every note will be used should be found in this dict. And the real note should be represent by 'cx_y', while 'x' means pitch, 'y' means name of the note in number.
    str_notes: notes represent by str.
    """
    notes = str_notes.split()
    final_notes = []
    for note in notes:
        final_notes.append(eval(mapping_dict[note]))
    return final_notes

rest = None

# lowest
c1_1 = mp.note(Note.n1, Pitch.LOWEST)
c1_2 = mp.note(Note.n2, Pitch.LOWEST)
c1_3 = mp.note(Note.n3, Pitch.LOWEST)
c1_4 = mp.note(Note.n4, Pitch.LOWEST)
c1_5 = mp.note(Note.n5, Pitch.LOWEST)
c1_6 = mp.note(Note.n6, Pitch.LOWEST)
c1_7 = mp.note(Note.n7, Pitch.LOWEST)

# lower
c2_1 = mp.note(Note.n1, Pitch.LOWER)
c2_2 = mp.note(Note.n2, Pitch.LOWER)
c2_3 = mp.note(Note.n3, Pitch.LOWER)
c2_4 = mp.note(Note.n4, Pitch.LOWER)
c2_5 = mp.note(Note.n5, Pitch.LOWER)
c2_6 = mp.note(Note.n6, Pitch.LOWER)
c2_7 = mp.note(Note.n7, Pitch.LOWER)

# low
c3_1 = mp.note(Note.n1, Pitch.LOW)
c3_2 = mp.note(Note.n2, Pitch.LOW)
c3_3 = mp.note(Note.n3, Pitch.LOW)
c3_4 = mp.note(Note.n4, Pitch.LOW)
c3_5 = mp.note(Note.n5, Pitch.LOW)
c3_6 = mp.note(Note.n6, Pitch.LOW)
c3_7 = mp.note(Note.n7, Pitch.LOW)

# base
c4_1 = mp.note(Note.n1, Pitch.BASE)
c4_2 = mp.note(Note.n2, Pitch.BASE)
c4_3 = mp.note(Note.n3, Pitch.BASE)
c4_4 = mp.note(Note.n4, Pitch.BASE)
c4_5 = mp.note(Note.n5, Pitch.BASE)
c4_6 = mp.note(Note.n6, Pitch.BASE)
c4_7 = mp.note(Note.n7, Pitch.BASE)

# high
c5_1 = mp.note(Note.n1, Pitch.HIGH)
c5_2 = mp.note(Note.n2, Pitch.HIGH)
c5_3 = mp.note(Note.n3, Pitch.HIGH)
c5_4 = mp.note(Note.n4, Pitch.HIGH)
c5_5 = mp.note(Note.n5, Pitch.HIGH)
c5_6 = mp.note(Note.n6, Pitch.HIGH)
c5_7 = mp.note(Note.n7, Pitch.HIGH)

# higher
c6_1 = mp.note(Note.n1, Pitch.HIGHER)
c6_2 = mp.note(Note.n2, Pitch.HIGHER)
c6_3 = mp.note(Note.n3, Pitch.HIGHER)
c6_4 = mp.note(Note.n4, Pitch.HIGHER)
c6_5 = mp.note(Note.n5, Pitch.HIGHER)
c6_6 = mp.note(Note.n6, Pitch.HIGHER)
c6_7 = mp.note(Note.n7, Pitch.HIGHER)

# highest
c7_1 = mp.note(Note.n1, Pitch.HIGHEST)
c7_2 = mp.note(Note.n2, Pitch.HIGHEST)
c7_3 = mp.note(Note.n3, Pitch.HIGHEST)
c7_4 = mp.note(Note.n4, Pitch.HIGHEST)
c7_5 = mp.note(Note.n5, Pitch.HIGHEST)
c7_6 = mp.note(Note.n6, Pitch.HIGHEST)
c7_7 = mp.note(Note.n7, Pitch.HIGHEST)
