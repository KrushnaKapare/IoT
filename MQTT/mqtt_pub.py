import paho.mqtt.client as mqtt

def on_publish(client,userdata, mid, reason_code, properties):
    print("message is published")

publisher = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

publisher.on_publish = on_publish

publisher.connect(host="localhost")

publisher.publish(topic="sensor/ldr",payload='bye')

publisher.disconnect()