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

@app.route('/api/associations', methods=['GET'])
def asso_list():
    return 200, associations_df['nom'].tolist()

@app.route('/api/association/<int:id>', methods=['GET'])
def asso_details(id):
    if associations_df['id'].isin([id]).sum() != 0:
        return 200, associations_df['description'].iloc(id-1)
    else : 
        return 404, 'Not Found : { "error": "Association not found" }'

@app.route('/api/association/<int:id>/evenements', methods=['GET'])
def event(asso):
    return 200, evenements_df.loc[evenements_df['association_id'] == asso]


