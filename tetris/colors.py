class Colors:
    # Background
    dark_purple = (15, 0, 45)           # Very dark violet/indigo

    # Tetrominoes (bright, bold colors)
    Cyan   = (0, 255, 255)              # Bright cyan
    Pink   = (255, 0, 144)              # Hot pink
    Green  = (0, 255, 0)                # Neon green
    Yellow = (255, 255, 0)              # Bright yellow
    Orange = (255, 127, 0)              # Vivid orange
    Blue   = (0, 0, 255)                # Pure blue
    Red    = (255, 0, 0)                # Bright red

    # UI / Cards / Text
    white         = (255, 255, 255)     # Pure white
    light_purple  = (170, 0, 255)       # Electric purple (for Score card)
    light_blue    = (0, 255, 255)       # Bright cyan (for Next card)

    @classmethod
    def get_cell_colors(cls):
        return [cls.dark_purple, cls.Cyan, cls.Pink, cls.Green, cls.Yellow, cls.Orange, cls.Blue, cls.Red]
