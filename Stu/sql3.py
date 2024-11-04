import datetime
import json
import sqlite3
def get_age(birthday_str):
    try:
        born_year = int(birthday_str.split('-')[0])
        current_year = datetime.datetime.now().year
        return current_year - born_year
    except (ValueError, IndexError):
        return None
def get_overall_rating(cur, player_api_id):
    rows = cur.execute(
        "SELECT overall_rating FROM Player_Attributes WHERE player_api_id = ?;", (player_api_id,)).fetchall()
    ratings = [float(row[0]) for row in rows if row[0] is not None]
    if ratings:
        mean_rating = sum(ratings) / len(ratings)
    else:
        mean_rating = None
    return mean_rating

def get_players_info(cur, n_players=None, json_filepath='D:\\迅雷下载\\chapter4\\chapter4\\players_info.json'):
    sql = "SELECT * FROM Player"1
    if n_players:
        sql += " LIMIT ?"

    rows = cur.execute(sql, (n_players,) if n_players else ()).fetchall()
    player_list = []

    for row in rows:
        player = dict()
        player['name'] = row[2]
        birthday_str = row[4]
        player['age'] = get_age(birthday_str)
        player['weight'] = row[5]
        player['height'] = row[6]
        player_api_id = row[1]
        player['average rating'] = get_overall_rating(cur, player_api_id)
        player_list.append(player)

    try:
        with open(json_filepath, "w") as f:
            json.dump(player_list, f, ensure_ascii=False, indent=4)
        print("已经成功写入到文件中")
    except IOError as e:
        print(f"写入 JSON 文件时出错: {e}")


try:
    conn = sqlite3.connect(r"D:\\迅雷下载\\chapter4\\chapter4\\soccer.db")
    cursor = conn.cursor()

    print("开始获取球员信息")
    get_players_info(cursor, n_players=50)

except sqlite3.Error as e:
    print(f"数据库错误: {e}")
finally:
    if conn:
        conn.commit()
        cursor.close()
        conn.close()