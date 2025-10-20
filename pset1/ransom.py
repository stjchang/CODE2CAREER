# Problem 2:
# You are writing a ransom note using letters from a magazine cut out,
# return True if you can construct the ransom note from the magazine. Otherwise, return false.

from collections import Counter

def ransom(ransom_note, magazine) -> bool:
    # more letters needed than you have
    if len(ransom_note) > len(magazine): return False
    
    letterCount = Counter(magazine.replace(" ", ""))
                
    for c in ransom_note.replace(" ", ""):
        if letterCount[c] == 0:
            return False
        
        letterCount[c] -= 1
        
    return True

print(ransom("abcdef", "a b c d e f"))
    



