from datetime import datetime
from google_calendar import GoogleCalendarManager

# Ahora `fecha_completa` es un objeto datetime con la fecha y la hora combinada
fecha_str = 'Vie 04/04/25'


calendar = GoogleCalendarManager()

calendar.create_event('Fisica cuantica','2025-03-04T17:00:00','2025-03-04T18:00:00')
