# Backend-Server
## 사용된 프레임워크, 설치 및 실행 방법

사용된 Python 프레임워크
```console
FastAPI
Uvicorn
```

프레임워크 설치
```console
pip install fastapi
pip install uvicorn
```

콘솔 내 실행 방법 (일반적인 python으로 실행 불가능)
```console
uvicorn main:app --reload
```

## Commit 또는 REST 규칙 참고 내용
커밋 시 다음과 같이 summary 작성


ex) user 기능 내 오류 수정시 : ```fix: user 업데이트 기능 오류 수정```

ex) 회원가입 기능 추가시 : ```feat: 회원가입 기능 추가```

prefix 관련 참고사항
```
feat : 새로운 기능 추가, 기존의 기능을 요구 사항에 맞추어 수정
fix : 기능에 대한 버그 수정
build : 빌드 관련 수정
chore : 패키지 매니저 수정, 그 외 기타 수정 ex) .gitignore
ci : CI 관련 설정 수정
docs : 문서(주석) 수정
style : 코드 스타일, 포맷팅에 대한 수정
refactor : 기능의 변화가 아닌 코드 리팩터링 ex) 변수 이름 변경
test : 테스트 코드 추가/수정
release : 버전 릴리즈
```
커밋 summary 관련 [출처](https://velog.io/@jiheon/Git-Commit-message-%EA%B7%9C%EC%B9%99)

REST URL Rule에 대한 [참고](https://sanghaklee.tistory.com/57)
