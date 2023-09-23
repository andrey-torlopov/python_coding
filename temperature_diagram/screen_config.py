class ScreenConfig:
    def __init__(self, width: int = 640, height: int = 800,
                 title: str = "Temperature", fps: int = 60) -> None:
        self.width = width
        self.height = height
        self.title = title
        self.fps = fps
        self.top_offset = 60

    @property
    def screen_size(self) -> tuple[int, int]:
        return (self.width, self.height)

    @property
    def center(self) -> tuple[int, int]:
        return (self.width // 2, self.height // 2)
