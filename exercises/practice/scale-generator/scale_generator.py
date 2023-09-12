import itertools
import string
class Scale:
    def __init__(self, tonic):
        self.tonic = tonic.capitalize()
        self.sharps = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
        self.flats = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']
        self.chromatic_scale = self._create_chromatic_scale()

    def chromatic(self):
        return self.chromatic_scale

    def interval(self, intervals):
        scale = []
        index = 0
        for step in intervals:
            scale.append(self.chromatic_scale[index])
            index += {'m': 1, 'M': 2, 'A': 3}[step]
        return scale
    def _create_chromatic_scale(self):
        scale = self.sharps if self.tonic in self.sharps else self.flats
        start = scale.index(self.tonic)
        return list(itertools.islice(itertools.cycle(scale), start, start + 12))
