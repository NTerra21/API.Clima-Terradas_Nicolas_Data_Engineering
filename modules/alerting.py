import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

def send_email(subject, body):
    sender_email = "your_email@example.com"
    receiver_email = "receiver_email@example.com"
    password = "your_password"

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.example.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

def check_alerts():
    username = os.getenv('REDSHIFT_USERNAME')
    password = os.getenv('REDSHIFT_PASSWORD')
    host = os.getenv('REDSHIFT_HOST')
    port = os.getenv('REDSHIFT_PORT', '5439')
    dbname = os.getenv('REDSHIFT_DBNAME')

    connection_url = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{dbname}"
    engine = create_engine(connection_url)

    with engine.connect() as connection:
        result = connection.execute("""
            SELECT city, temperature, humidity
            FROM nicolas_terradas_coderhouse.weather_data
            WHERE temperature > 30 OR humidity > 80;
        """)

        alerts = result.fetchall()
        if alerts:
            body = "The following cities have surpassed the alert thresholds:\n\n"
            for alert in alerts:
                body += f"City: {alert[0]}, Temperature: {alert[1]}, Humidity: {alert[2]}\n"
            send_email("Weather Alert", body)
