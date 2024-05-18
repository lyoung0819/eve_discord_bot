import requests
# API responses from ESI 

# how to print War Details
class War: 

    def __init__(self, aggressor, declared, defender, finished):
        self.aggressor = aggressor
        self.declared = declared
        self.defender = defender
        self.finished = finished

    def __str__(self):
        return f'''
        Aggressor: {self.aggressor}
        War Declared On: {self.declared}
        Defender: {self.defender}
        War Finished On: {self.finished}
        '''


class EveAPI:
    base_url = 'https://esi.evetech.net/latest'

                            # >>>  Calendar Endpoints:  <<<
# Get an event: GET ||  /characters/{character_id}/calendar/{event_id}/
    def getEvents(self, char_id, event_id):
        request_url = self.base_url + '/characters/' + char_id + '/calendar/' + event_id + '/'
        response = requests.get(request_url)
        if response.ok:
            data = response.json()
            return data
        else:
            return 'Error'

                          # >>>  Corporations Endpoints:  <<<     
# Get corporation starbases (POSes): GET ||  /corporations/{corporation_id}/starbases/
    def getStarbases(self, corp_id):
        request_url = self.base_url + '/corporations/' + corp_id + '/starbases/'
        response = requests.get(request_url)
        if response.ok:
            data = response.json()
            return data
        else:
            return 'Error'


# Get starbase (POS) detail: GET ||  /corporations/{corporation_id}/starbases/{starbase_id}/
    def getStarbaseDetail(self, corp_id, sb_id):
        request_url = self.base_url + '/corporations/' + corp_id + '/starbases/' + sb_id + '/'
        response = requests.get(request_url)
        if response.ok:
            data = response.json()
            return data
        else:
            return 'Error'
        
# Get corporation structures: GET ||  /corporations/{corporation_id}/structures/
    def getStarbases(self, corp_id):
        request_url = self.base_url + '/corporations/' + corp_id + '/starbases/'
        response = requests.get(request_url)
        if response.ok:
            data = response.json()
            return data
        else:
            return 'Error'

# TEST ENDPOINTS:
    def getWarInfo(self, war_id):
        request_url = self.base_url + '/wars/' + war_id
        response = requests.get(request_url)
        if response.ok:
            data = response.json()
            print(data)
            war_info = War(data['aggressor'], data['declared'], data['defender'], data['finished'])
            return war_info
        else:
            return 'Error'

  
def mainWarTest():
    client = EveAPI()
    while True:
        war_id = input('Input ID of war OR "quit"')
        if war_id == 'quit':
            break
        war = client.getWarInfo(war_id)
        print(war)


mainWarTest()
