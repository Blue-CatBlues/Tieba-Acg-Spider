import datetime
import sqlite3
import json

# 数据库文件路径
db_filepath = r'D:\\迅雷下载\\chapter4\\chapter4\\soccer.db'
json_filepath = r'D:\\迅雷下载\\chapter4\\chapter4\\player_list.json'  # 保存的球员JSON文件

def get_age(birthday_str):
    born_year = int(birthday_str.split('-')[0])
    current_year = datetime.datetime.now().year
    return current_year - born_year

# 获取球员平均评分
def get_overall_rating(cur, player_api_id):
    rows = cur.execute(
        "SELECT overall_rating FROM Player_Attributes WHERE player_api_id={}".format(player_api_id)
    ).fetchall()
    ratings = [float(row[0]) for row in rows if row[0] is not None]
    if ratings:
        mean_rating = sum(ratings) / len(ratings)
    else:
        mean_rating = None
    return mean_rating

def get_players_info(cur, n_players=None):
    if n_players:
        sql = "SELECT * FROM Player LIMIT {}".format(n_players)
    else:
        sql = "SELECT * FROM Player"
    rows = cur.execute(sql).fetchall()
    player_list = []
    for row in rows:
        player = dict()
        player['name'] = row[2]
        birthday_str = row[4]
        player['age'] = get_age(birthday_str)
        player['weight'] = row[5]
        player['height'] = row[6]
        player_api_id = row[1]
        player['average_rating'] = get_overall_rating(cur, player_api_id)
        player_list.append(player)
    with open(json_filepath, 'w') as f:
        json.dump(player_list, f)

def main():
    conn = sqlite3.connect(db_filepath)
    cursor = conn.cursor()
    get_players_info(cursor, n_players=50)
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()
