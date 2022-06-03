def is_vowel(string):
  return len(string) == 1 and string.lower() in 'aeiou'

#
def calculate_tip(tip_percentage, bill):
  amount_to_tip = bill * tip_percentage
  return amount_to_tip

#
def get_letter_grade(grade):
    if type(grade) == int or type(grade) == float:
        if grade >=90:
            return 'A'
        elif grade >= 80:
            return 'B'
        elif grade >= 70:
            return 'C'
        elif grade >= 60:
            return 'D'
        else:
            return 'F'
    else:
        return " Grade must be a number"
