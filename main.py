import math

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty

from constants import STEP, MATS




class RootWidget(Widget):

    class SourceController(BoxLayout):

        source_label = ObjectProperty()
        info = StringProperty()

        def print_button_text_source(self):
            self.source_label.text = "from " + self.info


    class TargetController(BoxLayout):

        target_label = ObjectProperty()
        info = StringProperty()

        def print_button_text_target(self):
            self.target_label.text = "Make " + self.info


    class ResultController(BoxLayout):

        result_label = ObjectProperty()
        info = StringProperty()

        def update_result_label(self, instance):

            def getDifference(_target, _source):
                _difference = _target - _source
                if _difference < 0:
                    raise ValueError(_difference)
                return _difference

            try:

                target_name = RootWidget.target_label.text.lstrip("make ")
                target_level = MATS[target_name]["level"]

                source_name = RootWidget.source_label.text.lstrip("from ")
                source_level = MATS[source_name]["level"]

                difference = getDifference(target_level, source_level)

                raw_result = math.pow(STEP, difference)
                result = str(math.ceil(raw_result))
                RootWidget.result_label.text = result + " " + source_name + " = 1 " + target_name

            except KeyError as e:
                RootWidget.result_label.text = str(e)
            except ValueError:
                RootWidget.result_label.text = "---"
            except Exception as e:
                RootWidget.result_label.text = str(e)


    pass


class xvmcApp(App):
    def build(self):
        return RootWidget()


xvmcApp().run()
