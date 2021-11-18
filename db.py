from psycopg2 import Error
from flask import jsonify
import psycopg2


def getPersonnes():
    try:
        # Connect to an existing database
        connection = psycopg2.connect(user="u2sowhlu7bq2ggz6yj3d",
                                      password="tu9cuQ5cp5lnW78g2TN9",
                                      host="bgz0sw5zf20rlrzvysuh-postgresql.services.clever-cloud.com",
                                      port="5432",
                                      database="bgz0sw5zf20rlrzvysuh")
        cursor = connection.cursor()
        cursor.execute("SELECT 'id', 'nom', 'prenom', 'mail', 'numTel', 'sexe' from \"Personne\";")
        query = cursor.fetchall()

        return jsonify(query)
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL : ", error)


def postPersonnes():
    try:
        connection = psycopg2.connect(user="u2sowhlu7bq2ggz6yj3d",
                                      password="tu9cuQ5cp5lnW78g2TN9",
                                      host="bgz0sw5zf20rlrzvysuh-postgresql.services.clever-cloud.com",
                                      port="5432",
                                      database="bgz0sw5zf20rlrzvysuh")
        cursor = connection.cursor()
        postgres_insert_query = "INSERT INTO \"Personne\" (prenom, nom, mail, numTel, sexe) VALUES (%s,%s,%s,%s,%s)"
        record_to_insert = ('leo', 'catifait', 'leo.catifait@epsi.fr', '0771788763', 'homme')
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        return 'SUCCESS'

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL : ", error)
        return 'ERROR'


def updPersonnes():
    try:
        connection = psycopg2.connect(user="u2sowhlu7bq2ggz6yj3d",
                                      password="tu9cuQ5cp5lnW78g2TN9",
                                      host="bgz0sw5zf20rlrzvysuh-postgresql.services.clever-cloud.com",
                                      port="5432",
                                      database="bgz0sw5zf20rlrzvysuh")
        cursor = connection.cursor()
        postgres_update_query = "UPDATE \"Personne\" SET prenom=(%s), nom=(%s), mail=(%s), numTel=(%s), sexe=(%s) where id=%s"
        record_to_update = ('Prenom', 'Nom', 'mail@epsi.fr', 'Numero', 'SEXE', '3')
        cursor.execute(postgres_update_query, record_to_update)
        connection.commit()
        return 'SUCCESS'

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL : ", error)
        return 'ERROR'


def delPersonnes():
    try:
        connection = psycopg2.connect(user="u2sowhlu7bq2ggz6yj3d",
                                      password="tu9cuQ5cp5lnW78g2TN9",
                                      host="bgz0sw5zf20rlrzvysuh-postgresql.services.clever-cloud.com",
                                      port="5432",
                                      database="bgz0sw5zf20rlrzvysuh")
        cursor = connection.cursor()
        postgres_delete_query = "DELETE FROM \"Personne\" WHERE id=%s"
        record_to_delete = "2"
        cursor.execute(postgres_delete_query, record_to_delete)
        connection.commit()
        return 'SUCCESS'

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL : ", error)
        return 'ERROR'
