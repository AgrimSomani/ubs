from typing import List
from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class MonsterData(BaseModel):
    monsters: List[int]

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/efficient-hunter-kazuma")
async def efficient_hunter_kazuma(data: List[MonsterData]):
    def calculate_efficiency(monsters):
        n = len(monsters)
        dp = [[0] * (n + 2) for _ in range(2)]
        for i in range(n-1, -1, -1):
            for buy in range(2):
                if buy:
                    dp[buy][i] = max(-monsters[i] + dp[0][i+1], dp[1][i+1])
                else:
                    dp[buy][i] = max(monsters[i] + dp[1][i+2], dp[0][i+1])
        return dp[1][0]

    result = []
    for entry in data:
        monsters = entry.monsters
        efficiency = calculate_efficiency(monsters)
        result.append({'efficiency': efficiency})
    
    return result

