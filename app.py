import pathlib as pl

import numpy as np
import pandas as pd

from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

data = pl.Path(__file__).parent.absolute() / 'data'

# Charger les données CSV
associations_df = pd.read_csv(data / 'associations_etudiantes.csv')
evenements_df = pd.read_csv(data / 'evenements_associations.csv')

## Vous devez ajouter les routes ici : 

@app.route('/api/alive', methods=['GET'])    
def check_alive():
    return (200 '{"message" : "Alive"}')

print(associations_df.head())

@app.route('/api/associations', methods=['GET'])
def asso_list():
    return 200, associations_df['nom'].tolist()
