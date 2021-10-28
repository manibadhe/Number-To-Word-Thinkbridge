one = [ "", "One ", "Two ", "Three ", "Four ",
        "Five ", "Six ", "Seven ", "Eight ",
        "Nine ", "Ten ", "Eleven ", "Twelve ",
        "Thirteen ", "Fourteen ", "Fifteen ",
        "Sixteen ", "Seventeen ", "Sighteen ",
        "Sineteen "]

ten = [ "", "", "Twenty ", "Thirty ", "Forty ",
        "Fifty ", "Sixty ", "Seventy ", "Eighty ",
        "Ninety "]

def numToWords(n, s):
    out = ""
    if (n > 19):
        out += ten[int(n) // 10] + one[int(n) % 10]
    else:
        out += one[int(n)]
    if (n):
        out += s
    return out

def convertToWords(n):
    out = ""
    out += numToWords((n // 10000000), "Crore ")
    out += numToWords(((n // 100000) % 100), "Lakh ")
    out += numToWords(((n // 1000) % 100), "Thousand ")
    out += numToWords(((n // 100) % 10), "Hundred ")

    if (n > 100 and n % 100):
        out += "And "

    out += numToWords((n % 100), "")
    num = str(n).split(".")
    if len(num) > 1:
        num = num[-1]
        out += num + "/1" + "0" * len(num) + " "
    return out + "Only"

n = input("Enter Number: ")

print(convertToWords(n))