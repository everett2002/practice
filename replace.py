def replace_100_with_emoji_via_loop(text):
    modified_text = ""
    i = 0
    while i < len(text):
        # If "100" is found, add '💯' to modified_text and skip the next two characters
        if text[i:i+3] == "100":
            modified_text += "💯"
            i += 3  # Skip the "100"
        else:
            # else add the current character to modified_text
            modified_text += text[i]
            i += 1
    return modified_text

# Example usage
example_text = "I scored 100 on my test, and my friend got 100 too, making us both score 100 points exactly."
modified_text = replace_100_with_emoji_via_loop(example_text)
print(modified_text)