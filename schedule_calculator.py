from datetime import datetime

def calculate_duration(start, end):
    try:
        start_time = datetime.strptime(start, '%H:%M')
        end_time = datetime.strptime(end, '%H:%M')
        duration = end_time - start_time
        return duration.total_seconds() / 60  
    except ValueError as e:
        print(f"時間のフォーマットに問題があります: {e}")
        return 0

def count_workdays(schedule):
    workdays = set()
    
    for entry in schedule:
        workdays.add(entry['date'])
    
    return len(workdays)

def calculate_total_salary(schedule, hourly_rate):
    """授業時間に基づいて合計給料を計算"""
    total_classes = 0
    full_class_duration = 80  

    for item in schedule:
        start = item['time']['start']
        end = item['time']['end']
        duration_minutes = calculate_duration(start, end)
        num_classes = duration_minutes / full_class_duration
        total_classes += num_classes
    
    total_salary = int(total_classes * hourly_rate)
    return total_salary

