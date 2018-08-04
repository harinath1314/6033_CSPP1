'''
This program will replace all the special characters(!, @, #, $, %, ^, &, *)
in a given string with a space.
example : if ab!@#cd is the input,
the output is ab   cd.
input  has three special characters, which are to be replaced with spaces in putput.
'''
def main():
    '''
    Read string from the input, store it given_str.
    '''
    given_str = input()
    answer = ""
    for i in given_str:
        if i == '!' or i == '%' or i == '@' or i == '$' or i == '#' or i == '^' or i == '&' or i == '*':
            # lu÷÷ck[i] = answer
            answer = answer+" "
        else:
            answer = answer + i
    print(answer)

if __name__ == "__main__":
    main()
