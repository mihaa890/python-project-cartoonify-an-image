class SlidersTypes:
    def __init__(self):
        self.THRESHOLD_BLOCK_SIZE_SLIDER = 'THRESHOLD_BLOCK_SIZE_SLIDER'
        self.THRESHOLD_DISTANCE_SLIDER = 'THRESHOLD_DISTANCE_SLIDER'
        self.BILATERAL_FILTER_DISTANCE_SLIDER = 'BILATERAL_FILTER_DISTANCE_SLIDER'
        self.BILATERAL_FILTER_SIGMA_COLOR_SLIDER = 'BILATERAL_FILTER_SIGMA_COLOR_SLIDER'
        self.BILATERAL_FILTER_SIGMA_SPACE_SLIDER = 'BILATERAL_FILTER_SIGMA_SPACE_SLIDER'

class DropdownTypes:
    def __init__(self):
        self.ADAPTIVE_METHOD = 'ADAPTIVE_METHOD'
        self.THRESHOLD_TYPE = 'THRESHOLD_TYPE'


class ThresholdTypes:
    def __init__(self):
        self.THRESH_BINARY = 'THRESH_BINARY'
        self.THRESH_BINARY_INV = 'THRESH_BINARY_INV'


    def _all(cls):
        return [i for i in dir(cls) if not i.startswith('__') and not i.startswith('_')]

class ThresholdAdaptiveMethods:
    def __init__(self):
        self.ADAPTIVE_THRESH_MEAN_C = 'ADAPTIVE_THRESH_MEAN_C'
        self.ADAPTIVE_THRESH_GAUSSIAN_C = 'ADAPTIVE_THRESH_GAUSSIAN_C'

    def _all(cls):
        return [i for i in dir(cls) if not i.startswith('__') and not i.startswith('_')]

class Constants:
    def __init__(self):
        self.THRESHOLD_TYPES = ThresholdTypes()
        self.THRESHOLD_ADAPTIVE_METHODS = ThresholdAdaptiveMethods()
        self.DROPDOWN_TYPES = DropdownTypes()
        self.SLIDERS_TYPES = SlidersTypes()