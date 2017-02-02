import sublime
import sublime_plugin
import io


class PyDiagrammView(sublime_plugin.TextCommand):

    sv = None
    end_words = ('if', 'else', 'elif', 'for', 'def', 'return')

    def run(self, edit):
        global sv
        sv = self.view
        position = sv.rowcol(sv.sel()[0].begin())
        curr_line_pos = self.view.sel()[0].begin()
        curr_row = self.view.substr(self.view.line(curr_line_pos))
        file_name = sv.file_name()

        content_array = self.get_current_method_code(self.get_edit_file_arr(file_name), position[0])
        cont = self.convert_arr_to_str(content_array)
        if self.check_def_contains_line(curr_row):
            content = self.popup_style() + self.popup_div_open() + cont + self.popup_div_close()
            sv.show_popup(content, flags=sublime.HTML, location=-1,
                          max_height=self.get_content_lines_cnt(cont) * 40, max_width=400, on_navigate=print)

    def view_Block_Scheme(self, selected_test):
        pass

    def popup_style(self):
        return '<style>html { background-color: #449; margin: 0px; } .block1 { width: 200px; color:#000;    background-color: #fff;    padding: 15px;    padding-right: 50px;     border: solid 1px black;     float: left;   }</style>'

    def popup_div_open(self):
        return '<div class="block1">'

    def popup_div_close(self):
        return '</div>'

    def check_def_contains_line(self, row):
        return 'def' in str(row)

    def set_content_row_next(self, content):
        return content.replace('\n', '')

    def get_content_lines_cnt(self, content):
        return len(content)

    def get_content_max_code_lenght(self, content):
        pass

    def get_edit_file_arr(self, file):
        return open(file, 'r').readlines()

    def get_current_method_code(self, file_content, selected_row):
        ret_file_content = []
        first_row = ''
        for index, text in enumerate(file_content):
            if index == selected_row:
                first_row = text
            if index >= selected_row:
                if first_row != text and 'def ' in text:
                    break
                else:
                    ret_file_content.append(text)

        return ret_file_content

    def if_to_block(self, file_content):
        pass

    def convert_arr_to_str(self, array):
        str_row = ""
        for row in array:
            str_row += row
        return str_row
