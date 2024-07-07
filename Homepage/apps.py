from django.apps import AppConfig

class HomepageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Homepage'

    def ready(self):
        import Homepage.startup  # Ensure 'Homepage' is the name of your app directory
