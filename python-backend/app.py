# app.py (Flask Backend)

from flask import Flask, jsonify
from genetic_algorithm import genetic_algorithm

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Genetic Algorithm API! Visit /api/genetic-algorithm to run the algorithm."

@app.route('/api/genetic-algorithm')
def run_genetic_algorithm():
    best_solution = genetic_algorithm(population_size=10, generations=20)
    return jsonify(best_solution[0])

if __name__ == '__main__':
    app.run(debug=True)
