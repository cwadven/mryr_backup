import React from 'react';
import styled from "styled-components";

const CardWrapper = styled.article`
    width:220px;
    height:280px;
`;

const CardImage = styled.img`
    height:150px;
`;

const CardContent = styled.div`

`;

const CardBold = styled.p`

`;

const CardParagraph=styeld.p`

`;

const CardPresenter = ()=>{
    return(
        <CardWrapper>
            <CardImage/>
            <CardContent>
                <CardParagraph></CardParagraph>
                <CardBold></CardBold>
                <CardParagraph></CardParagraph>
                <CardParagraph></CardParagraph>
            </CardContent>
        </CardWrapper>
    )
}

export default CardPresenter;