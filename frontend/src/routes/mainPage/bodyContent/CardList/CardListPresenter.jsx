import React from 'react';
import styled from 'styled-components';
import Card from 'components/Card/CardPresenter';

const CardListWrapper = styled.div`
width:980px;
hieght:100%;
`;

const CardListHeader = styled.div``;

const CardListContent = styled.div`
overflow:scroll;
display:flex;
flex:wrap;
justify-content:space-around;
`;
const CardList=()=>{
    return (
        <CardListWrapper>
            <CardListHeader></CardListHeader>
            <CardListContent></CardListContent>
        </CardListWrapper>
    )
}

export default CardList;