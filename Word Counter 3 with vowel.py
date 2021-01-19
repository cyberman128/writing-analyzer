#enter text file path
f = open("/home/stephen/cyberman_git_hub/writing-analyzer/my_file.txt")

character_count_modifier = 3600
num_pages = input("Enter a number of pages:")

number_of_characters_selected = character_count_modifier * int(num_pages)
file_output = f.readlines(number_of_characters_selected)
raw_output_string = " ".join(file_output)
word_list = raw_output_string.split()

lowercase_word_list = []
filtered_lowercase_word_list = []
count_ready_list = []
word_dict_with_counts = {}

exceptions = ["simply", "family"]
fillers_to_remove = ["a", "and", "as", "at", "are", "for", "have", "has", "he", "her", "his",
                     "i", "if", "in", "is", "it", "its", "my", "mine", "no", "not",
                     "of", "she", "that", "this", "the", "them", "then", "than", "to", "was", "we", "with", "you"]

for a in word_list:
    lowercase_word_list.append(a.lower())

for b in lowercase_word_list:
    if b not in fillers_to_remove:
        filtered_lowercase_word_list.append(b)

for c in filtered_lowercase_word_list:
    if c in exceptions:
        if c not in word_dict_with_counts:
            word_dict_with_counts[c] = 1
        else: word_dict_with_counts[c] = 1
        
    elif c[-2:] == "ed" and c[-4] in ["a", "e", "i", "o", "u"] and len(c) > 3 and c[:-1] not in word_dict_with_counts:
        word_dict_with_counts[(c[:-1])] = 1
        
    elif c[-2:] == "ed" and c[-4] in ["a", "e", "i", "o", "u"] and len(c) > 3 and c[:-1] in word_dict_with_counts:
        word_dict_with_counts[(c[:-1])] += 1   
        
    elif c[-2:] == "ed" and c[:-2] not in word_dict_with_counts and len(c) > 3:
        word_dict_with_counts[(c[:-2] )] = 1
        
    elif c[-2:] == "ed" and c[:-2] in word_dict_with_counts and len(c) > 3:
        word_dict_with_counts[(c[:-2])] += 1
    
    
    
    elif c[-2:] == "ly" and c[:-2] not in word_dict_with_counts and len(c) > 3:
        word_dict_with_counts[(c[:-2])] = 1
        
    elif c[-2:] == "ly" and c[:-2] in word_dict_with_counts and len(c) > 3:
        word_dict_with_counts[(c[:-2])] += 1
        
        
         
    elif c[-3:] == "ing" and c[-5] in ["a", "e", "i", "o", "u"] and len(c) > 4 and (c[:-3] + "e") not in word_dict_with_counts:
        word_dict_with_counts[(c[:-3] + "e")] = 1
        
    elif c[-3:] == "ing" and c[-5] in ["a", "e", "i", "o", "u"] and len(c) > 4 and (c[:-3] + "e") in word_dict_with_counts:
        word_dict_with_counts[(c[:-3]) + "e"] += 1
        
    elif c[-3:] == "ing" and len(c) > 4 and c[:-3] not in word_dict_with_counts:
        word_dict_with_counts[(c[:-3])] = 1
    
    elif c[-3:] == "ing" and len(c) > 4 and c[:-3] in word_dict_with_counts:
        word_dict_with_counts[(c[:-3])] += 1
        
        
        
    elif c in word_dict_with_counts:
        word_dict_with_counts[c] += 1
        
    else:
        word_dict_with_counts[c] = 1



result = list(word_dict_with_counts.items())
result.sort(key=lambda x: x[1])
result.reverse()
print(result)