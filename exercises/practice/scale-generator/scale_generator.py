class Scale:
    CHROMATIC_SCALE_SHARPS = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    CHROMATIC_SCALE_FLATS = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']

    @staticmethod
    def use_sharps(tonic):
        return tonic.upper() in ('A', 'C', 'D', 'E', 'G', 'D#', 'A#', 'E#', 'B#', 'F##', 'C##', 'G##')
    def __init__(self, tonic):
        self.tonic = tonic.capitalize()
        self.chromatic_scale = self.CHROMATIC_SCALE_SHARPS if self.use_sharps(tonic) else self.CHROMATIC_SCALE_FLATS

    def chromatic(self):
        start = self.chromatic_scale.index(self.tonic)
        return self.chromatic_scale[start:] + self.chromatic_scale[:start]

    def interval(self, intervals):
        chromatic = self.chromatic()
        scale = [chromatic[0]]
        index = 0
        for interval in intervals:
            if interval == 'M':
                index += 2
            elif interval == 'm':
                index += 1
            elif interval == 'A':
                index += 3
            index %= len(chromatic)
            scale.append(chromatic[index])
        return scale
            if 'b' in note:
                note = note.replace('b', '♭')
            elif '#' in note:
                note = note.replace('#', '♯')
            scale.append(note)
        return scale
        return scale
