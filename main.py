import sys 

def parse_args(argv):
    files = [] 
    flags = [] 
    for arg in argv: 
        try: 
            f = open(arg)
            f.close()
            files.append(arg)
        except: 
            pass 
    return files, flags 
        
def wc(data): 
    line_count = len(data) 
    word_count = 0 
    byte_count = 0 
    new_data = []  
    for line in data: 
        line = line.replace('\n', '')
        words = line.split(" ")
        words = [i for i in words if i != ""]
        word_count += len(words)
        new_data.append(line) 
    print(line_count)
    print(word_count) 
    print(new_data)
        

if __name__ == "__main__": 
    files, flags = parse_args(sys.argv[1::]) 
    
    for file in files: 
        f = open(file, "r") 
        data = f.readlines() 
        wc(data)
