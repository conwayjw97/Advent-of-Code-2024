def parse_input():
    ordering_rules = {}
    update_pages = []
    with open('day_5_in.txt') as f:
        for line in f:
            line = line.strip()
            if '|' in line:
                [previous_page, following_page] = line.split('|')
                if previous_page in ordering_rules:
                    ordering_rules[previous_page].append(following_page)
                else:
                    ordering_rules[previous_page] = [following_page]
            elif ',' in line:
                update_pages.append(line.split(','))
    return ordering_rules, update_pages

def are_following_pages_valid(ordering_rules, update, i, page):
    print("Checking pages for " + str(update))
    for j in range(i+1, len(update)):
        page_to_check = update[j]
        if page_to_check in ordering_rules and page in ordering_rules[page_to_check]:
            print("Invalid because page " + page_to_check + " is specified to come before the page " + page + " in ordering rules for page " + page_to_check + ": " + str(ordering_rules[page_to_check]))
            return False
    return True

def are_all_pages_valid(ordering_rules, update):
    for i, page in enumerate(update):
        update_valid = are_following_pages_valid(ordering_rules, update, i, page)
        if not update_valid:
            return False
    return True

def check_update_validity(ordering_rules, update_pages):
    valid_update_pages = []
    invalid_update_pages = []
    for update in update_pages:
        if are_all_pages_valid(ordering_rules, update):
            valid_update_pages.append(update)
        else:
            invalid_update_pages.append(update)
    return valid_update_pages, invalid_update_pages

def sum_middle_page_nums(valid_update_pages):
    middle_page_num_sum = 0
    for update in valid_update_pages:
        middleIndex = int((len(update) - 1)/2)
        middle_page_num_sum += int(update[middleIndex])
    return middle_page_num_sum

def correct_invalid_updates(invalid_update_pages):
    corrected_invalid_updates = []
    for update in invalid_update_pages:
        while True:
            if not update_needs_correcting(update):
                break
        corrected_invalid_updates.append(update)
    return corrected_invalid_updates

def update_needs_correcting(update):
    for i, page in enumerate(update):
        for j in range(i+1, len(update)):
            page_to_check = update[j]
            if page_to_check in ordering_rules and page in ordering_rules[page_to_check]:
                print("Invalid because page " + page_to_check + " is specified to come before the page " + page + " in ordering rules for page " + page_to_check + ": " + str(ordering_rules[page_to_check]))
                print("Moving invalid page number " + page_to_check + " from " + str(j) + " to " + str(i))
                update.insert(i, update.pop(j))
                return True 
    return False


if __name__ == '__main__':
    [ordering_rules, update_pages] = parse_input()
    [valid_update_pages, invalid_update_pages] = check_update_validity(ordering_rules, update_pages)
    print("Sum of all valid update middle page numbers: " + str(sum_middle_page_nums(valid_update_pages)))
    corrected_invalid_updates = correct_invalid_updates(invalid_update_pages)
    print("Sum of all corrected update middle page numbers: " + str(sum_middle_page_nums(corrected_invalid_updates)))
