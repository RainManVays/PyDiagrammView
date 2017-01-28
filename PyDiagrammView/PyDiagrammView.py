import sublime, sublime_plugin

class PyDiagrammView(sublime_plugin.TextCommand):


    def run(self, edit):
    	pos = self.view.sel()[0].begin()
    	content = '<b>bold</b> text and <a href="link value">link</a>'
    	cont=self.view.substr(self.view.line(pos))
    	self.view.show_popup(cont, flags=sublime.HTML, location=-1, max_width=400, on_navigate=print)
   
   def view_Block_Scheme():
    	pass