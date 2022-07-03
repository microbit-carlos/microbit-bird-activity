# This is a temporary class for SoundEffect to get the code to
# run without errors until MicroPython implements it
from audio import *
import music as __m

WAVE_SINE = "sine"
WAVE_SAWTOOTH = "sawtooth"
WAVE_TRIANGLE = "triangle"
WAVE_SQUARE = "square"
WAVE_NOISE = "noise"
FX_TREMOLO = "tremolo"
FX_VIBRATO = "vibrato"
FX_WARBLE = "warble"
INTER_LINEAR = "linear"
INTER_CURVE = "curve"
INTER_LOG = "log"


class SoundEffect():
    def __init__(
        self,
        preset=None,
        freq_start=500,
        freq_end=2500,
        duration=500,
        vol_start=255,
        vol_end=0,
        wave=WAVE_SQUARE,
        fx=None,
        interpolation=INTER_LOG
    ):
        pass


__audio_play = play

def play(*argv, **kwargs):
    print(argv)
    print(kwargs)
    if type(argv[0]) == SoundEffect:
        print("SoundEffect!")
        __m.play(__m.JUMP_UP, **kwargs)
    else:
        print("Other")
        __audio_play(*argv, **kwargs)
