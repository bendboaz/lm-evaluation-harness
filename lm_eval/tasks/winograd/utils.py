from typing import List


def doc_to_text(doc: dict) -> str:
    """
    Convert a document dictionary to a text string.

    Args:
        doc (dict): The document dictionary containing the following keys:
            - context (str): The context of the document.
            - question (str): The question to be answered.
            - option1 (str): The first option for the answer.
            - option2 (str): The second option for the answer.

    Returns:
        str: The text content of the document.
    """
    return """Context: {{ context }}
  Question:{{ question }}
  Options:
  - "{{ option1 }}"
  - "{{ option2 }}\"""".format(**doc)


def doc_to_target(doc: dict) -> str:
    """
    Returns the correct answer option from the document based on the label.
    Args:
        doc (dict): The document dictionary containing 'option1', 'option2', and 'label'.
    Returns:
        str: The correct answer option as a string.
    """
    options = [doc["option1"], doc["option2"]]
    # label is expected to be 1 or 2 (as in the YAML: [option1, option2][label|int - 1])
    label = int(doc["label"])
    return options[label - 1]


def process_results(doc: dict, results: List[List[str]]):
    """
    Prepares a dictionary with all fields required for Tiny_Judge's generate_feedback function.
    Args:
        doc (dict): The document dictionary.
        results (List[List[str]]): The model's generated outputs (list of lists of strings).
    Returns:
        dict: Dictionary with all required fields for generate_feedback.
    """
    # Compose the instruction as description + doc_to_text(doc)
    description = doc.get("description", "<DESCRIPTION_PLACEHOLDER>")
    # Use the same formatting as doc_to_text
    instruction_text = (
        f"{description}\n" + f"Context: {doc.get('context', '<CONTEXT_PLACEHOLDER>')}\n"
        f"Question:{doc.get('question', '<QUESTION_PLACEHOLDER>')}\n"
        f'Options:\n- "{doc.get("option1", "<OPTION1_PLACEHOLDER>")}"\n- "{doc.get("option2", "<OPTION2_PLACEHOLDER>")}"'
    )
    response = results[0][0] if results and results[0] else ""
    reference_response = doc_to_target(doc)
    rubric_question = (
        "Does the response exactly match the reference answer (including quotes and formatting)? "
        "Score 5: Exact match. Score 3: Correct option but not exact format. Score 1: Incorrect answer. "
        "Ignore scores 2 and 4."
    )
    return {
        "instruction": instruction_text,
        "response": response,
        "reference_response": reference_response,
        "rubric_question": rubric_question,
        "score_1": "The response does not match the correct answer (wrong option or irrelevant output).",
        "score_2": "(Ignore this score)",
        "score_3": "The response selects the correct option but does not match the required format exactly (e.g., missing quotes, extra text, or minor formatting issues).",
        "score_4": "(Ignore this score)",
        "score_5": "The response matches the reference answer exactly, including quotes and formatting.",
    }
