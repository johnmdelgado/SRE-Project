# SRE-Project

# Project Background
Project description from: https://gist.github.com/aminasian-ihr/10c2fb997fa84fb5760784d11fc309b3

[NIST](https://www.nist.gov/) recently updates their [Digital Identity Guidelines](https://pages.nist.gov/800-63-3/) in June 2017.
The new guidelines specify general rules for handling the security of user supplied passwords.
Previously passwords were suggested to have certain composition rules (special characters, numbers, etc), hints and expiration times.
Those have gone out the window and the new suggestions are as follows:
Passwords MUST
1. Have an 8 character minimum 
2. AT LEAST 64 character maximum
2. Allow all ASCII characters and spaces (unicode optional)
4. Not be a common password

# Project
We'd like you to build a program to detect if a password meets these requirements. Use a 64 character maximum and allow only ASCII characters.
As for checking if the password is common, the program should take a file of newline delimited common passwords and efficiently check if a password is in that file. Of course leverage appropriate data structures, but try to be efficient in your resource usage.
Use this [Common Password List](https://github.com/danielmiessler/SecLists/raw/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt) to develop with, but the program should be able to be supplied with any newline delimited file.
The program should accept passwords from STDIN in newline delimited format and print invalid passwords to the command line.
An example usage would look like the following: (asterixes used to print unprintable chars)
```
cat input_passwords.txt | ./password_validator weak_password_list.txt
mom -> Error: Too Short
password1 -> Error: Too Common
*** -> Error: Invalid Charaters
```
Feel free to use any language, libraries or tools, with a preference towards Python and Go. Treat this project as if it was an open source utility that you were going to distribute. Things like writing tests, a README with what it does, how to use it and how to build it locally.

# Getting Started
This will provide instuctions on how to get this up and running locally. 

Personal setup: Linux subsystem for windows running Debian  
PRETTY_NAME="Debian GNU/Linux 10 (buster)"  
NAME="Debian GNU/Linux"  
VERSION_ID="10"  
VERSION="10 (buster)"  
VERSION_CODENAME=buster  
ID=debian  
HOME_URL="https://www.debian.org/"  
SUPPORT_URL="https://www.debian.org/support"  
BUG_REPORT_URL="https://bugs.debian.org/"  

## Built with
[Python 3.7.3](https://www.python.org/downloads/release/python-373/)

## Prerequisites
### Python Version 3.7.3
    sudo apt-get update
    sudo apt-get install python3.7.3

### Python yaml package
    sudo apt-get install python-yaml
    sudo yum install python-yaml

## Installation
1. clone repo from: https://github.com/johnmdelgado/SRE-Project

## Configuration
Under the configs folder is the config.yaml file with configuration settings. These are the default values but can be updated as needed or as requirements change.  

**Notes**  
* If requirements change and you want to allow unicode characters you can flip the ascii check or if you want to exclude different characters using regex the ascii_only flag can be set to True and the regex in the config can be modified

        password_defaults:
            min_pw_length: 8
            max_pw_length: 64
            ascii_only: true
            password_regex: '^[ -~]+$'
            excluded_pw_filepath: "./data/common_passwords.txt"

        output_settings:
            output_valid_passwords: false

        debugging:
            debug: false
            test_debug: false

        testing:
            sample_txt_file: "../test_file.txt"
            sample_excluded_pw_filepath: "../data/common_passwords.txt"

## Example Usage
**Notes**
* In the repo there is a test_file.txt that you can use and or modify, but you can pass any values using cat from the commandline.  
* You can also use a custom txt file containing passwords that are common or want to be exempted. Included in this package under the data folder is a common_passwords.txt that will be used by default if there isn't a txt file specifed.  
    
        cat test_file.txt | python3 ./password_validator.py

* If you do supply your own exemption file it can be used by  

        cat test_file.txt | python3 ./password_validator.py "<Your Directory Here>"

* you can also run without sending a file and prompt for input. Newline delimited as well. When you are finished entering values press ctrl+D to finish your input

        python3 ./password_validator.py

## Testing 
To use the unit tests for the scripts supplied with this function. Navigate to the tests folder and enter the follwing command  

        python3 -m unittest

This will execute all unit tests for each of the supplied scripts. If you want additional output from the test results be sure to enable the test_debug config value in the config.yaml file

## Contributing 

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## References/Tools
* https://gist.github.com/aminasian-ihr/10c2fb997fa84fb5760784d11fc309b3
* https://regex101.com/


## License  

Distributed under the MIT License. See `LICENSE` for more information.





