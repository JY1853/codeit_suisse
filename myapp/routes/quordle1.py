test_answers = ["VVIDH", "MZLPS", "BPCYN", "XYGGM"]
test_attempts = ["JKGJB", "ZGRUJ", "XYGGM", "BPCYN", "MHXGE", "DZENT", "ZXWQW", "VVIDH", "MZLPS"]

def letters_in_list(list_of_strings):
    # takes list of strings
    # returns list of the characters in the strings
    holder = []
    for thing in list_of_strings:
        holder.append(list(thing))
    letters_in_answers = set([char for item in holder for char in item])
    return letters_in_answers

def quordle(ans_list, attempt_list):
    answers = ans_list
    letters_in_ans = sorted(letters_in_list(answers))
    print(letters_in_ans)
    all_letters_guessed = sorted(letters_in_list(attempt_list))
    answer_dict = dict.fromkeys(all_letters_guessed, 0)

    for guess in attempt_list:
        unique_chars = set([guess[chr] for chr in range(0, len(guess))])
        print(unique_chars)
        if guess in answers:
            answers.remove(guess)
            letters_in_ans = sorted(letters_in_list(answers))
            # updates the letters

            for chr in unique_chars:
                if chr not in letters_in_ans and answer_dict[chr] == 0:
                    answer_dict[chr] += 1
        else:
            for chr in unique_chars:
                if chr not in letters_in_ans and answer_dict[chr] == 0:
                    answer_dict[chr] += 1
        for key in answer_dict:
            if answer_dict[key] > 0:
                answer_dict[key] += 1
    
    for key in answer_dict:
        answer_dict[key] -= 1
    # i added 1 to everything somehow above, so this fixes it lol

    answer_string = ''.join(str(item) for item in answer_dict.values())
    print(answer_string)

quordle(test_answers, test_attempts)
