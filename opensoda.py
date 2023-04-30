import json
import requests

# fetch data with GitHub REST API
# support not only a single API
class getInfo():
    host:str
    owner:str
    repo:str
    page_tota:int
    page_now:int

    def __init__(self, url:str, owner:str, repo:str) -> None:
        self.host = url
        self.owner = owner
        self.repo = repo

    def __str__(self) -> str:
        return self.host + self.owner + self.repo

    def get_pages(self, links:dict) -> None:
        next_dict = links["next"]
        last_dict = links["last"]
        last_dict["url"]
        return

    def get_repo_stargazers(self) -> dict:
        # get the api addr
        url = combineUrl(self.host, "repos", self.owner, self.repo, "stargazers")
        
        # get stargazers list with star time
        rsp = requests.get(url, headers={"Accept":"application/vnd.github.v3.star+json"})
        
        # get page data of stargazers
        self.get_pages(rsp.links)
        
        # parse .json and convert it to dict
        data:dict = json.loads(rsp.text)

        return data
    
def combineUrl(*args) -> str:
        url = "https:/"
        for arg in args:
            url += '/'
            url += arg
        
        return url

def calStat (data:dict):
    ret:dict
    
    return ret

def output (data:str):
    ret = json.dumps(data)

    return ret

info = getInfo("api.github.com", "github-tools", "github")
data = info.get_repo_stargazers()
#print(data)
