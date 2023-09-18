class Scale:
    CHROMATIC_SCALE_SHARPS = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    CHROMATIC_SCALE_FLATS = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]
    SHARP_KEYS = ["G", "D", "A", "E", "B", "F#", "a", "e", "b", "f#", "c#", "g#", "d#"]
    def __init__(self, tonic):
        self.tonic = tonic if tonic.islower() else tonic.capitalize()
        self.use_sharps = self.tonic.capitalize() in self.SHARP_KEYS
        self.base_scale = self.CHROMATIC_SCALE_SHARPS if self.use_sharps else self.CHROMATIC_SCALE_FLATS

    def chromatic(self):
        start_idx = self.base_scale.index(self.tonic.capitalize())
        chromatic_scale = self.base_scale[start_idx:] + self.base_scale[:start_idx]
        return chromatic_scale

    def interval(self, intervals):
        chromatic_scale = self.chromatic()
        scale = [self.tonic]
        idx = chromatic_scale.index(self.tonic)
        for interval in intervals:
            if interval == "m":
                idx += 1
            elif interval == "M":
                idx += 2
            elif interval == "A":
                idx += 3
            idx %= len(chromatic_scale)
            scale.append(chromatic_scale[idx])
        return scale[:-1]
