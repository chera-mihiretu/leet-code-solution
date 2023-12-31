class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.users = {}
    def generate(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.users:
            self.users[tokenId] = currentTime + self.timeToLive
            
    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.users:
            if self.users[tokenId] > currentTime:
                self.users[tokenId] = currentTime+self.timeToLive
            else:
                self.users.pop(tokenId)
    def countUnexpiredTokens(self, currentTime: int) -> int:
        sum_to_ret = 0
        for item, time in self.users.items():
            if time > currentTime:
                sum_to_ret +=1
        return sum_to_ret
    
            


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)