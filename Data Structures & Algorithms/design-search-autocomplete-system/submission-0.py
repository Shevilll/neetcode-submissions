class AutocompleteSystem:

    def __init__(self, sentences: list[str], times: list[int]):
        self.current_prefix = []
        # Frequency map for historical sentences
        self.sentence_counts = {}
        for s, t in zip(sentences, times):
            self.sentence_counts[s] = t

    def input(self, c: str) -> list[str]:
        if c == '#':
            # Sentence ends, store/update it in the system
            sentence = "".join(self.current_prefix)
            self.sentence_counts[sentence] = (
                self.sentence_counts.get(sentence, 0) + 1
            )
            # Reset the current prefix for the next sentence
            self.current_prefix = []
            return []

        # Append character to the current prefix
        self.current_prefix.append(c)
        prefix = "".join(self.current_prefix)

        # Find all matching sentences and their frequencies
        matches = []
        for s, count in self.sentence_counts.items():
            if s.startswith(prefix):
                matches.append((s, count))

        # Sort by hot degree (descending), then ASCII order (ascending)
        matches.sort(key=lambda x: (-x[1], x[0]))

        # Return top 3
        return [s for s, count in matches[:3]]