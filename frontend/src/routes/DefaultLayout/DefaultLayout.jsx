import React from 'react';
import Navigation from "components/Navigation";

const DefaultLayout = ({children})=>{
    return (
        <>
        <Navigation/>
        {children}
        </>
    )
};

export default DefaultLayout;