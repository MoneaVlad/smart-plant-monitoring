import random
import time
import json

from paho.mqtt import client as mqtt_client

# 
broker = 'localhost'
port = 1883
# See [[inputs.mqtt_consumer]] on conf/telegraf/telegraf.conf
topic = "sensors"

# generate client ID with pub prefix randomly
client_id = 'sensor_1'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    temperature = 20
    while True:
        time.sleep(5) # sleep 5 sec
        temperature = temperature + random.randint(-1, 1)
        dict_msg = {
            "temperature": temperature
        }
        msg = json.dumps(dict_msg)
        
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()