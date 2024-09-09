from __future__ import print_function
import datetime
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar']

def authenticate_google_calendar():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('calendar', 'v3', credentials=creds)

def create_event(service, summary, description, location, start_time, end_time, reminders):
    event = {
        'summary': summary,
        'location': location,
        'description': description,
        'start': {
            'dateTime': start_time.isoformat(),
            'timeZone': 'America/Toronto',  # Use the correct time zone
        },
        'end': {
            'dateTime': end_time.isoformat(),
            'timeZone': 'America/Toronto',  # Use the correct time zone
        },
        'reminders': {
            'useDefault': False,
            'overrides': reminders,
        },
    }
    event = service.events().insert(calendarId='primary', body=event).execute()
    print(f'Event created: {event.get("htmlLink")}')

def main():
    service = authenticate_google_calendar()

    class_schedule = [
        {
            "summary": "MATH 1250 Lecture",
            "description": "Math 1250 Lecture",
            "location": "Chrysler Hall North G133",
            "day": "Thursday",
            "date": "2024-09-05",
            "time": "10:00",
            "duration_minutes": 90,
        },
        {
            "summary": "COMP 1000 Lecture",
            "description": "Intro to Computer Science",
            "location": "Toldo Health Education Ctr 102",
            "day": "Thursday",
            "date": "2024-09-05",
            "time": "14:30",
            "duration_minutes": 90,
        },
        {
            "summary": "COMP 1000 Laboratory",
            "description": "Computer Science Lab",
            "location": "Dillon Hall 359",
            "day": "Thursday",
            "date": "2024-09-05",
            "time": "19:00",
            "duration_minutes": 90,
        },
        {
            "summary": "MATH 1720 Laboratory",
            "description": "Math 1720 Laboratory",
            "location": "Toldo Health Education Ctr 100",
            "day": "Friday",
            "date": "2024-09-06",
            "time": "15:30",
            "duration_minutes": 90,
        },
        {
            "summary": "MATH 1250 Laboratory",
            "description": "Math 1250 Laboratory",
            "location": "Chrysler Hall North G133",
            "day": "Friday",
            "date": "2024-09-06",
            "time": "18:30",
            "duration_minutes": 90,
        },
        {
            "summary": "COMP 2650 Laboratory",
            "description": "Computer Architecture Laboratory",
            "location": "Dillon Hall 365",
            "day": "Monday",
            "date": "2024-09-09",
            "time": "11:30",
            "duration_minutes": 90,
        },
        {
            "summary": "MATH 1720 Lecture",
            "description": "Math 1720 Lecture",
            "location": "Toldo Health Education Ctr 100",
            "day": "Monday",
            "date": "2024-09-09",
            "time": "14:30",
            "duration_minutes": 90,
        },
        {
            "summary": "COMP 2650 Lecture",
            "description": "Computer Architecture Lecture",
            "location": "Odette Building 104",
            "day": "Monday",
            "date": "2024-09-09",
            "time": "16:00",
            "duration_minutes": 90,
        },
        {
            "summary": "MATH 1250 Lecture",
            "description": "Math 1250 Lecture",
            "location": "Chrysler Hall North G133",
            "day": "Tuesday",
            "date": "2024-09-10",
            "time": "10:00",
            "duration_minutes": 90,
        },
        {
            "summary": "COMP 1000 Lecture",
            "description": "Intro to Computer Science",
            "location": "Toldo Health Education Ctr 102",
            "day": "Tuesday",
            "date": "2024-09-10",
            "time": "14:30",
            "duration_minutes": 90,
        },
        {
            "summary": "MATH 1720 Lecture",
            "description": "Math 1720 Lecture",
            "location": "Toldo Health Education Ctr 100",
            "day": "Wednesday",
            "date": "2024-09-11",
            "time": "14:30",
            "duration_minutes": 90,
        },
        {
            "summary": "COMP 2650 Lecture",
            "description": "Computer Architecture Lecture",
            "location": "Odette Building 104",
            "day": "Wednesday",
            "date": "2024-09-11",
            "time": "16:00",
            "duration_minutes": 90,
        },
        # Additional classes till December
        {
            "summary": "MATH 1250 Lecture",
            "description": "Math 1250 Lecture",
            "location": "Chrysler Hall North G133",
            "day": "Thursday",
            "date": "2024-12-05",
            "time": "10:00",
            "duration_minutes": 90,
        },
        {
            "summary": "COMP 1000 Lecture",
            "description": "Intro to Computer Science",
            "location": "Toldo Health Education Ctr 102",
            "day": "Thursday",
            "date": "2024-12-05",
            "time": "14:30",
            "duration_minutes": 90,
        },
        {
            "summary": "COMP 1000 Laboratory",
            "description": "Computer Science Lab",
            "location": "Dillon Hall 359",
            "day": "Thursday",
            "date": "2024-12-05",
            "time": "19:00",
            "duration_minutes": 90,
        },
        {
            "summary": "MATH 1720 Laboratory",
            "description": "Math 1720 Laboratory",
            "location": "Toldo Health Education Ctr 100",
            "day": "Friday",
            "date": "2024-12-06",
            "time": "15:30",
            "duration_minutes": 90,
        },
        {
            "summary": "MATH 1250 Laboratory",
            "description": "Math 1250 Laboratory",
            "location": "Chrysler Hall North G133",
            "day": "Friday",
            "date": "2024-12-06",
            "time": "18:30",
            "duration_minutes": 90,
        },
        {
            "summary": "COMP 2650 Laboratory",
            "description": "Computer Architecture Laboratory",
            "location": "Dillon Hall 365",
            "day": "Monday",
            "date": "2024-12-09",
            "time": "11:30",
            "duration_minutes": 90,
        },
        {
            "summary": "MATH 1720 Lecture",
            "description": "Math 1720 Lecture",
            "location": "Toldo Health Education Ctr 100",
            "day": "Monday",
            "date": "2024-12-09",
            "time": "14:30",
            "duration_minutes": 90,
        },
        {
            "summary": "COMP 2650 Lecture",
            "description": "Computer Architecture Lecture",
            "location": "Odette Building 104",
            "day": "Monday",
            "date": "2024-12-09",
            "time": "16:00",
            "duration_minutes": 90,
        },
        {
            "summary": "MATH 1250 Lecture",
            "description": "Math 1250 Lecture",
            "location": "Chrysler Hall North G133",
            "day": "Tuesday",
            "date": "2024-12-10",
            "time": "10:00",
            "duration_minutes": 90,
        },
        {
            "summary": "COMP 1000 Lecture",
            "description": "Intro to Computer Science",
            "location": "Toldo Health Education Ctr 102",
            "day": "Tuesday",
            "date": "2024-12-10",
            "time": "14:30",
            "duration_minutes": 90,
        },
        {
            "summary": "MATH 1720 Lecture",
            "description": "Math 1720 Lecture",
            "location": "Toldo Health Education Ctr 100",
            "day": "Wednesday",
            "date": "2024-12-11",
            "time": "14:30",
            "duration_minutes": 90,
        },
        {
            "summary": "COMP 2650 Lecture",
            "description": "Computer Architecture Lecture",
            "location": "Odette Building 104",
            "day": "Wednesday",
            "date": "2024-12-11",
            "time": "16:00",
            "duration_minutes": 90,
        }
    ]

    for class_info in class_schedule:
        start_time = datetime.datetime.strptime(class_info["date"] + " " + class_info["time"], "%Y-%m-%d %H:%M")
        end_time = start_time + datetime.timedelta(minutes=class_info["duration_minutes"])

        reminders = [
            {'method': 'popup', 'minutes': 24 * 60},  # 1 day before
            {'method': 'popup', 'minutes': 2 * 60},   # 2 hours before
            {'method': 'popup', 'minutes': 60},       # 1 hour before
        ]

        create_event(
            service,
            summary=class_info["summary"],
            description=class_info["description"],
            location=class_info["location"],
            start_time=start_time,
            end_time=end_time,
            reminders=reminders
        )

if __name__ == '__main__':
    main()
