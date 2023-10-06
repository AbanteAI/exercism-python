class Scale:
    def __init__(self, tonic):
        self.tonic = tonic.upper()

    def chromatic(self):
        chromatic_scale = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']

    def interval(self, intervals):
        diatonic_scale = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
        start_index = diatonic_scale.index(self.tonic.upper())
        scale = [diatonic_scale[start_index]]
            if interval == 'M':
                start_index += 2
            elif interval == 'm':
                start_index += 1
            elif interval == 'A':
                start_index += 3
            scale.append(diatonic_scale[start_index % 7])
        return scale