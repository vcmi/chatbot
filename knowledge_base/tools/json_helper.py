import re

class JsonHelper:

    def remove_comments(json_str):
        # Regular expression to match C-style comments
        pattern = re.compile(
            r'//.*?$|/\*.*?\*/', 
            re.DOTALL | re.MULTILINE
        )
        # Remove the comments
        no_comments = re.sub(pattern, '', json_str)
        return no_comments
    
    def fix_trailing_commas(json_str):

        fix_commas =re.sub(r',\s*([}\]])', r'\1', json_str)
        return fix_commas
    
