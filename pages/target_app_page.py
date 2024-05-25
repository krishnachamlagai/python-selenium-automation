from pages.base_page import Page


class TargetAppPage(Page):
    def verify_tac_page_opened(self):
        self.verify_partial_url('terms-conditions/')

