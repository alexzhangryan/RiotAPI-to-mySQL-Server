#RiotAPI to mySQL Server

A script that automatically queries the Riot Games api to collet match data from challenger players. Uses sqlAlchemy and Pandas to automatically collect the data into a mySQL server setup beforehand. Collects data such as total kills and gold earned by each players on both teams, champions played by each player, and objectives taken by each team. Accounts for being rate limited by setting a timeout when the rate limit is reached. 

#How to Setup

1. Clone the repository
   ```bash
   git clone https://github.com/alexzhangryan/RiotAPI-to-mySQL-Server
   ```
2. Naviagate into the directory
  ```bash
  cd ./RiotAPI-to-mySQL-Server
  ```
3. Setup your Riot Developer account at https://developer.riotgames.com/apis
4. Paste your API key into the variable titled "APIKey"

#WIP
