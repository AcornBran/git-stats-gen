import os

def checkGitOrNot(path):
    jpgCount = 0
    list_of_dirs = os.listdir(path)
    print(list_of_dirs)
    if ('.git' not in list_of_dirs) and (len(list_of_dirs) > 0):
        for entry in list_of_dirs:
            if (os.path.isdir(os.path.join(path,entry)) == True):
                newPath = path+entry+'\\'
                #print("Here")
                checkGitOrNot(newPath)
    else:
        return True 

def main():
    if(checkGitOrNot("E:\\AOE\\") == True):
        print ("It is GIT")
    else:
        print ("Not GIT")

if __name__ == '__main__':
    main()
