from sys import argv, getwindowsversion, copyright, version, exit

print("명령 매개변수:", argv)
print("windows 버전:", getwindowsversion())
print("copyright: ", copyright)
print("버전:", version)

# `python 파일 값1 값2` 같은 형식으로 터미널에 입력하면 매개변수 출력됨
# ex. python module_sys.py hi hello
# --> 명령 매개변수: ['module_sys.py', 'hi', 'hello']