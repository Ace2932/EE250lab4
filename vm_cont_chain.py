"""VM Cont Chain"""
import paho.mqtt.client as mqtt
import time


def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    client.subscribe("asfox/numberSent")

    client.message_callback_add("asfox/numberSent", on_message_from_number_sent)


def on_message_from_number_sent(client, userdata, msg):
    try:
        received_number = int(msg.payload.decode())
    except Exception:
        print(f"[CONT] Bad payload on {msg.topic}: {msg.payload!r}")
        return

    sent_number = received_number + 1
    print(f"[CONT] got number sent={received_number} -> publish number received={sent_number}")
    time.sleep(1)
    client.publish("asfox/numberReceived", f"{sent_number}")

def on_message(client, userdata, msg):
    print("Default callback - topic: " + msg.topic + "   msg: " + str(msg.payload, "utf-8"))


if __name__ == '__main__':
    #get IP address
    ip_address="172.20.10.2" 
    """your code here"""
    received_number = 0
    sent_number = 0
    #create a client object
    client = mqtt.Client()
    
    client.on_message = on_message
    client.on_connect = on_connect

    client.connect(host=ip_address, port=1883, keepalive=60)
    # client.loop_forever()
    client.loop_forever()




        