from pymongo import MongoClient

def Connect_Mongo(collection_name):
    mongoClient = MongoClient("mongodb://mongodb:27017")    # mongodb 접속
    database = mongoClient["local"]   # database 연결
    collection = database[collection_name]
    return collection         # collection 작업

# 데이터 입력 function
def Data_insert(collection, data):
    # 데이터 입력 전 초기화
    try:
        collection.delete_many({})      # 초기화 중복구문 삭제
    except:
        pass
    # 데이터 입력
    collection.insert_many(data)           # todo list가 여러개이므로 many로 수정

# 사용자 이름 입력 function
def User_name(collection):
    #사용자 이름 입력 후 db 저장
    user_name = input("Input Your Name: ")
    print("")
    result_participants = collection.insert_one({"user_name" : user_name})
    inserted_participants_id = result_participants.inserted_id

    # 사용자 id를 return
    return inserted_participants_id

# 업무 보고 입력 function
def Todos(user_id, collection1, collection2):
    print("ToDo List 중 하나 선택 하세요 !")

    # todos_list 컬렉션의 내용 중 'title'만 print
    result_todo = collection1.find({})           # hint 타이틀만 찾기 콜렉션 제대로 설정
    count = 1
    for i in result_todo:
        print("{}. {}".format(count, i["title"]), end=" ")           # hint 필요없는 {} 삭제
        count+= 1           # hint 순서 표시를 위해 번호를 1씩 더하기
    print("")

    # todo중 하나 입력
    user_input = int(input("Title 번호: "))-1           # hint input을 int로 입력
    # Status 입력
    user_status = input("Status: ")          # hint status를 str으로 입력

    # 사용자가 입력한 번호에 해당하는 title과 그 title id를 찾음
    result_todo_title = collection1.find().skip(user_input).limit(1)
    for j in result_todo_title:
        inserted_todo = j['title']
        inserted_todo_id = j['_id']
        
    # user_id, 사용자가 입력한 title과 그 title id, 사용자가 입력한 status를 collection2에 담기
    collection2.insert_one({"user_id" : user_id, "user_todo_id" : inserted_todo_id, "todo_title" : inserted_todo, "user_status" : user_status})

# 종료 여부 입력 function
def End(collection, collection1, collection2):           # hint 3개의 콜렉션을 가져올 수 있도록 선언
    user_id = User_name(collection)                        # 누락된 내용 추가
    Todos(user_id, collection1, collection2)

    while True:
        print("c, q, x 중 하나를 입력하세요.")              # 프린트 위치 조절
        user_end = input("진행 여부: ")
        # c 입력 시 Todos() 다시 실행
        if user_end == "c":
            print("")
            Todos(user_id, collection1, collection2)
        # q 입력 시 User_name() 실행 후 Todos() 다시 실행
        elif user_end == "q":
            print("")
            print("------------------------")
            user_id = User_name(collection)
            Todos(user_id, collection1, collection2)
        # x 입력 시 프로그램 종료
        elif user_end == 'x': # hint 프로그램 종료 로직 위치 제대로 변경
            break



    print("------------------------")
    print("프로그램이 종료되었습니다.")