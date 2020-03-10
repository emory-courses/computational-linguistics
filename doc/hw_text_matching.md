# Text Maching

Your task is to create a dialogue manager that talks about "technology".


## Task

* Download [`hw_text_matching.py`](../src/hw/hw_text_matching.py) and put it under the [`src/`](../src) directory.
* Choose 1 topic in technology (e.g., smartphone, laptop, AI) and create a dialogue manager for the topic.
* Your dialogue manager must: 
    * Make the minimum of 10 turns, where 1 turn = (user input, system output).
    * Not lengthen the conversation by repetitive and patterned interactions like consecutive turns of jokes or quiz questions.
    * Not generate (political, religious, sexual, violent) responses potentially offensive to certain groups.
    * Not reveal any author's identify.
* Your dialogue manager is encouraged to:
    * Derive more opinion-based than information-based conversations.
      > Information-based: What is your smartphone &rarr; iPhone.<br>
        Opinion-based: Why do you like iPhone &rarr; Because it integrates well with my mac.
    * Use ontology to make more intelligent conversations.   
* The following criteria will be used for the assessment: 
    * **Conversation Flow**: how smooth the conversation flows.
    * **Uniqueness**: how unique the user's experience is.
    * **Engagement**: how much depth the conversation gives.
    * **Case Coverage**: how many different cases are covered.
    * **Error handling**: how well unexpected inputs are handled.
* Write a report and save it as `hw1.pdf` that includes:
    * Names of the team members.
    * Diagrams of your dialogue flows.
    * Explanation of your approach.


## Team

* Make a group of 2-3 members for this assignment.
* The same grade will be given to all team members.
* Use this as an opportunity to find the right teammates for the final project.
* Sign up the team under `HW1`: https://canvas.emory.edu/courses/71182/groups#tab-8717

## Submission

### Everyone

* Commit and push `src/hw_text_matching.py` to your GitHub repository.

### Team

* Submit `hw_text_matching.py` and `hw1.pdf` to https://canvas.emory.edu/courses/71182/assignments/294070
* Submit the URL of the GitHub repository that has the final copy of `hw_text_matching.py`.

## Grading Criteria
| Item | Points | Description |
| :--- | :---- | :--- |
| Report | 0 | Negligible information
| | 1 | Brief description; Unclear flowchart/conversational paths
| | 2 | Simpler approach description; Flowchart/conversational path given but does not provide an easily digestible understanding of what the possible conversation paths are
| | 3 | Detailed approach description; Clear flowchart; Easy to see the full paths of conversation (either from detailed flowchat or from fine-grained text description in report) 
| Dialogue Quality | 0 | Unable to run
| | 1 | Average experience
| | 2 | Good experience
| Depth | 0 | length minimum (10) not met
| | 1 |  length minimum (10) met
| Breadth | 0 | User transitions rely on any match, error transitions, or yes/no responses primarily
| | 1 | Majority of user transitions capture multiple options of responses (more than yes/no)
| Error Handling | 0 | Conversation breaks/Conversation loops infinitely in error case
| | 1 | Conversation never breaks and does not get stuck in infinite loop
| Uniqueness | 0 | Vanilla dialogueflow mechanisms (no ontology, no macros, no complex Natex)
| | 1 | Macros, vars, ontology, or complex Natex used
| Flow | 0 |Primarily abrupt topic changes, just a sequence of back to back questions, illogical sequence
| | 1 | Interesting, specific system responses focusing on opinions/experiences





