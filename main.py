from typing import List
from fastapi import FastAPI, Request
from pydantic import BaseModel
from english_words import get_english_words_set
import random

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


@app.post("/wordle-game")
async def wordle_game(data):
    
    
    web2lowerset = get_english_words_set(['web2'], lower=True)
    
    five_words_set = set()
    
    for word in web2lowerset:
        if len(word) == 5:
            five_words_set.add(word)
            

    
    data = {
        "guessHistory": ["slate", "lucky", "maser", "gapes", "wages"], 
        "evaluationHistory": ["?-X-X", "-?---", "-O?O-", "XO-?O", "OOOOO"]
    }
    
    guessHistory = data["guessHistory"]
    evaluationHistory = data["evaluationHistory"]
    
    if not guessHistory:
        first_guess = random.choice(list(five_words_set))
        return first_guess

    else:
        
        guess = ['', '', '', '', '']
        banned_letters = set()
        possible_letters = set()
        
        for i in range(len(evaluationHistory)):
            prev_guess  = guessHistory[i]
            prev_eval   = evaluationHistory[i]
            
            for i in range(len(prev_eval)):
                if prev_eval[i] == 'X':
                    possible_letters.add(prev_guess[i])
                elif prev_eval[i] == 'O':
                    guess[i] = prev_guess[i]
                    possible_letters.add(prev_guess[i])
                elif prev_eval[i] == '-':
                    banned_letters.add(prev_guess(i))
                elif prev_eval[i] == '?':
                    continue
        
        possible_guess = set()
        for word in five_words_set:
            
            for i in range(len(word)):
                if word[i] in banned_letters:
                    break
            
            
            
    
    
    # curr_letters = 






