class ReplayCache:
    def __init__(self):
        self._seen = set()

    def check_and_store(self, nonce: str) -> bool:
        """
        Returns True if nonce has not been seen before and stores it.
        Returns False if nonce has already been used (replay detected).
        """
        if nonce in self._seen:
            return False
        self._seen.add(nonce)
        return True