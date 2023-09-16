def add_time(start, duration, day_of_week=None):
  DAYS_OF_WEEK = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
  
  #convert to 24 hour
  st_hr, st_min = start.split()[0].split(":")
  tod = start.split()[1] #grab AM or PM for time of day (tod)
  if (tod == "PM"):
    st_hr = int(st_hr) + 12
  else:
    st_hr = int(st_hr)
  st_min = int(st_min)

  dur_hr, dur_min = duration.split(":")
  dur_hr = int(dur_hr) 
  dur_min = int(dur_min)

  #calculate end time
  end_hr = st_hr + dur_hr
  end_min = st_min + dur_min
  end_day = 0

  #convert to actual hrs, minutes, day
  end_hr = end_hr + (end_min // 60)
  end_min = end_min % 60
  end_day = end_day + (end_hr // 24)
  end_hr = end_hr % 24
    
  #convert hr to 12 hr formating
  if end_hr > 12:
    end_hr = end_hr - 12
    end_tod = 'PM'
  elif end_hr == 12: 
    end_tod = 'PM'
  elif end_hr == 0:
    end_hr = 12
    end_tod = 'AM'
  else: 
    end_tod = 'AM'
  #format the new time
  new_time = "{}:{:02d} {}".format(end_hr, end_min, end_tod)
  
  #calculate the ending day of the week
  if day_of_week:
    new_time += ", " + DAYS_OF_WEEK[(DAYS_OF_WEEK.index(day_of_week.lower()) + end_day) % 7].title()

  # If end_day > 0, add the number of days
  if end_day > 0:
    if end_day == 1:
        new_time += " (next day)"
    else:
        new_time += " ({} days later)".format(end_day)

  return new_time