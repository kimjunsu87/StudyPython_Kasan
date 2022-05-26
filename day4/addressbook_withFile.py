'''
주소록 프로그램 v1.1
작성일 2022-05-26 14:14
작성자 soop
설명 파일DB를 사용한 주소록 프로그램
''' 
import os # 운영체제 명령용 모듈
# 주소록 클래스
class Contact :
    name = ''; phone_number = ''; e_mail = ''; addr = ''

    # 생성자(constructor) 
    def __init__(self, name, phone_number, e_mail, addr) -> None:
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr
    
    def __str__(self) -> str:
        res_str = f'이름 : {self.name}\n' \
        f'폰번호 : {self.phone_number}\n' \
        f'이메일 : {self.e_mail}\n' \
        f'주소 : {self.addr}\n' \
        '====================================='
        return res_str
    
    def isNameExist(self, name) -> bool:
        if self.name == name :
            return True
        else :
            return False

# 화면 클리어 함수
def clearConsole() :
    command = 'clear' # UNIX, LINUX, MACOS
    if os.name in ('nt', 'dos') :
        command = 'cls'
    os.system(command)

# 사용자 정보 입력
def getContact() :
    member = None # 로컬변수 초기화
    try :
        (name, phone_number, e_mail, addr) = input('정보입력(이름, 폰번호, 이메일, 주소)[구분자 : /] > ').split('/')
        member = Contact(name, phone_number, e_mail, addr)
        # print(name, phone_number, e_mail, addr)
    except Exception as ex :
        # print(f'예외발생 : {ex}')
        print('정확한게 이름/폰번호/이메일/주소 순으로 입력해주세요.')

    return member

# 연락처 리스트 출력
def printContacts(contacts) :
    for item in contacts : # 리스트 원소 (Contact 객체)
        print(item)
             
# 연락처 삭제 함수
def delContact(contacts, name) :
    for i, item in enumerate(contacts) :
        if item.isNameExist(name) == True :
            del contacts[i]

# 연락처 수정 함수
def editContact(contacts, name):
    contact = None  # 수정할 연락처 담을 변수
    index = -1 # 찾은 리스트 인덱스
    isFind = False
    
    for i, item in enumerate(contacts):
        isfind = True
        contact = item
        index = i
        break
    if isFind == False:
        print('검색 정보가 없습니다!')
    else:
        #pass # Contact 객체를 보여주고 값을 수정할 입력받기
        print(f'{contact.name}/{contact.phone_number}/{contact.e_mail}/{contact.addr}')
        
        # 수정할 폰번호 / 이메일/ 주소 입력
        (phone_number, e_mail, addr) = \
            input('정보입력(폰번호,이메일,주소)[구분자:/'] > ').split('/')
        member = Contact(contact.name, phone_number, e_mail, addr)

        contacts()[index] = member  # 이전값을 새 연락처로 변경


# 메뉴 출력
def getMenu() :
    str_menu = ('주소록 프로그램 v1.0\n'
                '1. 연락처 추가\n'
                '2. 연락처 출력\n'
                '3. 연락처 삭제\n'
                '4. 프로그램 종료\n'
                '5. 연락처 수정\n')
    print(str_menu)
    menu = input('메뉴 선택 > ')
    try :
        menu = int(menu)
    except :
        menu = 0
    return menu

# 파일 저장함수
def saveContacts(contacts) :
    dir_name = 'C:/Repository/StudyPython_Kasan/day4/'
    f = open(f'{dir_name}contacts.txt', mode = 'w', encoding = 'UTF-8')
    for item in contacts :
        f.write(f'{item.name}/{item.phone_number}/{item.e_mail}/{item.addr}\n')
    f.close()
def run() :
    contacts = [] # 빈 리스트 변수 초기화
    clearConsole()
    while True :
        sel_menu = getMenu()
        if sel_menu == 1 : # 연락처 추가
            clearConsole()
            member = getContact()
            if member != None :
                contacts.append(member)  # 연락처 리스트에 새 연락처 추가
            input('계속하려면 아무키나 누르세요. > ')
            clearConsole()
        elif sel_menu == 2 : # 연락처 출력
            clearConsole()
            print('=====================================')
            printContacts(contacts)
            print(f'총 {len(contacts)} 건 입니다.')
            print('=====================================')  
            input('계속하려면 아무키나 누르세요. > ')
            clearConsole()
        elif sel_menu == 3 :
            clearConsole()
            name = input('삭제할 이름 입력 > ')
            delContact(contacts,name)
            input('계속하려면 아무키나 누르세요. > ')
            clearConsole()
        elif sel_menu == 4 : # 프로그램 종료
            saveContacts(contacts) # 파일DB에 저장
            break
        elif sel_menu == 5 :  # 연락처 수정


        else :
            clearConsole()

if __name__ == '__main__' : #EntryPoint (프로그램 시작점)
    print('프로그램 시작') ## 프로그램이 시작됨
    try :
        run()
    except KeyboardInterrupt as ex :
        print('비정상 종료!')