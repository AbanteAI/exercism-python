class Scale:
    def __init__(self, tonic):
        pass

    CHROMATIC_SCALE = {
        'C': ['C', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'],
        'F': ['F', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E'],
        'G': ['G', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#'],
        'D': ['D', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#'],
        'A': ['A', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#'],
        'E': ['E', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#'],
        'B': ['B', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#'],
        'C#': ['C#', 'D#', 'E', 'F', 'F#', 'G#', 'A', 'A#', 'B', 'C', 'C#'],
        'F#': ['F#', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F'],
        'D#': ['D#', 'E#', 'F#', 'G', 'G#', 'A#', 'B', 'C#', 'D', 'D#', 'E'],
        'G#': ['G#', 'A#', 'B', 'C', 'C#', 'D#', 'E', 'F#', 'G', 'G#', 'A'],
        'A#': ['A#', 'B#', 'C#', 'D', 'D#', 'E#', 'F#', 'G#', 'A', 'A#', 'B'],
    }

    def chromatic(self):
        tonic = self.tonic.upper()
        scale = self.CHROMATIC_SCALE[tonic]
        return scale

    INTERVALS = {
        'm': 1,
        'M': 2,
        'A': 3
    }

    def interval(self, intervals):
        tonic = self.tonic.upper()
        scale = [tonic]
        current_note = tonic
        for interval in intervals:
            step = self.INTERVALS[interval]
            next_note = self.CHROMATIC_SCALE[tonic][(self.CHROMATIC_SCALE[tonic].index(current_note) + step) % 12]
            scale.append(next_note)
            current_note = next_note
        return scale
