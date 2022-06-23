import random
import json
import torch
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

# Check for GPU support
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Open JSON file
with open('intents.json', 'r') as f:
    intents = json.load(f)

# Retrieve the saved model
FILE = "data.pth"
data = torch.load(FILE)

# Retrieve variables from data
input_size = data['input_size']
hidden_size = data['hidden_size']
output_size = data['output_size']
all_words = data['all_words']
tags = data['tags']
model_state = data['model_state']

# Create the model
model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

# Create the chat application/bot
bot_name = "Antonio"


def get_response(msg):
    # Tokenize input sentence
    sentence = tokenize(msg)
    # Get the word bag from the sentence and all words
    x = bag_of_words(sentence, all_words)

    # Reshape the bag of words
    x = x.reshape(1, x.shape[0])
    x = torch.from_numpy(x)

    # Get the predicted output & tag based on the trained model
    output = model(x.cuda())
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]

    # Gather the probablility of the user input match
    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    # If the probability of a match is greater than 75%, print that response
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent['tag']:
                return random.choice(intent['responses'])
    # Else let the user know the robot did not understand
    return "I do not understand..."