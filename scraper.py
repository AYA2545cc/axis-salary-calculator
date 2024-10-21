import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException

def parse_year_month(soup):
    current_year_month = soup.find('select', {'name': 'year_month'}).find('option', selected=True)
    return current_year_month['value']

def parse_date_terms(soup):
    return soup.find('select', {'name': 'date_term'}).find_all('option')

def fetch_schedule(scrape_url, session, year_month_value, date_term_value):
    params = {
        'year_month': year_month_value,
        'date_term': date_term_value
    }
    
    data_response = session.get(scrape_url, params=params)
    
    if data_response.status_code != 200:
        print(f"取得に失敗しました: {data_response.status_code}")
        return []

    soup = BeautifulSoup(data_response.text, 'html.parser')
    return parse_schedule(soup)

def parse_schedule(soup):
    schedule = []
    date_elements = soup.find_all('h3', class_='box-title')

    for date_element in date_elements:
        date_text = date_element.get_text(strip=True)
        if "授業予定一覧" in date_text:
            continue

        table = date_element.find_parent('div').find_next('div', class_='box-body').find('table')
        
        if table:
            time_elements = table.find_all('td', class_='text-center')
            for time_element in time_elements:
                time_range = [time.strip() for time in time_element.get_text(strip=True).split('-')]
                schedule.append({
                    "date": date_text,
                    "time": {
                        "start": time_range[0],
                        "end": time_range[1],
                    }
                })
    return schedule

def scrape_schedule(session, scrape_url):
    try:
        response = session.get(scrape_url)
        response.raise_for_status()  
    except RequestException as e:
        print(f"スクレイピング中にエラーが発生しました: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    year_month_value = parse_year_month(soup)
    date_term_options = parse_date_terms(soup)
    
    all_schedules = []

    for date_term in date_term_options:
        date_term_value = date_term['value']
        schedules = fetch_schedule(scrape_url, session, year_month_value, date_term_value)
        all_schedules.extend(schedules)

    return all_schedules
