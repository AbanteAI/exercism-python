class Scale:
    def __init__(self, tonic):
        self.tonic = tonic.upper()
        if tonic.upper() in ["C", "G", "D", "A", "E", "B", "F#", "Ab"]:
            self.use_sharps = True
        else:
            self.use_sharps = False

    def chromatic(self):
        chromatic_sharps = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
        chromatic_flats = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]
        chromatic = chromatic_sharps if self.use_sharps else chromatic_flats
        start = chromatic.index(self.tonic)
        return chromatic[start:] + chromatic[:start]

    def interval(self, intervals):
        chromatic_scale = self.chromatic()
        scale = [self.tonic]
        current_index = 0
        for interval in intervals:
            if interval == "m":
                current_index += 1
            elif interval == "M":
                current_index += 2
            elif interval == "A":
                current_index += 3
            scale.append(chromatic_scale[current_index % len(chromatic_scale)])
        return scale
