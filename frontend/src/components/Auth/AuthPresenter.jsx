import React from "react";
import styled from "styled-components";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faUser, faKey } from "@fortawesome/free-solid-svg-icons";

const Wrapper = styled.div``;
const Title = styled.div`
  text-align: center;
  font-size: 35px;
  margin-bottom: 40px;
  font-weight: bold;
`;

const InputContainer = styled.div`
  display: flex;
  border-bottom: 2px solid;
  line-height: 45px;
  color: black;
  margin-bottom: 20px;

  &:hover {
    border-bottom: 2px solid #57c55e;
  }
`;

const Label = styled.label`
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
`;

const Icon = styled(FontAwesomeIcon)`
  font-size: 25px;
`;

const Input = styled.input`
  width: 100%;
  font-size: 17px;
  border: none;
  outline: none;
`;

const Submit = styled.input`
  width: 100%;
  height: 50px;
  border: none;
  outline: none;
  border-radius: 6px;
  margin-bottom: 20px;
  font-size: 17px;
  color: white;
  background: #57c55e;
  cursor: pointer;
  transition: 0.3s;

  &:hover {
    background: #439448;
  }
`;

const SignUpContainer = styled.div`
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-top: 1px solid #e4e4e5;
  padding: 20px 0px;
`;

const SignText = styled.div`
  font-size: 16px;
  letter-spacing: -0.5px;
`;

const AuthPresenter = () => {
  return (
    <Wrapper>
      <Title>로그인</Title>

      <form action="#" method="post">
        <InputContainer>
          <Label htmlFor="id">
            <Icon icon={faUser} />
          </Label>
          <Input type="text" name="user" id="id" placeholder="아이디" />
        </InputContainer>
        <InputContainer>
          <Label htmlFor="pwd">
            <Icon icon={faKey} />
          </Label>
          <Input type="password" name="pwd" id="pwd" placeholder="비밀번호" />
        </InputContainer>
        <Submit type="submit" value="로그인" />
      </form>

      <SignUpContainer>
        <SignText>아직 빌리지 가족원이 아니신가요?</SignText>
        <div>회원가입</div>
      </SignUpContainer>
    </Wrapper>
  );
};

export default AuthPresenter;
