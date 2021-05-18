from collections import Counter
def first_non_repeating_letter(string):
    cnt = Counter(string.lower())
    for letter in string:
        if cnt[letter.lower()] == 1:
            return letter
    return ''

test.describe('Basic Tests')
test.it('should handle simple tests')
test.assert_equals(first_non_repeating_letter('a'), 'a')
test.assert_equals(first_non_repeating_letter('stress'), 't')
test.assert_equals(first_non_repeating_letter('moonmen'), 'e')

test.it('should handle empty strings')
test.assert_equals(first_non_repeating_letter(''), '')

test.it('should handle all repeating strings')
test.assert_equals(first_non_repeating_letter('abba'), '')
test.assert_equals(first_non_repeating_letter('aa'), '')

test.it('should handle odd characters')
test.assert_equals(first_non_repeating_letter('~><#~><'), '#')
test.assert_equals(first_non_repeating_letter('hello world, eh?'), 'w')

test.it('should handle letter cases')
test.assert_equals(first_non_repeating_letter('sTreSS'), 'T')
test.assert_equals(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'), ',')