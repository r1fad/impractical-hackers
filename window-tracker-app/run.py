import os

ACTIVE_WINDOWS_APPLESCRIPT = "callActiveWindowsScript.sh"
PYTHON_MIDDLEWARE = "arduino-gateway.py"

if __name__ == "__main__":
  if (os.path.isfile(ACTIVE_WINDOWS_APPLESCRIPT) and os.path.isfile(PYTHON_MIDDLEWARE)):
    os.system("./{} | python3 {}".format(ACTIVE_WINDOWS_APPLESCRIPT, PYTHON_MIDDLEWARE))