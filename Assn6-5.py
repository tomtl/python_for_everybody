text = "X-DSPAM-Confidence:    0.8475"
target_text = text[text.find(":") + 1:].lstrip()
target_number = float(target_text)
print target_number