from pages.base_page import Page


class TargetAppPage(Page):
    def verify_tac_page_opened(self):
        self.verify_partial_text('terms-conditions/')

    def switch_window_by_id(self, window_id):
        pass
