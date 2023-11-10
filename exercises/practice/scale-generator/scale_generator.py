class Scale:
    def __init__(self, tonic):
        self.tonic = tonic.capitalize()
        self.sharps = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        self.flats = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
        self.use_flats = tonic in ['F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb', 'd', 'g', 'c', 'f', 'bb', 'eb']
        self.tonic = tonic.capitalize()
        self.sharps = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        self.flats = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
        self.use_flats = tonic in ['F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb', 'd', 'g', 'c', 'f', 'bb', 'eb']

    def chromatic(self):
        if self.use_flats:
            scale = self.flats
        else:
            scale = self.sharps
        tonic_index = scale.index(self.tonic)
        return scale[tonic_index:] + scale[:tonic_index]
            scale = self.flats
        else:
            scale = self.sharps
        tonic_index = scale.index(self.tonic)
        return scale[tonic_index:] + scale[:tonic_index]

    def interval(self, intervals):
        scale = self.chromatic()
        interval_steps = {'m': 1, 'M': 2, 'A': 3}
        result = [self.tonic]
        index = 0
        for interval in intervals:
            index += interval_steps[interval]
            result.append(scale[index % len(scale)])
        return result
        interval_steps = {'m': 1, 'M': 2, 'A': 3}
        result = [self.tonic]
        index = 0
        for interval in intervals:
            index += interval_steps[interval]
            result.append(scale[index % len(scale)])
        return result
