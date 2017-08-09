def scores_to_rating(score_1, score_2, score_3, score_4, score_5):
    
    def convert_to_number(score):
        #Convert score to number
        converted_score = float(score)
        return converted_score
    
    def sum_of_middle_three(score_1, score_2, score_3, score_4, score_5):
        #Find the sum and average of the middle 3 numbers
        max_score = max(score_1,score_2,score_3,score_4,score_5)
        min_score = min(score_1,score_2,score_3,score_4,score_5)
        result_sum = score_1 + score_2 + score_3 + score_4 + score_5 - max_score - min_score
        return result_sum
    
    def score_to_rating(average_score):
        #Convert the average score into a string rating
        if average_score < 1:
            rating = "Terrible"
        elif average_score < 2:
            rating = "Bad"
        elif average_score < 3:
            rating = "OK"
        elif average_score < 4:
            rating = "Good"
        else:
            rating = "Excellent"
            
        return rating
    
    #Turn 5 inputted scores into floats and integers
    score_1 = convert_to_number(score_1)
    score_2 = convert_to_number(score_2)
    score_3 = convert_to_number(score_3)
    score_4 = convert_to_number(score_4)
    score_5 = convert_to_number(score_5)
    
    #Find 3 middle scores
    #Find the average of the three scores
    average_score =  sum_of_middle_three(score_1,score_2,score_3,score_4,score_5)/3
    
    #Convert to appropiate text
    rating = score_to_rating(average_score)
    
    return rating

print(scores_to_rating(1, 2, 3, 4, 5))
