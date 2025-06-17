import requests
import sys
import pandas as py
class api: 
    api_key = "RGAPI-9d2c41cd-bb35-479a-92b1-cda7bc32eca7"
    def get_puuid(self, name, tag):
        user_api_url = "https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id"
        self.name = name
        try:
            user_url = f"{user_api_url}/{name}/{tag}?api_key={self.api_key}"
            response = requests.get(user_url)

            if(response.status_code == 200):
                user_data = response.json()
                return user_data['puuid']
                
            else:
                raise Exception("unable connect to user api" + str(response.status_code))
        except:
            raise Exception("User not found")
    def get_matches(self, puuid):
        matches_api_url = "https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/"
        try:
            matches_url = f"{matches_api_url}{puuid}/ids?start=0&count=20&api_key={self.api_key}"
            response = requests.get(matches_url)
            
            if(response.status_code == 200):
                matches_data = response.json()
                return matches_data
            else:
                raise Exception("unable to connect to matches api " + str(response.status_code))
        except:
            raise Exception("puuid not found")
    def get_match_data(self, match):
        match_api_url = "https://americas.api.riotgames.com/lol/match/v5/matches/"
        try:
            match_url = f"{match_api_url}{match}?api_key={self.api_key}"
            response = requests.get(match_url)

            if(response.status_code == 200):
                match_data = response.json()
                return match_data
            else:
                raise Exception("unable to connect to match api" + str(response.status_code))
        except:
            raise Exception("match not found")
    def get_challenger_ladder(self):
        chall_api_url = "https://na1.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5?api_key="
        try:
            match_url = f"{chall_api_url}{self.api_key}"
            response = requests.get(match_url)

            if(response.status_code == 200):
                match_data = response.json()
                return match_data
            else:
                raise Exception("unable to connect to match api" + str(response.status_code))
        except:
            raise Exception("match not found")
    def __init__(self):
        
        '''
        matches = self.get_matches(puuid)
        print(matches[0])
        match = self.get_match_data(matches[0])
        print(match['info']['participants'][0]['riotIdGameName'])
        for user in match['info']['participants']:
            print(user['riotIdGameName'])
        
        chall_ladder = self.get_challenger_ladder()
        for user in chall_ladder['entries']:
            print(user['puuid'])
        '''
        
if __name__ == "__main__":
    api()