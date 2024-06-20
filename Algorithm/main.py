import Taha
def main(skill):

    # Assumptions
    salary = 50000  # Salary of a single developer
    productivityNew = 50  # LOC (Lines Of Code) written by a new programmer
    productivityExperienced = 80  # LOC (Lines Of Code) written by an experienced programmer
    productivityProfessional = 100  # LOC (Lines Of Code) written by a professional programmer

    productivity = 0
    if skill == "New":
        productivity = productivityNew
    elif skill == "Experienced":
        productivity = productivityExperienced
    elif skill == "Professional":
        productivity = productivityProfessional
    else:
        print("incorrect skill value")