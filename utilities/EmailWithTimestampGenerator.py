from datetime import datetime


def get_new_email_with_timestamp():
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H%M%S")
    invalid_email = "test" + time_stamp + "@outlook.com"
    return invalid_email