import todolist_functions

# ToDo 리스트 생성
todo_list = [
    {"title": "주간 보고서 작성", "description": "팀의 주간 성과와 진행 상황에 대한 보고서를 작성합니다."},
    {"title": "이메일 확인 및 응답", "description": "미처 확인하지 못한 이메일을 확인하고 필요한 이메일에 대해 응답합니다."},
    {"title": "회의 준비", "description": "다가오는 회의에 대해 준비합니다. 주제 연구, 발표 자료 준비 등이 포함될 수 있습니다."},
    {"title": "프로젝트 계획서 수정", "description": "현재 진행 중인 프로젝트의 계획서를 검토하고 필요한 부분을 수정합니다."},
    {"title": "팀 멤버와의 1:1 면담", "description": "팀 멤버와 개별적으로 만나서 그들의 업무 진행 상황, 이슈, 우려사항 등을 논의합니다."},
  ]  # 딕셔너리들의 리스트 선언

# todos_list 컬렉션 생성 후 collection_todos 변수에 담기
collection_todos = todolist_functions.Connect_Mongo("todos_list")          # hint 변수이름 맞춤
# participants 컬렉션 생성 후 collection_participants 변수에 담기
collection_participants = todolist_functions.Connect_Mongo("participants")
# participants_todos 컬렉션 생성 후 collection_participants_todos 변수에 담기
collection_participants_todos = todolist_functions.Connect_Mongo("participants_todos")

# 데이터 입력 function Data_insert()호출
# todos_list 컬렉션에 todo_list 데이터를 입력
todolist_functions.Data_insert(collection_todos, todo_list)         # data insert 호출, 콜렉션 이름 수정

# 종료 여부 입력 function 호출
# user_end = 'q' --> User_name function 호출 --> Todos function 호출 --> 종료 여부 입력 (반복)
todolist_functions.End(collection_participants, collection_todos, collection_participants_todos)
