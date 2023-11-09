class Scale:
    SHARP_KEYS = ['G', 'D', 'A', 'E', 'B', 'F#', 'C#', 'e', 'b', 'f#', 'c#', 'g#', 'd#']
    FLAT_KEYS = ['F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb', 'd', 'g', 'c', 'f', 'bb', 'eb']
    CHROMATIC_SCALE_SHARPS = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    CHROMATIC_SCALE_FLATS = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']

    def __init__(self, tonic):
        self.tonic = tonic.capitalize()
        self.scale_type = 'flats' if self.tonic in Scale.FLAT_KEYS else 'sharps'

    def chromatic(self):
        if self.scale_type == 'sharps':
            scale = Scale.CHROMATIC_SCALE_SHARPS
        else:
            scale = Scale.CHROMATIC_SCALE_FLATS

        tonic_index = scale.index(self.tonic)
        return scale[tonic_index:] + scale[:tonic_index]

    def interval(self, intervals):
        chromatic_scale = self.chromatic()
        scale_with_intervals = [self.tonic]
        index = chromatic_scale.index(self.tonic)

        for interval in intervals:
            if interval == 'M':
                index += 2
            elif interval == 'm':
                index += 1
            elif interval == 'A':
                index += 3
            else:
                raise ValueError("Invalid interval")

            index = index % len(chromatic_scale)
            note = chromatic_scale[index]

            # Convert between enharmonic equivalents if necessary
            if self.scale_type == 'flats' and '#' in note:
                note = {
                    'A#': 'Bb', 'C#': 'Db', 'D#': 'Eb', 'F#': 'Gb', 'G#': 'Ab'
                }.get(note, note)
            elif self.scale_type == 'sharps' and 'b' in note:
                note = {
                    'Bb': 'A#', 'Db': 'C#', 'Eb': 'D#', 'Gb': 'F#', 'Ab': 'G#'
                }.get(note, note)

            scale_with_intervals.append(note)

        return scale_with_intervals
