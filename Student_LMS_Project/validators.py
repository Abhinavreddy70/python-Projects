# User-defined Exception
class ValidationError(Exception):
    pass

def validate_student_id(s_id, existing_ids):
    if not s_id.isalnum():
        raise ValidationError("Student ID must be alphanumeric!")
    if s_id in existing_ids:
        raise ValidationError("Student ID already exists!")
    return True

def validate_score(score):
    if not (0 <= score <= 100):
        raise ValidationError("Score must be between 0 and 100.")
    return True