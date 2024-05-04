from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
import pandas as pd
import os



class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.users = [
            {'username': 'hello', 'password': 'hello'},
            {'username': 'user2', 'password': 'pass2'},
            # Add more users as needed
        ]

        self.username_input = TextInput(hint_text='Username', multiline=False)
        self.password_input = TextInput(hint_text='Password', multiline=False, password=True)
        self.login_button = Button(text='Login', on_release=self.check_login)

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Login Page'))
        layout.add_widget(self.username_input)
        layout.add_widget(self.password_input)
        layout.add_widget(self.login_button)

        self.add_widget(layout)

    def check_login(self, _):
        username = self.username_input.text
        password = self.password_input.text

        for user in self.users:
            if user['username'] == username and user['password'] == password:
                self.manager.current = 'file_upload'
                return

        self.username_input.text = ""
        self.password_input.text = ""
        self.username_input.hint_text = "Invalid username or password"
        self.password_input.hint_text = "Invalid username or password"


class FileUploadScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.file_1_label = Label(text='Choose Excel File 1:')
        self.file_2_label = Label(text='Choose Excel File 2:')
        self.file_1_chooser = FileChooserListView()
        self.file_2_chooser = FileChooserListView()
        self.process_button = Button(text='Process Files', on_release=self.process_files)

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.file_1_label)
        layout.add_widget(self.file_1_chooser)
        layout.add_widget(self.file_2_label)
        layout.add_widget(self.file_2_chooser)
        layout.add_widget(self.process_button)

        self.add_widget(layout)

    def process_files(self, _):
        file_1_path = self.file_1_chooser.selection[0]
        file_2_path = self.file_2_chooser.selection[0]

        # Simple Excel processing (Merging files for demonstration purposes)
        df1 = pd.read_excel(file_1_path)
        df2 = pd.read_excel(file_2_path)
        merged_df = pd.concat([df1, df2], axis=0)

        # Create the output DataFrame and convert it to bytes
        output_df = pd.DataFrame(merged_df)
        output_bytes = output_df.to_excel(index=False)

        self.download_data(output_bytes)


class ProcessedDataScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.processed_data_label = Label(text='Processed Data:')
        self.download_button = Button(text='Download', on_release=self.download_data)

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.processed_data_label)
        layout.add_widget(self.download_button)

        self.add_widget(layout)

    def download_data(self, output_bytes):
        # Define the path and name for the output file
        output_filename = "output.xlsx"

        # Send the output file as a response to download
        self.send_download_response(output_bytes, output_filename)

    def send_download_response(self, output_bytes, filename):
        try:
            # Create the headers to prompt the browser to download the file
            headers = {
                'Content-Disposition': f'attachment; filename={filename}',
                'Content-Type': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            }

            # Use the UrlRequest to send the response directly to the browser
            UrlRequest(
                url='',
                req_body=output_bytes,
                req_headers=headers,
                method='POST',
                on_error=self.on_error,
                on_failure=self.on_failure
            )
        except Exception as e:
            print(f"Error sending download response: {e}")

    def on_error(self, req, result):
        print(f"Request error: {result}")

    def on_failure(self, req, result):
        print(f"Request failed: {result}")


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(FileUploadScreen(name='file_upload'))
        sm.add_widget(ProcessedDataScreen(name='processed_data'))
        return sm


if __name__ == '__main__':
    MyApp().run()
