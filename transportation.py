def calculate_commuting_cost(workdays, round_trip_cost):
    return workdays * round_trip_cost

def print_commuting_info(workdays, round_trip_cost, total_cost):
    print(f"出勤日数: {workdays}日")
    print(f"往復交通費: {round_trip_cost}円")
    print(f"合計交通費: {total_cost}円")
