from django.apps import AppConfig


class CarsRepairsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cars_repairs_app'
    
    def ready(self):
        # Importa los signals aquí para que se carguen cuando la aplicación esté lista.
        import cars_repairs_app.signals 
