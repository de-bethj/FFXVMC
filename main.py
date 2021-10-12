import math

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

from constants import STEP, MATS


class YourApp(App):
    def build(self):
        root_widget = GridLayout(cols=2)

        button_names = ('gold', 'purple', 'blue', 'green', 'white',
                        'black')

        target_buttons = BoxLayout(orientation='vertical')
        source_buttons = BoxLayout(orientation='vertical')
        output_label_target = Label(text="What color do you want to make?", size_hint_y=None)
        output_label_source = Label(text="What color are you starting with?", size_hint_y=None)
        for name in button_names:
            source_buttons.add_widget(Button(text=name))
            target_buttons.add_widget(Button(text=name))

        clear_button = Button(text='clear all', size_hint_y=None,
                              height=100)
        result_label = Label(text='', size_hint_y=None, height=100)

        def print_button_text_source(instance):
            output_label_source.text = "from " + instance.text
        for button in source_buttons.children[:]:
            button.bind(on_press=print_button_text_source)

        def print_button_text_target(instance):
            output_label_target.text = "make " + instance.text
        for button in target_buttons.children[:]:
            button.bind(on_press=print_button_text_target)

        def resize_label_text_source(label, new_height):
            label.font_size = 0.5 * label.height
        output_label_source.bind(height=resize_label_text_source)

        def reset_labels(instance):
            output_label_source.text = 'What color are you starting with?'
            output_label_target.text = 'What color do you want to make?'
            result_label.text = ''
        clear_button.bind(on_press=reset_labels)

        def update_result_label(instance):

            def getDifference(_target, _source):
                _difference = _target - _source
                if _difference < 0:
                    raise ValueError(_difference)
                return _difference

            try:
                source_name = output_label_source.text.lstrip("from ")
                source_level = MATS[source_name]["level"]

                target_name = output_label_target.text.lstrip("make ")
                target_level = MATS[target_name]["level"]

                difference = getDifference(target_level, source_level)

                raw_result = math.pow(STEP, difference)
                result = str(math.ceil(raw_result))
                result_label.text = result + " " + source_name + " = 1 " + target_name

            except KeyError:
                result_label.text = "---"
            except ValueError:
                result_label.text = "---"
            except Exception as e:
                result_label.text = str(e)

        for button in source_buttons.children[:]:
            button.bind(on_release=update_result_label)
        for button in target_buttons.children[:]:
            button.bind(on_release=update_result_label)

        root_widget.add_widget(output_label_target)
        root_widget.add_widget(output_label_source)
        root_widget.add_widget(target_buttons)
        root_widget.add_widget(source_buttons)
        root_widget.add_widget(clear_button)
        root_widget.add_widget(result_label)

        return root_widget


YourApp().run()
