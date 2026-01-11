#Alert Manager 

from abc import ABC, abstractmethod

# 1. The Interface (The "Contract")
class Notification(ABC):
    @abstractmethod
    def send(self, user_id, message):
        """All notification types must implement this method"""
        pass

# 2. Specific Implementations
class EmailService(Notification):
    def send(self, user_id, message):
        return f"📧 Sending Email to {user_id}: {message}"

class SMSService(Notification):
    def send(self, user_id, message):
        return f"📱 Sending SMS to {user_id}: {message} [Carrier rates may apply]"

class SlackService(Notification):
    def send(self, user_id, message):
        return f"💬 Posting to Slack channel for {user_id}: {message}"

# 3. The Polymorphic Engine (The "Dispatcher")
class AlertManager:
    def __init__(self):
        self.subscribers = []

    def add_channel(self, channel: Notification):
        self.subscribers.append(channel)

    def notify_all(self, user, msg):
        print(f"--- System Alert for {user} ---")
        for channel in self.subscribers:
            # Polymorphism in action: 
            # We don't know the class, we just know it has a .send() method.
            print(channel.send(user, msg))

# --- Execution ---
manager = AlertManager()

# We can plug in any notification type at any time
manager.add_channel(EmailService())
manager.add_channel(SMSService())
manager.add_channel(SlackService())

manager.notify_all("JohnDoe", "Your package has arrived!")