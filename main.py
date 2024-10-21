from scraper import scrape_schedule
from schedule_calculator import calculate_total_salary, count_workdays
from transportation import calculate_commuting_cost, print_commuting_info
from settings import Settings
import requests

def main():
    try:
        settings = Settings()

        session = requests.Session()

        login_data = {
            'error_flag': '1',
            'redirect_url': 'https://crmgw1.wao-corp.com/matching/tch/dashboard/',  
            'kojin_cd': settings.ID,          
            'password': settings.PASSWORD    
        }

        login_response = session.post(settings.LOGIN_URL, data=login_data)
        
        if login_response.status_code != 200 or 'ログインIDまたはパスワードが間違っています' in login_response.text :
            print("ログインに失敗しました。")
            return

        schedule = scrape_schedule(session, settings.SCRAPE_URL)
        
        if not schedule:
            print("スケジュールデータが空です。")
            return
        
        workdays_count = count_workdays(schedule)
        
        total_salary = calculate_total_salary(schedule, settings.HOURLY_RATE)

        total_commuting_cost = calculate_commuting_cost(workdays_count, settings.ROUND_TRIP_COST)
        print_commuting_info(workdays_count, settings.ROUND_TRIP_COST, total_commuting_cost)

        print(f"最終的な合計給料: {total_salary} 円")
    
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    main()
