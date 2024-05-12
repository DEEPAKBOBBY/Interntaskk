import flask
import pandas as pd
from flask import Flask,request,render_template,redirect,jsonify,session
import mysql.connector
import _mysql_connector
import os


app=Flask(__name__)

@app.route("/")
def homee():
    return render_template("index.html")

def managing():
    import pandas as pd
    import mysql.connector


    df = pd.read_excel("output.xlsx")


    df = df.where(pd.notnull(df), None)


    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="deepakbobby26229",
        database="intern"  # Specify your database name
    )
    myc = mydb.cursor()


    insert_query = f"INSERT INTO interndata (end_year, intensity, sector, topic, insight, url, region, start_year, impact, added, published, country, relevance, pestle, source, title, likelihood) VALUES ({', '.join(['%s'] * 17)});"


    for index, row in df.iterrows():
        values = tuple(row)
        myc.execute(insert_query, values)


    mydb.commit()

    myc.close()
    mydb.close()


@app.route("/count")
def country():
    return render_template("country.html")

@app.route("/pest")
def pestle():
    return render_template("pestle.html")

@app.route("/regi")
def region():
    return render_template("Region.html")

@app.route("/sec")
def sector():
    return render_template("sector.html")

@app.route("/sou")
def source():
    return render_template("Source.html")

@app.route("/top")
def topic():
    return render_template("topic.html")



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)

