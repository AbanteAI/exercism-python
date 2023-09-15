from typing import List

class Scale:
    def __init__(self, tonic: str):
        self.tonic = tonic

    def chromatic(self) -> List[str]:
        chromatic_scale = []
        notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
        tonic_index = notes.index(self.tonic.upper())
        for i in range(12):
            chromatic_scale.append(notes[(tonic_index + i) % 12])
        return chromatic_scale

    def interval(self, intervals: List[str]) -> List[str]:
        scale = [self.tonic.upper()]
        notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
        tonic_index = notes.index(self.tonic.upper())
        for interval in
    def chromatic(self):
        chromatic_scale = []
        notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
        tonic_index = notes.index(self.tonic.upper())
        for i in range(12):
            chromatic_scale.append(notes[(tonic_index + i) % 12])
        return chromatic_scale

    def interval(self, intervals):
        scale = [self.tonic.upper()]
        notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
        tonic_index = notes.index(self.tonic.upper())
        for interval in intervals:
            if interval == 'm':
                tonic_index += 1
            elif interval == 'M':
                tonic_index += 2
            elif interval == 'A':
                tonic_index += 3
            scale.append(notes[tonic_index % 12])
        return scale
