from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'


    #FOR SIGNALS
    def ready(self):
    	import accounts.signals

    #after this change the installed apps in the settings.