import json
from nltk_utils import tokenize, stem, bag_of_words
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from model import NeuralNet

# Opens the associated json file and saves it in 'intents'
with open('intents.json', 'r') as f:
    intents = json.load(f)
    
all_words = []
tags = []
xy = []

# Loop through the intent file
for intent in intents['intents']:
    # Save the tag, and append to tag list
    tag = intent['tag']
    tags.append(tag)
    # Loop through patterns in the pattern section
    for pattern in intent['patterns']:
        # Tokenize the pattern & save into all_words
        word = tokenize(pattern)
        all_words.extend(word)
        # Save the word & tag touple in xy
        xy.append((word, tag))
        
# Set up words to ignore, and stem all words excluding the ignores
ignore_words = ['?', '!', '.', ',']
all_words = [stem(word) for word in all_words if word not in ignore_words]
# Sort all words, and narrow down to only unique words
all_words = sorted(set(all_words))
# Sort tags, and narrow down to only unique
tags = sorted(set(tags))

# Create training lists for y & x
x_train = []
y_train = []
# Loop through xy list
for(pattern, tag) in xy:
    # Get the bad of words for xtrain and append
    bag = bag_of_words(pattern, all_words)
    x_train.append(bag)
    # Get the index of the tag and append to ytrain
    label = tags.index(tag)
    y_train.append(label)

# Turning x and y train datasets into numpy arrays
x_train = np.array(x_train)
y_train = np.array(y_train)

# Creating a class for chat data for easy iteration
class ChatDataset(Dataset):
    def __init__(self):
        self.n_samples = len(x_train)
        self.x_data = x_train
        self.y_data = y_train
        
    def __getitem__(self, i):
        return self.x_data[i], self.y_data[i]
    
    def __len__(self):
        return self.n_samples

# Hyperparameters
batch_size = 8
hidden_size = 8
output_size = len(tags)
input_size = len(x_train[0])
learning_rate = 0.001
num_epochs = 1000

dataset = ChatDataset()
train_loader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = NeuralNet(input_size, hidden_size, output_size).to(device)

# Loss and optimmizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

# Training Loop
for epoch in range(num_epochs):
    for(words, labels) in train_loader:
        # Have to convert labels to longtensor in order for criterion to work
        labels = labels.type(torch.LongTensor)
        
        # Sends words and labels to device (cpu or gpu)
        words = words.to(device)
        labels = labels.to(device)
        
        # Forward pass
        outputs = model(words)
        loss = criterion(outputs, labels)
        
        # Clear gradients
        optimizer.zero_grad()
        
        # Backward pass and optimizer
        loss.backward()
        optimizer.step()
    
    # Just prints loss on every 100th run
    if(epoch + 1) % 100 == 0:
        print(f'epoch {epoch+1}/{num_epochs}, loss={loss.item():.4f}')

# Prints the final loss amout
print(f'Final Loss: loss={loss.item():.4f}')

# Saving the data model
data = {
    "model_state":model.state_dict(),
    "input_size":input_size,
    "output_size":output_size,
    "hidden_size":hidden_size,
    "all_words":all_words,
    "tags":tags,
}

# Writing the data to pickle file
FILE = "data.pth"
torch.save(data, FILE)

print(f'Training Completed. Filed saved to {FILE}')
