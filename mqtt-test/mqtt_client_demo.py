import paho.mqtt.client as mqtt

# define static variable
# broker = "localhost" # for local connection
broker = "test.mosquitto.org"  # for online version
port = 1883
timeout = 60

username = ''
password = ''

topic = "didik/169"
topic_pub = "didik/169/greetings"
 
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() - if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(topic,qos=2)
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload.decode('utf-8')))
    message = str(msg.payload.decode('utf-8'))
    
    # mengirim balik
    ret = client.publish(topic_pub,payload=message,qos=1)
          
        
def on_publish(client,userdata,result):
	print("data published \n")

# Create an MQTT client and attach our routines to it.
client = mqtt.Client("didik/device1")
client.username_pw_set(username=username,password=password)
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish

client.connect(broker, port, timeout)

client.loop_forever()

