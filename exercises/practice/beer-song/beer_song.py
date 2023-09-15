def recite(start, take=1):
    def verse(n):
        if n == 0:
            return (
                "No more bottles of beer on the wall, no more bottles of beer.\n"
                "Go to the store and buy some more, 99 bottles of beer on the wall.\n"
            )
        if n == 1:
            return (
                "1 bottle of beer on the wall, 1 bottle of beer.\n"
                "Take it down and pass it around, no more bottles of beer on the wall.\n"
            )
        return (
            f"{n} bottles of beer on the wall, {n} bottles of beer.\n"
            f"Take one down and pass it around, {n - 1} {'bottle' if n == 2 else 'bottles'} of beer on the wall.\n"
        )

    return [verse(n).rstrip() for n in range(start, start - take, -1)]