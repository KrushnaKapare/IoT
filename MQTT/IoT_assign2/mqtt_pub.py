import paho.mqtt.client as mqtt
publisher = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

def pub(method, status):
    def on_publish(client,userdata, mid, reson_code, properties):
        print("message is published")

    publisher.on_publish = on_publish
    publisher.connect(host="localhost")
    message = f"{method} : {status}"
    publisher.publish(topic="health/status", payload=message)
    publisher.disconnect()