class WrittenText:
    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text


class UnderlineWrapper(WrittenText):
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return f"<u>{self._wrapped.render()}</u>"


class ItalicWrapper(WrittenText):
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return f"<i>{self._wrapped.render()}</i>"


class BoldWrapper(WrittenText):
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return f"<b>{self._wrapped.render()}</b>"


if __name__ == "__main__":
    before = WrittenText("Decorator")
    after = ItalicWrapper(UnderlineWrapper(BoldWrapper(before)))

    print("before :", before.render())
    print("after :", after.render())
