Students表

| id   | 姓名 | 性别 | 年龄|学号     | 密码     | 手机号 | 头像?    | 邮箱? | 创建时间    | 班级    | 状态(是否在读) |
| ---- | ---- | ---- |---| -------- | -------- | ------ | -------- | ----- | ----------- | ------- | -------------- |
| id   | name | sex  |age| username | password | mobile | portrait | email | create_time | classes | status         |
             
成绩表 Grade

| id   | 分数 | 试卷id(关联) | 
| ---- | ---- | ---- | 
| id   | source | id  |


试卷表 TestPaper

| id   | 提交时间 | 答题内容 | 是否被阅卷     | 学生id     | 题库id | 老师id(阅卷人)?    |
| ---- | ---- | ---- | -------- | -------- | ------ | -------- |
| id   | commit_time | answer  | is_check | students | test_bank | Teachers |


题库表 TestBank

| id   | 日期 | 题库类型?（题库名称） | 老师id |
| ---- | ---- | ---- |  ---- | 
| id   | date_time | title  |Teachers |           

试题表(出题) Subject

| id   | 题型 | 内容 | 题库id | 老师id |
| ---- | ---- | ---- |  ---- | ---- |
| id   | subject | question| teat_bank |Teachers |    

```python
subject_type = (
        (0, '单选题'),
        (1, '判断题'),
        (2, '简答题')
    )
```
签到情况表 SignDetail

|id| 当天日期   | 签到人数 | 未签到人数 | 
|---| ---- | ---- | ---- | 
|id| date_time   | sign_number | no_sign_number  |

签到表 Sign

| id   | 签到是否 | 是否迟到 | 签到时间 | 学生id|
| ---- | ---- | ---- |  ---- | ---|
| id   | is_sign | is_late  |sign_time |Students |  


Teachers表

| id   | 姓名 | 性别 | 工号     | 密码     | 手机号 | 头像?    | 邮箱? | 创建时间    | 状态(是否在读) |
| ---- | ---- | ---- | -------- | -------- | ------ | -------- | ----- | ------- | -------------- |
| id   | name | sex  | username | password | mobile | portrait | email | create_time |  status         |
        
Admins表

| id   | 姓名 | 性别 |工号     | 密码     | 手机号 | 头像?    | 邮箱? | 创建时间       | 状态(是否在读) |
| ---- | ---- | ---- | -------- | -------- | ------ | -------- | ----- | -----------  | -------------- |
| id   | name | sex  | username | password | mobile | portrait | email | create_time  | status         |
        

角色表

| 角色名称 |    角色id|
| ---- | ---- |
| 学生    |       1|
| 教师    |       2|
| admin   |      3|