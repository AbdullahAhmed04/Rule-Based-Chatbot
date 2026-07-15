
responses = {
    "hello": "Hi! How are you doing? How can I help you today?",
    "hi": "What is on your mind?",
    "how are you": "I am program and I am  running smoothly. You?",
    "your name": "I am RuleBot, your friendly rule based assistant.",
    "goat": "El Bicho",
    "what can you do": "I can respond to a few predefined commands. Try 'help'",
    "help": "Commands I know: hello, how are you, what is your name, who is the goat, what can yo do, bye",
    "thank you": "You are Welcome",
    "thanks": "Anytime",
}

EXIT_COMMANDS = {"bye", "exit", "quit", "goodnight", "bye bye", "adios", "sayonara"}
FALLBACK_RESPONSE = "I do not understand. Type 'help' to see what I can do"

def sanitize(raw_input: str) -> str:
  return raw_input.lower().strip()

def get_response(clean_input: str) -> str:
  if clean_input in responses:
    return responses[clean_input]
  for key, reply in responses.items():
    if key in clean_input:
      return reply
  return FALLBACK_RESPONSE

def main():
  print("RuleBot: Hello, I am your rule based chat bot. Enter 'bye' to exit")

  while True:
    raw_input_text = input("You: ")
    clean_input = sanitize(raw_input_text)

    if clean_input in EXIT_COMMANDS:
      print("RuleBot: Goodbye, Have a Great Day :)")
      break

    reply = get_response(clean_input)
    print(f"RuleBot: {reply}")
if __name__ == "__main__":
  main()