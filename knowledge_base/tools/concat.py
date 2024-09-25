import os
import json
from json_helper import JsonHelper as helper
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def concatenate_markdown_files(source_path, output_path):
	with open(output_path, 'w', encoding='utf-8') as output_file:
		for root, dirs, files in os.walk(source_path):
			for file in files:
				if file.endswith('.md'):
					with open(os.path.join(root, file), 'r', encoding='utf-8') as input_file:
						output_file.write(input_file.read())
						output_file.write('\n')

def concatenate_json_files(directory_path, output_file_path='output.json'):
	"""
	This function recursively iterates over all .json files in the given directory,
	concatenates their content into a single file, and marks the source file boundary
	with the file name.
	
	:param directory_path: The path to the directory to search for .json files.
	:param output_file_path: The path where the concatenated markdown file will be saved.
	"""
	file_contents = dict()

	# FIXME: Remove  // comments
	
	for root, dirs, files in os.walk(directory_path):
		for file in files:
			# FIXME: Parse schemas? Put in another file without processing?
			if "schemas" in root:
				continue
			if file.endswith('.json'):
				file_path = os.path.join(root, file)
				with open(file_path, 'r', encoding='utf-8') as f:
					print(f'Opening {file}')
					text = f.read()
					text = helper.remove_comments(text)
					text = helper.fix_trailing_commas(text)
					j = json.loads(text)
					file_contents[file] = j
					# TODO: Parse to json string

	with open(output_file_path, 'w', encoding='utf-8') as output_file:
		output_file.write(json.dumps(file_contents, indent=4))

def dump_json_files(directory_path, output_file_path='output.json'):
	
	file_contents = dict()

	# FIXME: Remove  // comments
	
	for root, dirs, files in os.walk(directory_path):
		for file in files:
			if file.endswith('.json'):
				file_path = os.path.join(root, file)
				with open(file_path, 'r', encoding='utf-8') as f:
					print(f'Opening {file}')
					text = f.read()
					text = helper.remove_comments(text)
					text = helper.fix_trailing_commas(text)
					file_contents[file] = text
					# TODO: Parse to json string

	with open(output_file_path, 'w', encoding='utf-8') as output_file:
		output_file.write(json.dumps(file_contents, indent=4))

def concatenate_txt_files(directory_path, output_file_path):
	"""
	Searches for all .txt files in the given directory and its subdirectories,
	concatenates their content into a single file, and marks the source file boundary
	with the file name.
	
	:param directory_path: The path to the directory to search for .txt files.
	:param output_file_path: The path where the concatenated txt file will be saved.
	"""
	with open(output_file_path, 'w', encoding='utf-8') as output_file:
		for root, dirs, files in os.walk(directory_path):
			for file in files:
				if file.endswith('.txt'):
					file_path = os.path.join(root, file)
					with open(file_path, 'r', encoding='utf-8') as f:
						print(f'Opening {file}')
						content = f.read()
						output_file.write(content)
						output_file.write("\n")

# Concatenate all the content of knowledge_base/qa folder to knowledge_base/qa.txt
qa_path = "knowledge_base/qa"
qa_output = "knowledge_base/qa.txt"

concatenate_txt_files(qa_path, qa_output)

# Combine all the docs/ md files into a single one
source_path = os.getenv('VCMI_PATH')
docs_path = os.path.join(source_path, 'docs')

docs_file = "../source_docs.md"

concatenate_markdown_files(docs_path, docs_file)

# Combine all the config/ json files into a single one
config_path = os.path.join(source_path, 'config')
config_file = "../source_config.json"

concatenate_json_files(config_path, config_file)

schemas_path = os.path.join(source_path, 'schemas')
schemas_file = "../schemas.json"

dump_json_files(schemas_path, schemas_file)