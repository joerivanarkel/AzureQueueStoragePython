class MessageModule:
    def add_message(queue_client, message):
        print(f"Adding message to the queue: {message}")
        try:
            return queue_client.send_message(message)
        except Exception as exception:
            print(exception)
            return None
    
    def peek_messages(queue_client):
        print("Peek at the messages in the queue")
        try:
            peeked_messages = queue_client.peek_messages(max_messages=5)
            for peeked_message in peeked_messages:
                print("Message: " + peeked_message.content)
            return True
        except Exception as exception:
            print(exception)
            return False
            
    def update_message(queue_client, saved_message, updated_content):   
        print("Updating a message in the queue")
        try:
            queue_client.update_message(saved_message, pop_receipt=saved_message.pop_receipt, content=updated_content)
            return True
        except Exception as exception:
            print(exception)
            return False

    def recieve_messages(queue_client):
        print("Receiving messages from the queue")
        try:
            return queue_client.receive_messages(messages_per_page=5)
        except Exception as exception:
            print(exception)
            return None
    
    def delete_messages(queue_client, message):
        try:
            print(f"Deleting: {message}")
            queue_client.delete_message(message)
            return True
        except Exception as exception:
            print(exception)
            return False

    def delete_queue(queue_client):
        print("Deleting queue...")
        try:
            queue_client.delete_queue()
            print("Done")
            return True
        except Exception as exception:
            print(exception)
            return False