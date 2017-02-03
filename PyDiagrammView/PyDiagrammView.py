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

        cont = self.convert_arr_to_str(self.block_generator(content_array))
        if self.check_def_contains_line(curr_row):
            content = self.popup_style() + self.popup_div_open() + cont + self.popup_div_close()
            sv.show_popup(content, flags=sublime.HTML, location=-1,
                          max_height=self.get_content_lines_cnt(content_array) * 100, max_width=800, on_navigate=print)

    def view_Block_Scheme(self, selected_test):
        pass

    def popup_style(self):
        return '<style>html { background-color: #449; } .block1 {color:#000;    background-color: #fff;    padding: 15px;    padding-right: 50px;     border: solid 1px black;     float: left;   }</style>'

    def popup_div_open(self):
        return '<div class="block1">'

    def popup_div_close(self):
        return '</div>'
#<div style="margin-left:20px; width:20px;height:20px;padding:10px; background-color:#777;"></div>

    def create_block_comment(self, row):
        style = 'style="margin:5px; margin-left:300px; border-radius:5px;  width:20px;height:20px;padding:10px; background-color:#78FD5D;"'
        return '<div ' + style + '>' + row + '</div>'

    def create_block_header(self, row):
        style = 'style="float:left;margin:5px;margin-right:8%; position:fixed; margin-bottom:20px;width:2%; font-weight: bold; border-radius:10px;  height:20px;padding:10px; background-color:#C3E4F8;"'
        return '<div><div ' + style + '>' + row[row.find('def') + 3:str(row).find(':')] + '</div> <div style="margin-right:100px;float:left;"></div></div>'

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

    def get_spaces_count(self, row):
        cnt = 0
        for item in row:
            if ' ' in item:
                cnt += 1
            elif '\t' in item:
                cnt += 4
            else:
                break
        return cnt

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

    def block_generator(self, content):
        ret_cont = []
        temp_spaces_count = 0
        temp_index = 0
        for index, row in enumerate(content):
            if index == 0:
                ret_cont.append(self.create_block_header(row) + self.check_row_have_comment(row))
            else:
                break
                ret_cont.append(row)

        return ret_cont

    def check_row_have_comment(self, row):
        if '#' in row:
            return self.create_block_comment(row[str(row).find('#'):])
        return ''

    def convert_arr_to_str(self, array):
        str_row = ""
        for row in array:
            str_row += row
        return str_row
