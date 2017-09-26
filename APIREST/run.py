from app import app
#Importando Rotas
from app.routes import *

if __name__ == '__main__':
    app.run(port=8045,debug=True)
