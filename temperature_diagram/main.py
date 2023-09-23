from data_provider import DataProvider
from draw_engine import DrawEngine
from screen_config import ScreenConfig
from styles import Styles

data_provider = DataProvider(file_name='data.csv')
styles = Styles()
screen_config = ScreenConfig()

draw_engine = DrawEngine(
    screen_config=screen_config,
    styles=styles,
    data=data_provider
)

draw_engine.run()
