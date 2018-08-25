from math import log


class FileService():
    @staticmethod
    def calculate_formatted_size(num):
        """Human friendly file size"""
        unit_list = zip(['bytes', 'kB', 'MB', 'GB', 'TB', 'PB'], [
                        0, 0, 1, 2, 2, 2])
        if num > 1:
            exponent = min(int(log(num, 1024)), len(unit_list) - 1)
            quotient = float(num) / 1024**exponent
            unit, num_decimals = unit_list[exponent]
            format_string = '{:.%sf} {}' % (num_decimals)
            return format_string.format(quotient, unit)
        if num == 0:
            return '0 bytes'
        if num == 1:
            return '1 byte'
