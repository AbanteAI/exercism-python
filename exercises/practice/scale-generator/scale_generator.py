class Scale:
    def __init__(self, tonic):
        self.tonic = tonic.capitalize()
        self.sharps = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        self.flats = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
        # Determine whether to use sharps or flats for the chromatic scale
        use_sharps = ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'a', 'e', 'b', 'f#', 'c#', 'g#', 'd#']
        self.use_flats = tonic.lower() not in use_sharps

    def chromatic(self):
        if self.use_flats:
            scale = self.flats
        else:
            scale = self.sharps

        tonic_index = scale.index(self.tonic)
        return scale[tonic_index:] + scale[:tonic_index]

    def interval(self, intervals):
        scale = self.chromatic()
        scale_with_intervals = [self.tonic.capitalize()]

        index = scale.index(self.tonic.capitalize())
        for interval in intervals[:-1]:  # Exclude the last interval as it brings us back to the tonic
            if interval == 'm':
                index = (index + 1) % len(scale)  # Minor second (half step)
            elif interval == 'M':
                index = (index + 2) % len(scale)  # Major second (whole step)
            elif interval == 'A':
                index = (index + 3) % len(scale)  # Augmented second (three half steps)
            scale_with_intervals.append(scale[index])

        return scale_with_intervals
