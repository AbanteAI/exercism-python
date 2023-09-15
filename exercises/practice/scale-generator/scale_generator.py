class Scale:
    def __init__(self, tonic):
        self.tonic = tonic.upper()
    def _shift(self, scale, tonic):
        idx = scale.index(tonic)
        return scale[idx:] + scale[:idx]

    def _select_scale(self, tonic):
        sharp_scale = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
        flat_scale = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']
        if tonic in sharp_scale:
            return sharp_scale
        return flat_scale

    def chromatic(self):
        scale = self._select_scale(self.tonic)
        return self._shift(scale, self.tonic)

    def interval(self, intervals):
        chromatic_scale = self.chromatic()
        result = [chromatic_scale[0]]
        index = 0
        for interval in intervals:
            if interval == 'M':
                index += 2
            elif interval == 'm':
                index += 1
            elif interval == 'A':
                index += 3
            index %= len(chromatic_scale)
            result.append(chromatic_scale[index])
        return result
