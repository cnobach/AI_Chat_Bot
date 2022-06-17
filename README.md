# AI Chat Bot

Practicing basic NLP usages within a chatbot application. Uses a Neural Network in order to predict responses to user input. This was made based off of a YouTube tutorial, which can be found here: **https://www.youtube.com/playlist?list=PLqnslRFeH2UrFW4AUgn-eY37qOAWQpJyg**. 

This is to simulate an AI Chat Bot within a online store application. The chatbot will be able to answer questions, such as, "What do you sell here?", and "How long does shipping take?". These inputs can be written in mixed orders - i.e. the question of "How long does shipping take?" can be rewritten as "long does How take shipping?" and the chatbot should be able to process this, and give an expected response.


## Usage

The **intents.json** file provides all the expected inputs from the user, and their respective outputs. In order to add, change, or remove any of these the file just needs to be edited. 

Once the file is edited, the **train.py** file needs to be ran again in order to train the model and save it with the new responses. 

After this, all that needs to be done is to run **chat.py** and the application will run in the terminal.

To the bot, you can type greetings to it such as "Hello", "How are you?", etc. You can also ask questions about what they sell at the store, how much the items cost, what forms of payment are accepted, and you can even ask it to tell you a joke.