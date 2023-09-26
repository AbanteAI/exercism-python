class Scale:
    CHROMATIC_SCALE_SHARPS = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    CHROMATIC_SCALE_FLATS = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']

    def __init__(self, tonic):
        self.tonic = tonic.capitalize()

    def chromatic(self):
        if self.tonic in self.CHROMATIC_SCALE_SHARPS:
            scale = self.CHROMATIC_SCALE_SHARPS
        else:
            scale = self.CHROMATIC_SCALE_FLATS

        start_index = scale.index(self.tonic)
        return scale[start_index:] + scale[:start_index]
        pass

    def chromatic(self):
        if self.tonic in self.CHROMATIC_SCALE_SHARPS:
            scale = self.CHROMATIC_SCALE_SHARPS
        else:
            scale = self.CHROMATIC_SCALE_FLATS

        start_index = scale.index(self.tonic)
        return scale[start_index:] + scale[:start_index]
    def chromatic(self):
        if self.tonic in self.CHROMATIC_SCALE_SHARPS:
            scale = self.CHROMATIC_SCALE_SHARPS
        else:
            scale = self.CHROMATIC_SCALE_FLATS

        start_index = scale.index(self.tonic)
        return scale[start_index:] + scale[:start_index]
    INTERVAL_MAPPING = {
        'm': 1,
        'M': 2,
        'A': 3
    }

    def interval(self, intervals):
        scale = [self.tonic]
        current_note = self.tonic

        for interval in intervals:
            steps = self.INTERVAL_MAPPING[interval]
            next_index = (scale.index(current_note) + steps) % len(scale)
            current_note = scale[next_index]
            scale.append(current_note)

        return scale
        pass
