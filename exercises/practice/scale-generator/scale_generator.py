class Scale:
    def __init__(self, tonic):
        self.tonic = tonic[0].upper() + tonic[1:].lower()
        self.use_flats = self._determine_accidental()

    def _determine_accidental(self):
        use_flats = "F Bb Eb Ab Db Gb d g c f bb eb".split()
        return self.tonic in use_flats or (self.tonic[0] == 'F' and len(self.tonic) == 1)

    def chromatic(self):
        sharps = "A A# B C C# D D# E F F# G G#".split()
        flats = "A Bb B C Db D Eb E F Gb G Ab".split()
        scale = flats if self.use_flats else sharps
        tonic_index = scale.index(self.tonic.capitalize())
        return scale[tonic_index:] + scale[:tonic_index]

    def interval(self, intervals):
        chromatic_scale = self.chromatic()
        scale_with_intervals = [self.tonic]
        index = 0
        for interval in intervals[:-1]:  # Exclude the last interval as it brings us back to the tonic
            if interval == 'm':
                step = 1
            elif interval == 'M':
                step = 2
            elif interval == 'A':
                step = 3
            index += step
            scale_with_intervals.append(chromatic_scale[index % len(chromatic_scale)])
        return scale_with_intervals
