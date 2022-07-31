import uuid
from dotenv import dotenv_values
from azure.storage.queue import QueueClient
from Message_Module import MessageModule

try:
    print("Azure Queue storage v12 - Python quickstart sample")
    
    #connection string
    config = dotenv_values(".env")
    connectionstring = config["CONNECTIONSTRING"]
    
    # Create a unique name for the queue
    queue_name = "quickstartqueues-" + str(uuid.uuid4())

    print("Creating queue: " + queue_name)

    # Instantiate a QueueClient which will be
    # used to create and manipulate the queue
    queue_client = QueueClient.from_connection_string(connectionstring, queue_name)

    # Create the queue
    queue_client.create_queue()
    
    
    MessageModule.add_message(queue_client, 'message for testing purposes only')
    
    MessageModule.peek_messages(queue_client) 
        
    MessageModule.update_message(queue_client, MessageModule.add_message(queue_client, 'hola'), 'hola but updated')
    
    
    print("Press Enter key to 'process' messages and delete them from the queue...")
    input()
    messages = MessageModule.recieve_messages(queue_client)
    for message in messages:
        print(f"message recieved: {message.content}")
    

    print("Press Enter key to 'process' messages and delete them from the queue...")
    input()
    
    MessageModule.delete_messages(queue_client, messages)
    
    print("Press Enter key to delete the queue...")
    input()
    
    MessageModule.delete_queue(queue_client)
        
except Exception as ex:
    print('Exception:')
    print(ex)