import datetime
from pytz import FixedOffset, utc
from datetime import timedelta

def unix_utc_to_local_dict(utc_timestamp, timezone_offset):

    # Create a FixedOffset object from the offset
    offset = timedelta(seconds=timezone_offset)
    total_minutes = offset.total_seconds() / 60
    request_tz = FixedOffset(total_minutes)

    # Convert UTC timestamp to datetime and then to local time
    utc_dt = datetime.datetime.fromtimestamp(utc_timestamp, utc)
    local_dt = utc_dt.astimezone(request_tz)

    # Format the date and time strings
    day_name = local_dt.strftime("%A")
    date_num = local_dt.strftime("%d")
    month_name = local_dt.strftime("%B")
    year = local_dt.strftime("%Y")
    hour = local_dt.strftime("%H") 

    date_str = f"{day_name}, {date_num} {month_name} {year}"
    

    # Add AM/PM indicator
    meridian = local_dt.strftime("%p").upper()

    time_str = f"{hour}:{local_dt.strftime('%M')} {meridian}"  # Include AM/PM

    short_date_str = local_dt.strftime("%d/%m/%Y")


    return {
        "date": date_str,
        "time": time_str,
        "short_date": short_date_str,
        "original_unix_timestamp": utc_timestamp,
        "original_timezone_offset": timezone_offset
    }

def kelvin_to_celsius(kelvin):

    celsius = kelvin - 273.15 
    return int(round(celsius))

def meters_per_second_to_kilometers_per_hour(meters_per_second):

    kilometers = meters_per_second / 1000
    hours = 1 / 3600

    kilometers_per_hour = kilometers / hours

    return round(kilometers_per_hour)

def build_weather_icon_url(icon_id):

    base_url = "http://openweathermap.org/img/wn/"
    icon_extension = ".png"
    return f"{base_url}{icon_id}{icon_extension}"