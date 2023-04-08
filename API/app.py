import mariadb
from flask import Flask, request, jsonify
from passlib.context import CryptContext
from flask_swagger_ui import get_swaggerui_blueprint
from flasgger import Swagger
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
Swagger(app)

app.config.update(THREADS_PER_PAGE=6)
app.config['debug']= True
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
########################################################################################################################
############################################ Configuration de swagger ##################################################
########################################################################################################################


SWAGGER_URL = '/documentation'
API_URL = '/static/doc.json'
swaggerui_blueprint = get_swaggerui_blueprint( # Swagger documentation
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "API meteo"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

########################################################################################################################
######################################## Initialisation de la connection avec la db ####################################
########################################################################################################################

conn = mariadb.connect(host='localhost',
                       user='guillaume',
                       password='Anapurna01',
                       database='meteo'
                       )


########################################################################################################################
#################################### Récupération de toutes les données par tables #####################################
########################################################################################################################

@app.route('/rambouillet')
def get_all():
    """
    description: Point d'entrée pour récupérer toutes les données pour Rambouillet
    """
    mesures = []
    cursor = conn.cursor()
    cursor.execute('select * from rambouillet')
    for row in cursor.fetchall():
        mesures.append({'temperature': row[0], 'pressure': row[1], 'humidity': row[2], 'IAQ': row[3], 'iCO2': row[4]})
    conn.close()
    return mesures


########################################################################################################################

@app.route('/Sevres')
def get_all_sevres():
    mesures_sevres = []
    cursor = conn.cursor()
    cursor.execute('select * from sevres')
    for row in cursor.fetchall():
        mesures_sevres.append(
            {'temperature': row[0], 'pressure': row[1], 'humidity': row[2], 'IAQ': row[3], 'iCO2': row[4]})
    conn.close()
    return mesures_sevres


########################################################################################################################
##################################### Ajout des données dans une table en particulier ##################################
########################################################################################################################


@app.route('/addRambouillet', methods=['POST'])
def add_rambouillet():
    try:
        record = request.get_json()
        _temp = record['temp']
        _press = record['press']
        _hum = record['hum']
        _IAQ = record['IAQ']
        _CO2 = record['CO2']

        if _temp and _press and _hum and _IAQ and _CO2:

            sql = "insert into rambouillet (temperature, pressure, humidity, IAQ, iCO2) values (%s, %s, %s , %s, %s)"
            data = (_temp, _press, _hum, _IAQ, _CO2)
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('Values added successfully!')
            resp.status_code = 200
            cursor.close()
            return resp

        else:
            resp = jsonify('Not found')
            resp.status_code = 404
            return resp

    except Exception as e:
        print(e)


########################################################################################################################

@app.route('/addSevres', methods=['POST'])
def add_sevres():
    try:
        record = request.get_json()
        _temp = record['temp']
        _press = record['press']
        _hum = record['hum']
        _IAQ = record['IAQ']
        _CO2 = record['CO2']

        if _temp and _press and _hum and _IAQ and _CO2:

            sql = "insert into sevres (temperature, pressure, humidity, IAQ, iCO2) values (%s, %s, %s , %s, %s)"
            data = (_temp, _press, _hum, _IAQ, _CO2)
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('Values added successfully!')
            resp.status_code = 200
            cursor.close()
            return resp

        else:
            resp = jsonify('Not found')
            resp.status_code = 404
            return resp

    except Exception as e:
        print(e)


########################################################################################################################
@app.route('/addRegades', methods=['POST'])
def add_regades():
    try:
        record = request.get_json()
        _temp = record['temp']
        _press = record['press']
        _hum = record['hum']
        _IAQ = record['IAQ']
        _CO2 = record['CO2']

        if _temp and _press and _hum and _IAQ and _CO2:

            sql = "insert into regades (temperature, pressure, humidity, IAQ, iCO2) values (%s, %s, %s , %s, %s)"
            data = (_temp, _press, _hum, _IAQ, _CO2)
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('Values added successfully!')
            resp.status_code = 200
            cursor.close()
            return resp

        else:
            resp = jsonify('Not found')
            resp.status_code = 404
            return resp

    except Exception as e:
        print(e)


########################################################################################################################
################################# Création d'une nouvelle table selon une valeur donnée ################################
########################################################################################################################


@app.route('/createTable', methods=['Post'])
def create_table():
    try:
        new = request.get_json()
        _name = new['name']

        if _name:
            cursor = conn.cursor()
            cursor.execute("create table %s (id int primary key auto_increment, temperature varchar(50), pressure varchar(50),\
                 humidity varchar(50), IAQ varchar(50), iCO2 varchar(50), created_at)", (_name,))
            conn.commit()
            resp = jsonify('Nouvelle table créée')
            resp.status_code = 200
            cursor.close()
            return resp

        else:
            resp = jsonify('Erreur, table non créée')
            resp.status_code = 404
            return resp

    except Exception as e:
        print(e)


########################################################################################################################
####################################### Récupération de la dernière ligne d'une base ###################################
########################################################################################################################


@app.route('/IARambouillet', methods=['GET'])
def ia_rambouillet():
    try:
        retour = []
        cursor = conn.cursor()
        cursor.execute('SELECT temperature, pressure, humidity FROM rambouillet ORDER BY created_at DESC LIMIT 1')
        for values in cursor:
            retour.append(values)
        jsonify(retour)
        cursor.close()
        return retour

    except Exception as e:
        print(e)


########################################################################################################################

@app.route('/IASevres', methods=['GET'])
def ia_sevres():
    try:
        retour = []
        cursor = conn.cursor()
        cursor.execute('SELECT temperature, pressure, humidity FROM sevres ORDER BY created_at DESC LIMIT 1')
        for values in cursor:
            retour.append(values)
        jsonify(retour)
        cursor.close()
        return retour

    except Exception as e:
        print(e)


########################################################################################################################


@app.route('/IARegades', methods=['GET'])
def ia_regades():
    try:
        retour = []
        cursor = conn.cursor()
        cursor.execute('SELECT temperature, pressure, humidity FROM regades ORDER BY created_at DESC LIMIT 1')
        for values in cursor:
            retour.append(values)
        jsonify(retour)
        cursor.close()
        return retour

    except Exception as e:
        print(e)


########################################################################################################################
########################################## Gestion des Users ###########################################################
########################################################################################################################

@app.route('/adduser', methods=['POST'])
def adduser():
    try:
         
        user = request.get_json()
        _username = user['username']
        _email = user['email']
        _password = user['password']
        _admin = user['admin']

        if _username and _email and _password and isinstance(_admin, int):
            new_hash = pwd_context.hash(_password)
            sql = "insert into users (username, email, password, admin) values (%s, %s, %s , %s)"
            data = (_username, _email, new_hash, _admin)
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('User added successfully!')
            resp.status_code = 200
            cursor.close()
            return resp

        else:
            resp = jsonify('Erreur, user non créée')
            resp.status_code = 404
            return resp

    except Exception as e:
        print(e)

########################################################################################################################

#verifiying user password
@app.route('/verifyUserPassword', methods=['POST'])
def verify_password():
    try:
        psswd = request.get_json()
        _username = psswd['username']
        _password = psswd['password']
        if _username and _password:
            cursor = conn.cursor()
            cursor.execute('select password from users where username = %s', (_username,))
            conn.commit()
            for i in cursor:
                for j in i:
                    user_hash = j

            if pwd_context.verify(_password, user_hash):
                resp = jsonify('success')
                resp.status_code = 200
                cursor.close()
                return resp

            else:
                resp = jsonify('not found')
                resp.status_code = 404
                cursor.close()
                return resp

    except Exception as e:
        print(e)

########################################################################################################################

#verifiying user mail
@app.route('/verifyUserMail', methods=['POST'])
def verify_mail():
    try:
        mail = request.get_json()
        _username = mail['username']
        _email = mail['email']
        if _username and _email:
            cursor = conn.cursor()
            cursor.execute('select email from users where username = %s', (_username,))
            conn.commit()
            for i in cursor:
                for j in i:
                    truc = j
            if truc == _email:
                resp = jsonify('success')
                resp.status_code = 200
                cursor.close()
                return resp

            else:
                resp = jsonify('not found')
                resp.status_code = 404
                cursor.close()
                return resp

    except Exception as e:
        print(e)

 
########################################################################################################################


@app.route('/deluser', methods=['POST'])
def del_user():
    try:
        user = request.get_json()
        _del_username = user['delusername']

        if _del_username:
            cursor = conn.cursor()
            cursor.execute('delete from users where username=%s', (_del_username,))
            conn.commit()
            resp = jsonify('User deleted successfully')
            resp.status_code = 200
            return resp

    except Exception as e:
        print(e)
        
########################################################################################################################

#get all users (for admin only)
@app.route('/getAllUsers', methods=['GET'])
def get_all_users():
    try:
        users = []
        cursor = conn.cursor()
        cursor.execute('select username, email, admin from users')
        for i in cursor:
            users.append(i)
        resp = jsonify(users)
        resp.status_code = 200
        return resp

    except Exception as e:
        print(e)
########################################################################################################################
################################################### Graphiques #########################################################
########################################################################################################################

@app.route('/globalDatas', methods=['GET'])
def graph_datas():
    try:
        temperatures_ramb = []
        pressure_ramb= []
        temp_sevres = []
        pressure_sevres = []
        temp_plaisir = []
        pressure_plaisir = []

        cursor = conn.cursor()
        cursor.execute('SELECT temperature, pressure FROM rambouillet order by created_at')
        for temperature, pressure in cursor:
            temperatures_ramb.append(float(temperature))
            pressure_ramb.append(pressure)

        cursor.execute('SELECT temperature, pressure FROM sevres order by created_at')
        for temperature, pressure in cursor:
            temp_sevres.append(float(temperature))
            pressure_sevres.append(pressure)

        retour = {"rambouillet": [temperatures_ramb, pressure_ramb], "sevres": [temp_sevres, pressure_sevres]}
        jsonify(retour)
        return retour

    except Exception as e:
        print(e)





########################################################################################################################
####################################### Gestion des exceptions #########################################################
########################################################################################################################


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp


if __name__ == '__main__':
    app.run(threaded=True)
