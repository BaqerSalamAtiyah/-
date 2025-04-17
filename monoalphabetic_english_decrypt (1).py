from collections import Counter

# Expected frequency order of English letters (most to least common)
COMMON_LETTERS = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

def monoalphabetic_decrypt(ciphertext, manual_map=None):
    # Clean text: keep only uppercase alphabetic characters
    cleaned_text = ''.join(filter(str.isalpha, ciphertext.upper()))
    
    # Frequency analysis
    freq = Counter(cleaned_text)
    most_common_in_cipher = ''.join([pair[0] for pair in freq.most_common()])

    # Auto-generated map based on frequency
    auto_map = dict(zip(most_common_in_cipher, COMMON_LETTERS))

    # Apply manual overrides if provided
    if manual_map:
        auto_map.update(manual_map)

    # Decrypt the ciphertext
    decrypted = ''
    for char in ciphertext.upper():
        if char in auto_map:
            decrypted += auto_map[char]
        else:
            decrypted += char  # keep non-alphabet characters as-is

    return decrypted, auto_map

# Example ciphertext
cipher_text = "GIEWIV GMTLIV HIQS"

# Optional manual corrections
manual_corrections = {
    'G': 'T',
    'I': 'H',
    'E': 'E'
}

decrypted_text, used_map = monoalphabetic_decrypt(cipher_text, manual_corrections)

print("Decrypted text:")
print(decrypted_text)
print("\nUsed map:")
print(used_map)
