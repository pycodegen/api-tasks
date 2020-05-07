일단 대략적으로만 설명드릴께요~
(** 자세한건 제가 직접 설명드릴께요ㅠ 아래 설명이 좀 많이 

현재 작업중인 레포는 여기 뒀어요~
https://github.com/pycodegen/api-tasks/tree/temp-wip-ts
(아직 ㄹㅇ 프로토타입 단계긴 해요ㅠ)

하려는게 이렇게 되요~ 

```
@task_definitions.add( options )
async def sleep_blocks_task(
  api_context: APIContext[
    NumberProgress,
    Union[
      RemoteFile[Literal['upload_file_a']],
      RemoteFile[Literal['upload_file_b']],
  ],
  count: int,
  length: int,
):
  ...
  api_context.progress.send(1)  # send progress

  remote_file_a = await api_context  # receive upload file
    .remote_files
    .upload_file_a
    .recv()
  # do other things
  
```





['task' 함수를 정의하고 decorator 달아주면 ]
 -> Typescript api-client code 튀어나오게  (generate_ts_api 폴더)
server-side 에서 등록된 task 부르면 (client 입장에선 some_task_func( args ) 
       task 실행하게 ( <-- 현재는 socketio 로 주어진걸 threadpool로 실행하지만 오늘 추가된 요구사항엔 task-queue 써야 됩니다)
3. progress, file-upload 가능하게
이건 task_func 형태에 'context' 를 줘서 할 생각입니다 

```python
def some_task_func(
api_context: APIContext[
     NumberProgress, # progress type
     RemoteFile,  # multiple remote file 은 생각좀 해야됩니다...
  ],  
  arg1: int, 
  arg2: float, ... 
):
```