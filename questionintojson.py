import os
import json
import subprocess
import re
import glob


def extract_questions_from_markdown(file_path):
    # Open the Markdown file and read its contents.
    with open(file_path, "r") as file:
        content = file.read()

    # Use regular expressions to match question blocks.
    pattern = r"#### Q\d+\.(.*?)\n\n((?:- \[.\] .*?\n)+)"
    matches = re.findall(pattern, content, re.DOTALL)

    # Create a list to store the questions.
    questions = []

    # Iterate over the matches and extract the questions and answers.
    for match in matches:
        # Separate the question and answers.
        question = match[0].strip()

        # Find the options.
        options_pattern = r"- \[.\] (.*?)\n"
        options = re.findall(options_pattern, match[1])

        # Find the correct answers.
        correct_answers_pattern = r"- \[x\] (.*?)\n"
        correct_answers = re.findall(correct_answers_pattern, match[1])

        # Create a list to store the answers.
        answers = []

        # Iterate over the options and create a dictionary for each answer.
        for option in options:
            is_correct = option in correct_answers
            answer = {"option": option, "correct": is_correct}
            answers.append(answer)

        # Create a dictionary to store the question and answers.
        question_data = {"question": question, "options": answers}

        # Add the question to the list of questions.
        questions.append(question_data)

    # Return the list of questions.
    return questions


# Get a list of all the Markdown files in the current directory.
command = ["find", ".", "-name", "*.md"]

try:
    # Run the `find` command and get the output.
    output = subprocess.check_output(command)

    # Convert the output to a string and remove the trailing newline.
    output = output.decode("utf-8").strip()

    # Split the output into a list of filenames.
    file_list = output.split("\n")

    # Iterate over the list of filenames and extract the questions from each file.
    for file_name in file_list:
        questions = extract_questions_from_markdown(file_name)

        # Write the questions to a JSON file.
        with open(file_name.split(".md")[0] + ".json", "w") as file:
            json.dump(questions, file, indent=4)

        # Print the filename.
        print(file_name)

except subprocess.CalledProcessError as e:
    # Print the error message.
    print(f"Error: {e}")


# Create a dictionary to store the subjects and their questions.
merged_json = {"subjects": {}}

# Get a list of all the JSON files in the current directory.
json_files = glob.glob("./*.json")

# Iterate over the list of JSON files and merge the questions into the `merged_json` dictionary.
for json_file in json_files:

    # Get the name of the subject.
    name = json_file.split("/")[-1].split(".json")[0]

    # Open the JSON file and read its contents.
    with open(json_file, "r") as json_file:

        data = json.load(json_file)

        # Add the questions to the `merged_json` dictionary.
        merged_json["subjects"][name] = data

# Write the `merged_json` dictionary to a JSON file.
with open("merged.json", "w") as output_file:
    json.dump(merged_json, output_file, indent=4)