import musicpy as mp

def queencard():
    music = [
        "3,5,3,4,r,r,3,3,3,5,3,4,r,r",
        "3,3,3,5,3,4,3,3,r,r",
        "3,5,3,4,r,r,3,3,3,5,3,4,r,r",
        "3,3,3,5,3,4,3,3,r,r",
        "3,3,6,3,r,r,2,3,4,3,r,r,2,3,r,r",
        "6,3,3,4,3,r,r,2,3,r,r",
        "3,3,6,3,r,r,2,3,4,3,r,r,2,6,r,r",
        "3,3,2,6.-1,r,r",
        "3,3,6,3,r,r,2,3,4,3,r,r,2,3,r,r",
        "6,3,3,4,3,r,r,2,3,r,r",
        "3,3,6,3,r,r,2,3,4,3,r,r,2,3,r,r",
        "3,3,2,1,2,3,6.-1,r,r"
    ]

    chord = mp.S("C major").get(",".join(music).replace(" ",""))

    return {
        "name": "Tomboy.mid",
        "current_chord": chord,
        "bpm": 120
    }
