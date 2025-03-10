import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar"]  

class GoogleCalendarManager:
  def __init__(self):
    self.service = self.authenticate()
    self.calendar_list = self.list_of_calendars()
    if 'FPUNA' not in self.calendar_list:
      FPUNA_calendar=self.create_calendar('FPUNA')
      FPUNA_CalendarId = FPUNA_calendar['id']
      print(f'Se ha creado el calendario "{FPUNA_calendar['summary']}" con id "{FPUNA_calendar['id']}"\n')
    else:
      FPUNA_calendar = self.service.calendarList().list(pageToken=None).execute()['items']
      for item in FPUNA_calendar:
        if item['summary']=='FPUNA':
          FPUNA_CalendarId = item['id']
    self.FPUNA_calendarId=FPUNA_CalendarId
    
  def create_calendar(self,summary):
    calendar = {
      'summary': summary,
      'timeZone': 'America/Asuncion',
      'backgroundColor': '6',  
        'foregroundColor': '#ffffff'
      
    }
    created_calendar = self.service.calendars().insert(body=calendar).execute()
    return created_calendar
  
  #retorna una lista con el nombre de cada calendario (propiedad summary)
  def list_of_calendars(self):
    page_token = None
    calendar_list = self.service.calendarList().list(pageToken=page_token).execute()['items']
    calendar_list = [calendar_list[i]['summary'] for i in range(len(calendar_list))]
    return calendar_list
  
  #retorna None si no encuentra un evento con ese nombre y el id se encuenta alguno  
  def get_eventId_from_eventSummary(self,summary):
    events = self.service.events().list(calendarId=self.FPUNA_calendarId, pageToken=None).execute()['items']
    for event in events:
      if event['summary'] == summary:
        Id = event['id']
        return Id
    return None
  
  def authenticate(self):
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
      creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
      if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
      else:
        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json", SCOPES
        )
        creds = flow.run_local_server(port=0)
      # Save the credentials for the next run
      with open("token.json", "w") as token:
        token.write(creds.to_json())

    try:
      service = build("calendar", "v3", credentials=creds) 
      return service
    except HttpError as error:
      print(f"An error occurred: {error}") 
  
  def upcoming_10_events(self):
    now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
    print("Getting the upcoming 10 events")
    events_result = (self.service.events().list(
            calendarId=self.FPUNA_calendarId,
            timeMin=now,
            maxResults=10,
            singleEvents=True,
            orderBy="startTime",
        ).execute())

    events = events_result.get("items", [])

    events_result = self.service.events().list(
            calendarId='FPUNA', 
            timeMin=now, 
            maxResults=10, singleEvents=True,
            orderBy='startTime'
        ).execute()
    events = events_result.get('items', [])

    if not events:
      print("No upcoming events found.")
      return

    # Prints the start and name of the next 10 events
    for event in events:
      start = event["start"].get("dateTime", event["start"].get("date"))
      print(start, event["summary"])
      
  def create_event(self,materia,startDateTime,endDateTime,FREQ=None,UNTIL=None,aula=None,attendees=None):
    event = {
      'summary':materia,
      'description':aula,
      'start':{
        'dateTime': startDateTime+'-03:00',
        "timeZone": "America/Asuncion"
      },
      'end':{
        'dateTime': endDateTime+'-03:00',
        "timeZone": "America/Asuncion"
      },
      'attendees':attendees
    }
    
    if FREQ and UNTIL:
      event['recurrence'] = {
          f'RRULE:FREQ={FREQ};UNTIL={UNTIL}'
        }
    
    try:
      event = self.service.events().insert(calendarId=self.FPUNA_calendarId,body=event).execute()
      print(f'Se añadió al calendario un evento:\nSummary: {event['summary']}\nLink: {event.get('htmlLink')}')
    except HttpError as error:
      print(f'Ocurrió un error: {error}')

  def delete_event(self,summary):
    Id = self.get_eventId_from_eventSummary(summary)
    
    if Id:
      self.service.events().delete(calendarId=self.FPUNA_calendarId,eventId=Id).execute()
      print(f'Se elimino el evento {summary}')
    else:
      print(f'No existe el evento {summary}')
  
  def update_event(self,summary,new_start_time,new_end_time,new_summary=None,new_FREQ=None,new_aula=None):
    event_Id = self.get_eventId_from_eventSummary(summary)
    if event_Id:
      event = self.service.events().get(calendarId=self.FPUNA_calendarId,eventId=event_Id).execute()
      
      if new_summary:
        event['summary'] = new_summary
      if new_aula:
        event['description'] = new_aula
      if new_start_time:
        event['start']['dateTime'] = new_start_time
      if new_end_time:
        event['end']['dateTime'] = new_end_time
      if new_FREQ:
        event['recurrence'] = {
          f'RRULE:FREQ={new_FREQ}'
        }
      
      updated_event = self.service.events().update(calendarId=self.FPUNA_calendarId,eventId=event_Id,body=event).execute()
      print('Se actualizo el evento')
      return updated_event
    print('El evento no existe')
    return None
      
  
