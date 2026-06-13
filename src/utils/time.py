def format_time(milliseconds):
    total_time_sec = int(milliseconds // 1000)

    seconds = total_time_sec % 60
    minutes = total_time_sec // 60
    hours = minutes // 60

    if hours > 0:
        return f"{hours}:{minutes:02d}:{seconds:02d}"
    else:
        return f"{minutes}:{seconds:02d}"