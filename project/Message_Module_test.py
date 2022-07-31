import imp
from unittest import result
import uuid
from dotenv import dotenv_values
import pytest
from Message_Module import MessageModule
from azure.storage.queue import QueueClient

def test_add_message():
    config = dotenv_values(".env")
    connectionstring = config["CONNECTIONSTRING"]
    queue_name = "quickstartqueues-" + str(uuid.uuid4())
    queue_client = QueueClient.from_connection_string(connectionstring, queue_name)
    queue_client.create_queue()
    
    result = MessageModule.add_message(queue_client, 'to test')
    assert result != None
    MessageModule.delete_messages(queue_client, result)
    MessageModule.delete_queue(queue_client)
    
def test_peek_messages():
    config = dotenv_values(".env")
    connectionstring = config["CONNECTIONSTRING"]
    queue_name = "quickstartqueues-" + str(uuid.uuid4())
    queue_client = QueueClient.from_connection_string(connectionstring, queue_name)
    queue_client.create_queue()
    
    message = MessageModule.add_message(queue_client, 'to test')
    result = MessageModule.peek_messages(queue_client)
    assert result == True
    MessageModule.delete_messages(queue_client, message)
    MessageModule.delete_queue(queue_client)
    
def test_update_message():
    config = dotenv_values(".env")
    connectionstring = config["CONNECTIONSTRING"]
    queue_name = "quickstartqueues-" + str(uuid.uuid4())
    queue_client = QueueClient.from_connection_string(connectionstring, queue_name)
    queue_client.create_queue()
    
    message = MessageModule.add_message(queue_client, 'to test')
    result = MessageModule.update_message(queue_client, message, 'to test UPDATE')
    assert result == True
    MessageModule.delete_messages(queue_client, result)
    MessageModule.delete_queue(queue_client)
    
def test_recieve_messages():
    config = dotenv_values(".env")
    connectionstring = config["CONNECTIONSTRING"]
    queue_name = "quickstartqueues-" + str(uuid.uuid4())
    queue_client = QueueClient.from_connection_string(connectionstring, queue_name)
    queue_client.create_queue()
    
    message = MessageModule.add_message(queue_client, 'to test')
    result = MessageModule.peek_messages(queue_client)
    assert result != None
    MessageModule.delete_messages(queue_client, message)
    MessageModule.delete_queue(queue_client)