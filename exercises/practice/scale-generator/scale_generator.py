class Scale:
    def __init__(self, tonic):
        self.tonic = tonic.capitalize()
        self.notes_sharps = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
        self.notes_flats = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]

    def chromatic(self):
        if self.tonic in self.notes_sharps:
            notes = self.notes_sharps
        else:
            notes = self.notes_flats
        start = notes.index(self.tonic)
        return notes[start:] + notes[:start]

    def interval(self, intervals):
        chromatic_scale = self.chromatic()
        scale = [chromatic_scale[0]]
        index = 0
        for interval in intervals[:-1]:
            if interval == "M":
                index += 2
            elif interval == "m":
                index += 1
            elif interval == "A":
                index += 3
            scale.append(chromatic_scale[index % len(chromatic_scale)])
        return scale