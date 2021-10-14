import math
#import logging

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty

from constants import MATS

#The value of the result display, when a valid result is not available
EMPTY_LINE = "----------------"

#The number of level N materials needed to make one material of level N+1
STEP = 4


class RootWidget(Widget):
    pass


class DummyDisplay(Label):
    pass


class TargetGrouping(BoxLayout):
    selected = StringProperty()
    pass


class SourceGrouping(BoxLayout):
    selected = StringProperty()
#    pass


class TargetButton(ToggleButton):
    pass


class SourceButton(ToggleButton):
    pass


class ResultController(Label):

    line = StringProperty(EMPTY_LINE)

    target_color = StringProperty()
    source_color = StringProperty()
    required_mats = NumericProperty()

    def findResult(self):

        self.required_mats = 0

        def getDifference(_target, _source):
            difference = _target - _source
            if difference < 0:
                raise ValueError(difference)
#                logging.debug(""Invalid value " + _difference +
#                              "; Proceeding anyway)
            return difference

        try:
            target_lvl = MATS[self.target_color]["level"]
            source_lvl = MATS[self.source_color]["level"]

            result = math.pow(STEP, getDifference(target_lvl, source_lvl))

            #round (mostly just truncates trailing zero)
            self.required_mats = math.ceil(result)

        except KeyError:
            pass
#        except KeyError as e:
            #logging.debug("Key Error on " + str(e))

        except ValueError:
            pass
#        except ValueError as e:
            #logging.debug("Value Error on " + str(e))
            #logging.debug("""(This is likely caused by trying to make a
            #              low-level part from high-level parts)""")

#        except Exception as e:
            #logging.debug("An unknown error occurred: \n")
            #logging.debug(e)


class xvmcApp(App):
    def build(self):
        root_widget = RootWidget()
        return root_widget


xvmcApp().run()
