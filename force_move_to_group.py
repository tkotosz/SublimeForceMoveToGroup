import sublime_plugin

class ForceMoveToGroupCommand(sublime_plugin.WindowCommand):
    def run(self, group):
        if group == self.window.active_group():
            return;

        if group > self.window.num_groups()-1:
            self.window.run_command('new_pane')
        else:
            if len(self.window.views_in_group(self.window.active_group())) == 1:
                self.window.run_command('close_pane')
            else:
                self.window.run_command('move_to_group', { 'group': group })
