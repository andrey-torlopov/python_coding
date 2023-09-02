class ScreenConfig:
    def __init__(self, width: int = 640, height: int = 800,
                 title: str = "Snake game", fps: int = 60,
                 side: int = 40) -> None:
        self.width = width
        self.height = height
        self.title = title
        self.fps = fps
        self.black = (43, 43, 43)
        self.side = side
        self.foreground = (240, 240, 240)
        self.top_offset = 60

    @property
    def screen_size(self) -> tuple[int, int]:
        return (self.width, self.height)

    @property
    def points_per_row(self) -> int:
        return (self.height - self.top_offset) // self.side

    @property
    def points_per_col(self) -> int:
        return self.width // self.side
