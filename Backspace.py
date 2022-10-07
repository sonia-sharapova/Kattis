def main():
    string = input()
    tempStr = []
    for char in string:
        if char != '<':
            tempStr.append(char)
        else:
            tempStr.pop()
        
    tempStr = ''.join(tempStr)
    print(tempStr)
    

if __name__ == "__main__":
    main()
