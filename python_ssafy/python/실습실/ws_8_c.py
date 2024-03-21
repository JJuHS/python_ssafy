class BaseModel:
    PK = 1
    TYPE = 'Basic Model'

    def __init__(self, data_type, title, content, created_at, updated_at):
        self.PK = BaseModel.PK
        self.data_type = data_type 
        self.title = title 
        self.content = content 
        self.created_at = created_at 
        self.updated_at = updated_at
        BaseModel.PK += 1
    
    def save(self):
        print('데이터를 저장합니다.')

class Novel(BaseModel):
    def __init__(self, data_type, title, content, created_at, updated_at, author):
        super().__init__(data_type, title, content, created_at, updated_at)
        self.author = author
    
class Other(BaseModel):
    TYPE = 'Other Model'
    def save(self):
        print('데이터를 다른 장소에 저장합니다.')

class ExtendedModel(Novel, Other):
    TYPE = 'extended_type'
    
    def __init__(self, data_type, title, content, created_at, updated_at, author, extended_type):
        super().__init__(data_type, title, content, created_at, updated_at, author,)
        self.extended_type = extended_type
    
    def display_info(self):
        print(self.PK, self.TYPE, self.extended_type)
    
    def save(self):
        print('데이터를 확장해서 저장합니다.')
        
hong = Novel('소설', '홍길동', '고전 소설', 1618, 1692, '허균')
company = Other('회사', '회사명', '회사 설명', 2000, 2023)
extended_instance = ExtendedModel('소설', '춘향전', '고전 소설', 1234, 5678, '작자', '원본')

extended_instance.display_info()
extended_instance.save()
print()
print('###모든객체출력###')

print(hong.author, hong.content, hong.created_at, hong.data_type, hong.PK, hong.title, hong.created_at, hong.updated_at, hong.TYPE)
hong.save()
print()

print(company.content, company.created_at, company.data_type, company.PK, company.title, company.created_at, company.updated_at, company.TYPE)
company.save()
print()

print(extended_instance.author, extended_instance.extended_type, extended_instance.content, extended_instance.created_at, extended_instance.data_type, extended_instance.PK, extended_instance.title, extended_instance.created_at, extended_instance.updated_at, extended_instance.TYPE)
extended_instance.display_info()
extended_instance.save()