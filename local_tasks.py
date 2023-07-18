from trivia_qa import TriviaQA

CUSTOM_TASKS = {
    "TriviaQA": TriviaQA
}

def get_task_dict():
    return CUSTOM_TASKS