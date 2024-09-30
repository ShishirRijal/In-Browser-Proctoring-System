from django.apps import AppConfig


class ProctoringsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'proctorings'

    def ready(self):
        from .google_sheets import get_sheet_data
        from .views import save_sheet_data_to_model

        data = get_sheet_data()
        #print(data)  # This should print the data fetched from Google Sheets
        save_sheet_data_to_model(data)

