# Lexicon & Entity Matching

Your task is to create a dialogue manager that talks about the topic of your choice.

## Task

* Download [`hw_lexicon_entity_matching.py`](../src/hw/hw_lexicon_entity_matching.py) and put it under the [`src/`](../src) directory.
* Choose 1 topic that you intend to proceed with the final project.
* Your dialogue manager must: 
    * Follow all the conventions from the [previous homework](hw_text_matching.md). 
    * Make use of a fairly large ontology and POS/NER tags.
* Write a report and save it as `hw2.pdf` that includes:
    * Names of the team members.
    * Diagrams of your dialogue flows.
    * Explanation of your approach.


## Team

* Make a group of 3-4 members for this assignment.
* The same grade will be given to all team members.
* This will be the group for your final project as well.
* Sign up the team under `Projects`: https://canvas.emory.edu/courses/71182/groups#tab-8413

## Submission

### Everyone

* Commit and push `src/hw_lexicon_entity_matching.py` to your GitHub repository.

### Team

* Submit `hw_lexicon_entity_matching.py` and `hw2.pdf` to https://canvas.emory.edu/courses/71182/assignments/294072
* Submit the URL of the GitHub repository that has the final copy of `hw_text_matching.py`. 



## Note
Remember, even though the interface by which you are testing your bot is through text, the ultimate goal is to create a conversation that is as natural as possible. Approach your responses as if they are being spoken in a real conversation, not typed. This makes things like long website urls or using parentheses as a way to list options not an appropriate choice.

### Things to Avoid
* No infinite self-loops, prompting user to try again
* Do not modify the format of the output (such as by inserting manual newlines with “S:” prompt in them)
* Do not use input() in Macros; all input, output should be handled through the built-in state machine functionality
* Do not include revealing information of authors, emory university, atlanta, or georgia
* Do not name your bot
* Include proper punctuation, especially commas (you use double quotation marks around the punctuated text to include it in Natex)
* Do not include website links
* Do not put use parentheses as a way to list options
* The bot responses should be conversational (e.g. replace commands like "enter" or "input" with a natural language question)


