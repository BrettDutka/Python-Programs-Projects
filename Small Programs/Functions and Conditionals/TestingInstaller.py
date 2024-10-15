import sys, importlib
def installationIssue(moduleName):
    try:
        module = importlib.import_module(moduleName)
        print(moduleName + " is installed, Version: " + str(module.__version__))
        print("'import {}' is able to run at the top of your code".format(moduleName))
    except:
        print("\tModule {} is not installed".format(moduleName))
        if sys.platform == "win32" or sys.platform == "cygwin":
            print("\tRun command:")
            print("\t\tpy -m pip install {}".format(moduleName))
        elif sys.platform == "darwin" and sys.platform == "linux":
            print("\tRun command:")
            print("\t\tpython3 -m pip install {}".format(moduleName))
            print("\t\t\t or use the one below if you are having issues with the top command")
            print("\t\t{} -m pip install {}".format(sys.executable.replace("\\", "/"), moduleName))
if __name__ == '__main__':
    print("Checking Installation of numpy and matplotlib")
    print()
    installationIssue("numpy")
    print()
    print()
    installationIssue("matplotlib")
