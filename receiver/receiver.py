import pika, os

def main():
    username = 'guest'
    password = 'guest'
    host = '/'
    port = 5672

    if 'RQMUSERNAME' in os.environ: 
        username = os.environ['RQMUSERNAME']
    if 'RQMUSERPASS' in os.environ: 
        password = os.environ['RQMUSERPASS']
    if 'RMQHOST' in os.environ: 
        host = os.environ['RMQHOST']
    if 'RMQPORT' in os.environ: 
        port = os.environ['RMQPORT']

    credentials = pika.PlainCredentials(username, password)
    parameters = pika.ConnectionParameters('rabbitmq', port, host, credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(queue='consumer')

    def callback(ch, method, properties, body):
        print(" [consumer] Received: %r" % body)

    channel.basic_consume(queue='consumer', on_message_callback=callback, auto_ack=True)

    print('Waiting for messages (consumer queue)')
    channel.start_consuming()

if __name__ == '__main__':
    main()