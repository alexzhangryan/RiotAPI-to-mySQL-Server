import requests
import sys
import pandas as pd
import mysql.connector
import sqlalchemy
from sqlalchemy import create_engine
from api import *
class TransferMatchData:
    def readMatches(self):
        con_string = "mysql+mysqlconnector://root:test_password@localhost/lol_data"
        engine = create_engine(con_string)
        query = "SELECT * FROM matches"
        df_read_sql = pd.read_sql(query, engine)
        print(df_read_sql)
    def readMatch_Players(self):
        con_string = "mysql+mysqlconnector://root:test_password@localhost/lol_data"
        engine = create_engine(con_string)
        query = "SELECT * FROM match_players"
        df_read_sql = pd.read_sql(query, engine)
        print(df_read_sql)
    def clearTables(self):
        try:
            connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="test_password",
            database="lol_data",
            )
            cursor = connection.cursor()

            cursor.execute("DELETE FROM match_players;")
            cursor.execute("DELETE FROM matches;")
            connection.commit()
            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            sys.exit(1)
    def insertMatch(self, match):
        match_id = match['metadata']['matchId']
        version = match['info']['gameVersion']
        game_mode = match['info']['gameMode']
        game_duration = match['info']['gameDuration']
        try:
            connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="test_password",
            database="lol_data",
            )
            cursor = connection.cursor()

            query = "INSERT INTO matches(match_id, game_duration, patch_version, game_mode) VALUES (%s,%s,%s,%s) ON DUPLICATE KEY UPDATE game_duration = %s, patch_version = %s, game_mode = %s"

            cursor.execute(query, (match_id, game_duration, version, game_mode, game_duration, version, game_mode))
            print(f"Number of participants: {len(match['info']['participants'])}")
            
            for participant in match['info']['participants']:
                match_id_puuid = f"{match_id}_{participant['puuid']}"
                puuid = participant['puuid']
                riot_id = participant['riotIdGameName']
                riot_id_tag_line = participant['riotIdTagline']
                champion_name = participant['championName']
                role = participant['role']
                item0 = participant['item0']
                item1 = participant['item1']
                item2 = participant['item2']
                item3 = participant['item3']
                item4 = participant['item4']
                item5 = participant['item5']
                item6 = participant['item6']
                baron_kills = participant['challenges']['teamBaronKills'] #gotta actually find out if this is the correct data
                dragon_kills = participant['dragonKills']
                elder_dragon_kills = participant['challenges']['teamElderDragonKills']
                rift_herald_kills = participant['challenges']['teamRiftHeraldKills']
                void_grub_kills = participant['challenges']['voidMonsterKill']
                turrets_kills = participant['turretKills']
                champion_level = participant['champLevel']
                gold_earned = participant['goldEarned']
                kills = participant['kills']
                deaths = participant['deaths']
                assists = participant['assists']
                vision_score = participant['visionScore']
                total_damage_dealt = participant['totalDamageDealt']
                total_damage_taken = participant['totalDamageTaken']
                total_heal = participant['totalHeal']
                total_minions_killed = participant['totalMinionsKilled']
                total_time_crowd_control_dealt = participant['totalTimeCCDealt']
                total_units_healed = participant['totalUnitsHealed']
                total_damage_to_champions = participant['totalDamageDealtToChampions']
                win = participant['win']

                query = """
                INSERT INTO match_players(
                match_id_puuid, match_id, puuid, riot_id, riot_id_tag_line,
                champion_name, role, item0, item1, item2, item3, item4, item5, item6,
                baron_kills, dragon_kills, elder_dragon_kills, rift_herald_kills, void_grub_kills, turrets_kills,
                champ_level, gold_earned, kills, deaths, assists, vision_score, total_damage_dealt,
                total_damage_taken, total_heal, total_minions_killed, total_time_crowd_control_dealt,
                total_units_healed, total_damage_to_champions, win
                ) VALUES (%s,
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s
                )
                ON DUPLICATE KEY UPDATE
                match_id = %s,
                puuid = %s,
                riot_id = %s,
                riot_id_tag_line = %s,
                champion_name = %s,
                role = %s,
                item0 = %s,
                item1 = %s,
                item2 = %s,
                item3 = %s,
                item4 = %s,
                item5 = %s,
                item6 = %s,
                baron_kills = %s,
                dragon_kills = %s,
                elder_dragon_kills = %s,
                rift_herald_kills = %s,
                void_grub_kills = %s,
                turrets_kills = %s,
                champ_level = %s,
                gold_earned = %s,
                kills = %s,
                deaths = %s,
                assists = %s,
                vision_score = %s,
                total_damage_dealt = %s,
                total_damage_taken = %s,
                total_heal = %s,
                total_minions_killed = %s,
                total_time_crowd_control_dealt = %s,
                total_units_healed = %s,
                total_damage_to_champions = %s,
                win = %s
                """
                match_id_puuid = f"{match_id}_{puuid}"
                cursor.execute(
                query,
                (
                match_id_puuid, match_id, puuid, riot_id, riot_id_tag_line,
                champion_name, role, item0, item1, item2, item3, item4, item5, item6,
                baron_kills, dragon_kills, elder_dragon_kills, rift_herald_kills, void_grub_kills, turrets_kills,
                champion_level, gold_earned, kills, deaths, assists, vision_score, total_damage_dealt,
                total_damage_taken, total_heal, total_minions_killed, total_time_crowd_control_dealt,
                total_units_healed, total_damage_to_champions, win,
                # Repeat for ON DUPLICATE KEY UPDATE (all except match_id_puuid)
                match_id, puuid, riot_id, riot_id_tag_line,
                champion_name, role, item0, item1, item2, item3, item4, item5, item6,
                baron_kills, dragon_kills, elder_dragon_kills, rift_herald_kills, void_grub_kills, turrets_kills,
                champion_level, gold_earned, kills, deaths, assists, vision_score, total_damage_dealt,
                total_damage_taken, total_heal, total_minions_killed, total_time_crowd_control_dealt,
                total_units_healed, total_damage_to_champions, win
                )
                )

            connection.commit()
            cursor.close()
            connection.close()
        except:
            print("match_id already exists in the database" +  str(sys.exc_info()))
    def __init__(self):
        
        puuid = 'mjP3GtqTPOeE2-jg8bqSOt2QsI5ml5VYA4O5jbKjLA7dVUIsVj44LuPN6kwD3NKV9AZOpVAJPS1htw'
        matches = api.get_matches(api, puuid)
        match = matches[0]
        match_data = api.get_match_data(api, match)
        for participant in match_data['info']['participants']:
            print(participant['championName'])
        self.insertMatch(match_data)
        self.readMatch_Players()


if __name__ == "__main__":
    TransferMatchData()