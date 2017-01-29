import sublime
import sublime_plugin
import io


class PyDiagrammView(sublime_plugin.TextCommand):

    sv = None

    def run(self, edit):
        global sv
        sv = self.view
        position = sv.rowcol(sv.sel()[0].begin())
        file_name = sv.file_name()
        cont = str(self.get_edit_file_arr(file_name))

        #content = self.popup_style() + self.popup_div_open() + self.set_content_row_next(cont) + '</div>'
        sv.show_popup(str(cont), flags=sublime.HTML, location=-1,
                      max_height=self.get_content_lines_cnt(cont) * 40, max_width=260, on_navigate=print)

    def view_Block_Scheme(self, selected_test):
        pass

    def popup_style(self):
        return '<style>html { background-color: #272822; margin: 0px; }</style>'

    def popup_div_open(self):
        return '<div>'

    def popup_div_close(self):
        return '</div>'

    def set_content_row_next(self, content):
        return content.replace('\n', '')

    def get_content_lines_cnt(self, content):
        return len(content.split('\n'))

    def get_content_max_code_lenght(self, content):
        pass

    def get_edit_file_arr(self, file):
        return open(file, 'r').readlines()

    def get_current_method_code():
        pass
