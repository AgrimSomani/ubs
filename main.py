from flask import Flask, request, jsonify
import json
app = Flask(__name__)

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


def efficient_hunter_kazuma(data):
    data = request.json
    result = []
    
    for entry in data:
        monsters = entry['monsters']
        efficiency = calculate_efficiency(monsters)
        result.append({'efficiency': efficiency})
    
    # return jsonify(result)
    return result

if __name__ == '__main__':
    inputFile = "in.json"
    with open(inputFile, 'r') as f:
        data = json.load(f)

    res = efficient_hunter_kazuma(data)
    
    with open('output.json', 'w') as f:
        json.dump(res , f, indent=4)

    # app.run(debug=True)