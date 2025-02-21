import musicpy as mp

from songs.FATE import fate

def main():
    mp.play(**fate())

if __name__ == "__main__":
    main()
