# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import sys

import pika


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

def main():
    credentials = pika.PlainCredentials('qos', 'admin')
    connection = pika.BlockingConnection(pika.ConnectionParameters('10.40.1.2', 30951, '/', credentials))
    channel = connection.channel()





    channel.queue_declare(queue='sigrail_best_network')
    channel.basic_consume(queue='sigrail_best_network',
                          auto_ack=True,
                          on_message_callback=callback)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)
