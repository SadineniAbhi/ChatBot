def removeEmptyLines(text):
    # Split the text into lines
    lines = text.split('\n')
    
    # Remove empty lines
    non_empty_lines = [line for line in lines if line.strip()]
    
    # Join the non-empty lines back together
    new_text = '\n'.join(non_empty_lines)
    
    return new_text
