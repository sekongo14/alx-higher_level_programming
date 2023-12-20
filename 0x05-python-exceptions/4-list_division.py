#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            elem_1 = my_list_1[i] if i < len(my_list_1) else 0
            elem_2 = my_list_2[i] if i < len(my_list_2) else 0

            # Try to perform the division
            division_result = elem_1 / elem_2

            # Handle the case where division_result is not an integer or float
            if not isinstance(division_result, (int, float)):
                raise TypeError("wrong type")

            result.append(division_result)

        except ZeroDivisionError:
            # Handle division by zero
            print("division by 0")
            result.append(0)

        except IndexError:
            # Handle out of range
            print("out of range")
            result.append(0)

        finally:
            # Optional: Any cleanup code that should be executed
            pass

    return result
