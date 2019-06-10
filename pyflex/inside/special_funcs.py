from typing import Iterable


def button_hover_color(basic_color: Iterable[int]):
    # Don't carp at the opinion of the author!
    new_color = []
    for channel in basic_color:
        if channel < 128:
            new_color.append(channel + int(20 - channel / 8))
        else:
            new_color.append(channel - int(5 + (channel - 128) / 8))
    return tuple(new_color)
