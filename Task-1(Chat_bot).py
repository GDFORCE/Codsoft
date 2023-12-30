import datetime
import time
import threading
import re

def medication_reminder():
    while True:
        medications = get_medication_schedule()
        for medication in medications:
            if medication['time'] == datetime.datetime.now().strftime("%H:%M"):
                print("Medication reminder: It's time to take your {} at {}.".format(medication['name'], medication['time']))
                send_reminder(medication['name'])
        time.sleep(60)  # Check for reminders every minute

def get_medication_schedule():
    # Replace with your actual implementation to retrieve medication data
    # Example using a hardcoded list:
    return [
        {'name': 'Aspirin', 'time': '08:00'},
        {'name': 'Allergy medication', 'time': '12:00'},
        {'name': 'Blood pressure medication', 'time': '20:00'}
    ]

def send_reminder(medication_name):
    # Replace with your preferred reminder method (e.g., text messaging, notification)
    print("Sending reminder for:", medication_name)

def basic_conversation():
    rules = {
        'hello|hi|hey': 'Hello there! How can I help you today?',
        'how are you': 'I\'m doing well, thanks for asking! How can I assist you?',
        'what time is it': 'The current time is {}'.format(datetime.datetime.now().strftime("%H:%M")),
        r'(what|list|show|tell me about) my (pills|medicines|medications)': 'You need to take the following medications today:',
        'can you repeat that': 'Sure, I can repeat that. What would you like me to repeat?',
        'thank you': 'You\'re welcome! I\'m here to help whenever you need me.',
        r'(what is|tell me about) (.*) medication': 'I\'m not able to provide specific medical information about medications. Please consult with your doctor or pharmacist for details about {} medication.',
        'bye': 'Thank you for chatting with us. If you have more questions, feel free to ask. Goodbye!'
    }

    while True:
        user_input = input("You: ").lower()
        response = "Sorry, I'm not sure I understand. If you have specific questions about medication or need reminders, feel free to ask."

        for pattern, rule_response in rules.items():
            if re.search(pattern, user_input, re.IGNORECASE):
                response = rule_response
                if pattern == r'(what|list|show|tell me about) my (pills|medicines|medications)':
                    medications = get_medication_schedule()
                    response += "\n" + "\n".join(f"- {med['name']} at {med['time']}" for med in medications)
                elif pattern == r'(what is|tell me about) (.*) medication':
                    medication_name = re.search(r'(what is|tell me about) (.*) medication', user_input).group(2)
                    response = response.format(medication_name)
                break

        print("Bot:", response)

        if user_input == 'bye':
            break

if __name__ == "__main__":
    reminder_thread = threading.Thread(target=medication_reminder)
    reminder_thread.start()

    basic_conversation()
