class Scale:
    SHARP_KEYS = ['G', 'D', 'A', 'E', 'B', 'F#', 'e', 'b', 'f#', 'c#', 'g#', 'd#']
    FLAT_KEYS = ['F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb', 'd', 'g', 'c', 'f', 'bb', 'eb']
    CHROMATIC_SCALE_SHARP = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    CHROMATIC_SCALE_FLAT = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']

    def __init__(self, tonic):
        self.tonic = tonic.capitalize()
        self.use_flats = self.tonic in Scale.FLAT_KEYS

    def chromatic(self):
        scale = Scale.CHROMATIC_SCALE_FLAT if self.use_flats else Scale.CHROMATIC_SCALE_SHARP
        tonic_index = scale.index(self.tonic)
        return scale[tonic_index:] + scale[:tonic_index]

    def interval(self, intervals):
        scale = self.chromatic()
        scale_with_intervals = [self.tonic]
        index = 0
        for interval in intervals[:-1]:  # Exclude the last interval as it brings us back to the tonic
            if interval == 'M':
                index += 2
            elif interval == 'm':
                index += 1
            elif interval == 'A':
                index += 3
            next_note = scale[(scale.index(scale_with_intervals[-1]) + index) % len(scale)]
            # Ensure that we use the correct enharmonic equivalent
            if next_note.endswith('#') and self.use_flats:
                next_note = {
                    'A#': 'Bb', 'C#': 'Db', 'D#': 'Eb',
                    'F#': 'Gb', 'G#': 'Ab'
                }[next_note]
            scale_with_intervals.append(next_note)
        scale_with_intervals.append(self.tonic)  # Add the tonic at the end to complete the scale
        return scale_with_intervals
