from django.apps import AppConfig
# from .settings import CUSER_SETTINGS
    # verbose_name = CUSER_SETTINGS['app_verbose_name']


class ShoppingConfig(AppConfig):
    name = 'shopping'

    def ready(self):
        import shopping.signals

