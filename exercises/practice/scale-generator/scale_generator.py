class Scale:
    def __init__(self, tonic):
        self.tonic = tonic

    def chromatic(self):
    def chromatic(self):
        chromatic_scale = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
        if self.tonic in chromatic_scale:
            tonic_index = chromatic_scale.index(self.tonic)
            return chromatic_scale[tonic_index:] + chromatic_scale[:tonic_index]
    def interval(self, intervals):
        chromatic_scale = self.chromatic()
        scale = [self.tonic]
        for interval in intervals:
            if interval == 'M':
                index = chromatic_scale.index(scale[-1]) + 2
            elif interval == 'm':
                index = chromatic_scale.index(scale[-1]) + 1
            else:
                raise ValueError("Invalid interval")
            scale.append(chromatic_scale[index % 12])
        return scale
