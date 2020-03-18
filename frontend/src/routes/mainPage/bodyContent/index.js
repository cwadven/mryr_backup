import React from 'react';
import styled from 'styled-components';
import CardList from './CardList';
import DetailInfo from './DetailInfo';

const ContentDivisor=styled.div`
    display:flex;
    height:80%;
`;
const BodyContent =()=>{
    return (
        <ContentDivisor>
            <CardList/>
            <DetailInfo/>
        </ContentDivisor>
    )

}

export default BodyContent;