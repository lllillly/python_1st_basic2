class Util:
    def custom_input():
        answer = input(">> ")

        if len(answer) > 1:
            # answer의 길이가 1보다 크다면
            return False
        elif len(answer) == 0:
            # answer의 길이가 0이라면
            return False
        else:
            ascii_value = ord(answer)

            if ascii_value >= 48 and ascii_value <= 57:
                return int(answer)
            else:
                return False
