import React from "react";
import ReactDOM from "react-dom";
import styled from "styled-components";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faTimes } from "@fortawesome/free-solid-svg-icons";

const Wrapper = styled.div`
  position: fixed;
  top: 0;
  left: 0;
  background-color: rgba(0, 0, 0, 0.5);
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
`;

const Container = styled.div`
  width: 420px;
  min-width: 420px;
  padding: 60px 25px 0px;
  background: white;
  border-radius: 6px;
  position: relative;
`;

const BtnContainer = styled.button`
  width: 30px;
  height: 30px;
  background: white;
  border: 1px solid #b6b6b6;
  border-radius: 50%;
  cursor: pointer;
  transition: 0.3s;
  position: absolute;
  top: 25px;
  right: 25px;

  &:hover {
    background: black;
    color: white;
  }
`;

const ModalPresenter = ({ open, handleClose, children }) => {
  return open
    ? ReactDOM.createPortal(
        <Wrapper>
          <Container>
            <BtnContainer onClick={handleClose}>
              <FontAwesomeIcon icon={faTimes} />
            </BtnContainer>
            {children}
          </Container>
        </Wrapper>,
        document.body
      )
    : null;
};

export default ModalPresenter;
