import React from "react";
import { Link } from "react-router-dom";
import styled from "styled-components";
import Modal from "components/Modal";
import Auth from "components/Auth";

const Wrapper = styled.div`
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: calc(100% - 40px);
  height: 70px;
  padding: 0px 20px;
  background: white;
`;

const LogoContainer = styled.div`
  display: flex;
  min-width: 250px;
  align-items: center;
`;

const Logo = styled(Link)`
  color: #57c55e;
  font-size: 25px;
  font-weight: bold;
  margin-right: 15px;
  text-decoration: none;
`;

const Service = styled.span`
  font-size: 14px;
  letter-spacing: -0.5px;
  color: rgb(136, 136, 136);
  padding-top: 4px;
`;

const NavContainer = styled.ul`
  display: flex;
  align-items: flex-end;
  list-style: none;
  font-size: 20px;
  margin: 0;
`;

const ListItem = styled.li`
  margin-left: 35px;
`;

const LinkItem = styled(Link)`
  font-size: 16px;
  text-decoration: none;
  color: ${props => (props.current ? "#57c55e" : "#6b6b6b")};
  font-weight: ${props => (props.current ? "bold" : "100")};

  &:hover {
    color: #57c55e;
  }
`;

const Login = styled.div`
  font-size: 16px;
  color: #6b6b6b;
  cursor: pointer;

  &:hover {
    color: #57c55e;
  }
`;

const NavigationPresenter = ({ open, handleOpen, handleClose }) => {
  const { pathname } = window.location;

  return (
    <>
      <Wrapper>
        <LogoContainer>
          <Logo to="/">빌리지</Logo>
          <Service>자취방 양도 서비스</Service>
        </LogoContainer>

        <NavContainer>
          <ListItem>
            <LinkItem to="/" current={pathname === "/"}>
              매물확인
            </LinkItem>
          </ListItem>
          <ListItem>
            <LinkItem to="/putout" current={pathname === "/putout"}>
              양도하기
            </LinkItem>
          </ListItem>
          <ListItem>
            <LinkItem to="/notice" current={pathname === "/notice"}>
              공지사항
            </LinkItem>
          </ListItem>
          <ListItem>
            <Login onClick={handleOpen}>로그인</Login>
          </ListItem>
        </NavContainer>
      </Wrapper>
      {open && (
        <Modal open={open} handleClose={handleClose}>
          <Auth />
        </Modal>
      )}
    </>
  );
};

export default NavigationPresenter;
