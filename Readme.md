<h1 align="center">Welcome to YouRoomMyRoom 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-0.1.0-blue.svg?cacheSeconds=2592000" />
</p>

> 유룸마룸은 자취방 양도 서비스 플랫폼입니다.

## DB 상세 모델 (추가될 예정)

### 1. 사용자 (Users)

> 사용자를 나타내는 모델입니다.

- 이름
- 이메일
- 비밀번호
- 비밀번호 확인
- 휴대폰번호
- 첫거래유무
- 신용도

### 2. 거래게시판 (Trade)

> 자취방 양도 게시판을 나타내는 모델입니다.
>
> 자취방을 양도할 사용자가 작성할 수 있도록 할 예정입니다.

- 건물이름
- 주소
- 월세/전세
- 가격
- 층/건물층수
- 면적
- 양도기간
- 상세설명
- 사진(여러장)
- 찜기능

### 3. 방옵션 (RoomOption)

> 양도할 자취방의 옵션의 유무를 나타내는 모델입니다.
>
> True/False 형식으로 구현할 예정이며 각 이름에 맞는 아이콘을 매칭시킬 예정입니다.

- 가스레인지
- 냉장고
- 세탁기
- 책상
- 침대
- 에어컨
- 인터넷
- 옷장
- 신발장
- etc...

### 4. 자유게시판 (Board)

> 자취방을 양도할 때 필요한 정보 또는 사기방지 정보 게시판입니다.

- 작성자(외래키 - 사용자)
- 글 제목
- 글 내용
- 작성된날짜
- 수정된날짜
- 조회수

### 5. 공지사항 (Notice)

> 공지사항 게시판입니다.

### 6. 좋아요 (Likes)

> 자유게시판에 좋아요를 표현할 수 있는 기능입니다.

- 사용자(외래키 - 사용자)
- 게시글(외래키 - 자유게시판)

### 7. 댓글 (Comments)

> 자유게시판 해당글에 댓글을 다는 기능입니다.

- 사용자(외래키 - 사용자)
- 댓글내용(외래키 - 자유게시판)

## 구현 예정인 기능

- [ ] 로그인/로그아웃

- [ ] 거래게시판

- [ ] 자유게시판

- [ ] 알림

- [ ] 신용도

- [ ] 방옵션

- [ ] 공지사항

- [ ] 필터기능

## 구현 완료된 기능

## 개발자

👤 **한성민**

- Github: [@zhsks528](https://github.com/zhsks528)

👤 **이창우**

- Github: [@cwadven](https://github.com/cwadven)

👤 **이승준**

- Github: [@KINOTZ](https://github.com/sneak7581)

## Show your support

Give a ⭐️ if this project helped you!

---

_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
