# No module named pandas 
pip3 install --upgrade pandas



# python version management
python -V -> Default python version (maybe 2.x)
python3 -V -> 3.xx

So, you need to set 3.xx as a default 

vi ~/.zshrc 에서,

alias python="python3"
# Setting PATH for pythin 3.8
# The original version is saved in .bash_profile.pysave
PATH="/Library/Frameworks/Python.framework/Version/3.8.9/bin:${PATH}" export PATH
python --version 으로 확인한다.
출처: https://sora9z.tistory.com/5 [9Jaeng's 삽질 blog]


